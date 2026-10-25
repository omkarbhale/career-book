#!/usr/bin/env python3
"""Build the book into a static site in docs/ (served by GitHub Pages).

    python3 tools/build.py                       build docs/ (fails on any error)
    python3 tools/build.py --check               run every check, write nothing
    python3 tools/build.py --sync-figure-style   copy book/figures/figure.css into every figure

Needs Python 3.11 or newer and nothing else: no packages, no network. The same
sources always produce byte-identical output.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from bookkit.site import Site, sync_figure_styles  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build the book into docs/.")
    parser.add_argument("--check", action="store_true", help="run all checks without writing docs/")
    parser.add_argument("--out", type=Path, help="write the site somewhere other than docs/")
    parser.add_argument("--sync-figure-style", action="store_true", help="refresh the <style> block in every figure")
    args = parser.parse_args(argv)

    if sys.version_info < (3, 11):
        print("error: the build needs Python 3.11 or newer", file=sys.stderr)
        return 2
    if args.sync_figure_style:
        for name in sync_figure_styles(ROOT):
            print(f"updated {name}")
        return 0

    site = Site(ROOT, args.out.resolve() if args.out else None)
    report = site.build(write=not args.check)
    report.print()
    if not report.ok:
        print(f"build failed: {len(report.errors)} error(s)", file=sys.stderr)
        return 1
    pages = sum(1 for p in site.pages if p.written)
    target = "checks passed" if args.check else f"wrote {site.out.relative_to(ROOT) if site.out.is_relative_to(ROOT) else site.out}"
    print(f"ok: {pages} written page(s), {len(site.pages) - pages} planned, {len(site.book.cited_in)} cited source(s); {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
