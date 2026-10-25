"""Regenerate Chapter 18's figures: python3 book/figures/_src/ch18_figures.py"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
import figkit as fk  # noqa: E402


def star(cx, cy, r, cls="f-a3s k-thin"):
    pts = []
    for i in range(10):
        a = -math.pi / 2 + i * math.pi / 5
        rr = r if i % 2 == 0 else r * 0.45
        pts.append(f"{cx + rr * math.cos(a):.1f} {cy + rr * math.sin(a):.1f}")
    return f'<path d="M{" L".join(pts)} Z" class="{cls}"/>'


# ---------------------------------------------------------- Figure 18.1


def fig_cycle():
    pen = fk.Pen(seed=181)
    stops = [
        ("Expectations", ["start of the year: what good", "looks like, agreed"], "star"),
        ("The year", ["evidence piles up,", "mostly in memories"], "star"),
        ("Self-review", ["your account of", "the year"], "star"),
        ("Draft and calibration", ["your manager’s draft,", "compared with everyone’s"], "room"),
        ("The conversation", ["you hear the rating"], "out"),
    ]
    y0, gap = 112, 118
    b = [
        fk.text(24, 40, "A review year", "t t-sans"),
        pen.line(70, y0, 70, y0 + gap * (len(stops) - 1), "k-thick k-a4"),
    ]
    for i, (title, note, kind) in enumerate(stops):
        y = y0 + i * gap
        if kind == "room":
            b.append(f'<rect x="100" y="{y - 44}" width="516" height="102" rx="14" class="f-soft"/>')
            b.append(pen.rect(100, y - 44, 516, 102, "k-thin k-dash"))
            b.append(fk.lines(600, y - 6, ["a room", "you’re not in"], "t t-end t-a1", 28))
        b.append(f'<circle cx="70" cy="{y}" r="24" class="f-a4"/>')
        b.append(f'<path d="{pen.circle_d(70, y, 24)}" class="k"/>')
        b.append(fk.text(70, y + 9, str(i + 1), "t t-bold t-mid"))
        b.append(fk.text(116, y - 6, title, "t t-bold"))
        b.append(fk.lines(116, y + 24, note, "t t-sm t-mute", 24))
        if kind == "star":
            b.append(star(456, y - 4, 20))
            b.append(fk.lines(484, y - 6, ["you shape", "this"], "t t-sm", 24))
        if kind == "out":
            b.append(pen.arrow(330, y - 4, 440, y - 4, "k", bend=-6))
            b.append(fk.lines(452, y - 10, ["pay, promotion,", "next year"], "t", 28))
    yb = y0 + gap * (len(stops) - 1) + 82
    b.append(fk.text(320, yb, "Most of your influence comes before the room, not after it.", "t t-sm t-mid t-mute"))
    fk.write_svg("ch18/cycle.svg", 640, yb + 22, "The anatomy of a review cycle", "\n".join(b))


# ---------------------------------------------------------- Figure 18.2

# Scullen, Mount & Goff (2000): shares of rating variance in two data sets.
SETS = [
    ("Data set 1: 2,350 managers", [62, 21, 11, 6]),
    ("Data set 2: 2,142 managers", [53, 25, 18, 4]),
]
PARTS = [
    ("the rater’s own tendencies", "f-a4s", "t-paper"),
    ("the ratee’s performance", "f-a3s", ""),
    ("random error", "f-mute", "t-paper"),
    ("the rater’s role (boss, peer, report)", "f-soft", ""),
]


def fig_variance():
    pen = fk.Pen(seed=182)
    x0, w, bh = 40, 560, 64
    b = [fk.text(24, 40, "What goes into a rating", "t t-sans")]
    tops = [130, 290]
    # headers over the first bar
    b.append(fk.text(x0 + w * 0.62 / 2, 80, "who rates you", "t t-mid t-a4"))
    b.append(fk.text(x0 + w * (0.62 + 0.21 / 2), 80, "what you did", "t t-mid"))
    b.append(pen.arrow(x0 + w * 0.31, 88, x0 + w * 0.31, 122, "k-thin k-a4", head=9))
    b.append(pen.arrow(x0 + w * 0.725, 88, x0 + w * 0.725, 122, "k-thin", head=9))
    for (label, shares), top in zip(SETS, tops):
        if top != tops[0]:
            b.append(fk.text(x0, top - 14, label, "t t-sm"))
        x = x0
        for (name, fill, tcls), s in zip(PARTS, shares):
            sw = w * s / 100
            b.append(f'<rect x="{x:.1f}" y="{top}" width="{sw:.1f}" height="{bh}" class="{fill}"/>')
            if s >= 10:
                pw = min(68, sw - 6)
                b.append(f'<rect x="{x + sw / 2 - pw / 2:.1f}" y="{top + 14}" width="{pw:.1f}" height="36" rx="18" class="f-paper"/>')
                b.append(fk.text(x + sw / 2, top + 42, f"{s}%", "t t-lg t-mid"))
            else:
                b.append(fk.text(x + sw / 2, top + bh + 26, f"{s}%", "t t-sm t-mid"))
            x += sw
        b.append(pen.rect(x0, top, w, bh, "k"))
    # first bar's label sits under the headers
    b.append(fk.text(x0, tops[0] + bh + 26, SETS[0][0], "t t-sm t-mute"))
    # key
    ky = 420
    for i, (name, fill, _) in enumerate(PARTS):
        y = ky + i * 34
        b.append(f'<rect x="{x0}" y="{y - 20}" width="26" height="26" rx="5" class="{fill}"/>')
        b.append(pen.rect(x0, y - 20, 26, 26, "k-thin"))
        b.append(fk.text(x0 + 40, y, name, "t"))
    fy = ky + 4 * 34 + 20
    b.append(fk.text(320, fy, "Shares of variance across many ratings,", "t t-sm t-mid t-mute"))
    b.append(fk.text(320, fy + 24, "not of any one person’s rating. Each manager had 7 raters.", "t t-sm t-mid t-mute"))
    fk.write_svg("ch18/variance.svg", 640, fy + 44, "Sources of variance in performance ratings", "\n".join(b))


# ---------------------------------------------------------- Figure 18.3

# Dev's 52 weeks: 28 with a Wins line. Two long gaps, plus scattered empty weeks.
EMPTY = set(range(13, 20)) | set(range(34, 39)) | {3, 7, 9, 11, 22, 25, 28, 30, 42, 45, 48, 51}


def fig_habit():
    pen = fk.Pen(seed=183)
    b = [fk.text(24, 40, "Every week: one line", "t t-sans")]
    cell, step, gx, gy = 30, 38, 66, 64
    for wk in range(52):
        r, c = divmod(wk, 13)
        x, y = gx + c * step, gy + r * step
        cls = "f-paper" if wk in EMPTY else "f-a3s"
        b.append(f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="5" class="{cls}"/>')
        b.append(pen.rect(x, y, cell, cell, "k-thin" + (" k-mute" if wk in EMPTY else "")))
    assert 52 - len(EMPTY) == 28
    # label the two long gaps
    sx = gx  # spring gap: weeks 14 to 20 sit in row 1, columns 0 to 6
    b.append(fk.text(sx, gy + 4 * step + 26, "spring: 7 empty weeks", "t t-sm t-a1"))
    b.append(pen.arrow(sx + 90, gy + 4 * step + 6, sx + 90, gy + step + cell + 4, "k-thin k-a1", head=8))
    ax = gx + 10 * step + cell / 2  # autumn gap: weeks 35 to 39, row 2, columns 8 to 12
    b.append(fk.text(616, gy + 4 * step + 26, "autumn: 5 empty", "t t-sm t-a1 t-end"))
    b.append(pen.arrow(ax + 70, gy + 4 * step + 6, ax + 6, gy + 2 * step + cell + 4, "k-thin k-a1", head=8))
    y1 = gy + 4 * step + 64
    b.append(fk.text(24, y1, "Fill gaps from: sent messages, tickets, demo channel,", "t t-sm t-mute"))
    b.append(fk.text(24, y1 + 24, "and two colleagues who remember.", "t t-sm t-mute"))
    b.append(pen.arrow(320, y1 + 40, 320, y1 + 84, "k"))

    # quarter notes
    y2 = y1 + 124
    b.append(fk.text(24, y2, "Every quarter: three lines to your manager", "t t-sans"))
    for q in range(4):
        x, y = 40 + q * 148, y2 + 22
        b.append(f'<rect x="{x}" y="{y}" width="124" height="96" rx="8" class="f-a4"/>')
        b.append(pen.rect(x, y, 124, 96, "k-thin"))
        b.append(fk.text(x + 14, y + 28, f"Q{q + 1}", "t t-sm t-bold"))
        for j in range(3):
            b.append(pen.line(x + 14, y + 48 + j * 16, x + 104 - (j % 2) * 18, y + 48 + j * 16, "k-thin k-mute"))
    b.append(pen.arrow(320, y2 + 132, 320, y2 + 176, "k"))

    # the self-review page
    y3 = y2 + 216
    b.append(fk.text(24, y3, "Once a year: the self-review", "t t-sans"))
    px, py, pw, ph = 190, y3 + 22, 260, 210
    b.append(f'<rect x="{px}" y="{py}" width="{pw}" height="{ph}" rx="6" class="f-paper"/>')
    b.append(pen.rect(px, py, pw, ph, "k"))
    for j in range(5):
        y = py + 30 + j * 26
        b.append(f'<circle cx="{px + 22}" cy="{y}" r="5" class="f-a3s"/>')
        b.append(pen.line(px + 36, y, px + pw - 30 - (j * 13) % 50, y, "k-thin"))
    for j in range(2):
        y = py + 172 + j * 18
        b.append(pen.line(px + 20, y, px + pw - 20 - j * 60, y, "k-thin k-mute"))
    b.append(fk.lines(px + pw + 20, py + 60, ["five true", "stories"], "t t-sm", 24))
    b.append(fk.lines(px + pw + 20, py + 168, ["one honest", "paragraph"], "t t-sm", 24))
    yf = py + ph + 40
    b.append(fk.text(320, yf, "Illustrative: Dev’s year, not data.", "t t-sm t-mid t-mute"))
    fk.write_svg("ch18/habit.svg", 640, yf + 20, "The year-long evidence habit", "\n".join(b))


if __name__ == "__main__":
    fig_cycle()
    fig_variance()
    fig_habit()
    print("wrote chapter 18 figures")
