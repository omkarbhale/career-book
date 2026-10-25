"""Regenerate Chapter 17's figures: python3 book/figures/_src/ch17_figures.py"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
import figkit as fk  # noqa: E402


def machine(x, y, s=1.0):
    """A small drawing of Old Faithful, origin at its bottom-left corner."""
    return (
        f'<g transform="translate({x} {y}) scale({s})">'
        '<rect x="0" y="-62" width="46" height="62" rx="5" class="f-mute k-thin"/>'
        '<rect x="8" y="-54" width="30" height="14" rx="2" class="f-a3 k-thin"/>'
        '<path d="M14 -30 L32 -30 L30 -16 L16 -16 Z" class="f-paper k-thin"/>'
        '<path d="M20 -36 L20 -31 M26 -36 L26 -31" class="k-thin"/></g>'
    )


# ---------------------------------------------------------- Figure 17.1


def fig_jdr():
    pen = fk.Pen(seed=17)
    bx0, by0, bx1, by1 = 50, 420, 610, 326

    def beam_y(x):
        return by0 + (by1 - by0) * (x - bx0) / (bx1 - bx0)

    b = [
        pen.line(20, 452, 640, 452, "k-thin k-mute"),
        f'<path d="M330 {beam_y(330):.1f} L292 452 L368 452 Z" class="f-soft k"/>',
        f'<path d="M{bx0} {by0} L{bx1} {by1}" class="k-thick"/>',
    ]
    left = ["workload", "long hours", "after-hours messages", "faking feelings", "other people's jobs"]
    right = ["switching off", "feedback", "support", "control over how you work"]
    for items, cx, fill, head, colour in ((left, 178, "f-a1", "demands", "t-a1"), (right, 474, "f-a2", "resources", "t-a2")):
        base = beam_y(cx) - 4
        for i, label in enumerate(items):
            w = max(150, len(label) * 10 + 30)
            y = base - (i + 1) * 40
            b.append(f'<path d="{pen.rect_d(cx - w / 2, y, w, 36)}" class="{fill} k-thin"/>')
            b.append(fk.text(cx, y + 26, label, "t t-mid"))
        top = base - len(items) * 40
        b.append(fk.text(cx, top - 18, head, f"t t-sans t-mid {colour}"))
    b += [
        fk.avatar("dev", 70, 520, 64, "j-dev"),
        f'<path d="{pen.rect_d(112, 498, 140, 36)}" class="f-a1 k-thin"/>',
        fk.text(182, 524, "Old Faithful", "t t-mid"),
        pen.arrow(64, 214, 100, 492, "k k-dash k-a1", bend=34, head=11),
        fk.text(330, 590, "strain comes from demands; resources buffer it", "t t-mid t-mute"),
    ]
    fk.write_svg("ch17/jdr.svg", 660, 520, "Job demands and job resources on a seesaw", '<g transform="translate(0 -90)">' + "\n".join(b) + "</g>")


# ---------------------------------------------------------- Figure 17.2


def fig_helping():
    pen = fk.Pen(seed=27)
    cx, cy, R = 330, 330, 200
    nodes = [
        (90, ["someone asks", "for help"]),
        (18, ["you say yes", "(it's quicker than explaining)"]),
        (-54, ["you become", "“the person who”"]),
        (-132, ["more people", "ask"]),
        (162, ["less time for the work", "your review rewards"]),
    ]

    def pt(deg, r=R):
        a = math.radians(deg)
        return cx + r * math.cos(a), cy - r * math.sin(a)

    b = []
    order = [90, 18, -48, -132, -198]
    for d0, d1 in zip(order, order[1:] + [order[0] - 360]):
        x0, y0 = pt(d0 - 22)
        x1, y1 = pt(d1 + 22)
        b.append(pen.arrow(x0, y0, x1, y1, "k k-a4", bend=-26, head=11))
    for deg, rows in nodes:
        x, y = pt(deg)
        w = 232
        b.append(f'<path d="{pen.rect_d(x - w / 2, y - 34, w, 64)}" class="f-paper k"/>')
        b.append(fk.text(x, y - 6, rows[0], "t t-mid"))
        b.append(fk.text(x, y + 20, rows[1], "t t-sm t-mid t-mute"))
    b += [
        fk.avatar("dev", cx - 30, cy - 4, 70, "h-dev"),
        machine(cx + 14, cy + 34, 1.0),
        fk.text(cx, cy + 66, "the helping trap", "t t-sans t-mid t-a4"),
    ]
    ex, ey = pt(-48)
    b += [
        pen.arrow(ex + 70, ey + 32, ex + 150, ey + 104, "k-thick k-a3", bend=-10, head=14),
        fk.text(650, ey + 140, "hand it over: write it down,", "t t-bold t-end"),
        fk.text(650, ey + 168, "give it an owner", "t t-bold t-end"),
    ]
    fk.write_svg("ch17/helping.svg", 660, int(ey + 190), "The helping trap", "\n".join(b))


# ---------------------------------------------------------- Figure 17.3


def fig_slope():
    pen = fk.Pen(seed=37)
    land_y = 150
    steps = [190, 250, 310, 370]
    xs = [240, 340, 440, 540, 640]
    d = f"M30 {land_y} L232 {land_y}"
    d += f" L232 {steps[0]}"
    for i, y in enumerate(steps):
        d += f" L{xs[i + 1]} {y}"
        if i + 1 < len(steps):
            d += f" L{xs[i + 1]} {steps[i + 1]}"
    b = [
        f'<path d="{d}" class="k-thick"/>',
        f'<path d="M{xs[3]} {steps[3]} L{xs[4]} {steps[3]}" class="k-thick k-a1"/>',
        # the gate
        f'<path d="M218 {land_y} L218 {land_y - 70} M246 {land_y} L246 {land_y - 70}" class="k-thick"/>',
        f'<rect x="216" y="{land_y - 62}" width="32" height="12" rx="3" class="f-a3s k-thin"/>',
        f'<rect x="216" y="{land_y - 34}" width="32" height="12" rx="3" class="f-a3s k-thin"/>',
        fk.avatar("dev", 120, land_y - 38, 64, "s-dev"),
        fk.text(40, land_y + 34, "your line,", "t t-bold"),
        fk.text(40, land_y + 60, "set in advance", "t t-bold"),
        fk.text(640, 100, "each step makes", "t t-sm t-end t-mute"),
        fk.text(640, 122, "the next one feel normal", "t t-sm t-end t-mute"),
    ]
    for i, y in enumerate(steps):
        colour = "t-a1" if i == 3 else ""
        b.append(fk.text((xs[i] + xs[i + 1]) / 2 + (10 if i == 0 else 0), y - 12, str(i + 1), f"t t-bold t-mid {colour}".strip()))
    labels = [
        ("1. skip one test, just this once", ""),
        ("2. report amber as green: “it's basically fine”", ""),
        ("3. call a real failure flaky", ""),
        ("4. the client's numbers are wrong, and they don't know", "t-a1"),
    ]
    b.append(pen.line(24, 410, 640, 410, "k-thin k-dash k-mute"))
    for i, (row, colour) in enumerate(labels):
        b.append(fk.text(40, 452 + i * 40, row, f"t {colour}".strip()))
    fk.write_svg("ch17/slope.svg", 660, 600, "A slippery slope of small steps", "\n".join(b))


if __name__ == "__main__":
    fig_jdr()
    fig_helping()
    fig_slope()
    print("wrote chapter 17 figures")
