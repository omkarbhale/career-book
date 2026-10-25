"""Regenerate Chapter 21's figures: python3 book/figures/_src/ch21_figures.py"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
import figkit as fk  # noqa: E402


def stop(x, y, label, colour, anchor="t-mid", dy=-18):
    """A station dot on a road, with its label."""
    return (
        f'<circle cx="{x}" cy="{y}" r="9" class="f-paper k {colour}"/>'
        + fk.text(x + (0 if anchor == "t-mid" else (16 if anchor == "" else -16)), y + dy, label, f"t {anchor}".strip())
    )


# ---------------------------------------------------------- Figure 21.1


def fig_fork():
    pen = fk.Pen(seed=21)
    fx, fy = 340, 400  # the fork
    b = [
        # the two roads
        f'<path d="M{fx} {fy} C300 330 180 300 120 90" class="k-thick k-a4"/>',
        f'<path d="M{fx} {fy} C380 330 500 300 560 90" class="k-thick k-a2"/>',
        f'<path d="M{fx} 470 L{fx} {fy}" class="k-thick"/>',
        fk.text(118, 50, "the manager track", "t t-sans t-mid t-a4"),
        fk.text(562, 50, "the expert track", "t t-sans t-mid t-a2"),
    ]
    def on(p0, p1, p2, p3, t):
        u = 1 - t
        return tuple(u**3 * a + 3 * u * u * t * b_ + 3 * u * t * t * c + t**3 * d for a, b_, c, d in zip(p0, p1, p2, p3))

    left = ((fx, fy), (300, 330), (180, 300), (120, 90))
    right = ((fx, fy), (380, 330), (500, 300), (560, 90))
    (lx1, ly1), (lx2, ly2), (lx3, ly3) = on(*left, 0.42), on(*left, 0.72), on(*left, 0.97)
    (rx1, ry1), (rx2, ry2) = on(*right, 0.45), on(*right, 0.85)
    b += [
        stop(round(lx1), round(ly1), "team lead", "k-a4", "t-end", 8),
        stop(round(lx2), round(ly2), "engineering manager", "k-a4", "t-end", 8),
        stop(round(lx3), round(ly3), "director", "k-a4", "", 8),
        stop(round(rx1), round(ry1), "staff engineer", "k-a2", "", 8),
        stop(round(rx2), round(ry2), "principal engineer", "k-a2", "t-end", 8),
    ]
    # the pendulum: dashed crossings between the roads
    b += [
        pen.arrow(lx1 + 14, ly1 - 4, rx1 - 14, ry1 - 4, "k k-dash k-mute", bend=-30, head=10),
        pen.arrow(rx2 - 14, ry2 + 6, lx2 + 14, ly2 + 6, "k k-dash k-mute", bend=-34, head=10),
        fk.text(fx, 250, "the pendulum: people do", "t t-sm t-mid t-mute"),
        fk.text(fx, 272, "switch back and forth", "t t-sm t-mid t-mute"),
    ]
    # Dev at the fork
    b += [
        fk.avatar("dev", fx, 500, 64, "fork-dev"),
        fk.text(fx, 560, "senior engineer", "t t-bold t-mid"),
    ]
    # what each road is judged on
    b += [
        f'<path d="{pen.rect_d(20, 404, 250, 118)}" class="f-a4 k-thin"/>',
        fk.text(36, 436, "judged on:", "t t-bold"),
        fk.text(36, 464, "your team's results,", "t"),
        fk.text(36, 490, "whether people grow", "t"),
        fk.text(36, 514, "and stay, who you hire", "t"),
        f'<path d="{pen.rect_d(410, 404, 250, 92)}" class="f-a2 k-thin"/>',
        fk.text(426, 436, "judged on:", "t t-bold"),
        fk.text(426, 464, "technical impact,", "t"),
        fk.text(426, 488, "at ever wider scope", "t"),
    ]
    # the gold sign
    b += [
        f'<path d="{pen.rect_d(110, 590, 460, 44)}" class="f-a3 k"/>',
        fk.text(340, 620, "first, check both roads exist where you work", "t t-mid"),
    ]
    fk.write_svg("ch21/fork.svg", 680, 660, "The fork: the manager track and the expert track", "\n".join(b))


# ---------------------------------------------------------- Figure 21.2


def fig_week():
    pen = fk.Pen(seed=22)
    days = ["M", "T", "W", "T", "F"]
    b = []

    def calendar(x0, title, colour, fill, blocks, who):
        """blocks: (day, start, end, label, cls); hours run 9 to 17 down the page."""
        top, hour = 140, 44
        col = 54
        out = [
            fk.avatar(who, x0 + 22, 52, 48, f"week-{who}"),
            fk.text(x0 + 54, 46, title[0], f"t t-bold {colour}"),
            fk.text(x0 + 54, 72, title[1], "t t-sm t-mute"),
        ]
        for i, d in enumerate(days):
            out.append(fk.text(x0 + i * col + col / 2, top - 14, d, "t t-sans t-mid"))
        out.append(f'<path d="{pen.rect_d(x0, top, col * 5, hour * 8)}" class="f-paper k-thin"/>')
        for day, s, e, label, cls in blocks:
            x, y = x0 + day * col + 3, top + (s - 9) * hour + 2
            h = (e - s) * hour - 4
            out.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{col - 6}" height="{h:.1f}" rx="5" class="{cls} k-thin"/>')
            if label:
                out.append(fk.text(x + (col - 6) / 2, y + h / 2 + 7, label, "t t-sm t-mid"))
        return out

    dev_blocks = []
    for d in range(5):
        dev_blocks.append((d, 9, 9.5, "", "f-mute"))
        dev_blocks.append((d, 9.6, 12.8, "build", "f-a2"))
        dev_blocks.append((d, 13.6, 17, "build" if d != 2 else "", "f-a2"))
    dev_blocks.append((2, 13.6, 14.6, "plan", "f-soft"))
    dev_blocks.append((2, 14.7, 17, "review", "f-a2"))
    kai_blocks = [
        (0, 9, 10, "1:1", "f-a4"), (0, 10, 11, "1:1", "f-a4"), (0, 11.2, 12.4, "plan", "f-soft"),
        (0, 13.5, 14.5, "1:1", "f-a4"), (0, 14.6, 15.6, "hire", "f-a3"), (0, 15.8, 17, "help", "f-soft"),
        (1, 9, 10.2, "road", "f-soft"), (1, 10.4, 11.4, "1:1", "f-a4"), (1, 11.6, 12.6, "hire", "f-a3"),
        (1, 13.5, 14.5, "upset", "f-a1"), (1, 14.7, 16, "plan", "f-soft"), (1, 16.1, 17, "1:1", "f-a4"),
        (2, 9, 10, "help", "f-soft"), (2, 10.2, 11.2, "1:1", "f-a4"), (2, 11.4, 12.6, "", "f-mute"),
        (2, 13.5, 15, "road", "f-soft"), (2, 15.2, 16.2, "hire", "f-a3"), (2, 16.3, 17, "", "f-mute"),
        (3, 9, 10, "1:1", "f-a4"), (3, 10.2, 11.4, "upset", "f-a1"), (3, 11.6, 12.6, "plan", "f-soft"),
        (3, 13.5, 15.2, "mine", "f-paper"), (3, 15.4, 17, "help", "f-soft"),
        (4, 9, 10, "", "f-mute"), (4, 10.2, 12.6, "mine", "f-paper"), (4, 13.5, 14.5, "1:1", "f-a4"),
        (4, 14.7, 17, "mine", "f-paper"),
    ]
    b += calendar(24, ("Dev", "senior engineer"), "t-a2", "f-a2", dev_blocks, "dev")
    b += calendar(362, ("Kai", "squad lead"), "t-a4", "f-a4", kai_blocks, "kai")
    # Thursday's "mine" block gets crossed out
    tx, ty = 362 + 3 * 54 + 3, 140 + (13.5 - 9) * 44 + 2
    b.append(f'<path d="M{tx + 4} {ty + 6} L{tx + 44} {ty + 66} M{tx + 44} {ty + 6} L{tx + 4} {ty + 66}" class="k-thick k-a1"/>')
    b += [
        fk.text(24, 524, "build = long, unbroken work", "t t-sm t-mute"),
        fk.text(24, 548, "grey = stand-ups and meetings", "t t-sm t-mute"),
        fk.text(362, 524, "1:1, hire, plan, road(map), help (unblock),", "t t-sm t-mute"),
        fk.text(362, 548, "upset (someone is), mine (own work)", "t t-sm t-mute"),
        fk.text(340, 600, "the job is in the small boxes", "t t-bold t-mid t-a4"),
        fk.text(340, 632, "illustrative calendars, not data", "t t-sm t-mid t-mute"),
    ]
    fk.write_svg("ch21/week.svg", 660, 650, "A maker's week and a manager's week", "\n".join(b))


# ---------------------------------------------------------- Figure 21.3


def fig_way_back():
    pen = fk.Pen(seed=23)
    b = []

    def card(x, y, w, h, n, head, rows, fill, head_cls=""):
        out = [f'<path d="{pen.rect_d(x, y, w, h)}" class="{fill} k"/>']
        out.append(f'<circle cx="{x + 24}" cy="{y + 26}" r="15" class="f-paper k"/>')
        out.append(fk.text(x + 24, y + 34, str(n), "t t-bold t-mid"))
        out.append(fk.text(x + 48, y + 34, head, f"t t-bold {head_cls}".strip()))
        for i, r in enumerate(rows):
            out.append(fk.text(x + 22, y + 66 + i * 26, r, "t t-sm"))
        return out

    b += card(30, 30, 290, 150, 1, "agree it in writing", ["how long it lasts", "what good looks like", "how you'd step back"], "f-a3")
    b += card(360, 30, 290, 150, 2, "do the real job", ["one-to-ones, hiring,", "planning, interruptions", "(not a demo of it)"], "f-a4")
    b += card(360, 240, 290, 150, 3, "check in: weeks 4, 8", ["what energises you?", "what drains you?", "what does the team say?"], "f-paper")
    b += [
        pen.arrow(322, 104, 356, 104, "k-thick", head=12),
        pen.arrow(505, 184, 505, 234, "k-thick", head=12),
    ]
    # stop 4: three outcomes
    outcomes = [(90, "take it", "f-a4"), (250, "not yet", "f-soft"), (410, "step back", "f-a2")]
    b.append(f'<circle cx="{300 + 24}" cy="{470}" r="15" class="f-paper k"/>')
    b.append(fk.text(324, 478, "4", "t t-bold t-mid"))
    b.append(fk.text(348, 478, "decide", "t t-bold"))
    b.append(pen.arrow(470, 394, 400, 450, "k-thick", bend=-8, head=12))
    for x, label, fill in outcomes:
        b.append(f'<path d="{pen.rect_d(x, 510, 150, 50)}" class="{fill} k"/>')
        b.append(fk.text(x + 75, 543, label, "t t-bold t-mid"))
        b.append(pen.line(324, 490, x + 75, 508, "k-thin"))
    # the way back
    b += [
        f'<path d="M485 562 C470 650 10 640 14 470 C12 350 40 240 80 188" class="k-thick k-dash k-a2"/>',
        '<path d="M80 188 L64 194 M80 188 L80 205" class="k-thick k-a2"/>',
        fk.text(62, 300, "the way back,", "t t-a2"),
        fk.text(62, 326, "agreed in advance", "t t-a2"),
        fk.text(340, 676, "stepping back is a result, not a failure", "t t-bold t-mid"),
    ]
    fk.write_svg("ch21/way-back.svg", 680, 700, "A management trial with a way back", "\n".join(b))


if __name__ == "__main__":
    fig_fork()
    fig_week()
    fig_way_back()
    print("wrote chapter 21 figures")
