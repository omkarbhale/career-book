"""Regenerate Chapter 11's figures: python3 book/figures/_src/ch11_figures.py"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
import figkit as fk  # noqa: E402


def bubble(x, y, w, h, tail_x, tail_y, cls="f-paper k-thin"):
    """A rounded thought bubble with two small circles trailing to (tail_x, tail_y)."""
    mx, my = (x + w / 2 + tail_x) / 2, (y + h + tail_y) / 2
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="22" class="{cls}"/>'
        f'<circle cx="{mx:.1f}" cy="{my:.1f}" r="6" class="{cls}"/>'
        f'<circle cx="{tail_x:.1f}" cy="{tail_y:.1f}" r="3.5" class="{cls}"/>'
    )


# ---------------------------------------------------------- Figure 11.1


def fig_newcomer():
    pen = fk.Pen(seed=111)
    b = [
        pen.rect(24, 24, 280, 128, "f-soft k-thin"),
        fk.text(40, 56, "What you do", "t t-sans"),
        fk.lines(40, 90, ["ask, and ask again", "seek feedback early", "get to know people"], "t t-sm", 24),
        pen.rect(336, 24, 280, 128, "f-soft k-thin"),
        fk.text(352, 56, "What they do", "t t-sans"),
        fk.lines(352, 90, ["onboarding that explains", "clear goals, a buddy", "people who include you"], "t t-sm", 24),
    ]
    circles = [
        (112, "Clarity", ["I know what", "good looks", "like here"], "a3"),
        (320, "Competence", ["I can", "do this"], "a1"),
        (528, "Connection", ["they want", "me here"], "a2"),
    ]
    for x, name, rows, colour in circles:
        b.append(pen.arrow(164 if x < 320 else (476 if x > 320 else 320), 160, x, 214, "k-thin k-mute", head=10))
        b.append(f'<circle cx="{x}" cy="{300}" r="84" class="f-{colour} k"/>')
        b.append(fk.text(x, 262, name, "t t-sans t-mid"))
        b.append(fk.lines(x, 300, rows, "t t-mid", 26))
        b.append(pen.arrow(x, 392, 320 + (x - 320) * 0.3, 446, "k k-mute", head=12))
    b.append(pen.arrow(320, 160, 320, 214, "k-thin k-mute", head=10))
    b += [
        pen.rect(70, 456, 500, 96, "f-paper k"),
        fk.text(320, 492, "A good start", "t t-sans t-mid"),
        fk.lines(320, 526, ["better performance, more satisfied, more likely to stay"], "t t-sm t-mid", 24),
    ]
    fk.write_svg("ch11/newcomer.svg", 640, 576, "What makes a newcomer succeed", "\n".join(b))


# ---------------------------------------------------------- Figure 11.2


def fig_liking():
    pen = fk.Pen(seed=112)
    b = [
        '<rect x="200" y="214" width="240" height="18" rx="4" class="f-soft k-thin"/>',
        fk.person("dev", 196, 300, 0.62),
        fk.person("kai", 444, 300, 0.62),
        '<rect x="300" y="196" width="40" height="18" rx="3" class="f-paper k-thin"/>',
        bubble(14, 18, 250, 98, 170, 160, "f-a1 k-thin"),
        fk.lines(139, 56, ["I talked too much.", "Kai thinks I'm dull."], "t t-mid", 28),
        bubble(376, 18, 250, 98, 470, 160, "f-a2 k-thin"),
        fk.lines(501, 56, ["She's funny. Lunch", "again on Thursday?"], "t t-mid", 28),
        fk.text(320, 352, "After the same conversation:", "t t-mid"),
        fk.text(40, 404, "how much Dev thinks", "t t-sm"),
        fk.text(40, 428, "Kai liked her", "t t-sm"),
        pen.rect(250, 392, 150, 34, "f-a1s k-thin"),
        fk.text(40, 480, "how much Kai", "t t-sm"),
        fk.text(40, 504, "actually did", "t t-sm"),
        pen.rect(250, 468, 340, 34, "f-a2s k-thin"),
        pen.arrow(410, 409, 584, 409, "k-thin k-dash", head=10),
        fk.text(498, 396, "the gap", "t t-sm t-mid"),
        fk.text(320, 552, "Illustrative bar lengths; the gap is real, its size varies", "t t-sm t-mid t-mute"),
    ]
    fk.write_svg("ch11/liking-gap.svg", 640, 572, "The liking gap", "\n".join(b))


# ---------------------------------------------------------- Figure 11.3


def fig_month():
    pen = fk.Pen(seed=113)
    weeks = [
        ("Week 1", "Learn the map", ["who decides what, how work", "flows, where questions go"], "a3"),
        ("Week 2", "Ask, shadow, fix something small", ["pair with someone; ship", "one tiny, real change"], "a1"),
        ("Week 3", "Own one real task", ["end to end, with a check-in", "halfway, not at the end"], "a1"),
        ("Week 4", "Check the target", ["ask: what does good look", "like at three months?"], "a3"),
    ]
    X = 76
    y = 100
    b = [fk.text(24, 40, "A first month, as a plan", "t t-sans")]
    line_top = y
    for i, (wk, head, rows, colour) in enumerate(weeks):
        b.append(f'<circle cx="{X}" cy="{y}" r="22" class="f-{colour} k"/>')
        b.append(fk.text(X, y + 7, str(i + 1), "t t-bold t-mid"))
        b.append(fk.text(X + 40, y - 6, wk, "t t-sans t-mute"))
        b.append(fk.text(X + 40, y + 24, head, "t t-bold"))
        b.append(fk.lines(X + 40, y + 54, rows, "t t-sm", 24))
        y += 140
    b.insert(1, f'<path d="M{X} {line_top} L{X} {y - 140}" class="k-thick k-mute"/>')
    b.append(pen.rect(X - 40, y - 40, 556, 76, "f-a2 k-thin"))
    b.append(fk.lines(X - 22, y - 8, ["every week: meet two people, and ask more", "questions than feels comfortable"], "t t-sm", 26))
    b.append(fk.text(320, y + 76, "Practitioner advice, not a finding: adapt it to your job", "t t-sm t-mid t-mute"))
    fk.write_svg("ch11/first-month.svg", 640, int(y + 100), "A first-month map", "\n".join(b))


if __name__ == "__main__":
    fig_newcomer()
    fig_liking()
    fig_month()
    print("wrote chapter 11 figures")
