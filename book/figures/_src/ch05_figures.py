"""Regenerate Chapter 5's figures: python3 book/figures/_src/ch05_figures.py"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
import figkit as fk  # noqa: E402


def bar(x, y, w, cls="k-thin k-mute"):
    return f'<path d="M{x} {y} L{x + w} {y}" class="{cls}"/>'


def page(x, y, s=1.0, hl=()):
    """A one-page résumé drawn at (x, y), 260 wide and 400 tall at scale 1.

    ``hl`` names the parts to highlight in gold: 'head', 'titles', 'bullets', 'skills', 'edu'.
    """
    g = [f'<rect x="0" y="0" width="260" height="400" rx="6" class="f-paper"/>']

    def mark(part, rx, ry, rw, rh):
        if part in hl:
            g.append(f'<rect x="{rx}" y="{ry}" width="{rw}" height="{rh}" rx="4" class="f-a3"/>')

    mark("head", 14, 12, 232, 58)
    mark("titles", 14, 84, 232, 22)
    mark("titles", 14, 210, 232, 22)
    mark("bullets", 14, 110, 232, 88)
    mark("bullets", 14, 236, 232, 50)
    mark("skills", 14, 300, 232, 34)
    mark("edu", 14, 346, 232, 40)
    g += [
        '<path d="M24 32 L150 32" class="k-thick"/>',
        bar(24, 50, 200, "k"), bar(24, 62, 160),
        '<path d="M24 95 L130 95" class="k"/>', '<path d="M190 95 L236 95" class="k-thin"/>',
    ]
    for i in range(4):
        g.append(f'<circle cx="28" cy="{122 + i * 20}" r="2.5" class="f-ink"/>')
        g.append(bar(38, 122 + i * 20, 190 - (i % 2) * 30))
    g += ['<path d="M24 221 L120 221" class="k"/>', '<path d="M190 221 L236 221" class="k-thin"/>']
    for i in range(2):
        g.append(f'<circle cx="28" cy="{248 + i * 20}" r="2.5" class="f-ink"/>')
        g.append(bar(38, 248 + i * 20, 180 - i * 40))
    g += [
        '<path d="M24 310 L80 310" class="k"/>', bar(24, 324, 210),
        '<path d="M24 356 L90 356" class="k"/>', bar(24, 372, 170),
    ]
    pen = fk.Pen(seed=int(x + y))
    g.append(pen.rect(0, 0, 260, 400, "k"))
    return f'<g transform="translate({x} {y}) scale({s})">' + "".join(g) + "</g>"


# ---------------------------------------------------------- Figure 5.1


def fig_anatomy():
    pen = fk.Pen(seed=51)
    px, py, s = 30, 40, 1.0
    b = [
        page(px, py, s, hl=("head",)),
        pen.line(px - 12, py + 4, px - 12, py + 206, "k-thick k-a1"),
    ]
    notes = [
        (30, ["headline: your one-", "line answer (Ch 4)"]),
        (94, ["titles, employers,", "dates: read first"]),
        (164, ["bullets: what changed,", "by how much"]),
        (302, ["skills: the ad\u2019s words,", "if they are true"]),
        (364, ["education: short,", "unless it\u2019s your best"]),
    ]
    ax = px + 260 * s
    for ty, rows in notes:
        y = py + ty * s
        b.append(pen.arrow(ax + 90, y - 6, ax + 8, y, "k-thin", head=9))
        b.append(fk.lines(ax + 98, y, rows, "t", 26))
    b += [
        fk.lines(px - 12, py + 400 * s + 44, ["where the first skim lands:", "titles, names and dates up top"], "t t-a1", 28),
    ]
    fk.write_svg("ch05/anatomy.svg", 640, int(py + 400 * s + 110), "Anatomy of a résumé as a trailer", "\n".join(b))


# ---------------------------------------------------------- Figure 5.2


def fig_two_reads():
    pen = fk.Pen(seed=52)
    s = 0.62
    b = []
    rows = [
        ("THE FIRST GLANCE", "seconds, for everyone", "Is this plausibly a fit?",
         ["looks at: titles, employers,", "dates, education"], ("titles", "edu", "head")),
        ("THE FULL READ", "minutes, if you pass", "Is it true, and is it them?",
         ["looks at: what changed, by", "how much; what to ask about"], ("bullets",)),
    ]
    y = 24
    for i, (head, when, q, look, hl) in enumerate(rows):
        b.append(page(30, y, s, hl=hl))
        tx = 30 + 260 * s + 34
        b.append(fk.text(tx, y + 34, head, "t t-sans t-a1" if i == 0 else "t t-sans"))
        b.append(fk.text(tx, y + 64, when, "t t-sm t-mute"))
        b.append(fk.text(tx, y + 112, q, "t t-bold"))
        b.append(fk.lines(tx, y + 156, look, "t", 28))
        if i == 1:
            for qx, qy in ((236, 70), (236, 150)):
                b.append(fk.text(30 + qx * s + 20, y + qy * s + 16, "?", "t t-lg t-bold t-a1"))
        y += 400 * s + 40
        if i == 0:
            b.append(pen.arrow(30 + 130 * s, y - 36, 30 + 130 * s, y - 4, "k"))
            b.append(fk.text(30 + 130 * s + 16, y - 14, "only if you pass", "t t-sm"))
    fk.write_svg("ch05/two-reads.svg", 640, int(y + 4), "The first glance and the full read", "\n".join(b))


# ---------------------------------------------------------- Figure 5.3


def fig_regions():
    pen = fk.Pen(seed=53)
    regions = [
        ("US", "f-a1", ["no photo: the EEOC tells employers to", "avoid asking for one before an offer;",
                        "age, religion and origin are irrelevant"]),
        ("UK", "f-a2", ["“not your age, date of birth, whether", "you’re married or your nationality”",
                        "(National Careers Service)"]),
        ("EU", "f-a4", ["Europass, the EU’s CV tool, suggests", "adding a professional photo;",
                        "national habits vary (not verified)"]),
        ("INDIA", "f-a3", ["no official guidance we could verify;", "ask people in your sector what",
                           "employers there expect"]),
    ]
    b = [fk.text(24, 40, "What goes on the page, by region", "t t-sans")]
    y = 64
    for name, fill, rows in regions:
        h = 30 + 30 * len(rows)
        b.append(f'<rect x="24" y="{y}" width="592" height="{h}" rx="12" class="f-paper"/>')
        b.append(f'<rect x="24" y="{y}" width="112" height="{h}" rx="12" class="{fill}"/>')
        b.append(pen.rect(24, y, 592, h, "k"))
        b.append(fk.text(80, y + h / 2 + 7, name, "t t-sans t-mid"))
        b.append(fk.lines(156, y + 38, rows, "t", 30))
        y += h + 16
    b.append(fk.text(24, y + 22, "Only what we verified; everywhere else, check local norms.", "t t-sm t-mute"))
    fk.write_svg("ch05/regions.svg", 640, y + 42, "CV conventions by region", "\n".join(b))


if __name__ == "__main__":
    fig_anatomy()
    fig_two_reads()
    fig_regions()
    print("wrote chapter 5 figures")
