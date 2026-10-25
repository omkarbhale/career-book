"""Regenerate Chapter 16's figures: python3 book/figures/_src/ch16_figures.py"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
import figkit as fk  # noqa: E402


def pie(cx, cy, r, slices):
    """slices: list of (fraction, fill class); drawn clockwise from 12 o'clock."""
    out, a0 = [], -math.pi / 2
    for frac, cls in slices:
        a1 = a0 + frac * 2 * math.pi
        x0, y0 = cx + r * math.cos(a0), cy + r * math.sin(a0)
        x1, y1 = cx + r * math.cos(a1), cy + r * math.sin(a1)
        large = 1 if frac > 0.5 else 0
        out.append(
            f'<path d="M{cx} {cy} L{x0:.1f} {y0:.1f} A{r} {r} 0 {large} 1 {x1:.1f} {y1:.1f} Z" class="{cls} k-thin"/>'
        )
        a0 = a1
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" class="k"/>')
    return "".join(out)


# ---------------------------------------------------------- Figure 16.1


def fig_credit():
    pen = fk.Pen(seed=16)
    b = [
        f'<path d="{pen.rect_d(110, 14, 440, 40)}" class="f-a3 k-thin"/>',
        fk.text(330, 42, "illustrative numbers: the direction is the finding", "t t-sm t-mid"),
        fk.text(170, 94, "how Dev remembers it", "t t-bold t-mid"),
        pie(170, 196, 82, [(0.85, "f-dev"), (0.15, "f-a4")]),
        fk.lines(170, 308, ["found it, reproduced it,", "wrote the patch"], "t t-sm t-mid", 22),
        fk.text(490, 94, "how Marcus remembers it", "t t-bold t-mid"),
        pie(490, 196, 82, [(0.5, "f-dev"), (0.5, "f-a4")]),
        fk.lines(490, 308, ["knew the ledger, fixed the", "lock, added the logging"], "t t-sm t-mid", 22),
        fk.text(330, 380, "each remembers their own part best", "t t-mid t-a1"),
        pen.line(30, 404, 630, 404, "k-thin k-dash k-mute"),
        fk.text(330, 446, "listed out, step by step", "t t-bold t-mid"),
        pie(150, 560, 94, [(1 / 6, "f-dev")] * 4 + [(1 / 6, "f-a4")] * 2),
    ]
    for i in range(6):
        a = -math.pi / 2 + (i + 0.5) * math.pi / 3
        b.append(fk.text(150 + 62 * math.cos(a), 568 + 62 * math.sin(a), str(i + 1), "t t-sm t-bold t-mid"))
    legend = [
        ("1  found the race condition", "t-a1"),
        ("2  reproduced it, one Saturday", "t-a1"),
        ("3  wrote the patch", "t-a1"),
        ("4  tested it", "t-a1"),
        ("5  fixed the ledger lock", "t-a4"),
        ("6  added the logging", "t-a4"),
    ]
    b.append(f'<rect x="282" y="476" width="20" height="14" rx="3" class="f-dev k-thin"/>')
    b.append(fk.text(310, 489, "Dev", "t t-sm t-bold"))
    b.append(f'<rect x="372" y="476" width="20" height="14" rx="3" class="f-a4 k-thin"/>')
    b.append(fk.text(400, 489, "Marcus", "t t-sm t-bold"))
    for i, (row, cls) in enumerate(legend):
        b.append(fk.text(282, 524 + i * 26, row, f"t t-sm {cls}"))
    b.append(fk.text(282, 690, "both agree on this one", "t t-mid t-a2", style="text-anchor:start"))
    fk.write_svg("ch16/credit.svg", 660, 710, "The credit gap", "\n".join(b))


# ---------------------------------------------------------- Figure 16.2


def fig_conflict():
    pen = fk.Pen(seed=26)
    x0, x1, y0, y1 = 110, 620, 520, 40
    xm, ym = (x0 + x1) / 2, (y0 + y1) / 2
    b = [
        f'<rect x="{xm}" y="{ym}" width="{x1 - xm}" height="{y0 - ym}" class="f-a2"/>',
        f'<rect x="{xm}" y="{y1}" width="{x1 - xm}" height="{ym - y1}" class="f-a1"/>',
        pen.arrow(x0, y0, x1 + 20, y0, "k"),
        pen.arrow(x0, y0, x0, y1 - 16, "k"),
        pen.line(xm, y1, xm, y0, "k-thin k-dash k-mute"),
        pen.line(x0, ym, x1, ym, "k-thin k-dash k-mute"),
        fk.text(xm, y0 + 42, "task conflict: disagreeing about the work →", "t t-mid"),
        f'<g transform="rotate(-90 64 {ym})">{fk.text(64, ym, "relationship conflict: friction between people →", "t t-mid")}</g>',
    ]
    cells = [
        ((x0 + xm) / 2, ym + 90, "quiet", ["fine, unless", "it's silence"], "t-mute"),
        ((xm + x1) / 2, ym + 90, "productive debate", ["can improve", "decisions"], "t-a2"),
        ((x0 + xm) / 2, y1 + 90, "a feud", ["people dislike each other,", "about nothing in particular"], ""),
        ((xm + x1) / 2, y1 + 90, "the spiral", ["every disagreement", "is personal"], "t-a1"),
    ]
    for cx, cy, head, rows, colour in cells:
        b.append(fk.text(cx, cy, head, f"t t-sans t-mid {colour}".strip()))
        b.append(fk.lines(cx, cy + 38, rows, "t t-sm t-mid", 24))
    b += [
        pen.arrow(xm + 22, ym + 160, xm + 22, ym - 60, "k-thick k-dash k-a1", bend=-30, head=14),
        fk.text(xm + 40, ym + 196, "the leak", "t t-bold t-a1"),
    ]
    fk.write_svg("ch16/conflict.svg", 660, 580, "Task conflict versus relationship conflict", "\n".join(b))


# ---------------------------------------------------------- Figure 16.3


def fig_escalation():
    pen = fk.Pen(seed=36)
    rungs = [
        ("talk to the person", "if it's safe"),
        ("write it down", "dates, facts, witnesses"),
        ("your manager, or theirs", ""),
        ("HR, or a formal grievance", ""),
        ("the reporting channel", "whistleblowing or ethics line"),
        ("outside", "a regulator, a lawyer, a public body"),
    ]
    bottom, step = 560, 84
    lx0, lx1 = 86, 140
    top = bottom - step * (len(rungs) - 1)
    b = [
        pen.line(lx0, top - 44, lx0, bottom + 34, "k-thick"),
        pen.line(lx1, top - 44, lx1, bottom + 34, "k-thick"),
    ]
    for i, (head, note) in enumerate(rungs):
        y = bottom - i * step
        b.append(pen.line(lx0, y, lx1, y, "k"))
        b.append(fk.text(lx1 + 24, y - (4 if note else -8), f"{i + 1}. {head}", "t"))
        if note:
            b.append(fk.text(lx1 + 46, y + 20, note, "t t-sm t-mute"))
    # skip arrow, then the side rail as a box under the ladder
    b += [
        pen.arrow(60, bottom - 6, 60, bottom - 3 * step + 6, "k-thick k-dash k-a1", bend=26, head=13),
        fk.text(8, bottom - 1.5 * step + 8, "skip", "t t-sm t-a1"),
        fk.text(lx1 + 24, bottom + 74, "keep your notes at every rung", "t t-a2"),
    ]
    by = bottom + 104
    b += [
        f'<path d="{pen.rect_d(24, by, 632, 148)}" class="f-a1 k"/>',
        fk.text(44, by + 36, "skip rungs when", "t t-sans t-a1"),
        fk.text(44, by + 76, "\u2022 harassment or discrimination", "t"),
        fk.text(44, by + 112, "\u2022 safety or a crime", "t"),
        fk.text(360, by + 76, "\u2022 the problem is your manager", "t"),
        fk.text(360, by + 112, "\u2022 you fear retaliation", "t"),
        fk.text(656, by + 182, "a general guide, not legal advice", "t t-sm t-end t-mute"),
    ]
    fk.write_svg("ch16/escalation.svg", 680, bottom + 300, "An escalation ladder", "\n".join(b))


if __name__ == "__main__":
    fig_credit()
    fig_conflict()
    fig_escalation()
    print("wrote chapter 16 figures")
