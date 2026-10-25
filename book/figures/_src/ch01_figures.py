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


def staircase(x, y, step=34, rise=26, n=3):
    """Steps rising to the right from (x, y) (bottom-left corner), with a star on the top step."""
    parts = []
    for i in range(n):
        parts.append(
            f'<rect x="{x + i * step}" y="{y - (i + 1) * rise}" width="{step}" height="{(i + 1) * rise}" class="f-a4 k-thin"/>'
        )
    parts.append(star(x + (n - 0.5) * step, y - n * rise - 22, 16, "f-a3s k-thin"))
    return "".join(parts)

# ---------------------------------------------------------- Figure 1.1


def fig_two_games():
    pen = fk.Pen(seed=3)
    bands = [
        ("The snapshot game \u00b7 Part I", "t-a1",
         ["judged by strangers, in hours", "they see a trailer you edit", "what wins: clear, honest signals"],
         polaroid(118, 108, 120, 138, -5, resume(84, 54, 38, 46) + fk.avatar("dev", 140, 82, 40, "p-dev"), "you, in an hour")
         + stopwatch(200, 46, 20)),
        ("The long game \u00b7 Part II", "t-a2",
         ["judged by colleagues, every day", "they see the whole film, uncut", "what wins: being reliably yourself"],
         film_strip(20, 72, FRAMES[:3], fw=52, fh=46, angle=-4)),
        ("The career game \u00b7 Part III", "t-a4",
         ["judged by managers and panels, in cycles", "they see the film, summarised", "what wins: good work, made visible"],
         staircase(40, 200) + checklist(160, 136, 1.1)),
    ]
    b = []
    for i, (head, colour, rows, art) in enumerate(bands):
        y0 = i * 236
        if i:
            b.append(pen.line(24, y0 + 4, 616, y0 + 4, "k-thin k-dash k-mute"))
        b.append(f'<g transform="translate(0 {y0})">{art}</g>')
        b.append(fk.text(250, y0 + 62, head, f"t-sans {colour}"))
        b.append(fk.lines(250, y0 + 104, rows, f"t {colour}", 36))
    fk.write_svg("ch01/three-games.svg", 640, 708, "The three games compared", "\n".join(b))


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
    cx, cy, R = 360, 300, 170

    def pt(deg, r=R):
        a = math.radians(deg)
        return cx + r * math.cos(a), cy - r * math.sin(a)

    def arc(d0, d1, cls):
        x0, y0 = pt(d0)
        x1, y1 = pt(d1)
        return f'<path d="M{x0:.1f} {y0:.1f} A{R} {R} 0 0 1 {x1:.1f} {y1:.1f}" class="{cls}"/>'

    def head(deg, cls):
        # arrowhead at angle deg, pointing clockwise along the circle
        x, y = pt(deg)
        a = math.radians(deg)
        tx, ty = math.sin(a), math.cos(a)  # clockwise tangent on screen
        wings = []
        for sgn in (1, -1):
            ang = math.radians(150) * sgn
            wx = x + 15 * (tx * math.cos(ang) - ty * math.sin(ang))
            wy = y + 15 * (tx * math.sin(ang) + ty * math.cos(ang))
            wings.append(f"M{x:.1f} {y:.1f} L{wx:.1f} {wy:.1f}")
        return f'<path d="{" ".join(wings)}" class="{cls}"/>'

    b = [
        arc(150, 30, "k-thick k-a1"), head(32, "k-thick k-a1"),
        arc(30, -90, "k-thick k-a2"), head(-88, "k-thick k-a2"),
        arc(-90, -210, "k-thick k-a4"), head(-208, "k-thick k-a4"),
        fk.text(cx, cy - R - 34, "Part I \u00b7 the snapshot game", "t-sans t-a1 t-mid"),
    ]
    x, y = pt(-38, R + 22)
    b.append(fk.lines(x, y, ["Part II \u00b7", "the long game"], "t-sans t-a2", 22))
    x, y = pt(-142, R + 22)
    b.append(fk.lines(x, y, ["Part III \u00b7", "the career game"], "t-sans t-a4 t-end", 22))
    for deg, word, colour, rr in ((128, "apply", "t-a1", 46), (90, "interview", "t-a1", 40), (52, "offer", "t-a1", 46),
                                  (-6, "do the work", "t-a2", 78), (-58, "earn trust", "t-a2", 52),
                                  (-122, "get good", "t-a4", 52), (-174, "get reviewed", "t-a4", 80)):
        tx, ty = pt(deg, R - rr)
        b.append(fk.text(tx, ty + 8, word, f"t t-mid {colour}"))
    hx, hy = pt(30)
    nx, ny = pt(150)
    b += [
        f'<circle cx="{hx:.1f}" cy="{hy:.1f}" r="15" class="f-paper k"/>',
        star(hx, hy, 9, "f-a3s k-thin"),
        fk.lines(hx + 26, hy - 6, ["you\u2019re", "hired"], "t", 26),
        f'<circle cx="{nx:.1f}" cy="{ny:.1f}" r="15" class="f-paper k"/>',
        fk.lines(nx - 24, ny - 52, ["reputation,", "skills, stories,", "people: your", "next trailer"], "t t-end", 26),
        fk.avatar("dev", cx, cy - 22, 92, "l-dev"),
        fk.text(cx, cy + 52, "one you", "t t-lg t-bold t-mid"),
        fk.text(cx, cy + 80, "in all three games", "t t-mid t-mute"),
    ]
    fk.write_svg("ch01/loop.svg", 720, 600, "The loop between the three games", "\n".join(b))


# ---------------------------------------------------------- Figure 1.5


def fig_map():
    pen = fk.Pen(seed=17)
    groups = [
        ("Part I \u00b7 the snapshot game", "a1", 2,
         ["Stay or go?", "The other side", "Your evidence", "Paper you", "People, not portals", "Interviews", "Show your work", "Offer and exit"]),
        ("Part II \u00b7 the long game", "a2", 10,
         ["Trust", "First 90 days", "Reliability", "Talk and write", "The dial", "Friends at work", "Conflict", "Under pressure"]),
        ("Part III \u00b7 the career game", "a4", 18,
         ["The review", "The promotion case", "What to get good at", "Expert or manager?", "The whole career"]),
    ]
    X, gap = 110, 46
    y = 110
    b = [f'<circle cx="{X}" cy="{y}" r="22" class="f-a3 k"/>', fk.text(X, y + 8, "1", "t t-bold t-mid"),
         fk.text(X + 40, y + 8, "Start: three games", "t")]
    line_top = y
    segments = []
    for title, colour, first, names in groups:
        y += 58
        b.append(fk.text(X + 40, y + 6, title, f"t-sans t-{colour}"))
        seg_start = y - 30
        for i, name in enumerate(names):
            y += gap
            b.append(f'<circle cx="{X}" cy="{y}" r="17" class="f-paper k k-{colour}"/>')
            b.append(fk.text(X, y + 7, str(first + i), "t t-sm t-bold t-mid"))
            b.append(fk.text(X + 40, y + 8, name, "t"))
            if first == 2 and i == len(names) - 1:
                pass
        segments.append((seg_start, y + 20, colour))
        if first == 2:
            y += gap
            b.append(f'<circle cx="{X}" cy="{y}" r="18" class="f-paper k"/>')
            b.append(star(X, y, 11, "f-a3s k-thin"))
            b.append(fk.text(X + 40, y + 8, "you\u2019re hired", "t t-mute"))
    y += gap + 10
    b.append(f'<circle cx="{X}" cy="{y}" r="22" class="f-a3 k"/>')
    b.append(fk.text(X, y + 8, "E", "t t-bold t-mid"))
    b.append(fk.text(X + 40, y + 8, "Epilogue: the loop", "t"))
    bottom = y
    lines = [f'<path d="M{X} {line_top + 22} L{X} {segments[0][0]}" class="k-thick k-mute"/>']
    prev_end = None
    for start, end, colour in segments:
        if prev_end is not None:
            lines.append(f'<path d="M{X} {prev_end} L{X} {start}" class="k-thick k-mute"/>')
        lines.append(f'<path d="M{X} {start} L{X} {end}" class="k-thick k-{colour}"/>')
        prev_end = end
    lines.append(f'<path d="M{X} {prev_end} L{X} {bottom - 22}" class="k-thick k-mute"/>')
    loop = (
        f'<path d="M{X + 24} {bottom + 10} C{X + 160} {bottom + 70} 560 {bottom + 20} 560 {bottom - 120} '
        f'L560 {line_top + 80} C560 {line_top - 70} {X + 70} {line_top - 86} {X + 6} {line_top - 28}" class="k-thick k-dash k-a1"/>'
        f'<path d="M{X + 6} {line_top - 28} L{X + 9} {line_top - 46} M{X + 6} {line_top - 28} L{X + 24} {line_top - 32}" class="k-thick k-a1"/>'
    )
    mid = (line_top + bottom) / 2
    label = f'<g transform="rotate(90 590 {mid})">{fk.text(590, mid, "the next move, made from strength", "t t-a1 t-mid")}</g>'
    fk.write_svg("ch01/map.svg", 620, int(bottom + 80), "Map of the book as a loop of chapters", "\n".join(lines + b) + loop + label)


# ---------------------------------------------------------- the cover


def cover():
    b = [
        polaroid(150, 200, 190, 220, -6, resume(98, 122, 56, 70) + fk.avatar("dev", 196, 160, 64, "c-dev-photo"), "the snapshot"),
        stopwatch(250, 102, 26),
        film_strip(372, 110, FRAMES, fw=66, fh=56, angle=9),
        fk.text(560, 292, "the long game", "t t-lg t-mid"),
        staircase(470, 470, step=40, rise=30),
        fk.text(612, 500, "the career game", "t t-lg t-end"),
        '<ellipse cx="318" cy="474" rx="56" ry="9" class="f-soft"/>',
        fk.person("dev", 318, 476, 1.05,
                  '<g transform="translate(26 -96) rotate(-12)"><rect x="0" y="0" width="30" height="21" rx="2" class="f-paper k-thin"/>'
                  '<path d="M4 21 L-2 27 L30 27 L30 21" class="f-soft k-thin"/><circle cx="15" cy="10" r="3.4" class="f-a2"/></g>'),
    ]
    fk.write_svg("front/cover.svg", 660, 520, "Cover illustration", "\n".join(b))


if __name__ == "__main__":
    fig_two_games()
    fig_quadrant()
    fig_correlation()
    fig_loop()
    fig_map()
    cover()
    print("wrote chapter 1 figures and the cover")
