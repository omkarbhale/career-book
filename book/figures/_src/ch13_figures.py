"""Regenerate Chapter 13's figures: python3 book/figures/_src/ch13_figures.py"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
import figkit as fk  # noqa: E402

# ---------------------------------------------------------- Figure 13.1


def fig_point_first():
    pen = fk.Pen(seed=131)
    b = [
        fk.text(160, 36, "Story order", "t t-sans t-mid t-a1"),
        fk.text(480, 36, "Point first", "t t-sans t-mid t-a2"),
        pen.line(320, 20, 320, 520, "k-thin k-dash k-mute"),
    ]
    left = [("background", 1), ("how we got here", 1), ("what I tried", 1), ("more context", 1),
            ("three options", 1), ("caveats", 1)]
    y = 60
    for label, _ in left:
        b.append(pen.rect(40, y, 240, 46, "f-soft k-thin"))
        b.append(fk.text(56, y + 31, label, "t t-sm t-mute"))
        y += 56
    b.append(pen.rect(40, y, 240, 52, "f-a1s k"))
    b.append(fk.text(160, y + 34, "the ask", "t t-bold t-mid t-paper"))
    b.append(fk.lines(160, y + 96, ["most readers", "stop before here"], "t t-sm t-mid t-a1", 24))
    b.append(pen.arrow(250, y + 82, 262, y + 58, "k-thin k-a1", head=8))
    b += [
        pen.rect(360, 60, 240, 52, "f-a2s k"),
        fk.text(480, 94, "the ask", "t t-bold t-mid t-paper"),
        pen.rect(360, 122, 240, 46, "f-a2 k-thin"),
        fk.text(376, 153, "why, in one line", "t t-sm"),
        pen.rect(360, 178, 240, 46, "f-a2 k-thin"),
        fk.text(376, 209, "what you need from them", "t t-sm"),
        pen.rect(360, 244, 240, 46, "f-paper k-thin k-dash"),
        fk.text(376, 275, "details, if wanted", "t t-sm t-mute"),
        fk.lines(480, 340, ["a reader who stops", "after one line still", "knows what to do"], "t t-sm t-mid t-a2", 26),
    ]
    fk.write_svg("ch13/point-first.svg", 640, 540, "Story order versus point first", "\n".join(b))


# ---------------------------------------------------------- Figure 13.2


def fig_tone():
    pen = fk.Pen(seed=132)
    b = [
        fk.avatar("dev", 90, 170, 110, "t-dev"),
        fk.avatar("kai", 550, 170, 110, "t-kai"),
        # sender's head: tone included
        '<path d="M30 30 h170 a18 18 0 0 1 18 18 v44 a18 18 0 0 1 -18 18 h-110 l-18 20 v-20 h-42 a18 18 0 0 1 -18 -18 v-44 a18 18 0 0 1 18 -18 z" class="f-a3 k-thin"/>',
        fk.lines(115, 62, ["(said with a grin,", "obviously joking)"], "t t-sm t-mid", 24),
        '<path d="M440 30 h170 a18 18 0 0 1 18 18 v44 a18 18 0 0 1 -18 18 h-42 v20 l-18 -20 h-110 a18 18 0 0 1 -18 -18 v-44 a18 18 0 0 1 18 -18 z" class="f-a1 k-thin"/>',
        fk.lines(525, 62, ["...is she annoyed", "with me?"], "t t-sm t-mid", 24),
        pen.rect(196, 140, 248, 64, "f-paper k"),
        fk.text(320, 180, "“Oh great, another meeting.”", "t t-sm t-mid"),
        pen.arrow(150, 172, 192, 172, "k", head=10),
        pen.arrow(448, 172, 490, 172, "k", head=10),
        fk.lines(90, 266, ["what you hear", "when you reread it"], "t t-sm t-mid", 24),
        fk.lines(320, 236, ["what actually", "travels: the words"], "t t-sm t-mid t-mute", 24),
        fk.lines(550, 266, ["what they get:", "their own guess"], "t t-sm t-mid", 24),
        pen.line(24, 318, 616, 318, "k-thin k-mute"),
        fk.lines(320, 354, ["Senders overestimate how well tone comes across in writing,", "because they hear their own voice when they reread it."], "t t-sm t-mid", 26),
    ]
    fk.write_svg("ch13/tone-gap.svg", 640, 400, "The tone gap in written messages", "\n".join(b))


# ---------------------------------------------------------- Figure 13.3


def fig_feedback():
    pen = fk.Pen(seed=133)
    b = [
        fk.text(24, 40, "Feedback interventions, on average", "t t-sans"),
        '<rect x="24" y="60" width="370" height="46" class="f-a2s"/>',
        '<rect x="394" y="60" width="222" height="46" class="f-a1s"/>',
        pen.rect(24, 60, 592, 46, "k"),
        fk.text(209, 92, "the rest", "t t-bold t-mid t-paper"),
        fk.text(505, 92, "made it worse", "t t-bold t-mid t-paper"),
        fk.lines(505, 136, ["more than a third", "of interventions"], "t t-sm t-mid t-a1", 24),
        fk.text(24, 140, "segment sizes approximate", "t t-sm t-mute"),
        pen.line(24, 194, 616, 194, "k-thin k-dash k-mute"),
        fk.text(24, 232, "Where the feedback points", "t t-sans"),
        pen.arrow(320, 270, 40, 270, "k-thick k-a2", head=14),
        pen.arrow(320, 270, 600, 270, "k-thick k-a1", head=14),
        f'<circle cx="320" cy="270" r="7" class="f-ink"/>',
        fk.text(40, 310, "at the task", "t t-bold t-a2"),
        fk.text(600, 310, "at the self", "t t-bold t-a1 t-end"),
        pen.rect(24, 330, 284, 150, "f-a2 k-thin"),
        fk.lines(40, 366, ["“The decision is in", "paragraph six. Put it", "in the first line.”"], "t t-sm", 26),
        fk.text(40, 460, "tends to help", "t t-bold t-a2"),
        pen.rect(332, 330, 284, 150, "f-a1 k-thin"),
        fk.lines(348, 366, ["“You’re not a very", "clear writer, are", "you?”"], "t t-sm", 26),
        fk.text(348, 460, "tends to backfire", "t t-bold t-a1"),
    ]
    fk.write_svg("ch13/feedback.svg", 640, 500, "Feedback that helps versus feedback that hurts", "\n".join(b))


if __name__ == "__main__":
    fig_point_first()
    fig_tone()
    fig_feedback()
    print("wrote chapter 13 figures")
