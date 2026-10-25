"""Regenerate Chapter 20's figures: python3 book/figures/_src/ch20_figures.py"""

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


# ---------------------------------------------------------- Figure 20.1


def fig_compound():
    pen = fk.Pen(seed=201)
    x0, x1, y0, y1 = 70, 616, 64, 520  # plot box (y0 top)
    xm, ym = (x0 + x1) / 2, (y0 + y1) / 2
    b = [
        fk.text(24, 36, "Skills that compound", "t t-sans"),
        f'<rect x="{xm}" y="{y0}" width="{x1 - xm}" height="{ym - y0}" class="f-a3"/>',
        pen.rect(x0, y0, x1 - x0, y1 - y0, "k"),
        pen.line(xm, y0, xm, y1, "k-thin k-dash"),
        pen.line(x0, ym, x1, ym, "k-thin k-dash"),
        # quadrant labels
        fk.lines(x0 + 16, y0 + 34, ["a niche:", "a bet on one market"], "t", 28),
        fk.lines(x1 - 16, y0 + 34, ["career capital:", "it compounds"], "t t-bold t-end", 28),
        star(x1 - 30, y0 + 98, 16),
        fk.text(x0 + 16, y1 - 20, "a hobby", "t t-mute"),
        fk.lines(x1 - 16, y1 - 48, ["a commodity:", "everyone has it soon"], "t t-end", 28),
    ]
    # skills
    dots = [
        (xm + 46, y0 + 116, ["Dev: making", "systems testable"]),
        (xm + 46, y0 + 176, ["Bea: zero-downtime", "migrations"]),
    ]
    for cx, cy, lab in dots:
        b.append(f'<circle cx="{cx}" cy="{cy}" r="9" class="f-a4s"/>')
        b.append(fk.lines(cx + 18, cy + 6, lab, "t t-sm", 22))
    hx, hy = x1 - 70, ym + 64
    b += [
        f'<circle cx="{hx}" cy="{hy}" r="9" class="f-a1s"/>',
        fk.text(hx - 16, hy + 7, "this year’s hot tool", "t t-sm t-end"),
        pen.arrow(hx - 8, hy + 14, xm - 40, y1 - 70, "k-thin k-dash k-a1", bend=-20, head=10),
        fk.text(xm - 50, y1 - 46, "goes stale", "t t-sm t-a1 t-end"),
    ]
    # axes
    b += [
        fk.text(xm, y1 + 34, "few employers value it  →  many employers value it", "t t-mid"),
        f'<g transform="rotate(-90 40 {ym})">{fk.text(40, ym, "easy to pick up  →  hard to acquire", "t t-mid")}</g>',
        fk.text(xm, y1 + 72, "A thinking tool, not a measurement.", "t t-sm t-mid t-mute"),
    ]
    fk.write_svg("ch20/compound.svg", 640, y1 + 92, "Skills that compound", "\n".join(b))


# ---------------------------------------------------------- Figure 20.2

# Macnamara, Hambrick & Oswald (2014): variance in performance explained by deliberate practice.
DOMAINS = [("Games", 26), ("Music", 21), ("Sports", 18), ("Education", 4), ("Professions", 0.6)]


def fig_practice():
    pen = fk.Pen(seed=202)
    bx, bw, bh, gap = 170, 430, 40, 66
    b = [fk.text(24, 40, "What practice explains", "t t-sans")]
    y = 74
    for i, (name, pct) in enumerate(DOMAINS):
        b.append(fk.text(bx - 16, y + 28, name, "t t-end"))
        fw = max(2.5, bw * pct / 100)
        b.append(f'<rect x="{bx}" y="{y}" width="{bw}" height="{bh}" class="f-paper"/>')
        b.append(f'<rect x="{bx}" y="{y}" width="{fw:.1f}" height="{bh}" class="f-a4s"/>')
        b.append(pen.rect(bx, y, bw, bh, "k"))
        label = "under 1%" if pct < 1 else f"{pct}%"
        b.append(fk.text(bx + fw + 12, y + 28, label, "t t-bold"))
        if i == 0:
            b.append(fk.text(bx + bw - 12, y + 28, "everything else", "t t-sm t-end t-mute"))
        y += gap
    py = y - gap + bh
    b.append(pen.arrow(bx + 150, py + 52, bx + 6, py + 6, "k-thin k-a1", bend=-10, head=10))
    b.append(fk.text(bx + 160, py + 60, "your job is here", "t t-a1"))
    b.append(fk.text(320, py + 108, "Share of differences in performance explained by", "t t-sm t-mid t-mute"))
    b.append(fk.text(320, py + 132, "deliberate practice. Macnamara, Hambrick and Oswald (2014).", "t t-sm t-mid t-mute"))
    fk.write_svg("ch20/practice.svg", 640, py + 152, "What deliberate practice explains, by domain", "\n".join(b))


# ---------------------------------------------------------- Figure 20.3


def fig_loop():
    pen = fk.Pen(seed=203)
    cx, cy = 320, 236
    steps = [
        (cx, 86, ["1  pick one", "sub-skill"]),
        (528, cy, ["2  do it for real,", "a notch harder"]),
        (cx, 386, ["3  get feedback, fast,", "about the task"]),
        (112, cy, ["4  write down", "what you’ll change"]),
    ]
    w, h = 210, 76
    b = [f'<circle cx="{cx}" cy="{cy}" r="56" class="f-a4"/>',
         f'<path d="{pen.circle_d(cx, cy, 56)}" class="k-thin"/>',
         fk.lines(cx, cy - 4, ["one sub-skill", "at a time"], "t t-sm t-mid", 24)]
    for x, y, lab in steps:
        b.append(f'<rect x="{x - w / 2}" y="{y - h / 2}" width="{w}" height="{h}" rx="14" class="f-paper"/>')
        b.append(pen.rect(x - w / 2, y - h / 2, w, h, "k"))
        b.append(fk.lines(x, y - 6, lab, "t t-mid", 28))
    # clockwise arrows between the boxes
    b += [
        pen.arrow(cx + w / 2 + 4, 86, 528, cy - h / 2 - 6, "k-thick k-a4", bend=-24),
        pen.arrow(528, cy + h / 2 + 6, cx + w / 2 + 4, 386, "k-thick k-a4", bend=-24),
        pen.arrow(cx - w / 2 - 4, 386, 112, cy + h / 2 + 6, "k-thick k-a4", bend=-24),
        pen.arrow(112, cy - h / 2 - 6, cx - w / 2 - 4, 86, "k-thick k-a4", bend=-24),
    ]
    # inset: challenge vs skill gained
    gx0, gx1, gy0, gy1 = 150, 520, 530, 690  # gy0 top, gy1 baseline
    b += [
        fk.text(24, 476, "Challenge pays, with diminishing returns", "t t-sans"),
        pen.arrow(gx0, gy1, gx1 + 20, gy1, "k"),
        pen.arrow(gx0, gy1, gx0, gy0 - 10, "k"),
        fk.text((gx0 + gx1) / 2, gy1 + 32, "challenge →", "t t-mid"),
        f'<g transform="rotate(-90 {gx0 - 24} {(gy0 + gy1) / 2})">{fk.text(gx0 - 24, (gy0 + gy1) / 2, "skill gained →", "t t-mid")}</g>',
        f'<path d="M{gx0} {gy1} C{gx0 + 120} {gy1 - 110} {gx0 + 220} {gy1 - 120} {gx1} {gy1 - 118}" class="k-thick k-mute"/>',
        f'<path d="M{gx0} {gy1} C{gx0 + 120} {gy1 - 112} {gx0 + 240} {gy1 - 140} {gx1} {gy1 - 162}" class="k-thick k-a2"/>',
        fk.text(gx1, gy1 - 174, "with feedback", "t t-a2 t-end"),
        fk.text(gx1, gy1 - 92, "without", "t t-mute t-end"),
        fk.text(320, gy1 + 68, "Shape illustrative, after DeRue and Wellman (2009).", "t t-sm t-mid t-mute"),
    ]
    fk.write_svg("ch20/loop.svg", 640, gy1 + 88, "A learning loop at work", "\n".join(b))


if __name__ == "__main__":
    fig_compound()
    fig_practice()
    fig_loop()
    print("wrote chapter 20 figures")
