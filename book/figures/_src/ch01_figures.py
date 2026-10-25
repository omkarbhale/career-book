"""Regenerate Chapter 1's figures and the cover: python3 book/figures/_src/ch01_figures.py"""

import math
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
import figkit as fk  # noqa: E402

# ------------------------------------------------------------ small props


def stopwatch(cx, cy, r=24):
    return (
        f'<rect x="{cx - 4}" y="{cy - r - 9}" width="8" height="7" rx="2" class="f-ink"/>'
        f'<circle cx="{cx}" cy="{cy}" r="{r}" class="f-paper k"/>'
        f'<path d="M{cx} {cy} L{cx} {cy - r + 7} M{cx} {cy} L{cx + r * 0.45:.1f} {cy + 4}" class="k"/>'
        f'<circle cx="{cx}" cy="{cy}" r="2.6" class="f-ink"/>'
    )


def resume(x, y, w=44, h=56):
    rows = "".join(
        f'<path d="M{x + 7} {y + 18 + i * 8} L{x + w - 7 - (i % 2) * 9} {y + 18 + i * 8}" class="k-thin k-mute"/>'
        for i in range(5)
    )
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3" class="f-paper k-thin"/>'
        f'<path d="M{x + 7} {y + 9} L{x + w - 16} {y + 9}" class="k"/>{rows}'
    )


def mug(x, y, s=1.0):
    return (
        f'<g transform="translate({x} {y}) scale({s})"><path d="M0 0 L2 22 L20 22 L22 0 Z" class="f-a3 k-thin"/>'
        '<path d="M22 5 C31 5 31 16 21 16" class="k-thin"/>'
        '<path d="M6 -4 Q8 -9 6 -14 M14 -4 Q16 -9 14 -14" class="k-thin k-mute"/></g>'
    )


def bubbles(x, y, s=1.0):
    return (
        f'<g transform="translate({x} {y}) scale({s})">'
        '<path d="M0 0 h26 a4 4 0 0 1 4 4 v12 a4 4 0 0 1 -4 4 h-16 l-6 6 v-6 h-4 a4 4 0 0 1 -4 -4 v-12 a4 4 0 0 1 4 -4 z" class="f-a2 k-thin"/>'
        '<path d="M14 16 h26 a4 4 0 0 1 4 4 v12 a4 4 0 0 1 -4 4 h-4 v6 l-6 -6 h-16 a4 4 0 0 1 -4 -4 v-12 a4 4 0 0 1 4 -4 z" class="f-paper k-thin"/></g>'
    )


def checklist(x, y, s=1.0):
    rows = "".join(
        f'<path d="M4 {6 + i * 11} l3 3 l6 -7" class="k-thin k-a2"/><path d="M17 {6 + i * 11} h16" class="k-thin k-mute"/>'
        for i in range(3)
    )
    return f'<g transform="translate({x} {y}) scale({s})"><rect x="0" y="-4" width="38" height="38" rx="3" class="f-paper k-thin"/>{rows}</g>'


def handshake(x, y, s=1.0):
    return (
        f'<g transform="translate({x} {y}) scale({s})">'
        '<path d="M0 14 L12 6 L22 10 L30 4 L42 12" class="k"/>'
        '<path d="M8 18 C14 26 22 26 28 20 L36 16" class="k"/>'
        '<path d="M12 6 L20 16 M22 10 L28 20" class="k-thin"/></g>'
    )


def star(cx, cy, r, cls="f-a3s k"):
    pts = []
    for i in range(10):
        a = -math.pi / 2 + i * math.pi / 5
        rr = r if i % 2 == 0 else r * 0.45
        pts.append(f"{cx + rr * math.cos(a):.1f} {cy + rr * math.sin(a):.1f}")
    return f'<path d="M{" L".join(pts)} Z" class="{cls}"/>'


def polaroid(cx, cy, w, h, angle, inner, caption):
    return (
        f'<g transform="rotate({angle} {cx} {cy})">'
        f'<rect x="{cx - w / 2}" y="{cy - h / 2}" width="{w}" height="{h}" rx="4" class="f-paper k"/>'
        f'<rect x="{cx - w / 2 + 10}" y="{cy - h / 2 + 10}" width="{w - 20}" height="{h - 52}" class="f-a1"/>'
        f"{inner}"
        f'{fk.text(cx, cy + h / 2 - 15, caption, "t t-sm t-mid")}</g>'
    )


def film_strip(x, y, frames, fw=74, fh=62, angle=0):
    w = len(frames) * (fw + 10) + 10
    holes = "".join(
        f'<rect x="{x + 8 + i * 14}" y="{y + 5}" width="7" height="6" rx="1.5" class="f-paper"/>'
        f'<rect x="{x + 8 + i * 14}" y="{y + fh + 25}" width="7" height="6" rx="1.5" class="f-paper"/>'
        for i in range(int((w - 8) // 14))
    )
    cells = ""
    for i, art in enumerate(frames):
        fx = x + 10 + i * (fw + 10)
        cells += f'<rect x="{fx}" y="{y + 16}" width="{fw}" height="{fh}" rx="3" class="f-a2"/>'
        cells += f'<g transform="translate({fx} {y + 16})">{art}</g>'
    return (
        f'<g transform="rotate({angle} {x} {y})"><rect x="{x}" y="{y}" width="{w}" height="{fh + 36}" rx="4" class="f-ink"/>'
        f"{holes}{cells}</g>"
    )


FRAMES = [mug(26, 22), bubbles(14, 10), checklist(18, 12), handshake(16, 18)]

# ---------------------------------------------------------- Figure 1.1


def fig_two_games():
    pen = fk.Pen(seed=3)
    b = [
        fk.text(175, 48, "The snapshot game", "t-sans t-a1 t-mid"),
        fk.text(505, 48, "The long game", "t-sans t-a2 t-mid"),
        polaroid(165, 160, 150, 170, -5, resume(126, 92) + fk.avatar("dev", 196, 125, 50, "p-dev"), "you, in an hour"),
        stopwatch(278, 104),
        film_strip(372, 102, FRAMES[:3], angle=-3),
        fk.text(505, 240, "you, every day, for years", "t t-mid"),
        pen.line(340, 268, 340, 596, "k-thin k-dash k-mute"),
    ]
    rows = [
        ("Who judges", "strangers", "people who know you"),
        ("For how long", "a few hours, over weeks", "years, every working day"),
        ("What they see", "a trailer you edit", "the whole film, uncut"),
        ("What wins", "clear, honest signals", "being reliably yourself"),
    ]
    for i, (label, left, right) in enumerate(rows):
        y = 300 + i * 78
        b.append(f'<rect x="250" y="{y - 18}" width="180" height="26" rx="13" class="f-soft"/>')
        b.append(fk.text(340, y, label, "t-sans t-mute t-mid"))
        b.append(fk.text(175, y + 38, left, "t t-mid t-a1"))
        b.append(fk.text(505, y + 38, right, "t t-mid t-a2"))
    fk.write_svg(
        "ch01/two-games.svg", 680, 620,
        "The snapshot game and the long game compared", "\n".join(b),
    )


# ---------------------------------------------------------- Figure 1.2


def fig_quadrant():
    pen = fk.Pen(seed=5)
    b = [
        '<rect x="370" y="40" width="250" height="250" class="f-a3"/>',
        pen.arrow(100, 540, 640, 540, "k"),
        pen.arrow(100, 540, 100, 24, "k"),
        pen.line(370, 40, 370, 540, "k-thin k-dash k-mute"),
        pen.line(100, 290, 640, 290, "k-thin k-dash k-mute"),
        fk.text(370, 584, "good at doing the job (the film) →", "t t-mid"),
        f'<g transform="rotate(-90 58 290)">{fk.text(58, 290, "good at getting hired (the trailer) →", "t t-mid")}</g>',
        fk.text(235, 74, "All trailer", "t-sans t-mid"),
        fk.avatar("rex", 235, 152, 84, "q-rex"),
        fk.lines(235, 228, ["great in interviews,", "hard to work with"], "t t-sm t-mid", 25),
        fk.text(495, 74, "One you", "t-sans t-mid"),
        star(495, 150, 46),
        fk.lines(495, 228, ["a true trailer", "of a good film"], "t t-sm t-mid", 24),
        fk.text(235, 324, "Not yet", "t-sans t-mid t-mute"),
        fk.lines(235, 362, ["where everyone", "starts, at something"], "t t-sm t-mid t-mute", 24),
        fk.text(520, 324, "All film", "t-sans t-mid"),
        fk.avatar("bea", 560, 392, 78, "q-bea"),
        fk.lines(560, 462, ["brilliant at the work,", "invisible on paper"], "t t-sm t-mid", 24),
        fk.avatar("dev", 412, 468, 58, "q-dev"),
        fk.text(412, 518, "Dev, today", "t t-sm t-mid t-a1"),
        pen.arrow(428, 432, 404, 262, "k k-dash k-a1", bend=-18, head=14),
    ]
    fk.write_svg("ch01/quadrant.svg", 660, 610, "Two skills plotted against each other", "\n".join(b))


# ---------------------------------------------------------- Figure 1.3


def fig_correlation():
    rng = random.Random(42)
    r = 0.42
    pts = []
    for _ in range(150):
        zx = rng.gauss(0, 1)
        zy = r * zx + math.sqrt(1 - r * r) * rng.gauss(0, 1)
        pts.append((max(-2.4, min(2.4, zx)), max(-2.4, min(2.4, zy))))
    x0, x1, y0, y1 = 110, 610, 500, 60

    def px(z):
        return x0 + (z + 2.5) / 5 * (x1 - x0)

    def py(z):
        return y0 - (z + 2.5) / 5 * (y0 - y1)

    pen = fk.Pen(seed=9)
    dots = []
    coral, teal = [], []
    for zx, zy in pts:
        if zx > 0.7 and zy < -0.3:
            cls = "f-a1s"
            coral.append((px(zx), py(zy)))
        elif zx < -0.3 and zy > 0.7:
            cls = "f-a2s"
            teal.append((px(zx), py(zy)))
        else:
            cls = "f-mute"
        dots.append(f'<circle cx="{px(zx):.1f}" cy="{py(zy):.1f}" r="5" class="{cls}"/>')

    def nearest(group, x, y):
        return min(group, key=lambda p: (p[0] - x) ** 2 + (p[1] - y) ** 2)

    cx_t, cy_t = nearest(teal, 205, 150)
    cx_c, cy_c = nearest(coral, 480, 400)
    b = [
        pen.arrow(x0, y0 + 10, x1 + 20, y0 + 10, "k"),
        pen.arrow(x0 - 10, y0 + 10, x0 - 10, y1 - 20, "k"),
        *dots,
        pen.line(px(-2.4), py(-2.4 * r), px(2.4), py(2.4 * r), "k k-dash"),
        f'<rect x="{px(2.4) - 160:.1f}" y="{py(2.4 * r) - 64:.1f}" width="156" height="32" rx="6" class="f-paper"/>',
        fk.text(px(2.4) - 8, py(2.4 * r) - 40, "trend: r = .42", "t t-end"),
        fk.lines(130, 92, ["fumbled the interview,", "star on the job"], "t t-a2", 26),
        pen.arrow(205, 130, cx_t + 4, cy_t - 8, "k-thin k-a2", bend=12),
        fk.lines(600, 418, ["aced the interview,", "struggled on the job"], "t t-a1 t-end", 26),
        pen.arrow(470, 408, cx_c + 3, cy_c + 8, "k-thin k-a1", bend=-12),
        fk.text(360, 548, "interview score →", "t t-mid"),
        f'<g transform="rotate(-90 70 280)">{fk.text(70, 280, "job performance a year later →", "t t-mid")}</g>',
        fk.text(360, 586, "Simulated people, drawn with a correlation of .42", "t t-sm t-mute t-mid"),
    ]
    fk.write_svg(
        "ch01/correlation.svg", 660, 600,
        "Scatter plot of simulated interview scores against job performance", "\n".join(b),
    )


# ---------------------------------------------------------- Figure 1.4


def fig_loop():
    pen = fk.Pen(seed=13)
    cx, cy, R = 340, 290, 190
    left, right = cx - R, cx + R
    b = [
        f'<path d="M{left} {cy} A{R} {R} 0 0 1 {right} {cy}" class="k-thick k-a1"/>',
        f'<path d="M{right} {cy} A{R} {R} 0 0 1 {left} {cy}" class="k-thick k-a2"/>',
        f'<path d="M{right} {cy + 2} L{right - 11} {cy - 14} M{right} {cy + 2} L{right + 11} {cy - 14}" class="k-thick k-a1"/>',
        f'<path d="M{left} {cy - 2} L{left - 11} {cy + 14} M{left} {cy - 2} L{left + 11} {cy + 14}" class="k-thick k-a2"/>',
        fk.text(cx, 64, "Part I · the snapshot game", "t-sans t-a1 t-mid"),
        fk.text(cx, 538, "Part II · the long game", "t-sans t-a2 t-mid"),
    ]
    for ang, word in ((158, "apply"), (90, "interview"), (22, "offer")):
        a = math.radians(ang)
        tx, ty = cx + (R - 34) * math.cos(a), cy - (R - 34) * math.sin(a) + 8
        b.append(fk.text(tx, ty, word, "t t-mid t-a1"))
    for ang, word in ((-26, "do the work"), (-90, "earn trust"), (-154, "grow")):
        a = math.radians(ang)
        tx, ty = cx + (R - 66) * math.cos(a), cy - (R - 66) * math.sin(a) + 8
        b.append(fk.text(tx, ty, word, "t t-mid t-a2"))
    b += [
        f'<circle cx="{right}" cy="{cy}" r="15" class="f-paper k"/>',
        star(right, cy, 9, "f-a3s k-thin"),
        fk.lines(right + 24, cy - 6, ["you’re", "hired"], "t", 26),
        f'<circle cx="{left}" cy="{cy}" r="15" class="f-paper k"/>',
        fk.lines(left - 22, cy - 48, ["reputation,", "skills, stories,", "people:", "your next", "trailer"], "t t-end", 26),
        fk.avatar("dev", cx, cy - 26, 96, "l-dev"),
        fk.text(cx, cy + 52, "one you", "t t-lg t-bold t-mid"),
        fk.text(cx, cy + 82, "in both games", "t t-mid t-mute"),
    ]
    fk.write_svg("ch01/loop.svg", 640, 570, "The loop between the two games", "\n".join(b))


# ---------------------------------------------------------- Figure 1.5


def fig_map():
    part1 = ["Stay or go?", "The other side", "Your evidence", "Paper you", "People", "Interviews", "Show your work", "Offer & exit"]
    part2 = ["Trust", "First 90 days", "Reliability", "Talk & write", "The dial", "Friends at work", "Conflict", "Growing"]
    L, Rr, top, bot = 120, 480, 120, 880
    b = [
        f'<path d="M{L + 80} {top} C{L + 20} {top} {L} {top + 20} {L} {top + 80} L{L} {bot - 80} C{L} {bot - 20} {L + 20} {bot} {L + 80} {bot}" class="k-thick k-a1"/>',
        f'<path d="M{L + 80} {bot} L{Rr - 80} {bot}" class="k-thick k-mute"/>',
        f'<path d="M{Rr - 80} {bot} C{Rr - 20} {bot} {Rr} {bot - 20} {Rr} {bot - 80} L{Rr} {top + 80} C{Rr} {top + 20} {Rr - 20} {top} {Rr - 80} {top}" class="k-thick k-a2"/>',
        f'<path d="M{Rr - 80} {top} L{L + 80} {top}" class="k-thick k-mute k-dash"/>',
        f'<g transform="rotate(-90 70 {(top + bot) / 2})">{fk.text(70, (top + bot) / 2, "Part I · the snapshot game", "t-sans t-a1 t-mid")}</g>',
        f'<g transform="rotate(90 530 {(top + bot) / 2})">{fk.text(530, (top + bot) / 2, "Part II · the long game", "t-sans t-a2 t-mid")}</g>',
    ]
    ys = [top + 110 + i * 84 for i in range(8)]
    for i, (y, name) in enumerate(zip(ys, part1)):
        b.append(f'<circle cx="{L}" cy="{y}" r="17" class="f-paper k k-a1"/>')
        b.append(fk.text(L, y + 7, str(i + 2), "t t-sm t-bold t-mid"))
        b.append(fk.text(L + 30, y + 8, name, "t"))
    for i, (y, name) in enumerate(zip(reversed(ys), part2)):
        b.append(f'<circle cx="{Rr}" cy="{y}" r="17" class="f-paper k k-a2"/>')
        b.append(fk.text(Rr, y + 7, str(i + 10), "t t-sm t-bold t-mid"))
        b.append(fk.text(Rr - 30, y + 8, name, "t t-end"))
    b += [
        f'<circle cx="{L + 80}" cy="{top}" r="22" class="f-a3 k"/>',
        fk.text(L + 80, top + 8, "1", "t t-bold t-mid"),
        fk.text(L + 80, top - 36, "Start: two games", "t t-mid"),
        f'<circle cx="{Rr - 80}" cy="{top}" r="22" class="f-a3 k"/>',
        fk.text(Rr - 80, top + 8, "E", "t t-bold t-mid"),
        fk.text(Rr - 80, top - 36, "Epilogue: the loop", "t t-mid"),
        f'<circle cx="300" cy="{bot}" r="18" class="f-paper k"/>',
        star(300, bot, 11, "f-a3s k-thin"),
        fk.text(300, bot + 46, "you’re hired", "t t-mid"),
        fk.text(300, top + 40, "the next move", "t t-sm t-mid t-mute"),
    ]
    fk.write_svg("ch01/map.svg", 600, 960, "Map of the book as a loop of chapters", "\n".join(b))


# ---------------------------------------------------------- the cover


def cover():
    b = [
        polaroid(150, 210, 190, 220, -6, resume(98, 132, 56, 70) + fk.avatar("dev", 196, 170, 64, "c-dev-photo"), "the snapshot"),
        stopwatch(250, 112, 26),
        film_strip(372, 150, FRAMES, fw=66, fh=56, angle=9),
        fk.text(520, 372, "the long game", "t t-lg t-mid"),
        '<ellipse cx="318" cy="444" rx="56" ry="9" class="f-soft"/>',
        fk.person("dev", 318, 446, 1.05,
                  '<g transform="translate(26 -96) rotate(-12)"><rect x="0" y="0" width="30" height="21" rx="2" class="f-paper k-thin"/>'
                  '<path d="M4 21 L-2 27 L30 27 L30 21" class="f-soft k-thin"/><circle cx="15" cy="10" r="3.4" class="f-a2"/></g>'),
    ]
    fk.write_svg("front/cover.svg", 660, 470, "Cover illustration", "\n".join(b))


if __name__ == "__main__":
    fig_two_games()
    fig_quadrant()
    fig_correlation()
    fig_loop()
    fig_map()
    cover()
    print("wrote chapter 1 figures and the cover")
