"""The bibliography: loading, validating and formatting sources.

Every source lives in a YAML registry with one schema, shared by the
researchers (``research/part1/sources.yaml``, ``research/part2/sources.yaml``)
and the chapter writers (``book/sources/chNN.yaml``). Each top-level key is the
citation key a chapter uses, as in ``[@sackett2022]``::

    sackett2022:
      type: article
      authors: ['Sackett, Paul R.', 'Zhang, Charlene', 'Berry, Christopher M.', 'Lievens, Filip']
      year: 2022
      title: Revisiting meta-analytic estimates of validity in personnel selection
      container: Journal of Applied Psychology
      volume: '107'
      issue: '11'
      pages: 2040-2068
      doi: 10.1037/apl0000994
      url: https://pubmed.ncbi.nlm.nih.gov/34968080/
      url_checked: '2026-10-25'
      url_note: Abstract read on PubMed.
      kind: evidence
      design: meta-analysis
      supports: >-
        What the source shows, as we use it.
      sample: Meta-analytic summary of prior meta-analyses.
      grade: strong
      caveats: Its limits.

The Part I registry names two fields differently (``venue`` for
``container``, ``accessed`` for ``url_checked``) and marks commercial sources
with ``commercial: true``; both spellings are accepted and normalised here.

The same key may appear in more than one registry (the researchers expect
overlaps); the build keeps the first copy when both point at the same work
(same DOI, or same URL) and fails when they disagree. A key marked
``deprecated`` stays readable but may not be cited.
"""

from __future__ import annotations

import html
import re
from dataclasses import dataclass, field
from pathlib import Path

from . import yamlsub

GRADES = {
    "strong": ("Strong evidence", 3),
    "moderate": ("Moderate evidence", 2),
    "weak": ("Weak evidence", 1),
    "myth-or-unsupported": ("Myth or unsupported", 0),
}
TYPES = {
    "article", "book", "chapter", "report", "web", "magazine", "news", "proceedings-article",
    "conference-paper", "working-paper", "industry-report", "industry-study", "industry-survey",
    "government", "statute", "law", "dataset", "talk", "post", "preprint", "thesis", "note",
}
BOOKLIKE = {"book", "report", "thesis", "dataset", "industry-report", "working-paper", "government"}
KINDS = {"evidence", "review", "theory", "data", "practitioner", "law"}
FLAGS = {
    "retracted": "retracted",
    "commercial": "commercial source",
    "self-interested": "self-interested source",
    "practitioner": "practitioner writing",
    "not-peer-reviewed": "not peer-reviewed",
    "coauthor-with-retractions": "a co-author has retractions elsewhere",
}
KEY_RE = re.compile(r"^[a-z0-9][a-z0-9_.-]*$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
TEXT_FIELDS = (
    "type", "title", "container", "publisher", "volume", "issue", "pages", "edition", "doi", "url",
    "url_checked", "url_note", "url_opened", "kind", "design", "supports", "sample", "grade", "caveats",
    "conflicts", "deprecated",
)
LIST_FIELDS = ("authors", "flags", "topics", "secondary_urls")
ALIASES = {"venue": "container", "accessed": "url_checked"}
ORG_WORDS = {
    "bureau", "department", "office", "organization", "organisation", "agency", "commission", "center",
    "centre", "institute", "council", "association", "society", "federal", "reserve", "bank", "inc", "ltd",
    "llc", "group", "university", "ministry", "government", "survey", "statistics", "research", "network",
    "labs", "lab", "media", "press", "foundation", "company", "corporation", "partners", "team", "staff",
    "editors", "board", "court", "union", "eeoc", "ftc", "gov.uk", "re:work", "google", "gallup", "pew",
}


def split_name(name: str) -> tuple[str, str]:
    """(family, given) for a person; (name, "") for an organisation.

    Registries write people as "Family, Given" (Part II) or "Given Family"
    (Part I, as Crossref gives them). A comma-free name of two or three
    capitalised words with no institutional word in it is read as a person.
    """
    name = name.strip()
    if "," in name:
        fam, given = name.split(",", 1)
        return fam.strip(), given.strip()
    words = name.split()
    particles = {"van", "von", "de", "der", "da", "di", "du", "la", "le"}
    looks_personal = 2 <= len(words) <= 4 and all(
        (w[:1].isupper() or w in particles) and re.fullmatch(r"[A-Za-z\u00C0-\u024F.'\-]+", w) for w in words
    )
    if looks_personal and not any(w.lower().strip(".") in ORG_WORDS for w in words):
        i = len(words) - 1
        while i > 1 and words[i - 1].lower() in particles:
            i -= 1
        return " ".join(words[i:]), " ".join(words[:i])
    return name, ""


def _norm_title(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", title.lower())


@dataclass
class Source:
    key: str
    origin: str
    type: str = ""
    title: str = ""
    year: str = ""
    grade: str = ""
    authors: list = field(default_factory=list)
    container: str = ""
    publisher: str = ""
    volume: str = ""
    issue: str = ""
    pages: str = ""
    edition: str = ""
    doi: str = ""
    url: str = ""
    url_checked: str = ""
    url_note: str = ""
    url_opened: str = ""
    kind: str = ""
    design: str = ""
    supports: str = ""
    sample: str = ""
    caveats: str = ""
    conflicts: str = ""
    deprecated: str = ""
    flags: list = field(default_factory=list)
    topics: list = field(default_factory=list)
    secondary_urls: list = field(default_factory=list)

    # -- formatting --------------------------------------------------------

    def family_names(self) -> list[str]:
        return [split_name(a)[0] for a in self.authors]

    def short(self) -> str:
        """``Sackett et al. 2022``, ``Axelrod & Hamilton 1981``, ``World Health Organization 2019``."""
        fam = self.family_names()
        if len(fam) == 1:
            who = fam[0]
        elif len(fam) == 2:
            who = f"{fam[0]} & {fam[1]}"
        else:
            who = f"{fam[0]} et al."
        return f"{who} {self.year}"

    def authors_html(self) -> str:
        names = []
        for a in self.authors:
            fam, given = split_name(a)
            if given:
                initials = " ".join(f"{g[0]}." for g in re.split(r"[\s.]+", given) if g)
                names.append(f"{fam}, {initials}")
            else:
                names.append(fam)
        if len(names) > 7:
            names = names[:6] + ["et al."]
            return html.escape(", ".join(names))
        if len(names) > 1:
            return html.escape(", ".join(names[:-1]) + ", & " + names[-1])
        return html.escape(names[0])

    def link(self) -> str:
        return f"https://doi.org/{self.doi}" if self.doi else self.url

    def full_html(self) -> str:
        """An APA-flavoured reference, as HTML."""
        parts = [f'<span class="ref-authors">{self.authors_html()}</span> ({html.escape(self.year)}).']
        title = html.escape(self.title.rstrip("."))
        parts.append(f"<em>{title}</em>." if self.type in BOOKLIKE else f"{title}.")
        where = []
        if self.container:
            cont = f"<em>{html.escape(self.container)}</em>"
            if self.volume:
                cont += f", <em>{html.escape(self.volume)}</em>"
                if self.issue:
                    cont += f"({html.escape(self.issue)})"
            if self.pages:
                pages = html.escape(self.pages.replace("-", "–"))
                cont += f", {pages}"
            where.append(cont)
        if self.edition:
            where.append(html.escape(self.edition))
        if self.publisher:
            where.append(html.escape(self.publisher))
        if where:
            parts.append("; ".join(where) + ".")
        link = self.link()
        if link:
            shown = re.sub(r"^https?://", "", link)
            parts.append(f'<a class="ext" rel="noopener" href="{html.escape(link)}">{html.escape(shown)}</a>')
        if self.doi and self.url and self.url != link:
            parts.append(f'(<a class="ext" rel="noopener" href="{html.escape(self.url)}">copy read</a>)')
        return " ".join(parts)

    def meta_html(self) -> str:
        bits = [grade_badge(self.grade), f'<span class="ref-kind">{html.escape(self.design or self.kind or self.type)}</span>']
        for flag in self.flags:
            bits.append(f'<span class="ref-flag">{html.escape(FLAGS.get(flag, flag))}</span>')
        if self.url_checked:
            bits.append(f'<span class="ref-date">opened {html.escape(self.url_checked)}</span>')
        return " ".join(bits)

    def notes_html(self) -> str:
        out = ""
        if self.supports:
            out += f'<p class="ref-note"><span class="ref-note-h">Shows:</span> {html.escape(self.supports)}</p>'
        if self.caveats:
            out += f'<p class="ref-note"><span class="ref-note-h">Caveats:</span> {html.escape(self.caveats)}</p>'
        if self.conflicts:
            out += f'<p class="ref-note"><span class="ref-note-h">Conflicts:</span> {html.escape(self.conflicts)}</p>'
        return out


def _text(value) -> str:
    if value is None:
        return ""
    return str(value).strip()


def load_sources(paths: list[Path], root: Path, report) -> dict[str, Source]:
    """Read every registry; problems go to ``report``."""
    sources: dict[str, Source] = {}
    for path in paths:
        rel = path.relative_to(root).as_posix()
        try:
            data = yamlsub.load(path.read_text(encoding="utf-8"), rel)
        except yamlsub.YamlError as exc:
            report.error(str(exc))
            continue
        if not isinstance(data, dict):
            report.error(f"{rel}: a registry maps citation keys to sources")
            continue
        for key, entry in data.items():
            where = f"{rel} [{key}]"
            if not KEY_RE.match(key):
                report.error(f"{where}: citation keys are lowercase letters, digits and _ . - (e.g. sackett2022)")
                continue
            if not isinstance(entry, dict):
                report.error(f"{where}: each source is a mapping of fields")
                continue
            src = _source_from(key, rel, entry, where, report)
            if not src:
                continue
            if key in sources:
                first = sources[key]
                same = (
                    (src.doi and first.doi and src.doi.lower() == first.doi.lower())
                    or (src.url and src.url == first.url)
                    or (_norm_title(src.title) == _norm_title(first.title) and src.year == first.year)
                )
                if not same:
                    report.error(f"{where}: key already used for a different work in {first.origin}")
                continue
            sources[key] = src
    return sources


def _source_from(key: str, origin: str, e: dict, where: str, report) -> Source | None:
    known = set(TEXT_FIELDS) | set(LIST_FIELDS) | set(ALIASES) | {"year", "commercial"}
    for k in e:
        if k not in known:
            report.error(f"{where}: unknown field {k!r}")
    e = dict(e)
    for alias, canonical in ALIASES.items():
        if alias in e:
            if canonical in e:
                report.error(f"{where}: give {canonical} or {alias}, not both")
            e[canonical] = e.pop(alias)
    commercial = e.pop("commercial", False)
    if commercial not in (True, False):
        report.error(f"{where}: commercial is true or false")
    src = Source(key=key, origin=origin, year=_text(e.get("year")), **{f: _text(e.get(f)) for f in TEXT_FIELDS})
    for f in LIST_FIELDS:
        value = e.get(f) or []
        if isinstance(value, str):
            value = [value]
        if not isinstance(value, list):
            report.error(f"{where}: {f} must be a list")
            value = []
        setattr(src, f, value if f == "secondary_urls" else [_text(v) for v in value])
    if commercial is True and "commercial" not in src.flags:
        src.flags.append("commercial")
    problems = []
    if src.type not in TYPES:
        problems.append(f"type must be one of {', '.join(sorted(TYPES))}")
    if src.grade not in GRADES:
        problems.append(f"grade must be one of {', '.join(GRADES)}")
    if src.kind and src.kind not in KINDS:
        problems.append(f"kind must be one of {', '.join(sorted(KINDS))}")
    if not src.title:
        problems.append("title is required")
    if not src.year:
        problems.append("year is required (use n.d. when there is none)")
    if not src.authors:
        problems.append("authors is required: ['Family, Given'] or ['Organisation Name']")
    if not src.url.startswith(("https://", "http://")):
        problems.append("url must be the http(s) address of the copy you opened")
    if not DATE_RE.match(src.url_checked):
        problems.append("url_checked must be the YYYY-MM-DD date you opened the source")
    if not src.supports:
        problems.append("supports must say what the source shows, as the book uses it")
    for flag in src.flags:
        if flag not in FLAGS:
            problems.append(f"unknown flag {flag!r}")
    for p in problems:
        report.error(f"{where}: {p}")
    return None if problems else src


def grade_badge(grade: str) -> str:
    label, dots = GRADES[grade]
    if dots == 0:
        glyph = '<span class="g-x" aria-hidden="true">✕</span>'
    else:
        glyph = "".join(
            f'<span class="g-dot{" on" if i < dots else ""}" aria-hidden="true"></span>' for i in range(3)
        )
    return f'<span class="grade grade-{grade}">{glyph}<span class="grade-text">{label}</span></span>'
