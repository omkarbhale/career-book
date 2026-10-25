"""Regenerate Chapter 8's figures: python3 book/figures/_src/ch08_figures.py"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import figkit as fk  # noqa: E402
from ch06_figures import badge, bubble  # noqa: E402


def whiteboard(pen, x, y, w=250, h=140):
    rows = "".join(
        pen.line(x + 18 + (i % 3) * 14, y + 26 + i * 22, x + w - 30 - (i * 37) % 70, y + 26 + i * 22, "k-thin k-mute")
        for i in range(5)
    )
    return f'<path d="{pen.rect_d(x, y, w, h)}" class="f-paper k"/>' + rows


def watcher(x, y):
    """A generic interviewer, seated, with a clipboard and a fixed stare (not one of the cast)."""
    return (
        f'<g transform="translate({x} {y})">'
        '<path d="M-26 0 C-28 -40 -20 -62 0 -62 C20 -62 28 -40 26 0 Z" class="f-soft k-thin"/>'
        '<circle cx="0" cy="-84" r="22" class="f-mute k-thin"/>'
        '<circle cx="-8" cy="-86" r="4" class="f-paper"/><circle cx="8" cy="-86" r="4" class="f-paper"/>'
        '<circle cx="-8" cy="-86" r="1.8" class="f-ink"/><circle cx="8" cy="-86" r="1.8" class="f-ink"/>'
        '<rect x="-30" y="-44" width="26" height="34" rx="3" class="f-paper k-thin"/>'
        '<path d="M-25 -34 L-9 -34 M-25 -26 L-12 -26" class="k-thin k-mute"/></g>'
    )


def sweat(x, y):
    return (
        f'<path d="M{x} {y} q-6 10 0 14 q6 -4 0 -14 Z" class="f-a2 k-thin"/>'
        f'<path d="M{x + 14} {y + 10} q-5 8 0 11 q5 -3 0 -11 Z" class="f-a2 k-thin"/>'
    )


# ---------------------------------------------------------- Figure 8.1


def fig_watched():
    pen = fk.Pen(seed=81)
    b = []
    for i, (label, x0) in enumerate((("alone", 20), ("watched", 330))):
        b.append(fk.text(x0 + 145, 36, label, "t t-sans t-mid"))
        b.append(whiteboard(pen, x0 + 10, 56))
        b.append(fk.person("bea", x0 + 200, 340, 0.62))
        if i == 1:
            b.append(sweat(x0 + 226, 206))
            b.append(watcher(x0 + 60, 340))
    b.append(pen.line(20, 342, 620, 342, "k-thin k-mute"))
    b.append(fk.text(30, 392, "how much they solved", "t t-sans"))
    b.append(f'<path d="{pen.rect_d(30, 408, 260, 40)}" class="f-a2 k"/>')
    b.append(f'<path d="{pen.rect_d(340, 408, 110, 40)}" class="f-a1 k"/>')
    b.append(fk.text(160, 478, "alone", "t t-mid"))
    b.append(fk.text(470, 478, "watched: less than half", "t t-mid t-a1 t-bold"))
    b.append(fk.lines(320, 528, ["schematic: in one trial with 48 students, performance", "fell by more than half when an interviewer watched"], "t t-sm t-mid t-mute", 26))
    fk.write_svg("ch08/watched.svg", 640, 570, "Solving a problem alone versus while watched", "\n".join(b))


# ---------------------------------------------------------- Figure 8.2


def clock(cx, cy, r, label):
    pen = fk.Pen(seed=82)
    ticks = "".join(
        f'<path d="M{cx}, {cy - r + 6} L{cx}, {cy - r + 14}" class="k-thin" transform="rotate({i * 30} {cx} {cy})"/>'
        for i in range(12)
    )
    return (
        f'<path d="M{cx} {cy} L{cx} {cy - r} A{r} {r} 0 0 1 {cx + r * 0.866:.1f} {cy + r * 0.5:.1f} Z" class="f-a3"/>'
        f'<path d="{pen.circle_d(cx, cy, r)}" class="k"/>{ticks}'
        f'<path d="M{cx} {cy} L{cx} {cy - r + 18} M{cx} {cy} L{cx + r * 0.6:.1f} {cy + r * 0.35:.1f}" class="k"/>'
        f'<circle cx="{cx}" cy="{cy}" r="3" class="f-ink"/>'
        + fk.text(cx, cy + r + 34, label, "t t-mid t-bold")
    )


def fig_scoping():
    pen = fk.Pen(seed=83)
    stages = [
        ("before", ["read the brief twice", "ask two questions", "agree the time cap"]),
        ("during", ["start a timer", "build the core first", "test the core", "stop at the cap"]),
        ("after", ["write the README:", "what I built; decisions and trade-offs;", "what I'd do with more time;", "how long I spent"]),
    ]
    b = [clock(552, 92, 52, "3-hour cap")]
    y = 30
    for i, (title, rows) in enumerate(stages, start=1):
        h = 58 + 30 * len(rows)
        cls = "f-a1 k" if title == "after" else "f-paper k"
        b.append(f'<path d="{pen.rect_d(30, y, 440, h)}" class="{cls}"/>')
        b.append(badge(58, y + 30, i))
        b.append(fk.text(84, y + 36, title, "t t-sans"))
        b.append(fk.lines(84, y + 72, rows, "t", 30))
        if i < len(stages):
            b.append(pen.arrow(250, y + h + 4, 250, y + h + 32, "k"))
        y += h + 36
    b.append(fk.lines(552, 330, ["the README", "is part of", "the work", "sample"], "t t-mid t-a1 t-bold", 30))
    b.append(pen.arrow(520, 452, 476, y - 110, "k k-a1", bend=-14))
    b.append(fk.text(30, y + 6, "craft, not research: a way to scope, not a rule", "t t-sm t-mute"))
    fk.write_svg("ch08/scoping.svg", 640, int(y + 34), "Scoping a take-home task", "\n".join(b))


# ---------------------------------------------------------- Figure 8.3


def fig_out_loud():
    pen = fk.Pen(seed=84)
    moves = [
        ("restate the problem", ["So: for each account, return the most", "recent transaction?"]),
        ("try a tiny example", ["Let me try three transactions for two", "accounts by hand first."]),
        ("say the simple version first", ["Simplest version: sort everything by time,", "keep the last one per account."]),
        ("name the trade-off", ["Sorting is n log n; one pass with a map is", "linear, so I'll do that."]),
        ("test out loud", ["Edge case: two transactions with the same", "timestamp. Can that happen?"]),
    ]
    b = [fk.avatar("bea", 66, 56, 72, "ol-bea"), fk.text(116, 66, "Bea, thinking out loud", "t t-lg")]
    y = 130
    for i, (tag, rows) in enumerate(moves, start=1):
        b.append(badge(48, y - 6, i))
        b.append(fk.text(74, y, tag, "t t-sans"))
        h = 20 + 30 * len(rows)
        b.append(bubble(pen, 40, y + 14, 570, h, "f-paper k-thin", tail=None))
        b.append(fk.lines(60, y + 46, [f"“{rows[0]}"] + rows[1:-1] + [f"{rows[-1]}”"] if len(rows) > 1 else [f"“{rows[0]}”"], "t", 30))
        y += h + 60
    b.append(fk.lines(320, y + 4, ["each bubble gives the interviewer", "something to score, and a chance to help"], "t t-mid t-a1 t-bold", 30))
    fk.write_svg("ch08/out-loud.svg", 640, int(y + 56), "Thinking out loud, annotated", "\n".join(b))


if __name__ == "__main__":
    fig_watched()
    fig_scoping()
    fig_out_loud()
