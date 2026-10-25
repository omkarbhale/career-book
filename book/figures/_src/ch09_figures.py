"""Regenerate Chapter 9's figures: python3 book/figures/_src/ch09_figures.py"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
import figkit as fk  # noqa: E402

# ---------------------------------------------------------- Figure 9.1


def fig_offer():
    pen = fk.Pen(seed=91)
    body = [(200, 176), (440, 176), (540, 262), (566, 400), (508, 540), (320, 590), (140, 540), (84, 400), (108, 262)]
    d = f"M{body[0][0]} {body[0][1]}" + "".join(
        f" Q{(ax + bx) / 2 + pen._j() * 4:.1f} {(ay + by) / 2 + pen._j() * 4:.1f} {bx} {by}"
        for (ax, ay), (bx, by) in zip(body, body[1:] + body[:1])
    )
    waves = "M20 176" + "".join(f" q15 -9 30 0" for _ in range(20))
    b = [
        '<rect x="20" y="176" width="600" height="440" class="f-a2"/>',
        f'<path d="{d} Z" class="f-paper k"/>',
        '<path d="M232 176 L262 84 L300 104 L336 60 L376 98 L412 176 Z" class="f-paper k"/>',
        f'<path d="{waves}" class="k k-a2"/>',
        fk.text(322, 150, "base salary", "t t-mid t-bold"),
        fk.text(560, 120, "above the", "t t-sm t-mid t-mute"),
        fk.text(560, 144, "waterline", "t t-sm t-mid t-mute"),
        fk.text(322, 228, "bonus (expected, not maximum)", "t t-mid"),
        fk.lines(322, 276, ["equity (how many, vesting,", "cliff, risk)"], "t t-mid", 28),
        fk.lines(322, 352, ["benefits (health, pension or", "provident fund, leave)"], "t t-mid", 28),
        pen.line(112, 412, 548, 412, "k-thin k-dash k-mute"),
        fk.text(322, 448, "not on paper", "t t-sans t-mid"),
        fk.lines(322, 482, ["the manager, the work,", "what you'll learn, flexibility,", "notice period, start date"], "t t-mid", 30),
        fk.lines(320, 650, ["India: CTC adds several of these together;", "ask what lands in your account"], "t t-mid t-a1 t-bold", 30),
    ]
    fk.write_svg("ch09/offer.svg", 640, 700, "What's in an offer, drawn as an iceberg", "\n".join(b))


# ---------------------------------------------------------- Figure 9.2


def fig_anchor():
    pen = fk.Pen(seed=92)
    y = 220
    b = [
        '<rect x="190" y="200" width="300" height="40" rx="4" class="f-a3"/>',
        fk.text(340, 190, "the posted range", "t t-mid"),
        pen.arrow(40, y, 612, y, "k"),
        fk.text(40, y + 40, "low", "t t-sm t-mute"),
        fk.text(612, y + 40, "high", "t t-sm t-mute t-end"),
        # the flag: the first number
        pen.line(566, y, 566, 70, "k"),
        '<path d="M566 72 L620 88 L566 106 Z" class="f-a1s k-thin"/>',
        fk.text(566, 56, "first number", "t t-mid t-a1 t-bold"),
        # the settlement marker, pulled right
        '<path d="M446 212 L460 186 L474 212 Z" class="f-ink"/>',
        fk.lines(460, 272, ["where it tends", "to land"], "t t-mid t-bold", 26),
        f'<path d="M466 190 Q520 120 562 112" class="k k-a1"/>',
        pen.arrow(500, 150, 540, 126, "k-thin k-a1", head=9),
        # the counterweight
        f'<path d="{pen.rect_d(60, 300, 96, 56)}" class="f-soft k"/>',
        fk.text(108, 336, "target", "t t-mid t-bold"),
        f'<path d="M452 204 Q300 270 156 316" class="k k-dash"/>',
        fk.lines(176, 330, ["your target and your alternatives,", "written down first"], "t", 28),
        fk.lines(320, 420, [
            "schematic, after lab experiments: first offers anchor the outcome",
            "unless the other side focuses on its own target and alternatives",
        ], "t t-sm t-mid t-mute", 26),
    ]
    fk.write_svg("ch09/anchor.svg", 640, 460, "How a first number anchors a negotiation", "\n".join(b))


# ---------------------------------------------------------- Figure 9.3


def calendar(x, y):
    rows = "".join(
        f'<rect x="{x + 6 + c * 9}" y="{y + 16 + r * 8}" width="5" height="4" class="f-mute"/>'
        for r in range(3) for c in range(4)
    )
    return (
        f'<rect x="{x}" y="{y}" width="44" height="44" rx="5" class="f-paper k-thin"/>'
        f'<rect x="{x}" y="{y}" width="44" height="11" rx="4" class="f-a1s"/>{rows}'
    )


def fig_notice():
    pen = fk.Pen(seed=93)
    cards = [
        ("United States", ["at will: either side can end it at almost", "any time, for almost any reason", "notice by custom or contract, not by law"]),
        ("United Kingdom", ["at least 1 week after a month in the job", "your contract may say more", "garden leave is allowed"]),
        ("Germany", ["4 weeks, to the 15th or the end of a month", "2 weeks during probation (up to 6 months)"]),
        ("India", ["set by your contract: often 1–2 months,", "3–6 for senior roles", "final dues within 2 days of leaving,", "under the Labour Codes"]),
    ]
    b = [fk.text(30, 34, "If you resign: notice and final pay", "t t-sans")]
    y = 54
    for title, rows in cards:
        h = 62 + 30 * len(rows)
        b.append(f'<path d="{pen.rect_d(30, y, 580, h)}" class="f-paper k"/>')
        b.append(calendar(50, y + 18))
        b.append(fk.text(112, y + 40, title, "t t-sans"))
        b.append(fk.lines(112, y + 76, rows, "t", 30))
        y += h + 18
    b.append(fk.lines(320, y + 24, ["check your own contract: it usually sets the", "actual period, within the law"], "t t-mid t-a1 t-bold", 30))
    fk.write_svg("ch09/notice.svg", 640, int(y + 76), "Notice and final pay rules by region", "\n".join(b))


if __name__ == "__main__":
    fig_offer()
    fig_anchor()
    fig_notice()
