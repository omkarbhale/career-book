"""Regenerate the appendix's figure: python3 book/figures/_src/more_figures.py"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
import figkit as fk  # noqa: E402

# ---------------------------------------------------------- Figure C.1


def fig_edges():
    pen = fk.Pen(seed=601)
    cx, cy = 340, 310
    a, bb = 250, 244
    topics = [
        ("managing", "people"), ("founding,", "freelancing"), ("money beyond", "the pay cheque"),
        ("employment", "law"), ("immigration", ""), ("mental", "health"), ("salary", "data"),
        ("interview", "drills"), ("personality", "types"), ("reading the", "research"),
    ]
    fills = ["f-a4", "f-a1", "f-a3", "f-a2", "f-soft"]
    b = []
    islands = []
    for i, rows in enumerate(topics):
        ang = math.radians(90 - i * 36)
        x, y = cx + a * math.cos(ang), cy - bb * math.sin(ang)
        islands.append((x, y, rows, fills[i % len(fills)]))
        # ferry route from the main island's coast
        ex, ey = cx + 150 * math.cos(ang), cy - 92 * math.sin(ang)
        sx, sy = x - 80 * math.cos(ang), y + 30 * math.sin(ang)
        b.append(pen.line(ex, ey, sx, sy, "k-thin k-dash k-mute"))
    # the main island
    b += [
        f'<ellipse cx="{cx}" cy="{cy}" rx="150" ry="92" class="f-soft k-thick"/>',
        fk.text(cx, cy - 40, "this book", "t t-sans t-mid"),
        fk.text(cx, cy - 6, "snapshot", "t t-bold t-mid t-a1"),
        fk.text(cx, cy + 24, "long game", "t t-bold t-mid t-a2"),
        fk.text(cx, cy + 54, "career game", "t t-bold t-mid t-a4"),
    ]
    for x, y, rows, fill in islands:
        b.append(f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="86" ry="36" class="{fill} k"/>')
        if rows[1]:
            b.append(fk.text(x, y - 5, rows[0], "t t-mid"))
            b.append(fk.text(x, y + 21, rows[1], "t t-mid"))
        else:
            b.append(fk.text(x, y + 7, rows[0], "t t-mid"))
    b.append(fk.text(cx, 628, "each ferry leaves from a chapter", "t t-mid t-mute"))
    fk.write_svg("more/edges.svg", 680, 646, "The edges of the map: what this book leaves out", "\n".join(b))


if __name__ == "__main__":
    fig_edges()
    print("wrote appendix figure")
