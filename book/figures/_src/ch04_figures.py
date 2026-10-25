"""Regenerate Chapter 4's figures: python3 book/figures/_src/ch04_figures.py"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
import figkit as fk  # noqa: E402


def card(pen, x, y, w, rows, fill, cls="t", lh=30, head=None):
    h = 26 + lh * len(rows) + (30 if head else 0)
    out = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" class="{fill}"/>' + pen.rect(x, y, w, h, "k")
    ty = y + 34
    if head:
        out += fk.text(x + 20, ty - 4, head, "t t-sans")
        ty += 30
    out += fk.lines(x + 20, ty, rows, cls, lh)
    return out, y + h


# ---------------------------------------------------------- Figure 4.1


def fig_duty():
    pen = fk.Pen(seed=41)
    b = []
    d, db = card(pen, 40, 24, 560, ["Responsible for regression testing", "of the payments platform."], "f-soft", "t t-mute", head="A DUTY")
    b.append(d)
    qs = ["What changed?", "By how much?", "Who noticed?"]
    y = db + 30
    for i, q in enumerate(qs):
        cx = 128 + i * 192
        b.append(f'<rect x="{cx - 84}" y="{y}" width="168" height="44" rx="22" class="f-a3"/>')
        b.append(pen.rect(cx - 84, y, 168, 44, "k-thin"))
        b.append(fk.text(cx, y + 30, q, "t t-mid"))
    b += [
        pen.arrow(320, db + 4, 320, y - 6, "k"),
        pen.arrow(320, y + 50, 320, y + 92, "k"),
    ]
    e, eb = card(
        pen, 40, y + 98, 560,
        ["Cut the nightly regression run from 6 hours", "to 40 minutes by running suites in parallel;",
         "the team now tests every merge, and the", "client’s defect reports fell."],
        "f-a1", "t", head="EVIDENCE",
    )
    b.append(e)
    b.append(fk.text(320, eb + 36, "Same work. One describes a job; the other describes you.", "t t-sm t-mid t-mute"))
    fk.write_svg("ch04/duty-evidence.svg", 640, int(eb + 56), "Turning a duty into evidence", "\n".join(b))


# ---------------------------------------------------------- Figure 4.2


def fig_story_bank():
    pen = fk.Pen(seed=42)
    cols = ["hard problem", "mistake owned", "disagreement", "led, no title", "learned fast", "under pressure"]
    stories = [
        ("The 6-hour suite", [1, 0, 0, 0, 1, 0]),
        ("Bug before the client", [1, 0, 0, 0, 0, 1]),
        ("Flaky deploy scripts", [1, 1, 0, 0, 1, 0]),
        ("The release I blocked", [0, 0, 1, 0, 0, 1]),
        ("Training the new tester", [0, 0, 0, 1, 0, 0]),
        ("Wrong about the cache", [0, 1, 1, 0, 1, 0]),
    ]
    x0, y0, cw, rh = 282, 190, 56, 54
    b = [fk.text(24, 40, "Dev’s story bank, first draft", "t t-sans")]
    # column headers, rotated
    for j, c in enumerate(cols):
        cx = x0 + j * cw + cw / 2
        b.append(f'<g transform="rotate(-62 {cx:.1f} {y0 - 12})">{fk.text(cx, y0 - 12, c, "t t-sm")}</g>')
    for i, (name, marks) in enumerate(stories):
        y = y0 + i * rh
        fill = "f-paper" if i % 2 else "f-soft"
        b.append(f'<rect x="20" y="{y}" width="{x0 - 20 + cw * len(cols)}" height="{rh}" class="{fill}"/>')
        b.append(fk.text(32, y + 35, name, "t"))
        for j, m in enumerate(marks):
            cx, cy = x0 + j * cw + cw / 2, y + rh / 2
            if m:
                b.append(f'<circle cx="{cx}" cy="{cy}" r="15" class="f-a3s"/>')
                b.append(f'<path d="M{cx - 7} {cy} l5 6 l10 -12" class="k"/>')
    yb = y0 + rh * len(stories)
    for j in range(len(cols) + 1):
        b.append(f'<path d="M{x0 + j * cw} {y0} L{x0 + j * cw} {yb}" class="k-thin k-mute"/>')
    b.append(pen.rect(20, y0, x0 - 20 + cw * len(cols), yb - y0, "k"))
    # the gap
    gx = x0 + 3 * cw + cw / 2
    b += [
        pen.arrow(gx + 40, yb + 64, gx + 4, yb + 8, "k-thin k-a1", bend=10),
        fk.lines(gx + 46, yb + 72, ["only one story:", "find another"], "t t-sm t-a1", 22),
        fk.text(24, yb + 44, "Rows: true stories. Columns: what a story can show.", "t t-sm t-mute"),
        fk.text(24, yb + 70, "Aim for two ticks in every column.", "t t-sm t-mute"),
    ]
    fk.write_svg("ch04/story-bank.svg", 640, int(yb + 126), "A story bank grid", "\n".join(b))


# ---------------------------------------------------------- Figure 4.3


def fig_overlap():
    pen = fk.Pen(seed=43)
    r = 150
    cA, cB, cC = (320, 210), (226, 368), (414, 368)
    b = [
        f'<circle cx="{cA[0]}" cy="{cA[1]}" r="{r}" class="f-a3" fill-opacity="0.7"/>',
        f'<circle cx="{cB[0]}" cy="{cB[1]}" r="{r}" class="f-a1" fill-opacity="0.7"/>',
        f'<circle cx="{cC[0]}" cy="{cC[1]}" r="{r}" class="f-a2" fill-opacity="0.7"/>',
        f'<path d="{pen.circle_d(*cA, r)}" class="k"/>',
        f'<path d="{pen.circle_d(*cB, r)}" class="k"/>',
        f'<path d="{pen.circle_d(*cC, r)}" class="k"/>',
        fk.text(320, 108, "WHAT YOU WANT", "t t-sans t-mid"),
        fk.text(170, 440, "WHAT YOU", "t t-sans t-mid"),
        fk.text(170, 462, "CAN SHOW", "t t-sans t-mid"),
        fk.text(470, 440, "WHAT THEY", "t t-sans t-mid"),
        fk.text(470, 462, "NEED", "t t-sans t-mid"),
        # pairwise regions, labelled outside with leaders
        fk.lines(24, 92, ["no one\u2019s", "hiring for it"], "t t-sm", 22),
        pen.arrow(70, 122, 250, 292, "k-thin", bend=-20, head=9),
        fk.lines(616, 92, ["stretch: build", "the evidence"], "t t-sm t-end", 22),
        pen.arrow(570, 122, 392, 292, "k-thin", bend=20, head=9),
        fk.lines(470, 548, ["jobs you\u2019d get,", "then regret"], "t t-sm", 22),
        pen.arrow(466, 548, 330, 432, "k-thin", bend=-14, head=9),
        # the centre
        '<circle cx="320" cy="318" r="40" class="f-paper"/>',
        f'<path d="{pen.circle_d(320, 318, 40)}" class="k-thick k-a1"/>',
        fk.text(320, 326, "targets", "t t-bold t-mid"),
        fk.text(320, 612, "Aim at the middle; plan your way into the stretch.", "t t-sm t-mid t-mute"),
    ]
    fk.write_svg("ch04/overlap.svg", 640, 632, "Choosing targets where three circles overlap", "\n".join(b))


if __name__ == "__main__":
    fig_duty()
    fig_story_bank()
    fig_overlap()
    print("wrote chapter 4 figures")
