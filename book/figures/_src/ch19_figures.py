"""Regenerate Chapter 19's figures: python3 book/figures/_src/ch19_figures.py"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
import figkit as fk  # noqa: E402


def anon(pen, cx, cy, r=26, dashed=False):
    """A plain, unnamed committee member: head and shoulders."""
    cls = "k-thin k-dash" if dashed else "k-thin"
    fill = "f-paper" if dashed else "f-mute"
    return (
        f'<path d="M{cx - r * 1.3:.1f} {cy + r * 1.9:.1f} C{cx - r * 1.2:.1f} {cy + r * 0.9:.1f} {cx + r * 1.2:.1f} {cy + r * 0.9:.1f} {cx + r * 1.3:.1f} {cy + r * 1.9:.1f} Z" class="{fill} {cls}"/>'
        f'<circle cx="{cx}" cy="{cy}" r="{r * 0.62:.1f}" class="{fill} {cls}"/>'
    )


# ---------------------------------------------------------- Figure 19.1


def fig_room():
    pen = fk.Pen(seed=191)
    b = [fk.text(24, 40, "Inside the promotion room", "t t-sans")]
    # walls, with a door gap in the bottom wall
    b += [
        pen.line(24, 64, 616, 64, "k-thick"),
        pen.line(24, 64, 24, 500, "k-thick"),
        pen.line(616, 64, 616, 500, "k-thick"),
        pen.line(24, 500, 330, 500, "k-thick"),
        pen.line(410, 500, 616, 500, "k-thick"),
        '<path d="M330 500 Q340 466 384 452" class="k-thin k-dash"/>',
    ]
    # table and packet
    b += [
        '<ellipse cx="320" cy="270" rx="150" ry="78" class="f-soft"/>',
        '<ellipse cx="320" cy="270" rx="150" ry="78" class="k"/>',
        '<rect x="262" y="236" width="116" height="66" rx="4" class="f-a4"/>',
        pen.rect(262, 236, 116, 66, "k-thin"),
        fk.text(320, 264, "THE PACKET", "t t-sans t-mid"),
        pen.line(280, 280, 360, 280, "k-thin k-mute"),
        pen.line(280, 292, 344, 292, "k-thin k-mute"),
    ]
    # seats
    b.append(fk.avatar("tomas", 196, 168, 64, "tomasroom"))
    b.append(fk.lines(44, 108, ["your manager:", "your advocate"], "t", 26))
    b.append(anon(pen, 444, 162))
    b.append(fk.lines(596, 108, ["a director from", "another squad"], "t t-end", 26))
    b.append(anon(pen, 196, 372))
    b.append(fk.lines(44, 446, ["a senior engineer", "who's never met you"], "t", 26))
    b.append(anon(pen, 444, 372, dashed=True))
    b.append(fk.lines(596, 450, ["saw your work", "first-hand?"], "t t-end t-a4", 26))
    # Dev outside the door
    b.append(fk.person("dev", 370, 632, 0.5))
    b.append(fk.lines(410, 578, ["you:", "not invited"], "t", 26))
    b.append(fk.lines(24, 548, ["the packet: what changed,", "at what scope,", "who says so"], "t t-sm t-mute", 24))
    b.append(fk.text(320, 670, "They know you through the packet, your manager,", "t t-sm t-mid t-mute"))
    b.append(fk.text(320, 694, "and anyone who has seen your work.", "t t-sm t-mid t-mute"))
    fk.write_svg("ch19/room.svg", 640, 712, "Inside the promotion room", "\n".join(b))


# ---------------------------------------------------------- Figure 19.2

ROWS = [
    ("SPECIFIC", ["Cut the test run", "from 6 hours", "to 40 minutes"],
     ["Made carriers testable", "for 3 squads: live in", "2 weeks, not 6"]),
    ("CHECKABLE", ["Ask me how I", "parallelised it"],
     ["The harness, the", "dashboards, and two", "squad leads who use it"]),
    ("COSTLY TO FAKE", ["Only the person who", "did it survives the", "follow-up"],
     ["Work beyond my squad", "that others now", "depend on"]),
]


def fig_trailer():
    pen = fk.Pen(seed=192)
    lx, rx, cw = 24, 332, 284
    b = [
        fk.text(lx, 40, "PART I", "t t-sans t-a1"),
        fk.text(lx, 66, "a résumé line", "t t-a1"),
        fk.text(rx, 40, "PART III", "t t-sans t-a4"),
        fk.text(rx, 66, "a promotion-case line", "t t-a4"),
    ]
    y = 100
    for head, left, right in ROWS:
        b.append(fk.text(320, y + 22, head, "t t-sans t-mid"))
        y += 36
        h = 24 + 28 * 3
        b.append(f'<rect x="{lx}" y="{y}" width="{cw}" height="{h}" rx="10" class="f-a1"/>')
        b.append(pen.rect(lx, y, cw, h, "k"))
        b.append(fk.lines(lx + 16, y + 34, left, "t", 28))
        b.append(f'<rect x="{rx}" y="{y}" width="{cw}" height="{h}" rx="10" class="f-a4"/>')
        b.append(pen.rect(rx, y, cw, h, "k"))
        b.append(fk.lines(rx + 16, y + 34, right, "t", 28))
        y += h + 16
    b.append(f'<rect x="120" y="{y + 8}" width="400" height="44" rx="22" class="f-a3"/>')
    b.append(pen.rect(120, y + 8, 400, 44, "k-thin"))
    b.append(fk.text(320, y + 38, "Same rules. Different audience.", "t t-bold t-mid"))
    fk.write_svg("ch19/trailer.svg", 640, y + 70, "A promotion case as a trailer", "\n".join(b))


# ---------------------------------------------------------- Figure 19.3

SEEN = [
    "warned me early, every time since Northwind",
    "found the race condition on a Saturday",
    "stopped a bad release, with evidence",
    "harness now used by three squads",
    "fixed the credit record, calmly",
]


def fig_ledger_spent():
    pen = fk.Pen(seed=193)
    b = [fk.text(24, 40, "What Tomás has seen, two years", "t t-sans")]
    top = 58
    h = 30 + 40 * len(SEEN)
    b.append(f'<rect x="24" y="{top}" width="592" height="{h}" rx="8" class="f-paper"/>')
    b.append(pen.rect(24, top, 592, h, "k"))
    for i, s in enumerate(SEEN):
        y = top + 40 + i * 40
        b.append(f'<rect x="44" y="{y - 18}" width="22" height="22" rx="4" class="f-a2s"/>')
        b.append(fk.text(55, y - 1, "+", "t t-bold t-mid t-paper"))
        b.append(fk.text(80, y, s, "t"))
    y = top + h + 12
    b.append(pen.arrow(320, y, 320, y + 62, "k-thick k-a4"))
    b.append(fk.text(340, y + 40, "spent in the room", "t t-a4"))
    # Tomás at the table, speaking
    y2 = y + 84
    b.append(fk.avatar("tomas", 92, y2 + 40, 84, "tomasledger"))
    b.append(f'<path d="M150 {y2 + 30} L176 {y2 + 22} L176 {y2 + 4} Q176 {y2 - 6} 186 {y2 - 6} L606 {y2 - 6} Q616 {y2 - 6} 616 {y2 + 4} L616 {y2 + 52} Q616 {y2 + 62} 606 {y2 + 62} L186 {y2 + 62} Q176 {y2 + 62} 176 {y2 + 52} L176 {y2 + 40} Z" class="f-a4 k-thin"/>')
    b.append(fk.text(396, y2 + 36, "“I’ll stake my judgement on this.”", "t t-mid"))
    # his own ledger
    y3 = y2 + 110
    b.append(fk.text(24, y3, "Tomás’s own ledger with the committee", "t t-sans"))
    rows = [
        ("f-a2s", "+", "if he’s right: his judgement gains credit", ""),
        ("f-a1s", "−", "if he’s wrong: his withdrawal, not hers", "t-a1"),
    ]
    for i, (fill, sign, text, tcls) in enumerate(rows):
        yy = y3 + 40 + i * 40
        b.append(f'<rect x="44" y="{yy - 18}" width="22" height="22" rx="4" class="{fill}"/>')
        b.append(fk.text(55, yy - 1, sign, "t t-bold t-mid t-paper"))
        b.append(fk.text(80, yy, text, f"t {tcls}".strip()))
    yf = y3 + 130
    b.append(fk.text(320, yf, "Illustrative, not a formula.", "t t-sm t-mid t-mute"))
    fk.write_svg("ch19/ledger-spent.svg", 640, yf + 20, "The trust ledger, spent", "\n".join(b))


if __name__ == "__main__":
    fig_room()
    fig_trailer()
    fig_ledger_spent()
    print("wrote chapter 19 figures")
