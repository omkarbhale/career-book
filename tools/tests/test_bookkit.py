"""Tests for the build toolchain: python3 -m unittest discover -s tools/tests"""

import filecmp
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1]
ROOT = TOOLS.parent
sys.path.insert(0, str(TOOLS))

from bookkit import svg, yamlsub  # noqa: E402
from bookkit.errors import BuildError, Report  # noqa: E402
from bookkit.inline import InlineContext, render_inline, slugify  # noqa: E402
from bookkit.markdown import parse_document  # noqa: E402
from bookkit.render import Book, Page  # noqa: E402
from bookkit.site import Site  # noqa: E402


class MarkdownTests(unittest.TestCase):
    def parse(self, text):
        return parse_document(text, "test.md")

    def test_front_matter_and_heading_ids(self):
        meta, nodes = self.parse("---\nid: ch99\nstatus: draft\n---\n\n## A section {#ch99.sec.a}\n\nText.\n")
        self.assertEqual(meta, {"id": "ch99", "status": "draft"})
        self.assertEqual(nodes[0].kind, "heading")
        self.assertEqual(nodes[0].attrs["id"], "ch99.sec.a")
        self.assertEqual(nodes[1].kind, "para")

    def test_nested_directives_with_same_colons(self):
        text = "::: move {#ch99.move.x} Title\nDo it.\n\n::: answer\nDone.\n:::\n:::\n"
        _, nodes = self.parse(text)
        self.assertEqual(len(nodes), 1)
        move = nodes[0]
        self.assertEqual((move.name, move.title, move.attrs["id"]), ("move", "Title", "ch99.move.x"))
        self.assertEqual([c.name for c in move.children if c.kind == "directive"], ["answer"])

    def test_unclosed_directive_is_an_error(self):
        with self.assertRaises(BuildError):
            self.parse("::: pause\nnever closed\n")

    def test_nested_lists_and_speech(self):
        _, nodes = self.parse("- one\n  - inner\n- two\n\n@dev: Hello there.\n")
        self.assertEqual(nodes[0].kind, "list")
        self.assertEqual(len(nodes[0].children), 2)
        self.assertEqual(nodes[0].children[0].children[1].kind, "list")
        self.assertEqual((nodes[1].kind, nodes[1].name, nodes[1].text), ("speech", "dev", "Hello there."))

    def test_table(self):
        _, nodes = self.parse("| a | b |\n| :-- | --: |\n| 1 | 2 |\n")
        self.assertEqual(nodes[0].kind, "table")
        self.assertEqual(nodes[0].align, ["left", "right"])
        self.assertEqual(nodes[0].rows[1][1], ["1", "2"])


class InlineTests(unittest.TestCase):
    def render(self, text):
        return render_inline(text, InlineContext(), "test")

    def test_emphasis_code_and_links(self):
        out = self.render('**bold** and *em* and `x < y` and [a link](https://example.org "t")')
        self.assertIn("<strong>bold</strong>", out)
        self.assertIn("<em>em</em>", out)
        self.assertIn("<code>x &lt; y</code>", out)
        self.assertIn('<a href="https://example.org" title="t" class="ext" rel="noopener">a link</a>', out)

    def test_typography(self):
        self.assertEqual(self.render('"Quote" -- it\'s --- fine...'), "\u201cQuote\u201d \u2013 it\u2019s \u2014 fine\u2026")

    def test_citations_and_xrefs_reach_the_context(self):
        out = self.render("See [[ch07|this]] and [@a; @b, p. 4].")
        self.assertIn("this", out)
        self.assertIn("[a; b]", out)

    def test_images_are_refused(self):
        with self.assertRaises(BuildError):
            self.render("![alt](picture.png)")

    def test_slugify(self):
        self.assertEqual(slugify("Signals, not *secrets*"), "signals-not-secrets")


class YamlTests(unittest.TestCase):
    def test_subset(self):
        text = (
            "key2024:\n"
            "  type: article\n"
            "  authors: ['Doe, Jane', 'O''Brien,\n"
            "      Pat']\n"
            "  year: 2024\n"
            "  title: >-\n"
            "    A folded\n"
            "    title\n"
            "  flags: [commercial]\n"
            "  secondary_urls:\n"
            "  - {url: 'https://a.example', how: seen}\n"
            '  note: "quoted \\u00e9"\n'
        )
        d = yamlsub.load(text, "t.yaml")["key2024"]
        self.assertEqual(d["authors"], ["Doe, Jane", "O'Brien, Pat"])
        self.assertEqual(d["year"], 2024)
        self.assertEqual(d["title"], "A folded title")
        self.assertEqual(d["secondary_urls"], [{"url": "https://a.example", "how": "seen"}])
        self.assertEqual(d["note"], "quoted \u00e9")

    def test_unsupported_constructs_fail_loudly(self):
        with self.assertRaises(yamlsub.YamlError):
            yamlsub.load("a: &anchor 1\n", "t.yaml")


class SvgTests(unittest.TestCase):
    CSS = (ROOT / "book" / "figures" / "figure.css").read_text(encoding="utf-8")

    def doc(self, body):
        return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10 10" class="fig"><style>{self.CSS}</style>{body}</svg>'

    def test_clean_figure_passes(self):
        self.assertEqual(svg.check_svg(self.doc('<circle cx="5" cy="5" r="3" class="f-a1 k"/>'), "f.svg", self.CSS), [])

    def test_hard_coded_colour_fails(self):
        problems = svg.check_svg(self.doc('<circle cx="5" cy="5" r="3" fill="#ff0000"/>'), "f.svg", self.CSS)
        self.assertTrue(any("hard-codes a colour" in p for p in problems))

    def test_ids_are_prefixed_when_inlined(self):
        text = self.doc('<defs><clipPath id="c"><rect width="1" height="1"/></clipPath></defs><g clip-path="url(#c)"/>')
        out = svg.inline_svg(text, "ch99-fig-x", "A label long enough")
        self.assertIn('id="ch99-fig-x-c"', out)
        self.assertIn("url(#ch99-fig-x-c)", out)
        self.assertIn('role="img"', out)
        self.assertNotIn("<style", out)


class RenderTests(unittest.TestCase):
    def test_broken_cross_reference_is_an_error(self):
        report = Report()
        _, nodes = parse_document("Go to [[ch42]].\n", "t.md")
        page = Page(id="ch99", kind="chapter", title="T", href="ch99.html", label="99", number=99, rel="t.md", nodes=nodes)
        book = Book({}, [page], {}, {}, lambda src, where: None, report)
        book.collect(page)
        book.render(page)
        self.assertTrue(any("[[ch42]]" in e for e in report.errors))

    def test_ids_must_live_in_the_page_namespace(self):
        report = Report()
        _, nodes = parse_document("## Heading {#ch01.sec.stolen}\n", "t.md")
        page = Page(id="ch99", kind="chapter", title="T", href="ch99.html", label="99", number=99, rel="t.md", nodes=nodes)
        Book({}, [page], {}, {}, lambda src, where: None, report).collect(page)
        self.assertTrue(report.errors)


class PlannedSectionTests(unittest.TestCase):
    def test_links_to_planned_sections_of_unwritten_pages_resolve(self):
        report = Report()
        _, nodes = parse_document("See [[more.sec.managing]].\n\n::: further {ref=more.sec.managing}\nMore.\n:::\n", "t.md")
        page = Page(id="ch99", kind="chapter", title="T", href="ch99.html", label="99", number=99, rel="t.md", nodes=nodes)
        more = Page(id="more", kind="appendix", title="Left Out", href="left-out.html", label="C",
                    planned=[("more.sec.managing", "Managing people")])
        book = Book({}, [page, more], {}, {}, lambda src, where: None, report)
        book.collect(page)
        book.render(page)
        self.assertEqual(report.errors, [])
        self.assertIn('href="left-out.html#more.sec.managing"', page.body_html)
        self.assertIn("Going Further", page.body_html)


class BuildTests(unittest.TestCase):
    def test_book_builds_and_is_reproducible(self):
        with tempfile.TemporaryDirectory() as tmp:
            first, second = Path(tmp) / "a", Path(tmp) / "b"
            for out in (first, second):
                report = Site(ROOT, out).build()
                self.assertTrue(report.ok, report.errors)
            cmp = filecmp.dircmp(first, second)
            self.assertEqual((cmp.left_only, cmp.right_only, cmp.diff_files), ([], [], []))
            for sub in cmp.subdirs.values():
                self.assertEqual(sub.diff_files, [])


if __name__ == "__main__":
    unittest.main()
