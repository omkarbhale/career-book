"""Regenerate Chapter 12's figures: python3 book/figures/_src/ch12_figures.py"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
import figkit as fk  # noqa: E402

# ---------------------------------------------------------- Figure 12.1


def fig_loop():
    pen = fk.Pen(seed=121)
    steps = [
        (24, 94, "1 · Hear the ask", ["what do they", "actually need?"], "f-soft"),
        (24, 254, "2 · Clarify", ["what, by when, and", "what does done mean?"], "f-soft"),
        (24, 414, "3 · Say it out loud", ["“Rates by Thursday,", "tested, in staging.”"], "f-a3"),
        (340, 414, "4 · Track it", ["somewhere you will", "see it tomorrow"], "f-soft"),
        (340, 254, "5 · Deliver, or", ["renegotiate early,", "the day you know"], "f-a2"),
        (340, 94, "6 · Close the loop", ["tell them it’s done;", "don’t make them ask"], "f-soft"),
    ]
    b = [fk.text(320, 32, "The commitment loop", "t t-sans t-mid")]
    for x, y, head, rows, fill in steps:
        b.append(pen.rect(x, y, 276, 124, f"{fill} k"))
        b.append(fk.text(x + 16, y + 36, head, "t t-bold"))
        b.append(fk.lines(x + 16, y + 72, rows, "t t-sm", 26))
    b += [
        pen.arrow(162, 220, 162, 250, "k", head=10),
        pen.arrow(162, 380, 162, 410, "k", head=10),
        pen.arrow(302, 476, 336, 476, "k", head=10),
        pen.arrow(478, 410, 478, 382, "k", head=10),
        pen.arrow(478, 250, 478, 222, "k", head=10),
        pen.arrow(410, 64, 230, 64, "k k-dash", bend=0, head=12),
        fk.text(320, 588, "Step 5's second half is not failure. It is the loop working.", "t t-sm t-mid t-mute"),
    ]
    fk.write_svg("ch12/commitment-loop.svg", 640, 612, "The commitment loop", "\n".join(b))


# ---------------------------------------------------------- Figure 12.2


def fig_early():
    pen = fk.Pen(seed=122)
    x0, x1, y0, y1 = 70, 600, 430, 90
    b = [
        pen.arrow(x0, y0, x1 + 14, y0, "k"),
        pen.arrow(x0, y0, x0, y1 - 24, "k"),
        # options left: falls steeply; cost of the surprise: rises
        f'<path d="M{x0 + 10} {y1 + 10} C{x0 + 220} {y1 + 30} {x1 - 160} {y0 - 120} {x1 - 20} {y0 - 22}" class="k-thick k-a2"/>',
        f'<path d="M{x0 + 10} {y0 - 30} C{x0 + 260} {y0 - 40} {x1 - 200} {y1 + 120} {x1 - 20} {y1 + 6}" class="k-thick k-a1"/>',
        fk.text(x0 + 24, y1 - 2, "options left", "t t-a2"),
        fk.lines(500, y1 - 4, ["cost of the", "surprise"], "t t-a1 t-end", 26),
        pen.line(150, y0, 150, y1 + 40, "k-thin k-dash"),
        pen.line(540, y0, 540, y1 + 40, "k-thin k-dash"),
        fk.lines(150, y0 + 32, ["Wednesday:", "Dev knows"], "t t-mid", 26),
        fk.lines(530, y0 + 32, ["Friday 4:47 pm:", "Dev says"], "t t-mid", 26),
        pen.rect(174, 150, 238, 108, "f-a2 k-thin"),
        fk.lines(188, 184, ["move the demo, cut", "scope, get help, or", "warn the customer"], "t t-sm", 26),
        pen.arrow(172, 210, 154, 210, "k-thin", head=8),
        pen.rect(370, 300, 150, 60, "f-a1 k-thin"),
        fk.text(445, 337, "apologise", "t t-sm t-mid"),
        pen.arrow(522, 330, 538, 330, "k-thin", head=8),
        fk.text(335, y0 + 104, "Illustrative shapes, not data", "t t-sm t-mid t-mute"),
    ]
    fk.write_svg("ch12/bad-news.svg", 640, 560, "Bad news early versus late", "\n".join(b))


# ---------------------------------------------------------- Figure 12.3


def fig_apology():
    pen = fk.Pen(seed=123)
    rows = [
        ("Name it", ["I said Northwind would be ready Friday,", "and I knew on Wednesday it wouldn’t."], "a3"),
        ("Own it", ["That’s on me. I should have told", "you that day."], "a3"),
        ("Impact", ["It cost you a scramble before the demo", "and a weekend of worrying."], "a1"),
        ("Fix", ["Rates and booking work now; tracking", "lands Wednesday. Demo notes attached."], "a2"),
        ("Prevent", ["From now on, you hear the day I know,", "and I’ll check in at the halfway point."], "a2"),
    ]
    b = [fk.text(24, 40, "Anatomy of an apology", "t t-sans")]
    y = 64
    for tag, lines_, colour in rows:
        b.append(pen.rect(24, y, 148, 76, f"f-{colour} k-thin"))
        b.append(fk.text(98, y + 46, tag, "t t-bold t-mid"))
        b.append(fk.lines(192, y + 30, lines_, "t t-sm", 26))
        y += 92
    b += [
        pen.line(24, y + 4, 616, y + 4, "k-thin k-mute"),
        fk.text(24, y + 40, "Missing on purpose: “but”, “if”, and a speech.", "t"),
        fk.text(24, y + 74, "Then the most important part: do it.", "t t-bold"),
    ]
    fk.write_svg("ch12/apology.svg", 640, int(y + 96), "Anatomy of an apology", "\n".join(b))


if __name__ == "__main__":
    fig_loop()
    fig_early()
    fig_apology()
    print("wrote chapter 12 figures")
