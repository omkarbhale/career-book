"""Regenerate Chapter 14's figures: python3 book/figures/_src/ch14_figures.py"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
import figkit as fk  # noqa: E402


# ---------------------------------------------------------- Figure 14.1


def fig_dial():
    pen = fk.Pen(seed=14)
    cx, cy, R = 330, 262, 168

    def pt(deg, r=R):
        a = math.radians(deg)
        return cx + r * math.cos(a), cy - r * math.sin(a)

    x0, y0 = pt(180)
    x1, y1 = pt(0)
    b = [
        f'<path d="M{x0:.1f} {y0:.1f} A{R} {R} 0 0 1 {x1:.1f} {y1:.1f}" class="k-thick k-a2"/>',
        f'<path d="M{cx - R + 26:.1f} {cy:.1f} A{R - 26} {R - 26} 0 0 1 {cx + R - 26:.1f} {cy:.1f}" class="k-thin k-mute k-dash"/>',
        fk.text(x0, cy + 34, "formal", "t t-sans t-mid"),
        fk.text(x1, cy + 34, "casual", "t t-sans t-mid"),
    ]
    marks = [
        (165, ["client board", "meeting"]),
        (135, ["incident review"]),
        (105, ["all-hands"]),
        (75, ["team stand-up"]),
        (45, ["the #old-faithful", "channel"]),
        (15, ["lunch with Kai"]),
    ]
    for deg, rows in marks:
        tx, ty = pt(deg, R - 10)
        ox, oy = pt(deg, R + 10)
        b.append(f'<path d="M{tx:.1f} {ty:.1f} L{ox:.1f} {oy:.1f}" class="k"/>')
        lx, ly = pt(deg, R + 24)
        anchor = "t-end" if deg > 95 else ("t-mid" if deg > 85 else "")
        if deg > 150 or deg < 30:
            ly -= 10
        b.append(fk.lines(lx, ly - (len(rows) - 1) * 12 + 4, rows, f"t {anchor}".strip(), 24))
    # pointer at "all-hands"
    px, py = pt(105, R - 44)
    b += [
        f'<path d="M{cx} {cy} L{px:.1f} {py:.1f}" class="k-thick k-a1"/>',
        f'<circle cx="{cx}" cy="{cy}" r="34" class="f-paper k"/>',
        f'<circle cx="{cx}" cy="{cy}" r="9" class="f-a1s k-thin"/>',
        fk.text(cx, cy + 66, "same you, different volume", "t t-mid t-mute"),
    ]
    # the two boxes underneath
    boxes = [
        (40, "turns with the dial", "t-a2", ["words", "volume", "jokes", "what you share"], "f-a2"),
        (350, "never turns", "t-a4", ["values", "honesty", "kindness", "keeping your word"], "f-a4"),
    ]
    for x, head, colour, rows, fill in boxes:
        b.append(f'<path d="{pen.rect_d(x, 362, 270, 200)}" class="{fill} k"/>')
        b.append(fk.text(x + 135, 398, head, f"t t-sans t-mid {colour}"))
        for i, row in enumerate(rows):
            y = 438 + i * 34
            b.append(f'<circle cx="{x + 34}" cy="{y - 7}" r="4" class="f-ink"/>')
            b.append(fk.text(x + 50, y, row, "t"))
    fk.write_svg("ch14/dial.svg", 660, 590, "The professionalism dial", "\n".join(b))


# ---------------------------------------------------------- Figure 14.2


def fig_humour():
    pen = fk.Pen(seed=21)
    rungs = [
        ("a group", "a team, a job, an identity", 170),
        ("a person in the room", "teasing, even friendly", 112),
        ("an in-joke", "only lands with insiders", 62),
        ("the situation", "the deploy, the coffee machine", 26),
        ("yourself", "your own mistake", 10),
    ]
    top, step = 120, 98
    lx0, lx1 = 74, 132
    bottom = top + step * (len(rungs) - 1)
    b = [
        pen.line(lx0, top - 40, lx0, bottom + 40, "k-thick"),
        pen.line(lx1, top - 40, lx1, bottom + 40, "k-thick"),
        fk.text(lx0 - 20, top - 70, "riskier", "t t-sans t-a1"),
        fk.text(lx0 - 20, bottom + 76, "safer", "t t-sans t-a2"),
        fk.text(470, top - 74, "upside", "t t-sans t-mute"),
        fk.text(470, top - 52, "downside", "t t-sans t-a1"),
        '<rect x="438" y="' + str(top - 86) + '" width="22" height="12" rx="3" class="f-a3s"/>',
        '<rect x="438" y="' + str(top - 64) + '" width="22" height="12" rx="3" class="f-a1s"/>',
    ]
    for i, (head, note, down) in enumerate(rungs):
        y = top + i * step
        b.append(pen.line(lx0, y, lx1, y, "k"))
        b.append(fk.text(lx0 + 29, y - 12, str(5 - i), "t t-sm t-bold t-mid"))
        b.append(fk.text(160, y - 6, head, "t"))
        b.append(fk.text(160, y + 20, note, "t t-sm t-mute"))
        b.append(f'<rect x="452" y="{y - 22}" width="70" height="16" rx="4" class="f-a3s"/>')
        b.append(f'<rect x="452" y="{y + 2}" width="{down}" height="16" rx="4" class="f-a1s"/>')
    # Dev's joke on rung five
    b += [
        fk.avatar("dev", 36, top - 2, 46, "h-dev"),
        fk.text(160, top + 50, "Dev's all-hands joke: the sales team", "t t-sm t-a1"),
        pen.line(24, bottom + 120, 636, bottom + 120, "k-thin k-dash k-mute"),
        fk.text(330, bottom + 154, "the audience decides whether it landed", "t t-mid"),
        fk.text(330, bottom + 182, "our ranking, from the research on humour and status; not a measured scale", "t t-sm t-mid t-mute"),
    ]
    fk.write_svg("ch14/humour.svg", 660, bottom + 200, "Humour targets ranked by risk", "\n".join(b))


# ---------------------------------------------------------- Figure 14.3


def fig_culture():
    pen = fk.Pen(seed=33)
    x0, x1, base, height = 60, 600, 300, 190

    def curve(mean, sd):
        pts = []
        for i in range(61):
            x = x0 + (x1 - x0) * i / 60
            z = (x - mean) / sd
            pts.append((x, base - height * math.exp(-0.5 * z * z)))
        return "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts)

    ma, mb, sd = 290, 372, 104
    b = [
        fk.text(330, 40, "illustrative curves", "t t-sm t-mid t-mute"),
        f'<path d="{curve(ma, sd)}" class="k-thick k-a2"/>',
        f'<path d="{curve(mb, sd)}" class="k-thick k-a4 k-dash"/>',
        pen.arrow(x0 - 10, base + 4, x1 + 24, base + 4, "k"),
        fk.text(x0 - 6, base + 76, "← prefers indirect feedback", "t t-sm"),
        fk.text(x1 + 20, base + 76, "prefers direct feedback →", "t t-sm t-end"),
        fk.text(ma - 70, base - height - 14, "people in country A", "t t-a2 t-end"),
        fk.text(mb + 64, base - height - 14, "people in country B", "t t-a4"),
    ]
    # two individuals far from their country's average, on the axis
    for x, colour, label, anchor in ((540, "a2", "Dev's colleague, country A", "t-end"), (118, "a4", "someone from country B", "")):
        b.append(f'<circle cx="{x}" cy="{base + 4}" r="9" class="f-{colour}s k-thin"/>')
        lx = x + 14 if anchor else x - 14
        b.append(fk.text(lx, base + 38, label, f"t t-sm t-{colour} {anchor}".strip()))
    # stacked bar
    by, bw = 470, 540
    split = x0 + bw * 0.8
    b += [
        fk.text(x0, by - 16, "where the variation in cultural values lies", "t t-sans"),
        f'<path d="{pen.rect_d(x0, by, split - x0, 48)}" class="f-a2 k"/>',
        f'<path d="{pen.rect_d(split, by, x0 + bw - split, 48)}" class="f-a4 k"/>',
        fk.text((x0 + split) / 2, by + 32, "within countries: about 80%", "t t-mid"),
        fk.text(x0 + bw, by + 80, "between countries: about 20%", "t t-end"),
    ]
    fk.write_svg("ch14/culture.svg", 660, 570, "Cultural values vary more within countries than between them", "\n".join(b))


if __name__ == "__main__":
    fig_dial()
    fig_humour()
    fig_culture()
    print("wrote chapter 14 figures")
