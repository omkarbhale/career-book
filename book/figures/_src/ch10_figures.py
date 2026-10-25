"""Regenerate Chapter 10's figures: python3 book/figures/_src/ch10_figures.py"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
import figkit as fk  # noqa: E402

# ------------------------------------------------------------ small props


def dial(cx, cy, r, value, colour):
    """A half-circle gauge with a needle; value runs 0 (left) to 1 (right)."""
    pen = fk.Pen(seed=int(cx + cy))
    arc = f'<path d="M{cx - r} {cy} A{r} {r} 0 0 1 {cx + r} {cy}" class="k-thick"/>'
    fill = f'<path d="M{cx - r + 8} {cy} A{r - 8} {r - 8} 0 0 1 {cx + r - 8} {cy} Z" class="f-{colour}"/>'
    ticks = ""
    for i in range(5):
        a = math.pi - i * math.pi / 4
        x0, y0 = cx + (r - 4) * math.cos(a), cy - (r - 4) * math.sin(a)
        x1, y1 = cx + (r - 14) * math.cos(a), cy - (r - 14) * math.sin(a)
        ticks += f'<path d="M{x0:.1f} {y0:.1f} L{x1:.1f} {y1:.1f}" class="k-thin"/>'
    a = math.pi - value * math.pi
    nx, ny = cx + (r - 18) * math.cos(a), cy - (r - 18) * math.sin(a)
    needle = pen.line(cx, cy, nx, ny, "k-thick")
    return fill + arc + ticks + needle + f'<circle cx="{cx}" cy="{cy}" r="6" class="f-ink"/>'


def star(cx, cy, r, cls="f-a3s k-thin"):
    pts = []
    for i in range(10):
        a = -math.pi / 2 + i * math.pi / 5
        rr = r if i % 2 == 0 else r * 0.45
        pts.append(f"{cx + rr * math.cos(a):.1f} {cy + rr * math.sin(a):.1f}")
    return f'<path d="M{" L".join(pts)} Z" class="{cls}"/>'


# ---------------------------------------------------------- Figure 10.1


def fig_trust():
    pen = fk.Pen(seed=10)
    cols = [
        (110, "Ability", "can you", "do the job?", ["your estimates", "come true"], "a1"),
        (320, "Benevolence", "are you", "on my side?", ["you warn me", "before I trip"], "a2"),
        (530, "Integrity", "do you keep to", "fair principles?", ["same you when", "nobody checks"], "a4"),
    ]
    b = []
    for x, name, q1, q2, ex, colour in cols:
        b.append(dial(x, 132, 72, 0.72, colour))
        b.append(fk.text(x, 40, name, f"t t-sans t-mid t-{colour if colour != 'a3' else 'a1'}"))
        b.append(fk.lines(x, 176, [q1, q2], "t t-mid", 28))
        b.append(fk.lines(x, 254, ex, "t t-sm t-mid t-mute", 24))
        b.append(pen.arrow(x, 316, 320 + (x - 320) * 0.28, 384, "k k-mute", bend=0, head=12))
    b += [
        pen.rect(70, 394, 500, 92, "f-a3 k"),
        fk.text(320, 432, "TRUST", "t t-sans t-mid"),
        fk.text(320, 466, "being willing to be vulnerable to you", "t t-mid"),
    ]
    fk.write_svg("ch10/trust.svg", 640, 510, "Three things trust is made of", "\n".join(b))


# ---------------------------------------------------------- Figure 10.2


def fig_repeated():
    pen = fk.Pen(seed=21)
    # Illustrative running totals over ten rounds.
    grab = [3, 4, 4.5, 4.5, 4.5, 4.4, 4.4, 4.3, 4.3, 4.2]
    keep = [1, 2.2, 3.4, 4.6, 5.8, 7.0, 8.2, 9.4, 10.6, 11.8]
    x0, x1, y0, y1 = 96, 600, 520, 276
    vmax = 12

    def px(i):
        return x0 + 20 + i * (x1 - x0 - 40) / 9

    def py(v):
        return y0 - v / vmax * (y0 - y1)

    def path(vals, cls):
        d = "M" + " L".join(f"{px(i):.1f} {py(v):.1f}" for i, v in enumerate(vals))
        dots = "".join(f'<circle cx="{px(i):.1f}" cy="{py(v):.1f}" r="5" class="{cls.replace("k-", "f-")}s"/>' for i, v in enumerate(vals))
        return f'<path d="{d}" class="k-thick {cls}"/>' + dots

    b = [
        # top panel: one round
        fk.text(24, 40, "One round, between strangers", "t t-sans"),
        pen.rect(24, 58, 290, 110, "f-a1 k"),
        fk.lines(40, 96, ["grab the credit", "+3 for you, today"], "t", 30),
        pen.rect(336, 58, 280, 110, "f-paper k"),
        fk.lines(352, 96, ["share the credit", "+1 for you, today"], "t", 30),
        fk.text(320, 196, "In a single round, grabbing wins.", "t t-mid t-mute"),
        # bottom panel: many rounds
        fk.text(24, 236, "Ten rounds, people who remember", "t t-sans"),
        pen.arrow(x0, y0, x1 + 16, y0, "k"),
        pen.arrow(x0, y0, x0, y1 - 20, "k"),
        path(keep, "k-a2"),
        path(grab, "k-a1"),
        fk.lines(128, 290, ["keep cooperating:", "trust compounds"], "t t-a2", 26),
        fk.lines(px(6), py(grab[6]) + 40, ["grab, then get", "frozen out"], "t t-a1 t-mid", 26),
        fk.text((x0 + x1) / 2, y0 + 38, "rounds: meetings, favours, deadlines →", "t t-mid"),
        f'<g transform="rotate(-90 56 {(y0 + y1) / 2})">{fk.text(56, (y0 + y1) / 2, "running total →", "t t-mid")}</g>',
        fk.text(320, y0 + 74, "Illustrative numbers, not data", "t t-sm t-mid t-mute"),
    ]
    fk.write_svg("ch10/repeated.svg", 640, 610, "One round versus a repeated game", "\n".join(b))


# ---------------------------------------------------------- Figure 10.3


def face(cx, cy, s, mouth):
    mouths = {
        "frown": "M-9 10 Q0 3 9 10",
        "smile": "M-10 5 Q0 15 10 5",
        "flat": "M-8 8 L8 8",
        "soft": "M-8 6 Q0 12 8 6",
    }
    return (
        f'<g transform="translate({cx} {cy}) scale({s})">'
        '<circle cx="0" cy="0" r="24" class="f-skin3 k-thin"/>'
        '<circle cx="-8" cy="-4" r="2" class="f-ink"/><circle cx="8" cy="-4" r="2" class="f-ink"/>'
        f'<path d="{mouths[mouth]}" class="k-thin"/></g>'
    )


def mask(cx, cy, s):
    return (
        f'<g transform="translate({cx} {cy}) scale({s})">'
        '<path d="M-26 -18 C-26 -32 26 -32 26 -18 L24 10 C18 28 -18 28 -24 10 Z" class="f-paper k"/>'
        '<path d="M-14 -8 Q-9 -13 -4 -8 M4 -8 Q9 -13 14 -8" class="k-thin"/>'
        '<path d="M-13 6 Q0 20 13 6" class="k"/>'
        '<path d="M26 -2 L44 18" class="k-thin"/><circle cx="46" cy="21" r="5" class="f-skin3 k-thin"/></g>'
    )


def fig_acting():
    pen = fk.Pen(seed=33)
    b = [
        fk.text(160, 38, "Surface acting", "t t-sans t-mid t-a1"),
        fk.text(480, 38, "Deep acting", "t t-sans t-mid t-a2"),
        pen.line(320, 20, 320, 470, "k-thin k-dash k-mute"),
        # left: a smiling mask held in front of a frowning face
        face(126, 128, 1.9, "frown"),
        mask(176, 132, 1.7),
        fk.lines(160, 236, ["inside: annoyed", "outside: a bright smile"], "t t-mid", 28),
        pen.rect(52, 284, 216, 54, "f-a1 k-thin"),
        fk.text(160, 319, "felt ≠ shown", "t t-mid t-bold"),
        fk.lines(160, 380, ["a gap you have to", "hold shut, all day"], "t t-sm t-mid t-mute", 24),
        fk.lines(160, 438, ["goes with worse", "well-being"], "t t-a1 t-mid", 28),
        # right: a thought bubble reframing the situation
        face(440, 132, 1.9, "soft"),
        '<path d="M486 92 C486 64 586 60 592 84 C612 86 614 120 592 124 C584 146 500 146 494 124 C474 122 472 96 486 92 Z" class="f-a2 k-thin"/>',
        '<circle cx="482" cy="132" r="5" class="f-a2 k-thin"/><circle cx="472" cy="146" r="3" class="f-a2 k-thin"/>',
        fk.lines(540, 100, ["she's scared,", "not hostile"], "t t-sm t-mid", 22),
        fk.lines(480, 236, ["you change how you", "see it, so you feel it"], "t t-mid", 28),
        pen.rect(372, 284, 216, 54, "f-a2 k-thin"),
        fk.text(480, 319, "felt ≈ shown", "t t-mid t-bold"),
        fk.lines(480, 380, ["nothing to hold", "shut"], "t t-sm t-mid t-mute", 24),
        fk.lines(480, 438, ["weak links", "to strain"], "t t-a2 t-mid", 28),
        pen.line(24, 482, 616, 482, "k-thin k-mute"),
        fk.lines(320, 516, ["Neither is choosing your words or your volume.", "That is register, not acting."], "t t-sm t-mid t-mute", 26),
    ]
    fk.write_svg("ch10/acting.svg", 640, 560, "Surface acting versus deep acting", "\n".join(b))


# ---------------------------------------------------------- Figure 10.4


def fig_ledger():
    pen = fk.Pen(seed=44)
    rows = [
        ("+", "did the boring fix nobody asked for", 1, "a2"),
        ("+", "kept a small promise, on time", 1, "a2"),
        ("+", "credited Kai by name in stand-up", 1, "a2"),
        ("−", "snapped at someone in a review", 3, "a1"),
        ("+", "warned early that a task would slip", 1, "a2"),
        ("+", "admitted a mistake before anyone found it", 1, "a2"),
    ]
    b = [
        pen.rect(40, 24, 560, 440, "f-paper k"),
        pen.line(40, 76, 600, 76, "k"),
        pen.line(462, 24, 462, 464, "k-thin"),
        fk.text(64, 60, "The trust ledger", "t t-sans"),
        fk.text(531, 60, "weight", "t t-sans t-mid"),
    ]
    y = 118
    for sign, label, weight, colour in rows:
        b.append(fk.text(64, y, sign, f"t t-lg t-bold t-{colour}"))
        b.append(fk.text(96, y, label, "t"))
        bw = 24 * weight
        b.append(f'<rect x="{531 - bw / 2:.1f}" y="{y - 22}" width="{bw}" height="26" rx="5" class="f-{colour}s"/>')
        y += 52
    b += [
        pen.line(60, y - 18, 580, y - 18, "k-thin k-mute"),
        fk.text(64, y + 16, "balance: what people will vouch for", "t t-bold"),
        fk.lines(320, 506, ["One withdrawal can cancel several deposits.", "Illustrative weights, not a formula."], "t t-sm t-mid t-mute", 26),
    ]
    fk.write_svg("ch10/ledger.svg", 640, 548, "The trust ledger", "\n".join(b))


if __name__ == "__main__":
    fig_trust()
    fig_repeated()
    fig_acting()
    fig_ledger()
    print("wrote chapter 10 figures")
