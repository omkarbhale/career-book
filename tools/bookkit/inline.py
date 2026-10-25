"""Inline rendering for Book Markdown.

Supported inline syntax:

* ``*emphasis*``, ``_emphasis_``, ``**strong**``, ```code```
* ``[text](https://example.org "optional title")`` and ``<https://example.org>``
* citations ``[@key]``, ``[@key, p. 12]``, ``[@a; @b]``; add ``!`` after a key
  (``[@key!]``) to print its evidence grade next to the number
* cross-references ``[[ch07]]``, ``[[ch01.fig.quadrant]]``,
  ``[[ch07|custom text]]`` and ``[[ch07:full]]`` (number plus title)
* evidence labels ``[!craft]`` (practitioner advice), ``[!view]`` (the author's
  view) and ``[!unverified]``
* a backslash at the end of a line forces a line break; ``\\*`` escapes

Typography is applied outside code: straight quotes become curly quotes,
``--`` an en dash, ``---`` an em dash and ``...`` an ellipsis.
"""

from __future__ import annotations

import html
import re

from .errors import BuildError

PH = "\x00"
ESCAPABLE = "\\`*_{}[]()#+-.!|@~<>\"'"
CODE_RE = re.compile(r"(`+)(.+?)\1", re.S)
CITE_RE = re.compile(r"\[(@[^\[\]]+)\]")
CITE_PART_RE = re.compile(r"^\s*@([A-Za-z0-9_:.-]+?)(!?)\s*(?:,\s*(.+?))?\s*$", re.S)
XREF_RE = re.compile(r"\[\[([^\[\]|]+?)(?:\|([^\[\]]+))?\]\]")
LABEL_RE = re.compile(r"\[!([a-z]+)\]")
LINK_RE = re.compile(r"(!?)\[((?:[^\[\]]|\[[^\[\]]*\])+)\]\(\s*([^()\s]+)(?:\s+\"([^\"]*)\")?\s*\)")
AUTOLINK_RE = re.compile(r"<(https?://[^>\s]+)>")
STRONG_RE = re.compile(r"\*\*(?=\S)(.+?)(?<=\S)\*\*", re.S)
EM_STAR_RE = re.compile(r"(?<![\w*])\*(?=[^\s*])(.+?)(?<=[^\s*])\*(?![\w*])", re.S)
EM_UNDER_RE = re.compile(r"(?<![\w])_(?=\S)(.+?)(?<=\S)_(?![\w])", re.S)
PH_RE = re.compile(PH + r"(\d+)" + PH)
OPENERS = set(" \n\t([{\u2014\u2013/*_")


class InlineContext:
    """Callbacks the renderer uses for book-specific inline syntax.

    ``render.Renderer`` provides the real implementation; tests can use this
    default, which renders keys and ids literally.
    """

    def cite(self, parts: list[tuple[str, bool, str]], where: str) -> str:
        return "[" + "; ".join(k for k, _, _ in parts) + "]"

    def xref(self, target: str, text_html: str | None, mode: str, where: str) -> str:
        return text_html or html.escape(target)

    def label(self, name: str, where: str) -> str:
        return f"<span class=\"label\">{html.escape(name)}</span>"


def smarten(text: str, after_fragment: bool = False) -> str:
    """Curly quotes and dashes for plain text (never called on code).

    ``after_fragment`` says the text directly follows rendered markup (a link,
    a citation), so a quote at its very start closes rather than opens.
    """
    text = text.replace("---", "\u2014").replace("--", "\u2013").replace("...", "\u2026")
    text = re.sub(r"'(?=\d0s\b)", "\u2019", text)
    out = []
    for idx, ch in enumerate(text):
        prev = text[idx - 1] if idx else ("x" if after_fragment else " ")
        if ch == '"':
            out.append("\u201c" if prev in OPENERS else "\u201d")
        elif ch == "'":
            nxt = text[idx + 1] if idx + 1 < len(text) else " "
            if prev in OPENERS and (nxt.isalnum()):
                out.append("\u2018")
            else:
                out.append("\u2019")
        else:
            out.append(ch)
    return "".join(out)


def check_url(url: str, where: str) -> str:
    if url.startswith(("https://", "http://", "mailto:", "#")):
        return url
    if re.match(r"^[a-z0-9-]+\.html(#[A-Za-z0-9_.:-]+)?$", url):
        return url
    raise BuildError(f"{where}: link target {url!r} is not an http(s) URL or a page in this book")


def render_inline(text: str, ctx: InlineContext, where: str) -> str:
    held: list[str] = []

    def hold(fragment: str) -> str:
        held.append(fragment)
        return f"{PH}{len(held) - 1}{PH}"

    # hard line breaks (backslash at end of a line) and backslash escapes
    text = re.sub(r"\\\n", lambda m: hold("<br>") + "\n", text)
    text = re.sub(r"\\$", "", text)
    text = re.sub(
        r"\\(.)",
        lambda m: hold(html.escape(m.group(1))) if m.group(1) in ESCAPABLE else m.group(0),
        text,
    )
    text = CODE_RE.sub(lambda m: hold(f"<code>{html.escape(m.group(2).strip())}</code>"), text)

    def do_cite(m: re.Match) -> str:
        parts = []
        for chunk in m.group(1).split(";"):
            pm = CITE_PART_RE.match(chunk)
            if not pm:
                raise BuildError(f"{where}: cannot read citation {m.group(0)!r}; write [@key] or [@key, p. 4]")
            locator = pm.group(3) or ""
            parts.append((pm.group(1), pm.group(2) == "!", smarten(locator)))
        return hold(ctx.cite(parts, where))

    text = CITE_RE.sub(do_cite, text)

    def do_xref(m: re.Match) -> str:
        target = m.group(1).strip()
        mode = ""
        if ":" in target:
            target, mode = target.split(":", 1)
            if mode not in ("full", "title"):
                raise BuildError(f"{where}: unknown cross-reference mode {mode!r} in {m.group(0)!r}")
        custom = render_inline(m.group(2), ctx, where) if m.group(2) else None
        return hold(ctx.xref(target, custom, mode, where))

    text = XREF_RE.sub(do_xref, text)
    text = LABEL_RE.sub(lambda m: hold(ctx.label(m.group(1), where)), text)

    def do_link(m: re.Match) -> str:
        if m.group(1):
            raise BuildError(f"{where}: images are not allowed inline; use a ::: figure with an SVG")
        url = check_url(m.group(3), where)
        inner = render_inline(m.group(2), ctx, where)
        title = f' title="{html.escape(m.group(4))}"' if m.group(4) else ""
        external = url.startswith("http")
        rel = ' class="ext" rel="noopener"' if external else ""
        return hold(f'<a href="{html.escape(url)}"{title}{rel}>{inner}</a>')

    text = LINK_RE.sub(do_link, text)
    text = AUTOLINK_RE.sub(
        lambda m: hold(f'<a href="{html.escape(m.group(1))}" class="ext" rel="noopener">{html.escape(m.group(1))}</a>'),
        text,
    )
    if "](" in text and "[" in text:
        raise BuildError(f"{where}: a link could not be read; check its brackets and parentheses")

    # typography and escaping outside held fragments
    pieces = re.split(f"({PH}\\d+{PH})", text)
    text = "".join(
        p if PH_RE.fullmatch(p) else html.escape(smarten(p, k > 0 and pieces[k - 1] != ""), quote=False)
        for k, p in enumerate(pieces)
    )

    for _ in range(3):
        text = STRONG_RE.sub(r"<strong>\1</strong>", text)
        text = EM_STAR_RE.sub(r"<em>\1</em>", text)
        text = EM_UNDER_RE.sub(r"<em>\1</em>", text)

    while PH_RE.search(text):
        text = PH_RE.sub(lambda m: held[int(m.group(1))], text)
    return text


def plain_text(text: str) -> str:
    """Inline source reduced to plain text, for titles, alt text and slugs."""
    text = CITE_RE.sub("", text)
    text = XREF_RE.sub(lambda m: m.group(2) or m.group(1), text)
    text = LABEL_RE.sub("", text)
    text = LINK_RE.sub(lambda m: m.group(2), text)
    text = re.sub(r"[*_`]", "", text)
    text = re.sub(r"\\(.)", r"\1", text)
    return smarten(re.sub(r"\s+", " ", text).strip())


def slugify(text: str) -> str:
    text = plain_text(text).lower()
    text = re.sub(r"[\u2018\u2019\u201c\u201d']", "", text)
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return text or "section"
