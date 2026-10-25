"""Regenerate Chapter 3's figures: python3 book/figures/_src/ch03_figures.py"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
import figkit as fk  # noqa: E402


def mug(x, y, s=1.0):
    return (
        f'<g transform="translate({x} {y}) scale({s})"><path d="M0 0 L2 22 L20 22 L22 0 Z" class="f-a3 k-thin"/>'
        '<path d="M22 5 C31 5 31 16 21 16" class="k-thin"/></g>'
    )


# ---------------------------------------------------------- Figure 3.1


def fig_funnel():
    pen = fk.Pen(seed=31)
    b = [fk.text(24, 40, "Inbound applicants (one vendor’s data, 2024)", "t t-sans")]
    # a funnel of four bands, not to scale
    stages = [
        ("1,000 apply", "", 560),
        ("about 60 get a first screen", "6%", 430),
        ("about 12 reach the final round", "20% of those", 300),
        ("about 4 get an offer", "35% of those", 180),
    ]
    y = 64
    cx = 320
    for i, (label, rate, w) in enumerate(stages):
        nxt = stages[i + 1][2] if i + 1 < len(stages) else w - 70
        b.append(
            f'<path d="M{cx - w / 2} {y} L{cx + w / 2} {y} L{cx + nxt / 2} {y + 56} L{cx - nxt / 2} {y + 56} Z" class="f-a1"/>'
        )
        b.append(pen.line(cx - w / 2, y, cx + w / 2, y, "k-thin"))
        b.append(fk.text(cx, y + 36, label, "t t-mid"))
        if rate:
            b.append(fk.text(cx + w / 2 + 14, y + 10, rate, "t t-sm t-a1"))
        y += 60
    b += [
        f'<path d="M{cx - 55} {y - 4} L{cx + 55} {y - 4}" class="k-thin"/>',
        fk.text(cx, y + 26, "0.4% hired. Not to scale.", "t t-sm t-mid t-mute"),
        pen.line(24, y + 52, 616, y + 52, "k-thin k-dash k-mute"),
    ]
    # bottom panel: referred candidates' share of each stage, to scale
    y0 = y + 92
    b.append(fk.text(24, y0, "Referred candidates’ share at each stage (one US firm)", "t t-sans"))
    bars = [("applicants", 6.1), ("interviewed", 21.4), ("offered", 27.3), ("hired", 29.1)]
    x0, scale = 190, 12.0  # 1 percentage point = 12 units, so 30% = 360
    for i, (label, v) in enumerate(bars):
        by = y0 + 30 + i * 52
        b.append(f'<rect x="{x0}" y="{by}" width="{30 * scale:.0f}" height="34" rx="4" class="f-soft"/>')
        b.append(f'<rect x="{x0}" y="{by}" width="{v * scale:.1f}" height="34" rx="4" class="f-a2s"/>')
        b.append(fk.text(x0 - 14, by + 25, label, "t t-end"))
        b.append(fk.text(x0 + v * scale + 10, by + 25, f"{v}%", "t t-bold"))
    yb = y0 + 30 + 4 * 52
    b += [
        fk.text(24, yb + 26, "Bar background = 30%. Sources: Gem 2025 benchmarks (top);", "t t-sm t-mute"),
        fk.text(24, yb + 50, "Brown, Setren & Topa 2016 (bottom).", "t t-sm t-mute"),
    ]
    fk.write_svg("ch03/funnel.svg", 640, int(yb + 70), "The hiring funnel, inbound and referred", "\n".join(b))


# ---------------------------------------------------------- Figure 3.2


def generic(cx, cy, cls="f-mute"):
    """A plain, faceless person icon for roles that are not cast members."""
    return (
        f'<circle cx="{cx}" cy="{cy - 14}" r="13" class="{cls} k-thin"/>'
        f'<path d="M{cx - 22} {cy + 26} C{cx - 22} {cy + 4} {cx + 22} {cy + 4} {cx + 22} {cy + 26} Z" class="{cls} k-thin"/>'
    )


def fig_room():
    pen = fk.Pen(seed=32)
    rows = [
        ("HIRING MANAGER", "owns the need; decides", "wants: someone who can do the work, soon", fk.avatar("meera", 70, 0, 64, "r-meera")),
        ("RECRUITER", "runs the process", "wants: a filled role and a smooth process", generic(70, 4)),
        ("INTERVIEW PANEL", "gathers evidence", "wants: answers they can score", generic(56, 6) + generic(84, 6, "f-soft")),
        ("BUDGET HOLDER", "approves the offer", "wants: the hire inside the budget", generic(70, 4, "f-a4")),
        ("YOU", "the only outsider", "wants: the right job, a fair offer", fk.avatar("dev", 70, 0, 64, "r-dev")),
    ]
    b = [
        f'<rect x="20" y="20" width="600" height="64" rx="10" class="f-a3"/>',
        pen.rect(20, 20, 600, 64, "k"),
        fk.text(320, 50, "THE REQUISITION", "t t-sans t-mid"),
        fk.text(320, 74, "one approved job, a budget and a deadline", "t t-sm t-mid"),
    ]
    y = 120
    for i, (role, does, wants, icon) in enumerate(rows):
        fill = "f-a1" if i == len(rows) - 1 else "f-paper"
        b.append(f'<rect x="20" y="{y}" width="600" height="92" rx="10" class="{fill}"/>')
        b.append(pen.rect(20, y, 600, 92, "k-thin"))
        b.append(f'<g transform="translate(0 {y + 46})">{icon}</g>')
        b.append(fk.text(136, y + 32, role, "t t-sans"))
        b.append(fk.text(136 + len(role) * 12.5 + 14, y + 33, does, "t t-sm t-mute"))
        b.append(fk.text(136, y + 70, wants, "t"))
        y += 104
    fk.write_svg("ch03/room.svg", 640, y + 6, "Who is in the hiring room, and what each wants", "\n".join(b))


# ---------------------------------------------------------- Figure 3.3


def fig_rejections():
    pen = fk.Pen(seed=33)
    x0, x1, y0, y1 = 100, 610, 470, 110  # applications 0..60, probability 0..100%

    def px(n):
        return x0 + n / 60 * (x1 - x0)

    def py(p):
        return y0 - p * (y0 - y1)

    b = [fk.text(24, 40, "Chance of still having no offer", "t t-sans")]
    for v in (0, 0.25, 0.5, 0.75, 1.0):
        b.append(f'<path d="M{x0} {py(v):.1f} L{x1} {py(v):.1f}" class="k-thin k-mute k-dash"/>')
        b.append(fk.text(x0 - 12, py(v) + 8, f"{int(v * 100)}%", "t t-sm t-end t-mute"))
    for n in (0, 20, 40, 60):
        b.append(fk.text(px(n), y0 + 32, str(n), "t t-sm t-mid t-mute"))
    curves = [(0.01, "k-thick k-a1", "1 in 100"), (0.05, "k-thick k-a3", "1 in 20"), (0.10, "k-thick k-a2", "1 in 10")]
    for p, cls, _ in curves:
        pts = " L".join(f"{px(n):.1f} {py((1 - p) ** n):.1f}" for n in range(0, 61))
        b.append(f'<path d="M{pts}" class="{cls}"/>')
    b += [
        pen.line(x0, y0, x1 + 8, y0, "k"),
        pen.line(x0, y0, x0, y1 - 10, "k"),
        fk.text(px(30), y0 + 66, "applications sent →", "t t-mid"),
        # labels on the curves
        fk.text(px(31), py(0.99 ** 31) - 16, "1 in 100 chance each", "t t-sm t-mid t-a1"),
        fk.text(px(21), py(0.95 ** 18) - 6, "1 in 20", "t t-sm"),
        fk.text(px(14), py(0.34), "1 in 10", "t t-sm t-a2"),
        # Dev's 46
        f'<path d="M{px(46):.1f} {y0} L{px(46):.1f} {y1}" class="k-thin k-dash"/>',
        fk.text(px(46) + 8, y1 + 22, "Dev: 46 noes", "t t-sm"),
        f'<circle cx="{px(46):.1f}" cy="{py(0.99 ** 46):.1f}" r="6" class="f-a1s"/>',
        fk.text(px(46) + 12, py(0.99 ** 46) + 30, "63%", "t t-sm t-a1"),
        f'<circle cx="{px(46):.1f}" cy="{py(0.95 ** 46):.1f}" r="6" class="f-a3s"/>',
        fk.text(px(46) + 12, py(0.95 ** 46) - 8, "9%", "t t-sm"),
        fk.text(24, 572, "Illustrative maths, not data: each application is treated as", "t t-sm t-mute"),
        fk.text(24, 596, "independent, with the same chance of ending in an offer.", "t t-sm t-mute"),
    ]
    fk.write_svg("ch03/rejections.svg", 640, 616, "Illustration: chance of no offer after many applications", "\n".join(b))


if __name__ == "__main__":
    fig_funnel()
    fig_room()
    fig_rejections()
    print("wrote chapter 3 figures")
