"""Regenerate Chapter 6's figures: python3 book/figures/_src/ch06_figures.py

The small helpers at the top are shared by the Chapter 7 to 9 scripts, which
import them from here.
"""

import math
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
import figkit as fk  # noqa: E402

# ------------------------------------------------------------ shared helpers


def badge(cx, cy, n, cls="f-a3"):
    """A numbered circle, for annotated parts of a figure."""
    return (
        f'<circle cx="{cx}" cy="{cy}" r="15" class="{cls} k-thin"/>'
        + fk.text(cx, cy + 7, str(n), "t t-mid t-bold")
    )


def bubble(pen, x, y, w, h, cls="f-paper k", tail="left"):
    """A speech bubble: a wobbly box with a small tail on one side, near the top."""
    body = f'<path d="{pen.rect_d(x, y, w, h)}" class="{cls}"/>'
    if tail == "left":
        t = f'<path d="M{x + 1} {y + 26} L{x - 16} {y + 34} L{x + 1} {y + 44}" class="{cls}"/>'
    elif tail == "right":
        t = f'<path d="M{x + w - 1} {y + 26} L{x + w + 16} {y + 34} L{x + w - 1} {y + 44}" class="{cls}"/>'
    else:
        t = ""
    return body + t


def dot(cx, cy, r=7, cls="f-mute"):
    return f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r}" class="{cls}"/>'


def ring(pen, cx, cy, r, cls):
    return f'<path d="{pen.circle_d(cx, cy, r, steps=14)}" class="{cls}"/>'


# ---------------------------------------------------------- Figure 6.1


def fig_tie_map():
    pen = fk.Pen(seed=61, wobble=1.4)
    cx, cy = 320, 380
    rng = random.Random(6)
    b = [
        ring(pen, cx, cy, 300, "f-soft k-thin"),
        ring(pen, cx, cy, 228, "f-a3 k-thin"),
        ring(pen, cx, cy, 100, "f-paper k"),
    ]
    # outer ring: faint dots for people you barely know
    for _ in range(30):
        a = rng.uniform(0, 2 * math.pi)
        r = rng.uniform(246, 284)
        x, y = cx + r * math.cos(a), cy + r * math.sin(a)
        if abs(x - cx) < 140 and abs(y - cy) > 220:
            continue  # keep the ring labels clear
        b.append(dot(x, y, 5, "f-mute"))
    b += [
        fk.text(cx, cy - 260, "very weak ties", "t t-sans t-mid t-mute"),
        fk.text(cx, cy + 270, "a name, a like, a badge", "t t-sm t-mid t-mute"),
        fk.text(cx, cy - 186, "moderately weak ties", "t t-sans t-mid"),
        fk.text(cx, cy - 156, "the sweet spot", "t t-mid t-bold"),
        fk.text(cx, cy - 60, "strong ties", "t t-sans t-mid"),
        fk.avatar("dev", cx, cy - 12, 54, "tm-dev"),
        fk.avatar("bea", cx - 40, cy + 44, 44, "tm-bea"),
        fk.avatar("meera", cx + 40, cy + 44, 44, "tm-meera"),
    ]
    chips = [
        (cx - 145, cy - 100, "Ana, from uni", "f-a1s"),
        (cx + 145, cy - 100, "ex-teammate", "f-mute"),
        (cx - 120, cy + 74, "a Corvid client", "f-mute"),
        (cx + 120, cy + 74, "meetup organiser", "f-mute"),
    ]
    for x, y, label, cls in chips:
        b.append(dot(x, y, 9, cls + " k-thin"))
        b.append(fk.text(x, y + 32, label, "t t-mid" + (" t-a1 t-bold" if cls == "f-a1s" else "")))
    b.append(fk.lines(cx, 736, ["most job help arrives from the middle ring,", "because there are so many people in it"], "t t-mid", 30))
    fk.write_svg("ch06/tie-map.svg", 640, 790, "A tie map: strong, moderately weak and very weak ties", "\n".join(b))


# ---------------------------------------------------------- Figure 6.2


def fig_referral_funnel():
    pen = fk.Pen(seed=62)
    x0, width = 40, 560

    def seg(x, y, pct, h, cls):
        w = width * pct / 100
        return f'<path d="{pen.rect_d(x, y, w, h)}" class="{cls}"/>', x + w

    b = [fk.text(x0, 34, "One large US firm, 62,127 applicants", "t t-sans")]
    # applicants
    b.append(fk.text(x0 + width, 86, "Who applied", "t t-bold t-end"))
    p, x1 = seg(x0, 100, 6.1, 64, "f-a1 k")
    b.append(p)
    p, x2 = seg(x1, 100, 60.1, 64, "f-soft k-thin")
    b.append(p)
    p, x3 = seg(x2, 100, 33.8, 64, "f-paper k-thin")
    b.append(p)
    b.append(fk.text((x1 + x2) / 2, 140, "job boards 60.1%", "t t-mid"))
    b.append(fk.lines((x2 + x3) / 2, 128, ["everything", "else 33.8%"], "t t-mid t-mute", 26))
    b.append(fk.text(x0, 196, "referred 6.1%", "t t-a1 t-bold"))
    # hires
    b.append(fk.text(x0 + width, 300, "Who got hired", "t t-bold t-end"))
    p, h1 = seg(x0, 314, 29.1, 64, "f-a1 k")
    b.append(p)
    p, h2 = seg(h1, 314, 23.5, 64, "f-soft k-thin")
    b.append(p)
    p, h3 = seg(h2, 314, 47.4, 64, "f-paper k-thin")
    b.append(p)
    b.append(fk.lines((x0 + h1) / 2, 342, ["referred", "29.1%"], "t t-mid t-a1 t-bold", 26))
    b.append(fk.lines((h1 + h2) / 2, 342, ["job boards", "23.5%"], "t t-mid", 26))
    b.append(fk.text((h2 + h3) / 2, 354, "everything else 47.4%", "t t-mid t-mute"))
    # the widening referral share
    b.append(pen.line(x1, 166, h1, 312, "k-thin k-dash k-a1"))
    b.append(fk.lines(250, 232, ["referred: 6.1% of who applies,", "29.1% of who gets hired"], "t t-a1", 30))
    b.append(fk.lines(x0, 420, [
        "everything else = the company website, applying on your own",
        "initiative, campus recruiting and other channels",
    ], "t t-sm t-mute", 26))
    b.append(fk.text(x0, 478, "Data: Brown, Setren & Topa (2016), shares of each stage by channel", "t t-sm t-mute"))
    fk.write_svg("ch06/referral-funnel.svg", 640, 500, "Referred candidates as a share of applicants and of hires", "\n".join(b))


# ---------------------------------------------------------- Figure 6.3


def fig_good_ask():
    pen = fk.Pen(seed=63)
    b = [fk.text(100, 24, "not this:", "t t-sm t-mute")]
    b.append(bubble(pen, 100, 36, 470, 60, "f-soft k-thin"))
    b.append(fk.text(124, 75, "Hey stranger! Can I pick your brain sometime?", "t t-mute"))
    b.append(pen.line(108, 92, 560, 42, "k-thick k-a1"))
    b.append(fk.text(100, 134, "but this:", "t t-sm"))
    b.append(fk.avatar("dev", 52, 190, 62, "ga-dev"))
    b.append(bubble(pen, 100, 150, 520, 560, "f-paper k"))
    sections = [
        ("the bridge", ["Hi Ana, it's Dev from second-year databases:", "you saved my exam with a charger."]),
        ("the specific ask", ["I've seen Lanternfish is hiring a backend", "developer, and I'd love to apply. Would you", "be comfortable referring me, or telling me", "who to talk to?"]),
        ("make it easy", ["I can send the link, my résumé and two lines", "on why I fit, so it takes you two minutes."]),
        ("the clean exit", ["And if it's not a good time, or you don't know", "my work well enough, no problem at all."]),
    ]
    y = 192
    for i, (label, rows) in enumerate(sections, start=1):
        if i > 1:
            b.append(pen.line(140, y - 30, 600, y - 30, "k-thin k-dash k-mute"))
        b.append(badge(136, y - 6, i))
        b.append(fk.text(162, y, label, "t t-sans"))
        b.append(fk.lines(162, y + 32, rows, "t", 29))
        y += 32 + 29 * len(rows) + 30
    b.append(fk.text(360, 752, "four sentences, one ask, no guilt", "t t-mid t-a1 t-bold"))
    fk.write_svg("ch06/good-ask.svg", 640, 776, "Anatomy of a good ask", "\n".join(b))


if __name__ == "__main__":
    fig_tie_map()
    fig_referral_funnel()
    fig_good_ask()
