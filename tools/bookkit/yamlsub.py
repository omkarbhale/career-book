"""A reader for the small subset of YAML the research registries use.

The researchers keep their source registries in ``research/*/sources.yaml``.
The standard library has no YAML parser and the build installs nothing, so
this module reads exactly the constructs those files use, and refuses anything
else rather than guessing:

* block mappings (``key: value``) and block sequences (``- item``), nested by
  indentation, including a sequence written at its parent key's indent
* plain, 'single-quoted' and "double-quoted" scalars
* folded (``>``, ``>-``) and literal (``|``, ``|-``) block scalars
* flow sequences ``[a, 'b, c']`` and flow mappings ``{k: v, k2: v2}``; a flow
  collection may wrap onto more-indented lines (line breaks fold to spaces)
* ``#`` comments

Anchors, aliases, tags, multi-line flow collections and multiple documents
are rejected with an error that names the line.
"""

from __future__ import annotations

import json
import re


class YamlError(ValueError):
    pass


KEY_RE = re.compile(r"^([A-Za-z0-9_][A-Za-z0-9_.-]*):(?:\s+|$)(.*)$")


def _strip_comment(text: str) -> str:
    """Remove a trailing comment from a plain (unquoted) value."""
    m = re.search(r"(^|\s)#", text)
    return text[: m.start()].rstrip() if m else text.rstrip()


def _scalar(text: str, where: str):
    text = text.strip()
    if not text:
        return ""
    if text[0] in "&*!|>%@`":
        raise YamlError(f"{where}: unsupported YAML construct {text[:20]!r}")
    if text.startswith("'"):
        m = re.match(r"^'((?:[^']|'')*)'\s*(#.*)?$", text)
        if not m:
            raise YamlError(f"{where}: unterminated single-quoted string")
        return m.group(1).replace("''", "'")
    if text.startswith('"'):
        m = re.match(r'^("(?:[^"\\]|\\.)*")\s*(#.*)?$', text)
        if not m:
            raise YamlError(f"{where}: unterminated double-quoted string")
        return json.loads(m.group(1))
    if text.startswith("["):
        return _flow_seq(_strip_comment(text), where)
    if text.startswith("{"):
        return _flow_map(_strip_comment(text), where)
    value = _strip_comment(text)
    if value in ("null", "~"):
        return None
    if value in ("true", "false"):
        return value == "true"
    if re.fullmatch(r"-?\d+", value):
        return int(value)
    return value


def _split_flow(body: str, where: str) -> list[str]:
    parts, cur, quote, depth = [], [], "", 0
    i = 0
    while i < len(body):
        ch = body[i]
        if quote:
            cur.append(ch)
            if ch == quote:
                if quote == "'" and i + 1 < len(body) and body[i + 1] == "'":
                    cur.append("'")
                    i += 1
                else:
                    quote = ""
            elif ch == "\\" and quote == '"' and i + 1 < len(body):
                cur.append(body[i + 1])
                i += 1
        elif ch in "'\"":
            quote = ch
            cur.append(ch)
        elif ch in "[{":
            depth += 1
            cur.append(ch)
        elif ch in "]}":
            depth -= 1
            cur.append(ch)
        elif ch == "," and depth == 0:
            parts.append("".join(cur).strip())
            cur = []
        else:
            cur.append(ch)
        i += 1
    if quote or depth:
        raise YamlError(f"{where}: unbalanced flow collection")
    tail = "".join(cur).strip()
    if tail:
        parts.append(tail)
    return parts


def _flow_seq(text: str, where: str) -> list:
    if not text.endswith("]"):
        raise YamlError(f"{where}: flow sequences must open and close on one line")
    return [_scalar(p, where) for p in _split_flow(text[1:-1], where)]


def _flow_map(text: str, where: str) -> dict:
    if not text.endswith("}"):
        raise YamlError(f"{where}: flow mappings must open and close on one line")
    out = {}
    for part in _split_flow(text[1:-1], where):
        m = re.match(r"^([A-Za-z0-9_][A-Za-z0-9_.-]*):\s+(.*)$", part)
        if not m:
            raise YamlError(f"{where}: cannot read flow mapping entry {part!r}")
        out[m.group(1)] = _scalar(m.group(2), where)
    return out


class _Lines:
    def __init__(self, text: str, name: str):
        self.name = name
        self.items = []
        for n, raw in enumerate(text.replace("\r\n", "\n").split("\n"), 1):
            if "\t" in raw[: len(raw) - len(raw.lstrip())]:
                raise YamlError(f"{name}:{n}: tabs are not allowed for indentation")
            self.items.append((n, raw))
        self.pos = 0

    def skip_blank(self):
        while self.pos < len(self.items):
            raw = self.items[self.pos][1]
            s = raw.strip()
            if s and not s.startswith("#"):
                return
            self.pos += 1

    def peek(self):
        self.skip_blank()
        if self.pos >= len(self.items):
            return None
        n, raw = self.items[self.pos]
        return n, len(raw) - len(raw.lstrip(" ")), raw.strip()


def _block_scalar(lines: _Lines, indicator: str, parent_indent: int) -> str:
    style, chomp = indicator[0], indicator[1:]
    body = []
    indent = None
    while lines.pos < len(lines.items):
        n, raw = lines.items[lines.pos]
        if raw.strip() == "":
            body.append("")
            lines.pos += 1
            continue
        ind = len(raw) - len(raw.lstrip(" "))
        if ind <= parent_indent:
            break
        if indent is None:
            indent = ind
        if ind < indent:
            break
        body.append(raw[indent:])
        lines.pos += 1
    while body and body[-1] == "":
        body.pop()
    if style == "|":
        text = "\n".join(body)
    else:
        paras, cur = [], []
        for b in body:
            if b == "":
                paras.append(" ".join(cur))
                cur = []
            else:
                cur.append(b.strip())
        paras.append(" ".join(cur))
        text = "\n".join(paras)
    if chomp == "-":
        return text
    return text + "\n"


def _balanced(text: str) -> bool:
    try:
        _split_flow(text[1:], "")
    except YamlError:
        return False
    depth, quote = 0, ""
    for ch in text:
        if quote:
            if ch == quote:
                quote = ""
        elif ch in "'\"":
            quote = ch
        elif ch in "[{":
            depth += 1
        elif ch in "]}":
            depth -= 1
    return depth == 0 and not quote


def _gather_flow(lines: _Lines, rest: str, indent: int) -> str:
    """Join the more-indented lines a wrapped flow collection continues onto."""
    while rest[:1] in "[{" and not _balanced(rest) and lines.pos < len(lines.items):
        n, raw = lines.items[lines.pos]
        if raw.strip() == "" or len(raw) - len(raw.lstrip(" ")) <= indent:
            break
        rest = rest + " " + raw.strip()
        lines.pos += 1
    return rest


def _value_after_key(lines: _Lines, rest: str, indent: int, where: str):
    rest = _gather_flow(lines, rest.strip(), indent)
    if rest in (">", ">-", ">+", "|", "|-", "|+"):
        return _block_scalar(lines, rest, indent)
    if rest == "" or rest.startswith("#"):
        nxt = lines.peek()
        if nxt is None:
            return None
        n, ind, s = nxt
        if s.startswith("- ") or s == "-":
            if ind < indent:
                return None
            return _block_seq(lines, ind)
        if ind > indent:
            return _block_map(lines, ind)
        return None
    return _scalar(rest, where)


def _block_map(lines: _Lines, indent: int) -> dict:
    out: dict = {}
    while True:
        nxt = lines.peek()
        if nxt is None:
            return out
        n, ind, s = nxt
        if ind < indent or (ind == indent and s.startswith("- ")):
            return out
        if ind > indent:
            raise YamlError(f"{lines.name}:{n}: unexpected indentation")
        m = KEY_RE.match(s)
        if not m:
            raise YamlError(f"{lines.name}:{n}: expected 'key: value', found {s[:40]!r}")
        key = m.group(1)
        if key in out:
            raise YamlError(f"{lines.name}:{n}: duplicate key {key!r}")
        lines.pos += 1
        out[key] = _value_after_key(lines, m.group(2), ind, f"{lines.name}:{n}")


def _block_seq(lines: _Lines, indent: int) -> list:
    out = []
    while True:
        nxt = lines.peek()
        if nxt is None:
            return out
        n, ind, s = nxt
        if ind != indent or not (s.startswith("- ") or s == "-"):
            return out
        content = s[1:].strip()
        where = f"{lines.name}:{n}"
        km = KEY_RE.match(content)
        if km:
            # "- key: value" starts a mapping whose keys sit at indent + 2
            n_line, raw = lines.items[lines.pos]
            item_indent = ind + 2
            lines.items[lines.pos] = (n_line, " " * item_indent + content)
            out.append(_block_map(lines, item_indent))
        else:
            lines.pos += 1
            content = _gather_flow(lines, content, ind)
            out.append(_scalar(content, where) if content else _value_after_key(lines, "", ind, where))


def load(text: str, name: str = "<yaml>"):
    if re.search(r"^---\s*$", text, flags=re.M) and text.count("\n---") > 1:
        raise YamlError(f"{name}: multiple YAML documents are not supported")
    lines = _Lines(text, name)
    nxt = lines.peek()
    if nxt is None:
        return {}
    n, ind, s = nxt
    if s == "---":
        lines.pos += 1
    result = _block_map(lines, 0)
    tail = lines.peek()
    if tail is not None:
        raise YamlError(f"{name}:{tail[0]}: could not read this line")
    return result
