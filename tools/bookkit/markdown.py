"""Block parser for Book Markdown, the small Markdown dialect the chapters use.

The dialect is CommonMark-flavoured but deliberately small, so that the whole
toolchain is this package plus the Python standard library:

* ATX headings with optional attributes: ``## Title {#ch01.sec.slug}``
* paragraphs, block quotes, bullet and numbered lists (nestable), pipe tables,
  fenced code blocks and thematic breaks
* container directives for the book's elements::

      ::: kind {#id key=value key="quoted value"} Optional title
      body, parsed as Book Markdown again
      :::

  A closing fence is a line holding only the same number of colons as its
  opener. Directives nest; use more colons on the outside if it helps you read.
* speech lines: a paragraph that starts ``@speaker: words`` renders as a speech
  bubble for a cast member (or for ``left``/``right`` inside a Two Chairs).

Inline syntax (emphasis, links, citations, cross-references) is handled in
``inline.py``; this module only keeps the raw inline text and its line number.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

from .errors import BuildError


@dataclass
class Node:
    kind: str
    line: int
    text: str = ""
    attrs: dict = field(default_factory=dict)
    children: list = field(default_factory=list)
    level: int = 0
    name: str = ""
    title: str = ""
    ordered: bool = False
    start: int = 1
    loose: bool = False
    rows: list = field(default_factory=list)
    align: list = field(default_factory=list)


FENCE_RE = re.compile(r"^(`{3,}|~{3,})\s*([\w+-]*)\s*$")
DIRECTIVE_OPEN_RE = re.compile(r"^(:{3,})\s*([a-z][a-z0-9-]*)\s*(\{[^{}]*\})?\s*(.*?)\s*$")
DIRECTIVE_CLOSE_RE = re.compile(r"^(:{3,})\s*$")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)(?:\s+\{([^{}]*)\})?\s*#*\s*$")
HR_RE = re.compile(r"^ {0,3}(?:(?:-\s*){3,}|(?:\*\s*){3,}|(?:_\s*){3,})$")
ITEM_RE = re.compile(r"^( {0,3})([-*+]|\d{1,9}[.)])(\s+|$)(.*)$")
TABLE_SEP_RE = re.compile(r"^(?=.*\|)\s*\|?\s*:?-+:?\s*(\|\s*:?-+:?\s*)*\|?\s*$")
SPEECH_RE = re.compile(r"^@([a-z][a-z0-9-]*):\s+")
ATTR_TOKEN_RE = re.compile(
    r"""\s*(?:\#(?P<id>[A-Za-z0-9_.:-]+)"""
    r"""|\.(?P<cls>[A-Za-z0-9_-]+)"""
    r"""|(?P<key>[A-Za-z][A-Za-z0-9_-]*)=(?:"(?P<dq>[^"]*)"|'(?P<sq>[^']*)'|(?P<bare>[^\s"'{}]+)))"""
)


def parse_attrs(raw: str | None, where: str) -> dict:
    """Parse ``{#id .class key=value key="quoted"}`` into a dict.

    The id is stored under ``id`` and classes under ``class`` (space separated).
    """
    attrs: dict = {}
    if not raw:
        return attrs
    body = raw.strip()
    if body.startswith("{") and body.endswith("}"):
        body = body[1:-1]
    pos = 0
    classes = []
    while pos < len(body):
        if body[pos:].strip() == "":
            break
        m = ATTR_TOKEN_RE.match(body, pos)
        if not m or m.end() == pos:
            raise BuildError(f"{where}: cannot read attributes near {body[pos:pos + 30]!r}")
        if m.group("id"):
            if "id" in attrs:
                raise BuildError(f"{where}: two ids in one attribute block")
            attrs["id"] = m.group("id")
        elif m.group("cls"):
            classes.append(m.group("cls"))
        else:
            value = m.group("dq")
            if value is None:
                value = m.group("sq")
            if value is None:
                value = m.group("bare")
            attrs[m.group("key")] = value
        pos = m.end()
    if classes:
        attrs["class"] = " ".join(classes)
    return attrs


def split_front_matter(source: str, where: str) -> tuple[dict, list[str], int]:
    """Split ``---`` delimited ``key: value`` front matter from the body.

    Returns (metadata, body lines, line number of the first body line).
    """
    lines = source.replace("\r\n", "\n").replace("\t", "    ").split("\n")
    meta: dict = {}
    if not lines or lines[0].strip() != "---":
        return meta, lines, 1
    for idx in range(1, len(lines)):
        line = lines[idx]
        if line.strip() == "---":
            return meta, lines[idx + 1:], idx + 2
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            raise BuildError(f"{where}:{idx + 1}: front matter lines look like 'key: value'")
        key, value = line.split(":", 1)
        meta[key.strip()] = value.strip().strip('"')
    raise BuildError(f"{where}: front matter is never closed with '---'")


class BlockParser:
    """Turns a list of source lines into a tree of ``Node`` objects."""

    def __init__(self, where: str):
        self.where = where

    def parse(self, lines: list[str], first_line: int = 1) -> list[Node]:
        return self._blocks(lines, first_line)

    # -- helpers -----------------------------------------------------------

    def _err(self, line: int, message: str) -> BuildError:
        return BuildError(f"{self.where}:{line}: {message}")

    @staticmethod
    def _indent(line: str) -> int:
        return len(line) - len(line.lstrip(" "))

    def _starts_block(self, line: str) -> bool:
        """True when ``line`` would interrupt a running paragraph."""
        stripped = line.strip()
        if not stripped:
            return True
        if FENCE_RE.match(stripped) or DIRECTIVE_OPEN_RE.match(stripped) or DIRECTIVE_CLOSE_RE.match(stripped):
            return True
        if HEADING_RE.match(stripped) or HR_RE.match(line) or stripped.startswith(">"):
            return True
        m = ITEM_RE.match(line)
        if m and m.group(4).strip() and (m.group(2) in "-*+" or m.group(2)[:-1] == "1"):
            return True
        return False

    # -- block dispatch ----------------------------------------------------

    def _blocks(self, lines: list[str], base: int) -> list[Node]:
        nodes: list[Node] = []
        i = 0
        n = len(lines)
        while i < n:
            line = lines[i]
            stripped = line.strip()
            lineno = base + i
            if not stripped:
                i += 1
                continue

            m = FENCE_RE.match(stripped)
            if m:
                i = self._fence(lines, i, base, m, nodes)
                continue
            m = DIRECTIVE_OPEN_RE.match(stripped)
            if m:
                i = self._directive(lines, i, base, m, nodes)
                continue
            if DIRECTIVE_CLOSE_RE.match(stripped):
                raise self._err(lineno, "closing ':::' without an opening directive")
            m = HEADING_RE.match(stripped)
            if m:
                attrs = parse_attrs(m.group(3), f"{self.where}:{lineno}")
                nodes.append(Node("heading", lineno, text=m.group(2).strip(), level=len(m.group(1)), attrs=attrs))
                i += 1
                continue
            if HR_RE.match(line):
                nodes.append(Node("hr", lineno))
                i += 1
                continue
            if stripped.startswith(">"):
                i = self._quote(lines, i, base, nodes)
                continue
            if ITEM_RE.match(line):
                i = self._list(lines, i, base, nodes)
                continue
            if "|" in stripped and i + 1 < n and TABLE_SEP_RE.match(lines[i + 1]):
                i = self._table(lines, i, base, nodes)
                continue
            i = self._paragraph(lines, i, base, nodes)
        return nodes

    def _fence(self, lines, i, base, m, nodes) -> int:
        marker = m.group(1)
        lang = m.group(2)
        body = []
        j = i + 1
        while j < len(lines):
            if lines[j].strip().startswith(marker[0] * len(marker)) and lines[j].strip().strip(marker[0]) == "":
                nodes.append(Node("code", base + i, text="\n".join(body), name=lang))
                return j + 1
            body.append(lines[j])
            j += 1
        raise self._err(base + i, "code fence is never closed")

    def _directive(self, lines, i, base, m, nodes) -> int:
        colons = m.group(1)
        name = m.group(2)
        lineno = base + i
        attrs = parse_attrs(m.group(3), f"{self.where}:{lineno}")
        title = m.group(4) or ""
        depth = 0
        j = i + 1
        while j < len(lines):
            s = lines[j].strip()
            mo = DIRECTIVE_OPEN_RE.match(s)
            if mo and mo.group(1) == colons:
                depth += 1
            elif s == colons:
                if depth == 0:
                    children = self._blocks(lines[i + 1:j], base + i + 1)
                    nodes.append(Node("directive", lineno, name=name, attrs=attrs, title=title, children=children))
                    return j + 1
                depth -= 1
            j += 1
        raise self._err(lineno, f"'{colons} {name}' is never closed with a line holding only '{colons}'")

    def _quote(self, lines, i, base, nodes) -> int:
        inner = []
        j = i
        while j < len(lines) and lines[j].strip().startswith(">"):
            s = lines[j].strip()[1:]
            inner.append(s[1:] if s.startswith(" ") else s)
            j += 1
        nodes.append(Node("quote", base + i, children=self._blocks(inner, base + i)))
        return j

    def _paragraph(self, lines, i, base, nodes) -> int:
        buf = [lines[i].strip()]
        j = i + 1
        while j < len(lines) and not self._starts_block(lines[j]):
            if "|" in lines[j] and j + 1 < len(lines) and TABLE_SEP_RE.match(lines[j + 1]):
                break
            buf.append(lines[j].strip())
            j += 1
        # keep a trailing backslash or double space as a hard-break marker
        raw = []
        for k, piece in enumerate(buf):
            original = lines[i + k]
            if original.endswith("  ") and k < len(buf) - 1:
                piece += "\\"
            raw.append(piece)
        text = "\n".join(raw)
        sm = SPEECH_RE.match(text)
        if sm:
            nodes.append(Node("speech", base + i, name=sm.group(1), text=text[sm.end():]))
        else:
            nodes.append(Node("para", base + i, text=text))
        return j

    def _table(self, lines, i, base, nodes) -> int:
        def cells(row: str) -> list[str]:
            row = row.strip()
            if row.startswith("|"):
                row = row[1:]
            if row.endswith("|") and not row.endswith("\\|"):
                row = row[:-1]
            out, cur, esc = [], [], False
            for ch in row:
                if esc:
                    cur.append(ch if ch == "|" else "\\" + ch)
                    esc = False
                elif ch == "\\":
                    esc = True
                elif ch == "|":
                    out.append("".join(cur).strip())
                    cur = []
                else:
                    cur.append(ch)
            out.append("".join(cur).strip())
            return out

        header = cells(lines[i])
        aligns = []
        for spec in cells(lines[i + 1]):
            left, right = spec.startswith(":"), spec.endswith(":")
            aligns.append("center" if left and right else "right" if right else "left" if left else "")
        if len(aligns) != len(header):
            raise self._err(base + i, "table separator has a different number of columns than the header")
        rows = []
        j = i + 2
        while j < len(lines) and lines[j].strip() and "|" in lines[j]:
            row = cells(lines[j])
            if len(row) != len(header):
                raise self._err(base + j, f"table row has {len(row)} cells, header has {len(header)}")
            rows.append((base + j, row))
            j += 1
        nodes.append(Node("table", base + i, rows=[(base + i, header)] + rows, align=aligns))
        return j

    def _list(self, lines, i, base, nodes) -> int:
        first = ITEM_RE.match(lines[i])
        ordered = first.group(2)[-1] in ".)"
        bullet = first.group(2) if not ordered else first.group(2)[-1]
        start = int(first.group(2)[:-1]) if ordered else 1
        items: list[Node] = []
        loose = False
        j = i
        n = len(lines)
        while j < n:
            m = ITEM_RE.match(lines[j])
            if not m:
                break
            marker = m.group(2)
            same_type = (marker[-1] == bullet) if ordered else (marker == bullet)
            if not same_type or len(m.group(1)) > 3:
                break
            pad = len(m.group(3)) if m.group(4) else 1
            if pad > 4:
                pad = 1
            content_indent = len(m.group(1)) + len(marker) + pad
            body = [m.group(4)]
            item_line = base + j
            j += 1
            saw_blank = False
            while j < n:
                line = lines[j]
                if not line.strip():
                    body.append("")
                    saw_blank = True
                    j += 1
                    continue
                if self._indent(line) >= content_indent:
                    body.append(line[content_indent:])
                    j += 1
                    if saw_blank:
                        loose = True
                    saw_blank = False
                    continue
                if saw_blank:
                    break
                if ITEM_RE.match(line) or self._starts_block(line):
                    break
                body.append(line.strip())  # lazy continuation
                j += 1
            while body and not body[-1].strip():
                body.pop()
            item = Node("item", item_line, children=self._blocks(body, item_line))
            items.append(item)
            # a blank line between items makes the list loose
            k = j - 1
            if k >= 0 and k < n and not lines[k].strip() and j < n and ITEM_RE.match(lines[j]):
                loose = True
            while j < n and not lines[j].strip():
                nxt = j
                while nxt < n and not lines[nxt].strip():
                    nxt += 1
                if nxt < n and ITEM_RE.match(lines[nxt]):
                    mm = ITEM_RE.match(lines[nxt])
                    mk = mm.group(2)
                    if ((mk[-1] == bullet) if ordered else (mk == bullet)) and len(mm.group(1)) <= 3:
                        loose = True
                        j = nxt
                        break
                break
        nodes.append(Node("list", base + i, children=items, ordered=ordered, start=start, loose=loose))
        return j


def parse_document(source: str, where: str) -> tuple[dict, list[Node]]:
    meta, lines, first = split_front_matter(source, where)
    return meta, BlockParser(where).parse(lines, first)
