"""Assembling the book: read sources, run the checks, write the static site."""

from __future__ import annotations

import html
import re
import shutil
import tomllib
from pathlib import Path

from . import svg as svgmod
from .bib import GRADES, grade_badge, load_sources
from .errors import BuildError, Report
from .inline import plain_text, render_inline
from .markdown import parse_document
from .render import Book, Page, Renderer

PLACEHOLDER_CASE_RE = re.compile(r"\b(?:TODO|TK|TBD|FIXME|XXX)\b")
LOREM_RE = re.compile(r"\blorem\b", re.I)
FONTS_URL = (
    "https://fonts.googleapis.com/css2?"
    "family=Bricolage+Grotesque:opsz,wght@12..96,400..800"
    "&family=Caveat:wght@500..700"
    "&family=Literata:ital,opsz,wght@0,7..72,400..700;1,7..72,400..700"
    "&display=swap"
)


class Site:
    def __init__(self, root: Path, out: Path | None = None):
        self.root = root
        self.book_dir = root / "book"
        self.out = out or (root / "docs")
        self.report = Report()
        self.config: dict = {}
        self.pages: list[Page] = []
        self.parts: dict = {}
        self.figure_cache: dict[str, str | None] = {}
        self.canonical_css = ""

    # -- loading -----------------------------------------------------------------

    def rel(self, path: Path) -> str:
        return path.relative_to(self.root).as_posix()

    def load(self) -> None:
        cfg_path = self.book_dir / "book.toml"
        self.config = tomllib.loads(cfg_path.read_text(encoding="utf-8"))
        self.canonical_css = (self.book_dir / "figures" / "figure.css").read_text(encoding="utf-8")
        self.parts = {p["id"]: p for p in self.config.get("parts", [])}
        chapter_files = sorted((self.book_dir / "chapters").glob("*.md"))
        claimed: set = set()
        for entry in self.config["pages"]:
            pid = entry["id"]
            kind = entry["kind"]
            if kind == "chapter":
                matches = [f for f in chapter_files if f.name.startswith(pid + "-")]
                if len(matches) > 1:
                    self.report.error(f"book/chapters: more than one file starts with {pid}-")
                path = matches[0] if matches else None
                claimed.update(matches)
                href = f"{pid}.html"
                label = str(entry["number"])
            else:
                path = self.book_dir / entry["file"] if entry.get("file") else None
                href = entry["href"]
                label = entry["label"]
            page = Page(
                id=pid,
                kind=kind,
                title=entry["title"],
                href=href,
                label=label,
                number=entry.get("number"),
                part=entry.get("part", ""),
                summary=entry.get("summary", ""),
                covers=list(entry.get("covers", [])),
                planned=[(sec["id"], sec["title"]) for sec in entry.get("sections", [])],
            )
            if path and path.exists():
                page.rel = self.rel(path)
                page.written = True
                try:
                    meta, nodes = parse_document(path.read_text(encoding="utf-8"), page.rel)
                except BuildError as exc:
                    self.report.error(str(exc))
                    meta, nodes = {}, []
                if meta.get("id") != pid:
                    self.report.error(f"{page.rel}: front matter must say 'id: {pid}'")
                page.meta = meta
                page.nodes = nodes
                page.status = meta.get("status", "draft")
                if page.status not in ("draft", "review", "final"):
                    self.report.error(f"{page.rel}: status must be draft, review or final")
            else:
                page.rel = f"book/book.toml ({pid})"
            self.pages.append(page)
        for f in chapter_files:
            if f not in claimed:
                self.report.error(f"{self.rel(f)}: no chapter in book.toml has an id matching this file name")

    def load_cast(self) -> dict:
        cast = {}
        for key, member in self.config.get("cast", {}).items():
            entry = dict(member)
            avatar = self.book_dir / "figures" / member["avatar"]
            text = self.figure_text(member["avatar"], f"book/book.toml [cast.{key}]")
            entry["svg"] = text
            entry["key"] = key
            if not avatar.exists():
                self.report.error(f"book/book.toml [cast.{key}]: avatar {member['avatar']} does not exist")
            cast[key] = entry
        return cast

    def figure_text(self, src: str, where: str) -> str | None:
        if src in self.figure_cache:
            return self.figure_cache[src]
        path = (self.book_dir / "figures" / src).resolve()
        figures_root = (self.book_dir / "figures").resolve()
        text = None
        if figures_root not in path.parents or path.suffix != ".svg":
            self.report.error(f"{where}: figure src {src!r} must be an .svg file under book/figures/")
        elif not path.exists():
            self.report.error(f"{where}: figure file book/figures/{src} does not exist")
        else:
            text = path.read_text(encoding="utf-8")
            problems = svgmod.check_svg(text, f"book/figures/{src}", self.canonical_css)
            for p in problems:
                self.report.error(p)
            if problems:
                text = None
        self.figure_cache[src] = text
        return text

    def bibliography_paths(self) -> list[Path]:
        paths = []
        for pattern in self.config.get("bibliography", {}).get("files", ["book/sources/*.yaml"]):
            paths.extend(sorted(self.root.glob(pattern)))
        return sorted(set(paths))

    # -- checks ------------------------------------------------------------------

    def check_placeholders(self) -> None:
        texts: list[tuple[str, str]] = []
        for page in self.pages:
            if page.written:
                texts.append((page.rel, (self.root / page.rel).read_text(encoding="utf-8")))
        texts.append(("book/book.toml", (self.book_dir / "book.toml").read_text(encoding="utf-8")))
        for svgfile in sorted((self.book_dir / "figures").rglob("*.svg")):
            texts.append((self.rel(svgfile), svgmod.svg_text_content(svgfile.read_text(encoding="utf-8"))))
        for rel, text in texts:
            for lineno, line in enumerate(text.split("\n"), 1):
                m = PLACEHOLDER_CASE_RE.search(line) or LOREM_RE.search(line)
                if m:
                    self.report.error(f"{rel}:{lineno}: placeholder text {m.group(0)!r} must not ship")

    # -- the build -----------------------------------------------------------------

    def build(self, write: bool = True) -> Report:
        try:
            self.load()
        except (OSError, tomllib.TOMLDecodeError, KeyError) as exc:
            self.report.error(f"book/book.toml: {exc}")
            return self.report
        sources = load_sources(self.bibliography_paths(), self.root, self.report)
        cast = self.load_cast()
        self.book = Book(self.config, self.pages, sources, cast, self.figure_text, self.report)
        for page in self.pages:
            self.book.collect(page)
        for page in self.pages:
            for ident, title in page.planned:
                anchor = self.book.anchors.get(ident)
                if page.written and (not anchor or anchor.page is not page):
                    self.report.error(
                        f"{page.rel}: book.toml promises a section {{#{ident}}} ({title}) that other pages may link to; add it"
                    )
        for page in self.pages:
            self.book.render(page)
        for page in self.pages:
            if page.written and page.kind == "chapter" and not any(
                n.kind == "directive" and n.name == "rewind" for n in page.nodes
            ):
                self.report.warn(f"{page.rel}: chapters end with a '::: rewind' summary")
        self.check_placeholders()
        if write and self.report.ok:
            self.write()
        return self.report

    # -- output --------------------------------------------------------------------

    def write(self) -> None:
        if self.out.exists():
            shutil.rmtree(self.out)
        (self.out / "assets").mkdir(parents=True)
        css = (self.book_dir / "theme" / "book.css").read_text(encoding="utf-8")
        css += "\n/* ---- figure vocabulary (book/figures/figure.css) ---- */\n" + self.canonical_css
        (self.out / "assets" / "book.css").write_text(css, encoding="utf-8")
        shutil.copyfile(self.book_dir / "theme" / "icon.svg", self.out / "assets" / "icon.svg")
        for svgfile in sorted((self.book_dir / "figures").rglob("*.svg")):
            dest = self.out / "figures" / svgfile.relative_to(self.book_dir / "figures")
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(svgfile, dest)
        (self.out / ".nojekyll").write_text("", encoding="utf-8")
        for i, page in enumerate(self.pages):
            prev_page = self.pages[i - 1] if i > 0 else None
            next_page = self.pages[i + 1] if i + 1 < len(self.pages) else None
            body = self.page_html(page) if page.written else self.stub_html(page)
            doc = self.document(page.title, page.summary, body + self.pager(prev_page, next_page), page.kind)
            (self.out / page.href).write_text(doc, encoding="utf-8")
        (self.out / "index.html").write_text(self.index_html(), encoding="utf-8")
        refs = self.document("References", "Every source the book cites, with its evidence grade.", self.references_html(), "refs")
        (self.out / "references.html").write_text(refs, encoding="utf-8")

    def inline(self, text: str, where: str) -> str:
        """Inline text outside any page (summaries on the contents page)."""
        contents = Page(id="contents", kind="front", title="Contents", href="index.html", label="", rel=where)
        return render_inline(text, Renderer(self.book, contents), where)

    def kicker(self, page: Page) -> str:
        if page.kind == "chapter":
            part = self.parts.get(page.part)
            if part:
                return f'{html.escape(part["label"])} · {html.escape(part["title"])}'
            return "Opening"
        if page.kind == "epilogue":
            return "Closing"
        if page.kind == "appendix":
            return "Back matter"
        return "Before you start"

    def status_badge(self, page: Page) -> str:
        if not page.written:
            return '<span class="status status-planned">In production</span>'
        if page.status == "final":
            return ""
        return f'<span class="status status-{page.status}">{page.status.capitalize()}</span>'

    def page_head(self, page: Page) -> str:
        number = f'<p class="chapter-num">Chapter {page.number}</p>' if page.kind == "chapter" else ""
        return (
            f'<header class="page-head"><p class="kicker">{self.kicker(page)}</p>{number}'
            f"<h1>{html.escape(page.title)}</h1>{self.status_badge(page)}</header>"
        )

    def page_html(self, page: Page) -> str:
        toc = ""
        if len(page.toc) > 1:
            items = "".join(f'<li><a href="#{i}">{html.escape(t)}</a></li>' for i, t in page.toc)
            label = "In this chapter" if page.kind == "chapter" else "On this page"
            toc = f'<nav class="mini-toc" aria-label="{label}"><p class="mini-toc-h">{label}</p><ol>{items}</ol></nav>'
        threads = ""
        backs = sorted(self.book.backlinks.get(page.id, []), key=lambda pid: self.page_index(pid))
        if backs:
            links = ", ".join(
                f'<a href="{self.book.anchors[b].page.href}">{self.short_name(self.book.anchors[b].page)}</a>' for b in backs
            )
            threads = f'<aside class="threads" aria-label="Threads"><p><span class="threads-h">Threads into this {"chapter" if page.kind == "chapter" else "page"}:</span> {links}</p></aside>'
        refs = ""
        if page.refs_html:
            refs = (
                '<section class="chapter-refs" aria-labelledby="refs-h">'
                f'<h2 id="refs-h">References for this {"chapter" if page.kind == "chapter" else "page"}</h2>'
                '<p class="refs-intro">Each source carries its evidence grade; '
                '<a href="references.html#grades">how we grade</a>.</p>'
                f"{page.refs_html}</section>"
            )
        return (
            f'<main id="main" class="page page-{page.kind}">{self.page_head(page)}{toc}'
            f'<article class="prose">{page.body_html}</article>{threads}{refs}'
        )

    def page_index(self, pid: str) -> int:
        for i, p in enumerate(self.pages):
            if p.id == pid:
                return i
        return 0

    def short_name(self, page: Page) -> str:
        return f"Chapter {page.number}" if page.kind == "chapter" else html.escape(page.title)

    def stub_html(self, page: Page) -> str:
        covers = "".join(f"<li>{self.inline(c, page.rel)}</li>" for c in page.covers)
        covers_html = f"<h2>What it will cover</h2><ul>{covers}</ul>" if covers else ""
        if page.planned:
            sections = "".join(f'<li id="{html.escape(i)}">{html.escape(t)}</li>' for i, t in page.planned)
            covers_html += f"<h2>Planned sections</h2><ul>{sections}</ul>"
        return (
            f'<main id="main" class="page page-stub">{self.page_head(page)}'
            '<article class="prose"><aside class="el el-coming" aria-label="In production">'
            '<header class="el-head"><span class="el-label">In production</span></header>'
            f'<div class="el-body"><p>This {"chapter" if page.kind == "chapter" else "page"} is being researched and written. '
            "The plan below is the brief its writer works from; it may change as the evidence comes in.</p></div></aside>"
            f"<p class=\"lede\">{self.inline(page.summary, page.rel)}</p>{covers_html}</article>"
        )

    def pager(self, prev_page: Page | None, next_page: Page | None) -> str:
        def link(p: Page | None, rel: str, arrow: str) -> str:
            if not p:
                return "<span></span>"
            label = "Previous" if rel == "prev" else "Next"
            return (
                f'<a class="pager-{rel}" rel="{rel}" href="{p.href}"><span class="pager-dir">{arrow} {label}</span>'
                f'<span class="pager-title">{self.short_name(p)}{": " + html.escape(p.title) if p.kind == "chapter" else ""}</span></a>'
            )
        return (
            f'<nav class="pager" aria-label="Previous and next pages">{link(prev_page, "prev", "←")}'
            f'{link(next_page, "next", "→")}</nav></main>'
        )

    def toc_html(self) -> str:
        groups: list[tuple[str, str, list[Page]]] = []
        front = [p for p in self.pages if p.kind == "front"]
        groups.append(("Before you start", "", front))
        opening = [p for p in self.pages if p.kind == "chapter" and not p.part]
        groups.append(("Opening", "", opening))
        for part in self.config.get("parts", []):
            chapters = [p for p in self.pages if p.part == part["id"]]
            groups.append((f'{part["label"]}: {part["title"]}', part.get("subtitle", ""), chapters))
        closing = [p for p in self.pages if p.kind == "epilogue"]
        groups.append(("Closing", "", closing))
        out = []
        for title, sub, pages in groups:
            if not pages:
                continue
            items = []
            for p in pages:
                num = f'<span class="toc-num">{p.number}</span>' if p.kind == "chapter" else '<span class="toc-num toc-num-blank"></span>'
                items.append(
                    f'<li class="toc-item{"" if p.written else " toc-planned"}">{num}<div class="toc-text">'
                    f'<a href="{p.href}">{html.escape(p.title)}</a> {self.status_badge(p)}'
                    f'<p class="toc-sum">{self.inline(p.summary, "book/book.toml")}</p></div></li>'
                )
            sub_html = f'<p class="toc-group-sub">{html.escape(sub)}</p>' if sub else ""
            out.append(f'<section class="toc-group"><h3>{html.escape(title)}</h3>{sub_html}<ol class="toc-list">{"".join(items)}</ol></section>')
        return "".join(out)

    def index_html(self) -> str:
        b = self.config["book"]
        written = sum(1 for p in self.pages if p.written and p.kind == "chapter")
        total = sum(1 for p in self.pages if p.kind == "chapter")
        cover = ""
        cover_src = b.get("cover")
        if cover_src:
            text = self.figure_text(cover_src, "book/book.toml [book.cover]")
            if text:
                cover = svgmod.inline_svg(text, "cover", b["cover_alt"])
        first = next((p for p in self.pages if p.written), self.pages[0])
        body = (
            '<main id="main" class="page page-index">'
            f'<header class="cover"><div class="cover-art">{cover}</div><div class="cover-text">'
            f'<h1 class="cover-title">{html.escape(b["title"])}</h1>'
            f'<p class="cover-sub">{html.escape(b["subtitle"])}</p>'
            f'<p class="cover-blurb">{self.inline(b["blurb"], "book/book.toml")}</p>'
            f'<p class="cover-cta"><a class="button" href="{first.href}">Start reading</a>'
            f'<a class="button button-quiet" href="ch01.html">Jump to Chapter 1</a></p>'
            f'<p class="cover-status">Status: {written} of {total} chapters written; the rest are in production. '
            f'Chapters marked <span class="status status-planned">In production</span> show their plan.</p>'
            "</div></header>"
            f'<section class="toc" id="contents" aria-labelledby="contents-h"><h2 id="contents-h">Contents</h2>{self.toc_html()}'
            f'<section class="toc-group"><h3>Back matter</h3><ol class="toc-list">{self.appendix_items()}<li class="toc-item"><span class="toc-num toc-num-blank"></span>'
            '<div class="toc-text"><a href="references.html">References</a><p class="toc-sum">Every source the book cites, '
            "with its evidence grade and the chapters that use it.</p></div></li></ol></section></section></main>"
        )
        return self.document(b["title"], b["subtitle"], body, "index", title_is_book=True)

    def appendix_items(self) -> str:
        items = []
        for p in self.pages:
            if p.kind == "appendix":
                items.append(
                    f'<li class="toc-item{"" if p.written else " toc-planned"}"><span class="toc-num toc-num-blank"></span><div class="toc-text">'
                    f'<a href="{p.href}">{html.escape(p.title)}</a> {self.status_badge(p)}'
                    f'<p class="toc-sum">{self.inline(p.summary, "book/book.toml")}</p></div></li>'
                )
        return "".join(items)

    def references_html(self) -> str:
        legend = "".join(
            f"<li>{grade_badge(g)} <span>{html.escape(desc)}</span></li>"
            for g, desc in (
                ("strong", "Meta-analyses, large randomised or natural experiments, official statistics and the text of laws. Hard to overturn."),
                ("moderate", "Single well-designed studies, large surveys with clear methods, careful reviews. Probably right; could shift."),
                ("weak", "Small or non-random samples, vendor surveys, case studies, expert opinion. A hint, not a finding."),
                ("myth-or-unsupported", "Claims contradicted by stronger evidence, retracted, or with no traceable support; we cite these only to show where a myth comes from."),
            )
        )
        keys = sorted(self.book.cited_in, key=lambda k: (self.book.sources[k].short().lower(), k))
        items = []
        for key in keys:
            src = self.book.sources[key]
            where = ", ".join(
                f'<a href="{self.book.anchors[pid].page.href}">{self.short_name(self.book.anchors[pid].page)}</a>'
                for pid in sorted(self.book.cited_in[key], key=self.page_index)
            )
            items.append(
                f'<li id="src-{html.escape(key)}"><p class="ref-main">{src.full_html()}</p>'
                f'<p class="ref-meta">{src.meta_html()} \u00b7 cited in {where}</p>{src.notes_html()}</li>'
            )
        counts = {g: sum(1 for k in keys if self.book.sources[k].grade == g) for g in GRADES}
        short = {"strong": "strong", "moderate": "moderate", "weak": "weak", "myth-or-unsupported": "myth or unsupported"}
        tally = ", ".join(f"{counts[g]} {short[g]}" for g in GRADES)
        return (
            '<main id="main" class="page page-refs"><header class="page-head"><p class="kicker">Back matter</p>'
            "<h1>References</h1></header><article class=\"prose\">"
            '<section aria-labelledby="grades"><h2 id="grades">How we grade evidence</h2>'
            "<p>Every factual claim in this book points at a source, and every source is graded for how much weight it can bear. "
            "Advice that rests on experience rather than research is labelled "
            '<span class="label label-craft">craft</span>, and our own arguments are labelled '
            '<span class="label label-view">our view</span>.</p>'
            f'<ul class="grade-legend">{legend}</ul></section>'
            f'<section aria-labelledby="all-sources"><h2 id="all-sources">All cited sources</h2><p>{len(keys)} sources: {tally}.</p>'
            f'<ul class="refs refs-global">{"".join(items)}</ul></section></article>'
        )

    def document(self, title: str, description: str, body: str, kind: str, title_is_book: bool = False) -> str:
        b = self.config["book"]
        full_title = html.escape(title if title_is_book else f"{title} · {b['title']}")
        desc = html.escape(plain_text(description or b["subtitle"]))
        return f"""<!doctype html>
<html lang="{b.get('language', 'en')}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full_title}</title>
<meta name="description" content="{desc}">
<meta name="color-scheme" content="light dark">
<link rel="icon" href="assets/icon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS_URL.replace('&', '&amp;')}">
<link rel="stylesheet" href="assets/book.css">
<script>try{{var t=localStorage.getItem("theme");if(t==="light"||t==="dark")document.documentElement.setAttribute("data-theme",t)}}catch(e){{}}</script>
</head>
<body class="kind-{kind}">
<a class="skip" href="#main">Skip to content</a>
<header class="site-head"><div class="site-head-inner">
<a class="brand" href="index.html"><svg class="brand-mark" viewBox="0 0 32 32" aria-hidden="true" focusable="false"><rect x="3" y="7" width="12" height="18" rx="2"/><path d="M19 9h10v14H19z"/><path d="M19 13h10M19 19h10"/></svg><span>{html.escape(b['title'])}</span></a>
<nav class="site-nav" aria-label="Book"><a href="index.html#contents">Contents</a><a href="references.html">References</a></nav>
<button class="theme-toggle" type="button" aria-label="Colour theme: automatic">Auto</button>
</div></header>
{body}
<footer class="site-foot"><p>{html.escape(b['title'])} &middot; {html.escape(b['copyright'])} &middot; <a href="{b['repo_url']}/blob/main/LICENSE">MIT License</a> &middot; <a href="{b['repo_url']}">Source on GitHub</a></p>
<p>Characters and companies in this book are fictional. Sources are graded; see <a href="references.html#grades">how we grade evidence</a>.</p></footer>
<script>
(function(){{var b=document.querySelector(".theme-toggle"),r=document.documentElement,order=["auto","light","dark"],names={{auto:"Auto",light:"Light",dark:"Dark"}};
function cur(){{return r.getAttribute("data-theme")||"auto"}}
function show(){{var c=cur();b.textContent=names[c];b.setAttribute("aria-label","Colour theme: "+(c==="auto"?"automatic":c)+". Activate to change.")}}
b.addEventListener("click",function(){{var n=order[(order.indexOf(cur())+1)%3];if(n==="auto")r.removeAttribute("data-theme");else r.setAttribute("data-theme",n);try{{if(n==="auto")localStorage.removeItem("theme");else localStorage.setItem("theme",n)}}catch(e){{}}show()}});show();
window.addEventListener("beforeprint",function(){{document.querySelectorAll("details").forEach(function(d){{d.setAttribute("data-was-open",d.open?"1":"0");d.open=true}})}});
window.addEventListener("afterprint",function(){{document.querySelectorAll("details[data-was-open]").forEach(function(d){{d.open=d.getAttribute("data-was-open")==="1";d.removeAttribute("data-was-open")}})}});
}})();
</script>
</body>
</html>
"""


def sync_figure_styles(root: Path) -> list[str]:
    """Rewrite every figure's <style> block from book/figures/figure.css."""
    css = (root / "book" / "figures" / "figure.css").read_text(encoding="utf-8")
    changed = []
    for svgfile in sorted((root / "book" / "figures").rglob("*.svg")):
        text = svgfile.read_text(encoding="utf-8")
        new = svgmod.sync_style(text, css)
        if new != text:
            svgfile.write_text(new, encoding="utf-8")
            changed.append(svgfile.relative_to(root).as_posix())
    return changed
