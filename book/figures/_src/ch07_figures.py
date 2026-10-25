"""Regenerate Chapter 7's figures: python3 book/figures/_src/ch07_figures.py"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import figkit as fk  # noqa: E402
from ch06_figures import badge  # noqa: E402


def mug(x, y, s=1.0):
    """Meera's mug (the same shape as in Chapter 1), with steam."""
    return (
        f'<g transform="translate({x} {y}) scale({s})"><path d="M0 0 L2 22 L20 22 L22 0 Z" class="f-meera k-thin"/>'
        '<path d="M22 5 C31 5 31 16 21 16" class="k-thin"/>'
        '<path d="M6 -4 Q8 -9 6 -14 M14 -4 Q16 -9 14 -14" class="k-thin k-mute"/></g>'
    )


# ---------------------------------------------------------- Figure 7.1


def fig_story():
    pen = fk.Pen(seed=71)
    x0, total = 30, 580
    parts = [
        ("situation and task", 20, "f-soft", ["the queue was dropping 1 in 2,000", "messages; nobody had spotted it"]),
        ("what I did", 70, "f-a1", ["noticed a pattern in the test logs, wrote", "a reproduction, paired with the developer", "on the fix, added a nightly test"]),
        ("result", 20, "f-a3", ["fixed two days before go-live;", "no repeats in a year"]),
        ("what I'd keep", 10, "f-a2", ["now I check retries first"]),
    ]
    b = [fk.text(x0, 34, "A two-minute answer, roughly to scale", "t t-sans")]
    x = x0
    for i, (label, secs, cls, _) in enumerate(parts, start=1):
        w = total * secs / 120
        b.append(f'<path d="{pen.rect_d(x, 52, w, 56)}" class="{cls} k"/>')
        b.append(badge(x + w / 2, 80, i, "f-paper"))
        x += w
    b.append(fk.text(x0, 136, "0", "t t-sm t-mute"))
    b.append(fk.text(x0 + total, 136, "2 minutes", "t t-sm t-mute t-end"))
    y = 190
    for i, (label, secs, cls, rows) in enumerate(parts, start=1):
        b.append(f'<path d="{pen.rect_d(x0, y - 22, 26, 26)}" class="{cls} k-thin"/>')
        b.append(fk.text(x0 + 13, y - 2, str(i), "t t-sm t-mid t-bold"))
        b.append(fk.text(x0 + 44, y, f"{label} · about {secs} seconds", "t t-sans"))
        b.append(fk.lines(x0 + 44, y + 34, rows, "t", 30))
        y += 34 + 30 * len(rows) + 28
    b.append(fk.lines(x0, y + 6, ["a rule of thumb, not a finding:", "most of the time goes on what you did"], "t t-sm t-mute", 26))
    fk.write_svg("ch07/story.svg", 640, int(y + 60), "Anatomy of a story answer", "\n".join(b))


# ---------------------------------------------------------- Figure 7.2


def fig_scoring_sheet():
    pen = fk.Pen(seed=72)
    b = [
        f'<path d="{pen.rect_d(30, 34, 470, 640)}" class="f-soft k"/>',
        f'<path d="{pen.rect_d(48, 52, 434, 606)}" class="f-paper k-thin"/>',
        '<rect x="205" y="18" width="120" height="34" rx="8" class="f-mute k-thin"/>',
        fk.text(70, 100, "Q3", "t t-sans"),
        fk.lines(70, 134, ["Tell me about a time you found a", "problem nobody else had noticed."], "t t-bold", 30),
        fk.text(70, 222, "score", "t t-sans"),
    ]
    for i in range(5):
        x = 150 + i * 62
        b.append(f'<path d="{pen.rect_d(x, 196, 42, 38)}" class="k-thin"/>')
        b.append(fk.text(x + 21, 223, str(i + 1), "t t-mid"))
    b.append(f'<path d="{pen.circle_d(150 + 3 * 62 + 21, 215, 28)}" class="k k-a1"/>')
    anchors = [
        ("1", ["vague, or someone else did it"]),
        ("3", ["clear problem, own action,", "some result"]),
        ("5", ["noticed early, acted, checked,", "and stopped it recurring"]),
    ]
    y = 284
    for n, rows in anchors:
        b.append(fk.text(70, y, n + " =", "t t-bold"))
        b.append(fk.lines(112, y, rows, "t", 28))
        y += 28 * len(rows) + 16
    b.append(fk.text(70, 462, "evidence heard", "t t-sans"))
    b.append(f'<path d="{pen.rect_d(62, 474, 406, 132)}" class="k-thin k-dash k-mute"/>')
    b.append(fk.lines(80, 508, ["queue bug, 2 days before go-live", "wrote a repro, paired on the fix", "added a nightly test"], "t t-a2", 32))
    b.append(fk.text(265, 640, "score alone, then discuss", "t t-mid t-bold t-a1"))
    b.append(mug(552, 548, 2.4))
    b.append(fk.text(578, 636, "structure", "t t-sans t-mid"))
    b.append(fk.text(578, 658, "is kindness", "t t-sans t-mid"))
    fk.write_svg("ch07/scoring-sheet.svg", 650, 690, "A structured interview scoring sheet", "\n".join(b))


# ---------------------------------------------------------- Figure 7.3


def fig_nerves():
    pen = fk.Pen(seed=73, wobble=0.9)
    b = [
        fk.text(240, 48, "about 4 in 100", "t t-lg t-mid t-a1 t-bold"),
        fk.lines(240, 84, ["of the differences in interview", "ratings go along with nerves"], "t t-mid", 28),
    ]
    for r in range(10):
        for c in range(10):
            x, y = 40 + c * 40, 140 + r * 40
            cls = "f-a1s k-thin" if (r == 0 and c < 4) else "f-soft k-thin k-mute"
            b.append(f'<path d="{pen.rect_d(x, y, 32, 32)}" class="{cls}"/>')
    b.append(fk.lines(240, 580, ["the other 96: what you say,", "what you've done, the questions,", "the interviewer, the day"], "t t-mid", 30))
    b.append(fk.lines(240, 690, ["illustration: −.19 squared ≈ .04", "(a meta-analysis of 30 studies)"], "t t-sm t-mid t-mute", 26))
    fk.write_svg("ch07/nerves.svg", 480, 730, "Nerves, to scale", "\n".join(b))


if __name__ == "__main__":
    fig_story()
    fig_scoring_sheet()
    fig_nerves()
