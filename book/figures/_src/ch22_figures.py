"""Regenerate Chapter 22's figures: python3 book/figures/_src/ch22_figures.py"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
import figkit as fk  # noqa: E402


def arc(cx, cy, r, a0, a1):
    """An arc path from angle a0 to a1 (degrees, 0 = east, counter-clockwise, y up)."""
    p0 = (cx + r * math.cos(math.radians(a0)), cy - r * math.sin(math.radians(a0)))
    p1 = (cx + r * math.cos(math.radians(a1)), cy - r * math.sin(math.radians(a1)))
    large = 1 if abs(a1 - a0) > 180 else 0
    sweep = 0 if a1 > a0 else 1
    return f"M{p0[0]:.1f} {p0[1]:.1f} A{r} {r} 0 {large} {sweep} {p1[0]:.1f} {p1[1]:.1f}"


# ---------------------------------------------------------- Figure 22.1


def fig_loops():
    pen = fk.Pen(seed=221)
    loops = [
        (130, 200, 62, "Corvid", "tester", ""),
        (370, 200, 92, "Lanternfish", "developer, then senior", ""),
        (680, 200, 122, "next", "staff", " k-dash"),
    ]
    b = []
    for cx, cy, r, name, role, dash in loops:
        # snapshot on top (coral), long game on the right (teal), career game on the left (purple)
        b.append(f'<path d="{arc(cx, cy, r, 150, 30)}" class="k-thick k-a1{dash}"/>')
        b.append(f'<path d="{arc(cx, cy, r, 25, -95)}" class="k-thick k-a2{dash}"/>')
        b.append(f'<path d="{arc(cx, cy, r, -100, -215)}" class="k-thick k-a4{dash}"/>')
        b.append(fk.text(cx, cy - 4, name, "t t-bold t-mid"))
        b.append(fk.text(cx, cy + 22, role, "t t-sm t-mid t-mute"))
    # arrows between the loops
    b += [
        pen.arrow(196, 228, 272, 228, "k-thick", bend=-10, head=12),
        pen.arrow(466, 228, 552, 228, "k-thick", bend=-10, head=12),
        fk.text(234, 340, "what each loop made:", "t t-sm t-mid"),
        fk.text(234, 364, "skills, stories, people", "t t-sm t-mid"),
        pen.arrow(234, 316, 234, 250, "k-thin k-mute", head=9),
    ]
    # legend
    b += [
        '<path d="M560 352 L600 352" class="k-thick k-a1"/>', fk.text(608, 360, "snapshot", "t t-sm"),
        '<path d="M560 382 L600 382" class="k-thick k-a2"/>', fk.text(608, 390, "long game", "t t-sm"),
        '<path d="M710 352 L750 352" class="k-thick k-a4"/>', fk.text(758, 360, "career game", "t t-sm"),
        '<path d="M710 382 L750 382" class="k-thick k-dash"/>', fk.text(758, 390, "not yet", "t t-sm"),
    ]
    # the timeline
    b += [
        pen.arrow(30, 420, 850, 420, "k k-mute", head=12),
        fk.text(850, 450, "years", "t t-sm t-end t-mute"),
        fk.text(440, 488, "not a ladder: each turn starts from what the last one built", "t t-mid t-bold"),
    ]
    fk.write_svg("ch22/loops.svg", 880, 510, "A career as a sequence of loops", "\n".join(b))


# ---------------------------------------------------------- Figure 22.2


def fig_meaning():
    pen = fk.Pen(seed=222)
    b = [fk.text(30, 40, "meaningful work goes with...", "t t-lg t-bold")]
    rows = [
        (0.75, "large: r = .70 or more", ["work engagement,", "commitment,", "job satisfaction"], "f-a4s"),
        (0.47, "moderate to large: r about .44 to .49", ["life satisfaction, meaning", "in life, general health,", "less wish to quit"], "f-a4"),
        (0.27, "small to moderate: up to about .33", ["helping beyond the role,", "self-rated performance,", "less bad mood"], "f-soft"),
    ]
    y = 70
    for r, head, lines, fill in rows:
        b.append(fk.text(30, y + 26, head, "t t-bold"))
        w = 300 * r / 0.75
        b.append(f'<path d="{pen.rect_d(30, y + 42, w, 74)}" class="{fill} k"/>')
        for i, row in enumerate(lines):
            b.append(fk.text(350, y + 66 + i * 26, row, "t"))
        y += 140
    b += [
        pen.line(30, y + 4, 630, y + 4, "k-thin k-mute"),
        fk.text(30, y + 32, "bar length shows the size of the correlation; ranges from one", "t t-sm t-mute"),
        fk.text(30, y + 56, "meta-analysis of 44 articles, not individual values;", "t t-sm t-mute"),
        fk.text(30, y + 80, "performance is self-rated", "t t-sm t-mute"),
    ]
    fk.write_svg("ch22/meaning.svg", 660, int(y + 100), "What meaningful work goes with", "\n".join(b))


# ---------------------------------------------------------- Figure 22.3


def fig_strength():
    pen = fk.Pen(seed=223)
    b = []

    def column(x, head, colour, fill, rows, last):
        out = [
            f'<path d="{pen.rect_d(x, 60, 280, 330)}" class="{fill} k"/>',
            fk.text(x + 140, 40, head, f"t t-sans t-mid {colour}"),
        ]
        for i, row in enumerate(rows):
            for j, part in enumerate(row):
                out.append(fk.text(x + 20, 104 + i * 66 + j * 26, part, "t" if j == 0 else "t t-sm t-mute"))
        out.append(f'<path d="{pen.rect_d(x + 20, 330, 240, 44)}" class="f-paper k-thin"/>')
        out.append(fk.text(x + 140, 360, last, "t t-bold t-mid"))
        return out

    b += column(
        20, "the first time (chapter 1)", "t-a1", "f-a1",
        [("47 applications,", "46 noes"), ("a résumé of duties", ""), ("nobody inside", "to vouch for her")],
        "any yes looks like rescue",
    )
    b += column(
        380, "this time", "t-a4", "f-a4",
        [("one call,", "and it came to her"), ("a Wins log and", "a story bank"), ("people who will vouch,", "inside and out")],
        "she can say no",
    )
    b += [
        pen.arrow(250, 420, 430, 420, "k-thick k-a3", bend=34, head=14),
        fk.text(340, 470, "the loop: the film became the trailer", "t t-mid t-bold"),
        fk.text(340, 500, "same game, different starting position", "t t-sm t-mid t-mute"),
        fk.avatar("dev", 340, 225, 64, "strength-dev"),
    ]
    fk.write_svg("ch22/strength.svg", 680, 520, "Two job searches, before and after the loop", "\n".join(b))


if __name__ == "__main__":
    fig_loops()
    fig_meaning()
    fig_strength()
    print("wrote chapter 22 figures")
