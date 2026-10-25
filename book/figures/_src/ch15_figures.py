"""Regenerate Chapter 15's figures: python3 book/figures/_src/ch15_figures.py"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
import figkit as fk  # noqa: E402


def tick(cx, cy, cls="k-thick k-a2"):
    return f'<path d="M{cx - 13} {cy} L{cx - 4} {cy + 10} L{cx + 14} {cy - 12}" class="{cls}"/>'


def cross(cx, cy, cls="k-thick k-a1"):
    return f'<path d="M{cx - 11} {cy - 11} L{cx + 11} {cy + 11} M{cx + 11} {cy - 11} L{cx - 11} {cy + 11}" class="{cls}"/>'


def wave(cx, cy, cls="k-thick k-a3"):
    return f'<path d="M{cx - 16} {cy + 2} C{cx - 10} {cy - 10} {cx - 4} {cy - 10} {cx} {cy} S{cx + 10} {cy + 10} {cx + 16} {cy - 2}" class="{cls}"/>'


# ---------------------------------------------------------- Figure 15.1


def fig_friendly():
    pen = fk.Pen(seed=15)
    stops = [
        ("colleague", "runs on the work", "talk: tasks", "f-soft"),
        ("friendly colleague", "runs on warmth", "talk: weekends, the coffee machine", "f-a3"),
        ("work friend", "runs on trust", "talk: how it's really going", "f-a2"),
        ("friend", "runs on life", "would stay friends if one of you left", "f-a2s"),
    ]
    ys = [118, 222, 352, 456]
    b = [
        f'<path d="{pen.rect_d(24, 66, 612, 208)}" class="f-paper k-thin k-mute"/>',
        f'<path d="{pen.rect_d(24, 298, 612, 208)}" class="f-a2 k-thin"/>',
        fk.text(620, 94, "most of your working relationships,", "t t-sm t-end t-mute"),
        fk.text(620, 116, "and that's fine", "t t-sm t-end t-mute"),
        fk.text(620, 326, "a few people: where the", "t t-sm t-end t-a2"),
        fk.text(620, 348, "rules start to collide", "t t-sm t-end t-a2"),
        pen.line(70, ys[0], 70, ys[-1], "k-thick k-mute"),
    ]
    for (name, runs, talk, fill), y in zip(stops, ys):
        b.append(f'<circle cx="70" cy="{y}" r="20" class="{fill} k"/>')
        b.append(fk.text(112, y - 10, name, "t t-bold"))
        b.append(fk.text(112, y + 18, runs, "t t-sm"))
        b.append(fk.text(112, y + 42, talk, "t t-sm t-mute"))
    b += [
        fk.avatar("dev", 486, 418, 52, "f-dev"),
        fk.avatar("kai", 548, 418, 52, "f-kai"),
        fk.text(517, 470, "Dev and Kai, month six:", "t t-sm t-mid"),
        fk.text(517, 492, "heading for friends", "t t-sm t-mid"),
    ]
    fk.write_svg("ch15/friendly.svg", 660, 530, "Four kinds of work relationship", "\n".join(b))


# ---------------------------------------------------------- Figure 15.2


def bowl(x, y):
    return (
        f'<path d="M{x - 18} {y} A18 14 0 0 0 {x + 18} {y} Z" class="f-a1 k-thin"/>'
        f'<path d="M{x - 4} {y - 4} L{x + 14} {y - 26} M{x + 2} {y - 4} L{x + 20} {y - 22}" class="k-thin"/>'
    )


def sun(x, y):
    rays = "".join(
        f'<path d="M{x + 13 * c:.1f} {y + 13 * s:.1f} L{x + 19 * c:.1f} {y + 19 * s:.1f}" class="k-thin k-a3"/>'
        for c, s in ((1, 0), (-1, 0), (0, 1), (0, -1), (0.7, 0.7), (-0.7, 0.7), (0.7, -0.7), (-0.7, -0.7))
    )
    return f'<circle cx="{x}" cy="{y}" r="9" class="f-a3 k-thin"/>{rays}'


def steps(x, y):
    return (
        f'<ellipse cx="{x - 8}" cy="{y + 4}" rx="5" ry="8" class="f-mute"/>'
        f'<ellipse cx="{x + 8}" cy="{y - 6}" rx="5" ry="8" class="f-mute"/>'
    )


def laptop(x, y):
    return (
        f'<rect x="{x - 14}" y="{y - 18}" width="28" height="18" rx="2" class="f-paper k-thin k-mute"/>'
        f'<path d="M{x - 19} {y + 2} L{x + 19} {y + 2}" class="k-thin k-mute"/>'
    )


def fig_hours():
    pen = fk.Pen(seed=25)
    x0, x1, y = 60, 610, 300

    def px(h):
        return x0 + h * (x1 - x0) / 220

    b = [
        pen.arrow(x0, y, x1 + 26, y, "k-thick"),
        fk.text(x0, y + 40, "0 h", "t t-sm t-mid"),
        fk.text(x1 + 26, y + 40, "hours together", "t t-sm t-end"),
    ]
    for h, label, cls in ((50, "casual friend", "t-a2"), (90, "friend", "t-a2"), (200, "close friend", "t-a2")):
        x = px(h)
        b.append(f'<path d="M{x:.1f} {y - 14} L{x:.1f} {y + 14}" class="k-thick k-a2"/>')
        b.append(fk.text(x, y - 56, f"~{h} h" if h < 200 else "200+ h", "t t-bold t-mid"))
        b.append(fk.text(x, y - 30, label, f"t t-sm t-mid {cls}"))
    # what Dev and Kai's hours were made of
    b += [
        sun(px(14), 136), bowl(px(42), 146), steps(px(70), 138),
        fk.text(px(42), 96, "lunches on the roof, one long dinner,", "t t-sm t-mid"),
        fk.text(px(42), 118, "walks to the station", "t t-sm t-mid"),
        f'<path d="M{px(2):.1f} 176 L{px(2):.1f} 184 L{px(92):.1f} 184 L{px(92):.1f} 176" class="k-thin"/>',
        fk.text(px(150), 196, "Dev and Kai, after the noodle bar", "t t-sm t-a1 t-mid"),
        pen.arrow(px(126), 204, px(96), y - 12, "k-thin k-a1", bend=12, head=9),
    ]
    # hours in meetings, dimmed
    for i in range(7):
        b.append(laptop(px(10 + i * 26), 392))
    b += [
        fk.text(x0, 440, "hours in meetings together: they count for less", "t t-sm t-mute"),
        fk.text(x1 + 26, 492, "approximate figures, from Hall (2019)", "t t-sm t-end t-mute"),
    ]
    fk.write_svg("ch15/hours.svg", 660, 510, "Hours it takes to make a friend", "\n".join(b))


# ---------------------------------------------------------- Figure 15.3


def fig_boundaries():
    pen = fk.Pen(seed=35)
    cols = [("the whole", "team"), ("a work", "friend"), ("a friend who", "is your lead")]
    rows = [
        ("weekend plans", "TTT"),
        ("how a project is really going", "WTT"),
        ("frustration with a colleague", "XTW"),
        ("your health", "WWW"),
        ("your job search", "XWX"),
        ("your pay or review", "XWT"),
    ]
    cx = [372, 488, 604]
    top, rh = 118, 62
    b = []
    for (a, c), x in zip(cols, cx):
        b.append(fk.text(x, 56, a, "t t-sm t-mid t-bold"))
        b.append(fk.text(x, 80, c, "t t-sm t-mid t-bold"))
    b.append(pen.line(20, 96, 660, 96, "k"))
    for i, (topic, marks) in enumerate(rows):
        y = top + i * rh
        if i % 2 == 0:
            b.append(f'<rect x="20" y="{y - 20}" width="640" height="{rh}" class="f-soft"/>')
        b.append(fk.text(30, y + 18, topic, "t"))
        for m, x in zip(marks, cx):
            mark = {"T": tick, "X": cross, "W": wave}[m]
            b.append(mark(x, y + 10))
    note_y = top + 5 * rh + 36
    b.append(fk.text(cx[2], note_y, "in the one-to-one,", "t t-sm t-mid t-a2"))
    b.append(fk.text(cx[2], note_y + 20, "not at dinner", "t t-sm t-mid t-a2"))
    ly = note_y + 70
    b += [
        pen.line(20, ly - 30, 660, ly - 30, "k-thin k-dash k-mute"),
        tick(44, ly), fk.text(70, ly + 8, "fine", "t t-sm"),
        wave(150, ly), fk.text(176, ly + 8, "depends: say which hat you're wearing", "t t-sm"),
        cross(44, ly + 44), fk.text(70, ly + 52, "keep it out of this relationship", "t t-sm"),
        fk.text(660, ly + 96, "our suggestions, not findings", "t t-sm t-end t-mute"),
    ]
    fk.write_svg("ch15/boundaries.svg", 680, ly + 114, "A boundary map for work relationships", "\n".join(b))


if __name__ == "__main__":
    fig_friendly()
    fig_hours()
    fig_boundaries()
    print("wrote chapter 15 figures")
