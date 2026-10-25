"""Rendering: Book Markdown trees to HTML, with the book's element catalogue.

Rendering happens in two passes over the whole book. ``collect`` walks every
page first, numbering figures and exercises and registering every explicit id,
so that ``render`` can resolve cross-references in either direction: forward
to a later chapter as easily as back to an earlier one.
"""

from __future__ import annotations

import html
import re
from dataclasses import dataclass, field

from . import svg as svgmod
from .bib import GRADES, grade_badge
from .inline import InlineContext, plain_text, render_inline, slugify
from .errors import BuildError
from .markdown import Node

# id grammar: <page>.<kind>.<slug>, e.g. ch01.fig.quadrant or howto.sec.elements
ID_RE = re.compile(r"^([a-z0-9]+)\.(sec|fig|move|myth|box)\.([a-z0-9]+(?:-[a-z0-9]+)*)$")

ICONS = {
    "scene": '<path d="M3 9h18v11H3z"/><path d="M3 9l2-5 16 3-1 2"/><path d="M8 5.2l2 3.4M13 6.1l2 3.2"/>',
    "pause": '<path d="M8 5v14M16 5v14"/>',
    "move": '<path d="M12 3.5a3 3 0 1 1 0 6 3 3 0 0 1 0-6z"/><path d="M9.5 9.5c0 3-1.5 5-2.5 7.5h10c-1-2.5-2.5-4.5-2.5-7.5"/><path d="M5.5 20.5h13"/>',
    "ask": '<path d="M4 5h16v11H9l-5 4z"/><path d="M10 9a2 2 0 1 1 3 1.7c-.7.4-1 .8-1 1.6"/><path d="M12 14.3v.2"/>',
    "chairs": '<path d="M4 4v16M4 12h6v8M10 12V8"/><path d="M20 4v16M20 12h-6v8M14 12V8"/>',
    "trapdoor": '<path d="M3 14h18"/><path d="M5 14l4 6h6l4-6"/><path d="M12 3v7M9 7l3 3 3-3"/>',
    "myth": '<path d="M10.5 4a6.5 6.5 0 1 1 0 13 6.5 6.5 0 0 1 0-13z"/><path d="M15.5 15.5L21 21"/><path d="M8 10.5h5"/>',
    "receipts": '<path d="M6 3h12v18l-2-1.5-2 1.5-2-1.5-2 1.5-2-1.5L6 21z"/><path d="M9 8h6M9 12h6M9 16h3"/>',
    "field": '<path d="M12 3a9 9 0 1 1 0 18 9 9 0 0 1 0-18z"/><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18"/>',
    "craft": '<path d="M15 4l5 5-9.5 9.5L5 20l1.5-5.5z"/><path d="M13 6l5 5"/>',
    "flashback": '<path d="M9 7H4V2"/><path d="M4.5 7A8 8 0 1 1 4 13"/>',
    "coming": '<path d="M15 7h5V2"/><path d="M19.5 7A8 8 0 1 0 20 13"/>',
    "rewind": '<path d="M11 6L4 12l7 6zM20 6l-7 6 7 6z"/>',
    "further": '<path d="M14 4h6v6"/><path d="M20 4l-9 9"/><path d="M18 14v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h5"/>',
    "resource": '<path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v15H6.5A2.5 2.5 0 0 0 4 20.5z"/><path d="M4 20.5A2.5 2.5 0 0 0 6.5 23H20v-5"/><path d="M8 7h8M8 11h6"/>',
}


def icon(name: str) -> str:
    return (
        '<svg class="el-icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false">'
        f'{ICONS[name]}</svg>'
    )


@dataclass
class Element:
    label: str
    tag: str = "aside"
    required: tuple = ()
    optional: tuple = ()
    id_kind: str = "box"
    numbered: bool = False
    inside: str = ""


ELEMENTS = {
    "scene": Element("Scene", tag="div", optional=("slug",)),
    "pause": Element("Pause"),
    "move": Element("Your Move", tag="section", id_kind="move", numbered=True),
    "answer": Element("Answer", tag="details", optional=("label",), inside="move"),
    "ask": Element("Ask Anyway"),
    "chairs": Element("Two Chairs", tag="section", required=("left", "right")),
    "trapdoor": Element("Trapdoor"),
    "myth": Element("Myth Check", required=("verdict", "grade"), id_kind="myth"),
    "receipts": Element("Receipts", optional=("grade", "source")),
    "field": Element("Field Note", required=("regions",)),
    "craft": Element("Craft Note", optional=("by",)),
    "flashback": Element("Flashback", required=("ref",)),
    "coming": Element("Coming Soon", required=("ref",)),
    "rewind": Element("Rewind", tag="section"),
    "further": Element("Going Further", optional=("ref",)),
    "resource": Element("Resource", required=("source",)),
    "figure": Element("Figure", tag="figure", required=("src",), optional=("alt", "size"), id_kind="fig", numbered=True),
}
VERDICTS = {"busted": "Busted", "partly": "Partly true", "holds": "Holds up"}
CRAFT_KINDS = {
    "craft": ("Craft Note", "Practitioner experience, not research"),
    "author": ("Author’s View", "Our opinion: argued, not proven"),
}
FIGURE_SIZES = ("", "small", "wide")


@dataclass
class Page:
    id: str
    kind: str  # front | chapter | epilogue
    title: str
    href: str
    label: str  # figure-number prefix: "1" for Chapter 1, "A" for front matter
    number: int | None = None
    part: str = ""
    rel: str = ""  # source path relative to the repo, for messages
    nodes: list = field(default_factory=list)
    meta: dict = field(default_factory=dict)
    summary: str = ""
    covers: list = field(default_factory=list)
    planned: list = field(default_factory=list)  # [(id, title)] sections other pages may link to before this one exists
    written: bool = False
    status: str = "planned"
    toc: list = field(default_factory=list)
    body_html: str = ""
    refs_html: str = ""
    cited: list = field(default_factory=list)


@dataclass
class Anchor:
    id: str
    page: Page
    kind: str  # page | sec | fig | move | myth | box
    title: str = ""
    number: str = ""
    element: str = ""

    @property
    def href(self) -> str:
        return self.page.href if self.kind == "page" else f"{self.page.href}#{self.id}"


class Book:
    """Everything rendering needs to know about the whole book."""

    def __init__(self, config: dict, pages: list[Page], sources: dict, cast: dict, figures, report):
        self.config = config
        self.pages = pages
        self.sources = sources
        self.cast = cast
        self.figures = figures  # callable(src, where) -> svg text or None
        self.report = report
        self.anchors: dict[str, Anchor] = {}
        self.backlinks: dict[str, set] = {p.id: set() for p in pages}
        self.cited_in: dict[str, list] = {}
        for p in pages:
            self.anchors[p.id] = Anchor(p.id, p, "page", title=p.title, number=str(p.number or ""))
            if not p.written:
                for ident, title in p.planned:
                    self.anchors[ident] = Anchor(ident, p, "sec", title=title)

    # -- pass 1 ------------------------------------------------------------

    def collect(self, page: Page) -> None:
        counters = {"fig": 0, "move": 0}
        auto_ids: set = set()

        def register(node: Node, kind: str, title: str, element: str = "", number: str = "") -> None:
            ident = node.attrs.get("id")
            where = f"{page.rel}:{node.line}"
            if not ident:
                return
            m = ID_RE.match(ident)
            if not m or m.group(1) != page.id:
                self.report.error(
                    f"{where}: id {ident!r} must look like {page.id}.{kind}.some-name "
                    f"(page id, kind, then lowercase words joined by hyphens)"
                )
                return
            if m.group(2) != kind:
                self.report.error(f"{where}: id {ident!r} should use the kind '{kind}' for this element")
                return
            if ident in self.anchors:
                self.report.error(f"{where}: id {ident!r} is already used on {self.anchors[ident].page.rel}")
                return
            self.anchors[ident] = Anchor(ident, page, kind, title=title, number=number, element=element)

        def walk(nodes: list[Node], depth: int, parent: str = "") -> None:
            for node in nodes:
                where = f"{page.rel}:{node.line}"
                if node.kind == "heading":
                    if node.level == 1:
                        self.report.error(f"{where}: '#' headings are reserved for the page title; start at '##'")
                    if node.level > 4:
                        self.report.error(f"{where}: headings deeper than '####' are not used in this book")
                    title = plain_text(node.text)
                    if not node.attrs.get("id"):
                        base = f"{page.id}-{slugify(node.text)}"
                        ident, k = base, 2
                        while ident in auto_ids:
                            ident, k = f"{base}-{k}", k + 1
                        auto_ids.add(ident)
                        node.attrs["auto_id"] = ident
                    else:
                        register(node, "sec", title)
                    if node.level == 2 and depth == 0:
                        page.toc.append((node.attrs.get("id") or node.attrs["auto_id"], title))
                elif node.kind == "directive":
                    el = ELEMENTS.get(node.name)
                    if not el:
                        self.report.error(
                            f"{where}: unknown element '::: {node.name}'; the catalogue is: "
                            + ", ".join(sorted(ELEMENTS))
                        )
                        continue
                    if el.inside and parent != el.inside:
                        self.report.error(f"{where}: '::: {node.name}' only goes inside '::: {el.inside}'")
                    allowed = set(el.required) | set(el.optional) | {"id", "class"}
                    for a in el.required:
                        if a not in node.attrs:
                            self.report.error(f"{where}: '::: {node.name}' needs {a}=...")
                    for a in node.attrs:
                        if a not in allowed:
                            self.report.error(f"{where}: '::: {node.name}' does not take {a}=...")
                    number = ""
                    if el.numbered:
                        counters[el.id_kind] += 1
                        number = f"{page.label}.{counters[el.id_kind]}"
                        node.attrs["_number"] = number
                    if node.name == "figure" and not node.attrs.get("id"):
                        self.report.error(f"{where}: every figure needs an id, like {{#{page.id}.fig.some-name}}")
                    register(node, el.id_kind, plain_text(node.title), element=node.name, number=number)
                    walk(node.children, depth + 1, node.name)
                elif node.kind in ("list", "item", "quote"):
                    walk(node.children, depth + 1, parent)

        walk(page.nodes, 0)

    # -- pass 2 ------------------------------------------------------------

    def render(self, page: Page) -> None:
        r = Renderer(self, page)
        page.body_html = r.blocks(page.nodes)
        page.refs_html = r.references()
        page.cited = list(r.cites)


class Renderer(InlineContext):
    def __init__(self, book: Book, page: Page):
        self.book = book
        self.page = page
        self.cites: dict[str, int] = {}
        self.cite_marks: dict[str, list[str]] = {}
        self.avatar_count = 0
        self.speakers: dict[str, str] = {}

    @property
    def report(self):
        return self.book.report

    def where(self, node: Node) -> str:
        return f"{self.page.rel}:{node.line}"

    def inline(self, text: str, node: Node) -> str:
        try:
            return render_inline(text, self, self.where(node))
        except BuildError as exc:  # carries its own location
            self.report.error(str(exc))
            return html.escape(text)

    # -- inline callbacks ----------------------------------------------------

    def cite(self, parts, where):
        out = []
        for key, show_grade, locator in parts:
            src = self.book.sources.get(key)
            if not src:
                self.report.error(f"{where}: citation key {key!r} is not in any bibliography file")
                out.append(f'<span class="cite-missing">{html.escape(key)}</span>')
                continue
            if src.deprecated:
                self.report.error(f"{where}: source {key!r} is deprecated ({src.deprecated}); cite its replacement")
            if "retracted" in src.flags:
                self.report.error(f"{where}: source {key!r} is retracted and cannot be cited as evidence")
            if key not in self.cites:
                self.cites[key] = len(self.cites) + 1
                self.cite_marks[key] = []
            n = self.cites[key]
            mark = f"cite-{self.page.id}-{n}-{len(self.cite_marks[key]) + 1}"
            self.cite_marks[key].append(mark)
            self.book.cited_in.setdefault(key, [])
            if self.page.id not in self.book.cited_in[key]:
                self.book.cited_in[key].append(self.page.id)
            label = GRADES[src.grade][0]
            tip = html.escape(f"{src.short()} · {label}")
            text = str(n)
            if locator:
                text += f", {html.escape(locator)}"
            grade = f' <span class="cite-grade grade-{src.grade}">{label.split()[0].lower()}</span>' if show_grade else ""
            out.append(
                f'<a id="{mark}" href="#ref-{self.page.id}-{n}" title="{tip}" '
                f'data-grade="{src.grade}">{text}</a>{grade}'
            )
        return '<span class="cite">[' + "; ".join(out) + "]</span>"

    def xref(self, target, text_html, mode, where):
        anchor = self.book.anchors.get(target)
        if not anchor:
            self.report.error(f"{where}: cross-reference [[{target}]] points at an id that does not exist")
            return f'<span class="xref-missing">{html.escape(target)}</span>'
        if anchor.page.id != self.page.id and self.page.id in self.book.backlinks:
            self.book.backlinks[anchor.page.id].add(self.page.id)
        if text_html is None:
            text_html = self.xref_text(anchor, mode)
        return f'<a class="xref xref-{anchor.kind}" href="{anchor.href}">{text_html}</a>'

    def xref_text(self, anchor: Anchor, mode: str = "") -> str:
        title = html.escape(anchor.title)
        if anchor.kind == "page":
            p = anchor.page
            if p.kind == "chapter":
                if mode in ("full", "title"):
                    lead = "" if mode == "title" else f"Chapter {p.number}, "
                    return f"{lead}“{html.escape(p.title)}”"
                return f"Chapter {p.number}"
            return f"“{html.escape(p.title)}”"
        if anchor.kind == "fig":
            return f"Figure {anchor.number}"
        if anchor.kind == "move":
            return f"Your Move {anchor.number}"
        elsewhere = ""
        if anchor.page.id != self.page.id:
            elsewhere = f" in {self.xref_text(self.book.anchors[anchor.page.id])}"
        if anchor.kind == "sec":
            if mode == "title":
                return f"“{title}”"
            return f"“{title}”{elsewhere}"
        label = ELEMENTS[anchor.element].label if anchor.element else "Box"
        return f"{label} “{title}”{elsewhere}" if title else f"{label}{elsewhere}"

    def label(self, name, where):
        labels = {
            "craft": ("craft", "Craft advice: practitioner experience, not research"),
            "view": ("our view", "The author’s view: argued, not proven"),
            "unverified": ("unverified", "We could not verify this; treat it with care"),
        }
        if name not in labels:
            self.report.error(f"{where}: unknown label [!{name}]; use [!craft], [!view] or [!unverified]")
            return ""
        text, tip = labels[name]
        return f'<span class="label label-{name}" title="{tip}">{text}</span>'

    # -- blocks --------------------------------------------------------------

    def blocks(self, nodes: list[Node], tight: bool = False, context: str = "") -> str:
        return "\n".join(self.block(n, tight, context) for n in nodes)

    def block(self, node: Node, tight: bool = False, context: str = "") -> str:
        k = node.kind
        if k == "para":
            text = node.text
            if context == "ask" and re.match(r"^[QA]:\s", text):
                mark = text[0]
                body = self.inline(text[2:].strip(), node)
                label = "Question" if mark == "Q" else "Answer"
                return (
                    f'<p class="qa qa-{mark.lower()}"><span class="qa-mark" aria-label="{label}">{mark}</span>'
                    f'<span class="qa-body">{body}</span></p>'
                )
            body = self.inline(text, node)
            return body if tight else f"<p>{body}</p>"
        if k == "heading":
            ident = node.attrs.get("id") or node.attrs.get("auto_id") or f"{self.page.id}-h-{node.line}"
            inner = self.inline(node.text, node)
            return (
                f'<h{node.level} id="{ident}">{inner}'
                f'<a class="h-anchor" href="#{ident}" aria-label="Link to this section">#</a></h{node.level}>'
            )
        if k == "hr":
            return '<hr>'
        if k == "quote":
            return f"<blockquote>{self.blocks(node.children)}</blockquote>"
        if k == "code":
            cls = f' class="lang-{html.escape(node.name)}"' if node.name else ""
            return f"<pre><code{cls}>{html.escape(node.text)}</code></pre>"
        if k == "list":
            tag = "ol" if node.ordered else "ul"
            start = f' start="{node.start}"' if node.ordered and node.start != 1 else ""
            items = []
            for item in node.children:
                inner = self.blocks(item.children, tight=not node.loose, context=context)
                items.append(f"<li>{inner}</li>")
            return f"<{tag}{start}>" + "".join(items) + f"</{tag}>"
        if k == "table":
            return self.table(node)
        if k == "speech":
            return self.speech(node, context)
        if k == "directive":
            return self.directive(node, context)
        self.report.error(f"{self.where(node)}: cannot render a {k}")
        return ""

    def table(self, node: Node) -> str:
        head_line, header = node.rows[0]
        # An empty top-left cell means the first column labels the rows.
        row_headers = header[0].strip() == ""
        # Tables of three or more columns become stacked cards on narrow screens; the
        # explicit roles keep their table semantics when CSS changes their display.
        stack = len(header) >= 3
        labels = [plain_text(h) for h in header]

        def cell(tag, text, i, line, scope=""):
            align = node.align[i]
            style = f' style="text-align:{align}"' if align else ""
            scope_attr = f' scope="{scope}"' if scope else ""
            role = ""
            if stack:
                role = {"col": "columnheader", "row": "rowheader"}.get(scope, "cell")
                role = f' role="{role}"'
                if tag == "td" and labels[i]:
                    role += f' data-label="{html.escape(labels[i])}"'
            return f"<{tag}{scope_attr}{role}{style}>{self.inline(text, Node('para', line))}</{tag}>"

        tr = '<tr role="row">' if stack else "<tr>"
        thead = tr + "".join(cell("th", t, i, head_line, "col") for i, t in enumerate(header)) + "</tr>"
        rows = "".join(
            tr
            + "".join(
                cell("th", t, i, line, "row") if (i == 0 and row_headers) else cell("td", t, i, line)
                for i, t in enumerate(row)
            )
            + "</tr>"
            for line, row in node.rows[1:]
        )
        if stack:
            return (
                '<div class="table-wrap table-stack" role="region" aria-label="Table" tabindex="0">'
                f'<table role="table"><thead role="rowgroup">{thead}</thead><tbody role="rowgroup">{rows}</tbody></table></div>'
            )
        return (
            '<div class="table-wrap" role="region" aria-label="Table" tabindex="0">'
            f"<table><thead>{thead}</thead><tbody>{rows}</tbody></table></div>"
        )

    def avatar(self, who: str) -> str:
        member = self.book.cast.get(who)
        if not member or not member.get("svg"):
            return ""
        self.avatar_count += 1
        return svgmod.inline_svg(member["svg"], f"av-{who}-{self.avatar_count}", "", decorative=True)

    def speech(self, node: Node, context: str) -> str:
        who = node.name
        body = self.inline(node.text, node)
        if context == "chairs":
            name = self.speakers.get(who)
            if not name:
                self.report.error(f"{self.where(node)}: inside a Two Chairs the speakers are @left: and @right:")
                name = who
            initial = html.escape(name.replace("The ", "")[:1].upper())
            return (
                f'<div class="say say-{who}"><span class="say-who chair-badge" aria-hidden="true">{initial}</span>'
                f'<div class="say-bubble"><span class="say-name">{html.escape(name)}</span> {body}</div></div>'
            )
        member = self.book.cast.get(who)
        if not member:
            self.report.error(
                f"{self.where(node)}: @{who}: is not in the cast; book.toml lists "
                + ", ".join(sorted(self.book.cast))
            )
            return f"<p>{body}</p>"
        return (
            f'<div class="say say-{who}"><span class="say-who" aria-hidden="true">{self.avatar(who)}</span>'
            f'<div class="say-bubble"><span class="say-name">{html.escape(member["name"])}</span> {body}</div></div>'
        )

    # -- the element catalogue ---------------------------------------------------

    def head(self, name: str, label: str, title_html: str, extra: str = "") -> str:
        title = f'<span class="el-title">{title_html}</span>' if title_html else ""
        return (
            f'<header class="el-head">{icon(name)}<span class="el-label">{html.escape(label)}</span>'
            f"{title}{extra}</header>"
        )

    def directive(self, node: Node, context: str) -> str:
        name = node.name
        el = ELEMENTS.get(name)
        if not el:
            return ""
        ident = node.attrs.get("id")
        id_attr = f' id="{ident}"' if ident else ""
        cls = f" {node.attrs['class']}" if node.attrs.get("class") else ""
        title_html = self.inline(node.title, node) if node.title else ""
        where = self.where(node)

        if name == "figure":
            return self.figure(node)
        if name == "answer":
            label = html.escape(node.attrs.get("label", "Reveal one way to play it"))
            return (
                f'<details class="answer"{id_attr}><summary>{label}</summary>'
                f'<div class="answer-body">{self.blocks(node.children)}</div></details>'
            )
        if name == "scene":
            slug = node.attrs.get("slug")
            slug_html = f'<p class="scene-slug">{html.escape(slug)}</p>' if slug else ""
            return (
                f'<div class="el el-scene{cls}"{id_attr} role="group" aria-label="Scene">'
                f"{slug_html}{self.blocks(node.children, context='scene')}</div>"
            )
        if name == "move":
            number = node.attrs.get("_number", "")
            return (
                f'<section class="el el-move{cls}"{id_attr} aria-label="Your Move {number}">'
                f'{self.head("move", f"Your Move {number}", title_html)}'
                f'<div class="el-body">{self.blocks(node.children, context="move")}</div></section>'
            )
        if name == "chairs":
            left, right = node.attrs.get("left", "Left"), node.attrs.get("right", "Right")
            self.speakers = {"left": left, "right": right}
            topic = title_html or f"{html.escape(left)} vs. {html.escape(right)}"
            body = self.blocks(node.children, context="chairs")
            self.speakers = {}
            return (
                f'<section class="el el-chairs{cls}"{id_attr} aria-label="Two Chairs">'
                f'{self.head("chairs", "Two Chairs", topic)}'
                f'<p class="chairs-cast"><span class="chair-badge" aria-hidden="true">{html.escape(left.replace("The ", "")[:1])}</span> {html.escape(left)}'
                f' <span class="chairs-vs">and</span> <span class="chair-badge chair-right" aria-hidden="true">{html.escape(right.replace("The ", "")[:1])}</span> {html.escape(right)}</p>'
                f'<div class="el-body">{body}</div></section>'
            )
        if name == "myth":
            verdict = node.attrs.get("verdict", "")
            grade = node.attrs.get("grade", "")
            if verdict not in VERDICTS:
                self.report.error(f"{where}: verdict must be one of {', '.join(VERDICTS)}")
                verdict = "busted"
            if grade not in GRADES:
                self.report.error(f"{where}: grade must be one of {', '.join(GRADES)}")
                grade = "weak"
            if not node.title:
                self.report.error(f"{where}: a Myth Check states the myth as its title")
            stamp = f'<span class="stamp stamp-{verdict}">{VERDICTS[verdict]}</span>'
            meta = f'<p class="el-meta">Strength of the evidence behind this verdict: {grade_badge(grade)}</p>'
            return (
                f'<aside class="el el-myth{cls}"{id_attr} aria-label="Myth Check">'
                f'{self.head("myth", "Myth Check", title_html, stamp)}'
                f'<div class="el-body">{meta}{self.blocks(node.children)}</div></aside>'
            )
        if name == "receipts":
            key = node.attrs.get("source")
            grade = node.attrs.get("grade")
            line = ""
            if key:
                src = self.book.sources.get(key)
                if not src:
                    self.report.error(f"{where}: receipts source {key!r} is not in any bibliography file")
                else:
                    grade = grade or src.grade
                    line = f'<p class="receipt-src">{html.escape(src.short())} {self.cite([(key, False, "")], where)}</p>'
            if grade not in GRADES:
                self.report.error(f"{where}: Receipts need grade=... or a source=... from the bibliography")
                grade = "weak"
            meta = f'<p class="el-meta">{grade_badge(grade)}</p>'
            return (
                f'<aside class="el el-receipts{cls}"{id_attr} aria-label="Receipts">'
                f'{self.head("receipts", "Receipts", title_html)}'
                f'<div class="el-body">{line}{meta}{self.blocks(node.children)}</div></aside>'
            )
        if name == "field":
            regions = [r.strip() for r in node.attrs.get("regions", "").split(",") if r.strip()]
            chips = "".join(f'<span class="chip">{html.escape(r)}</span>' for r in regions)
            return (
                f'<aside class="el el-field{cls}"{id_attr} aria-label="Field Note">'
                f'{self.head("field", "Field Note", title_html)}'
                f'<p class="chips" aria-label="Regions">{chips}</p>'
                f'<div class="el-body">{self.blocks(node.children)}</div></aside>'
            )
        if name == "craft":
            by = node.attrs.get("by", "craft")
            if by not in CRAFT_KINDS:
                self.report.error(f"{where}: by= must be 'craft' or 'author'")
                by = "craft"
            label, note = CRAFT_KINDS[by]
            return (
                f'<aside class="el el-craft el-craft-{by}{cls}"{id_attr} aria-label="{label}">'
                f'{self.head("craft", label, title_html)}'
                f'<p class="el-meta">{note}</p>'
                f'<div class="el-body">{self.blocks(node.children)}</div></aside>'
            )
        if name == "further":
            target = node.attrs.get("ref", "more")
            link = self.xref(target, None, "title", where)
            return (
                f'<aside class="el el-further{cls}"{id_attr} aria-label="Going Further">'
                f'{self.head("further", "Going Further", link)}'
                f'<div class="el-body">{self.blocks(node.children)}</div></aside>'
            )
        if name == "resource":
            key = node.attrs.get("source", "")
            src = self.book.sources.get(key)
            if not src:
                self.report.error(f"{where}: resource source {key!r} is not in any bibliography file")
                return ""
            evidence = src.kind in ("evidence", "review", "data", "law")
            kind_label = "Evidence-based" if evidence else ("Theory" if src.kind == "theory" else "Practitioner view")
            title = f'<a href="{html.escape(src.link())}" class="ext" rel="noopener"><cite>{html.escape(src.title.rstrip("."))}</cite></a>'
            byline = f'<span class="resource-by">{src.authors_html()} ({html.escape(src.year)}) {self.cite([(key, False, "")], where)}</span>'
            return (
                f'<aside class="el el-resource el-resource-{"evidence" if evidence else "practice"}{cls}"{id_attr} aria-label="Resource">'
                f'{self.head("resource", kind_label, title)}<p class="el-meta">{byline}</p>'
                f'<div class="el-body">{self.blocks(node.children)}</div></aside>'
            )
        if name in ("flashback", "coming"):
            target = node.attrs.get("ref", "")
            link = self.xref(target, None, "full", where)
            label = ELEMENTS[name].label
            return (
                f'<aside class="el el-{name}{cls}"{id_attr} aria-label="{label}">'
                f'{self.head(name, label, link)}'
                f'<div class="el-body">{self.blocks(node.children)}</div></aside>'
            )
        # pause, ask, trapdoor, rewind: a labelled box around Markdown
        tag = el.tag
        return (
            f'<{tag} class="el el-{name}{cls}"{id_attr} aria-label="{el.label}">'
            f'{self.head(name, el.label, title_html)}'
            f'<div class="el-body">{self.blocks(node.children, context=name)}</div></{tag}>'
        )

    def figure(self, node: Node) -> str:
        where = self.where(node)
        ident = node.attrs.get("id", "")
        number = node.attrs.get("_number", "")
        size = node.attrs.get("size", "")
        if size not in FIGURE_SIZES:
            self.report.error(f"{where}: size= must be small or wide")
        alt = node.attrs.get("alt", "")
        caption_nodes = []
        for child in node.children:
            if child.kind == "para" and child.text.lower().startswith("alt:") and not alt:
                alt = child.text[4:].strip()
            else:
                caption_nodes.append(child)
        alt = plain_text(alt)
        if len(alt) < 25:
            self.report.error(f"{where}: figure {ident} needs alt text (a paragraph starting 'Alt:'), at least 25 characters")
        if not caption_nodes:
            self.report.error(f"{where}: figure {ident} needs a caption paragraph")
        svg_text = self.book.figures(node.attrs.get("src", ""), where)
        markup = svgmod.inline_svg(svg_text, ident.replace(".", "-"), alt) if svg_text else ""
        caption = self.blocks(caption_nodes, tight=len(caption_nodes) == 1)
        size_cls = f" fig-{size}" if size else ""
        src = html.escape(node.attrs.get("src", ""))
        return (
            f'<figure class="fig-wrap{size_cls}" id="{ident}">{markup}'
            f'<figcaption><span class="fig-num">Figure {number}</span> {caption} '
            f'<a class="fig-open" href="figures/{src}">Open full size</a></figcaption></figure>'
        )

    # -- references -------------------------------------------------------------

    def references(self) -> str:
        if not self.cites:
            return ""
        items = []
        for key, n in sorted(self.cites.items(), key=lambda kv: kv[1]):
            src = self.book.sources[key]
            backs = " ".join(
                f'<a class="ref-back" href="#{m}" aria-label="Back to citation {n}, use {i}">↩</a>'
                for i, m in enumerate(self.cite_marks[key], 1)
            )
            items.append(
                f'<li id="ref-{self.page.id}-{n}" value="{n}"><p class="ref-main">{src.full_html()} {backs}</p>'
                f'<p class="ref-meta">{src.meta_html()}</p>{src.notes_html()}</li>'
            )
        return "<ol class=\"refs\">" + "".join(items) + "</ol>"
