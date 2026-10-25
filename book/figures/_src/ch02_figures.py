"""Regenerate Chapter 2's figures: python3 book/figures/_src/ch02_figures.py"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
import figkit as fk  # noqa: E402


def tag(pen, x, y, w, label, fill):
    """A rounded label card centred on x, with its top edge at y."""
    return (
        f'<rect x="{x - w / 2:.1f}" y="{y}" width="{w}" height="38" rx="9" class="{fill}"/>'
        + pen.rect(x - w / 2, y, w, 38, "k-thin")
        + fk.text(x, y + 27, label, "t t-mid")
    )


# ---------------------------------------------------------- Figure 2.1


def fig_push_pull():
    pen = fk.Pen(seed=21)
    # The beam tilts down to the right: the pull side is heavier in Dev's case.
    lx, ly, rx, ry = 150, 168, 490, 196
    b = [
        fk.text(320, 40, "Why leave?", "t t-sans t-mid"),
        # fulcrum and stand
        '<path d="M320 182 L292 236 L348 236 Z" class="f-soft k"/>',
        pen.line(270, 238, 370, 238, "k"),
        pen.line(lx - 20, ly - 2, rx + 20, ry + 2, "k-thick"),
        f'<circle cx="320" cy="182" r="6" class="f-ink"/>',
        # strings
        pen.line(lx, ly, lx - 92, ly + 92, "k-thin"),
        pen.line(lx, ly, lx + 92, ly + 92, "k-thin"),
        pen.line(rx, ry, rx - 92, ry + 92, "k-thin"),
        pen.line(rx, ry, rx + 92, ry + 92, "k-thin"),
        # pans
        f'<path d="M{lx - 104} {ly + 92} Q{lx} {ly + 128} {lx + 104} {ly + 92} Z" class="f-a1 k"/>',
        f'<path d="M{rx - 104} {ry + 92} Q{rx} {ry + 128} {rx + 104} {ry + 92} Z" class="f-a3 k"/>',
        fk.text(lx, 92, "PUSH", "t t-sans t-mid t-a1"),
        fk.text(lx, 118, "what’s wrong here", "t t-mid t-a1"),
        fk.text(rx, 92, "PULL", "t t-sans t-mid"),
        fk.text(rx, 118, "what’s right there", "t t-mid"),
    ]
    push = ["no route into dev", "same tests, year 3", "pay a bit low"]
    pull = ["build, not just break", "seniors to learn from", "fair pay"]
    for i, (p, q) in enumerate(zip(push, pull)):
        b.append(tag(pen, lx, 300 + i * 50, 218, p, "f-paper"))
        b.append(tag(pen, rx, 312 + i * 50, 236, q, "f-paper"))
    b += [
        pen.line(24, 470, 616, 470, "k-thin k-dash k-mute"),
        fk.lines(lx, 506, ["first question:", "could this be fixed here?"], "t t-mid t-a1", 28),
        fk.lines(rx, 506, ["first question:", "is this on offer here?"], "t t-mid", 28),
        fk.text(320, 584, "Dev’s reasons, sorted. Same feeling, two different questions.", "t t-sm t-mid t-mute"),
    ]
    fk.write_svg("ch02/push-pull.svg", 640, 604, "Push and pull reasons on a balance", "\n".join(b))


# ---------------------------------------------------------- Figure 2.2

# Calendar-year averages of the Atlanta Fed's 12-month moving averages of median wage growth,
# computed from the Wage Growth Tracker data file (sheet "Job Switcher") on 2026-10-25.
# (year, job switchers, job stayers); 2025 has 11 months, 2026 is January to September.
WGT = [
    (1997, 5.30, 4.08), (1998, 5.82, 4.47), (1999, 6.00, 4.69), (2000, 5.91, 4.62), (2001, 5.98, 4.81),
    (2002, 5.06, 4.42), (2003, 3.78, 3.68), (2004, 3.51, 3.43), (2005, 3.88, 3.59), (2006, 4.26, 3.76),
    (2007, 4.61, 3.81), (2008, 4.38, 3.93), (2009, 3.34, 3.47), (2010, 1.79, 2.07), (2011, 2.22, 1.73),
    (2012, 2.33, 1.89), (2013, 2.65, 1.93), (2014, 2.70, 2.14), (2015, 3.23, 2.77), (2016, 3.88, 2.98),
    (2017, 4.12, 3.06), (2018, 3.88, 2.87), (2019, 4.06, 3.33), (2020, 4.33, 3.22), (2021, 4.17, 3.23),
    (2022, 6.42, 4.79), (2023, 7.08, 5.47), (2024, 5.42, 4.86), (2025, 4.44, 4.34), (2026, 4.38, 3.68),
]


def fig_switchers():
    x0, x1, y0, y1 = 96, 620, 470, 110  # plot box: years 1997..2026, growth 0..8%

    def px(year):
        return x0 + (year - 1997) / (2026 - 1997) * (x1 - x0)

    def py(v):
        return y0 - v / 8 * (y0 - y1)

    pen = fk.Pen(seed=22)
    b = []
    for v in (0, 2, 4, 6, 8):
        b.append(f'<path d="M{x0} {py(v):.1f} L{x1} {py(v):.1f}" class="k-thin k-mute k-dash"/>')
        b.append(fk.text(x0 - 12, py(v) + 8, f"{v}%", "t t-sm t-end t-mute"))
    for year in (2000, 2010, 2020):
        b.append(fk.text(px(year), y0 + 34, str(year), "t t-sm t-mid t-mute"))
    # the stretch where switchers trailed stayers (annual averages: 2009 and 2010)
    b.append(f'<rect x="{px(2008.5):.1f}" y="{y1}" width="{px(2010.5) - px(2008.5):.1f}" height="{y0 - y1}" class="f-soft"/>')

    def series(idx, cls):
        pts = " L".join(f"{px(r[0]):.1f} {py(r[idx]):.1f}" for r in WGT)
        return f'<path d="M{pts}" class="{cls}"/>'

    b += [
        series(2, "k-thick k-a2"),
        series(1, "k-thick k-a1"),
        pen.line(x0, y0, x1 + 6, y0, "k"),
        pen.line(x0, y0, x0, y1 - 8, "k"),
        fk.text(24, 40, "Median yearly pay growth, US workers", "t t-sans"),
        # legend
        f'<path d="M{x0 + 10} 78 L{x0 + 50} 78" class="k-thick k-a1"/>',
        fk.text(x0 + 60, 86, "changed jobs", "t t-a1"),
        f'<path d="M{x0 + 230} 78 L{x0 + 270} 78" class="k-thick k-a2"/>',
        fk.text(x0 + 280, 86, "stayed put", "t t-a2"),
        # annotations
        fk.lines(px(2009.5), py(0.9), ["2009–10:", "switchers behind"], "t t-sm t-mid", 22),
        fk.lines(px(2022) - 14, py(7.35), ["2023:", "7.1% vs 5.5%"], "t t-sm t-end", 22),
        pen.arrow(px(2022) - 8, py(7.2), px(2023) - 6, py(7.1), "k-thin", head=8),
        fk.lines(640, py(2.6), ["2025:", "4.4% vs 4.3%"], "t t-sm t-end", 22),
        pen.arrow(px(2025) - 4, py(3.25), px(2025), py(4.0), "k-thin", head=8),
        fk.text(24, 548, "Annual averages of 12-month moving averages, 1997 to Sept 2026.", "t t-sm t-mute"),
        fk.text(24, 574, "Source: Atlanta Fed Wage Growth Tracker; our calculation.", "t t-sm t-mute"),
    ]
    fk.write_svg("ch02/switchers.svg", 660, 594, "Wage growth of job switchers and job stayers, 1997 to 2026", "\n".join(b))


# ---------------------------------------------------------- Figure 2.3


def node(pen, cx, y, w, rows, fill, cls="t t-mid", lh=28):
    h = 22 + lh * len(rows)
    return (
        f'<rect x="{cx - w / 2:.1f}" y="{y}" width="{w}" height="{h}" rx="12" class="{fill}"/>'
        + pen.rect(cx - w / 2, y, w, h, "k")
        + fk.lines(cx, y + 34, rows, cls, lh)
    ), y + h


def fig_decision():
    pen = fk.Pen(seed=23)
    b = []
    s, sb = node(pen, 320, 24, 420, ["Something is pushing or pulling you"], "f-paper")
    b.append(s)
    q, qb = node(pen, 320, sb + 40, 340, ["Is it about here, or there?"], "f-soft")
    b += [pen.arrow(320, sb + 2, 320, sb + 36, "k"), q]
    L, R = 170, 470
    y2 = qb + 64
    b += [
        pen.arrow(250, qb, L, y2 - 4, "k", bend=-8),
        pen.arrow(390, qb, R, y2 - 4, "k", bend=8),
        fk.text(178, qb + 34, "push", "t t-a1 t-end"),
        fk.text(462, qb + 34, "pull", "t"),
    ]
    a, ab = node(pen, L, y2, 270, ["Could it be fixed", "here? Ask, with", "a date attached."], "f-a1")
    c, cb = node(pen, R, y2, 270, ["Is what you want", "on offer here?", "Look inside first."], "f-a3")
    b += [a, c]
    y3 = max(ab, cb) + 70
    stay, stb = node(pen, 106, y3, 176, ["STAY", "and check", "again later"], "f-a2", "t t-mid", 26)
    go, gob = node(pen, 320, y3, 176, ["GO", "search while", "still employed"], "f-a1", "t t-mid", 26)
    grow, grb = node(pen, 534, y3, 176, ["GROW", "move or", "change inside"], "f-a4", "t t-mid", 26)
    b += [
        pen.arrow(120, ab, 106, y3 - 4, "k"), fk.text(100, ab + 38, "yes", "t t-sm t-end"),
        pen.arrow(220, ab, 300, y3 - 4, "k", bend=6),
        fk.lines(278, ab + 24, ["no, or \u201cmaybe", "next year\u201d"], "t t-sm t-a1", 22),
        pen.arrow(420, cb, 340, y3 - 4, "k", bend=-6), fk.text(392, cb + 52, "no", "t t-sm t-end"),
        pen.arrow(520, cb, 540, y3 - 4, "k"), fk.text(552, cb + 38, "yes", "t t-sm"),
        stay, go, grow,
    ]
    y4 = max(stb, grb, gob) + 40
    b += [
        f'<rect x="40" y="{y4}" width="560" height="78" rx="12" class="f-paper"/>',
        pen.rect(40, y4, 560, 78, "k k-dash k-mute"),
        fk.lines(320, y4 + 32, ["Laid off? The decision was made for you.", "Skip to GO, and start with the first two weeks."], "t t-mid", 28),
    ]
    fk.write_svg("ch02/decision.svg", 640, int(y4 + 100), "Stay, go or grow: a decision path", "\n".join(b))


if __name__ == "__main__":
    fig_push_pull()
    fig_switchers()
    fig_decision()
    print("wrote chapter 2 figures")
