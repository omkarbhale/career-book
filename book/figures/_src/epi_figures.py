"""Regenerate the epilogue's figure: python3 book/figures/_src/epi_figures.py"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
import figkit as fk  # noqa: E402


def star(cx, cy, r, cls="f-a3s k"):
    pts = []
    for i in range(10):
        a = -math.pi / 2 + i * math.pi / 5
        rr = r if i % 2 == 0 else r * 0.45
        pts.append(f"{cx + rr * math.cos(a):.1f} {cy + rr * math.sin(a):.1f}")
    return f'<path d="M{" L".join(pts)} Z" class="{cls}"/>'


def ghost(cx, cy, label):
    """Where a character stood in Chapter 1: a dashed empty circle."""
    return (
        f'<circle cx="{cx}" cy="{cy}" r="26" class="f-none k-thin k-dash k-mute"/>'
        + fk.text(cx, cy + 50, label, "t t-sm t-mid t-mute")
    )


# ---------------------------------------------------------- Figure E.1


def fig_quadrant():
    pen = fk.Pen(seed=501)
    b = [
        '<rect x="370" y="40" width="250" height="250" class="f-a3"/>',
        pen.arrow(100, 540, 640, 540, "k"),
        pen.arrow(100, 540, 100, 24, "k"),
        pen.line(370, 40, 370, 540, "k-thin k-dash k-mute"),
        pen.line(100, 290, 640, 290, "k-thin k-dash k-mute"),
        fk.text(370, 584, "good at doing the job (the film) →", "t t-mid"),
        f'<g transform="rotate(-90 58 290)">{fk.text(58, 290, "good at getting hired (the trailer) →", "t t-mid")}</g>',
        fk.text(235, 74, "All trailer", "t-sans t-mid"),
        fk.text(470, 74, "One you", "t-sans t-mid"),
        star(560, 70, 20),
        fk.text(235, 324, "Not yet", "t-sans t-mid t-mute"),
        fk.text(520, 324, "All film", "t-sans t-mid"),
    ]
    # where they started (Chapter 1)
    b += [
        ghost(200, 150, "Rex, chapter 1"),
        ghost(560, 410, "Bea, chapter 1"),
        ghost(412, 468, "Dev, chapter 1"),
    ]
    # where they are now
    b += [
        pen.arrow(230, 150, 318, 150, "k k-dash k-a1", head=12),
        fk.avatar("rex", 352, 150, 60, "e-rex"),
        fk.text(352, 206, "Rex:", "t t-sm t-mid"),
        fk.text(352, 228, "getting there", "t t-sm t-mid"),
        pen.arrow(560, 378, 560, 186, "k k-dash k-a2", head=12),
        fk.avatar("bea", 560, 150, 60, "e-bea"),
        pen.arrow(420, 436, 448, 236, "k k-dash k-a4", bend=-14, head=12),
        fk.avatar("dev", 450, 200, 60, "e-dev"),
        fk.text(488, 208, "Dev", "t t-sm"),
        fk.text(522, 158, "Bea", "t t-sm t-end"),
    ]
    fk.write_svg("epi/quadrant.svg", 660, 610, "The quadrant, four years on", "\n".join(b))


if __name__ == "__main__":
    fig_quadrant()
    print("wrote epilogue figure")
