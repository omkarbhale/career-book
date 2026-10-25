"""figkit: optional helpers for drawing the book's figures in Python.

Figures are plain standalone SVG files, and writers may hand-write them. This
module is for the parts that are tedious by hand and must stay consistent:

* the cast, drawn from one definition (``CAST``), as avatars, heads or full
  figures, so every chapter draws Dev the same way;
* "hand-drawn" lines and boxes: straight lines become gentle curves with a
  deterministic wobble (a fixed seed gives the same file every time);
* writing a standalone figure with the canonical style block.

Scripts in book/figures/_src/ use it. Run one to regenerate its figure:

    python3 book/figures/_src/ch01_figures.py
"""

from __future__ import annotations

import html
import math
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FIGURES = ROOT / "book" / "figures"

# ---------------------------------------------------------------- the cast
# Head parts are drawn on a 64x64 grid with the face centred at (32, 30).

EYES = '<circle cx="27.4" cy="30.4" r="1.6" class="f-ink"/><circle cx="36.6" cy="30.4" r="1.6" class="f-ink"/>'
NOSE = '<path d="M32.2 31.5 Q31 34.4 32.8 34.8" class="k-thin"/>'

CAST = {
    "dev": dict(
        name="Dev", skin="skin3", shirt="dev",
        back='<path d="M18.6 30 C17.4 18 24 13.6 32 13.6 C40.5 13.6 47 18.4 45.6 30 L47.4 46.5 C44 49.5 40.5 48.4 39.4 45.4 L24.6 45.4 C23.5 48.4 20 49.5 16.6 46.5 Z" class="f-hair1 k-thin"/>',
        collar='<path d="M21.5 49.5 C25 55.5 39 55.5 42.5 49.5" class="k-thin"/><path d="M28.4 54 L27.6 61" class="k-thin"/><path d="M35.6 54 L36.4 61" class="k-thin"/>',
        hair='<path d="M19.7 27.5 C20 18.4 26 15.2 32.6 15.6 C39.4 16 44.2 19.8 44.5 27.5 C40.4 22.6 35.4 21.2 30 21.8 C25.8 22.3 22.4 24.4 19.7 27.5 Z" class="f-hair1 k-thin"/><rect x="37.2" y="18.2" width="6.4" height="2.8" rx="1.2" transform="rotate(28 40.4 19.6)" class="f-a2s k-thin"/>',
        face=EYES + '<path d="M24.8 26.2 Q27.4 24.8 30 26" class="k-thin"/><path d="M34 26 Q36.6 24.8 39.2 26.2" class="k-thin"/>' + NOSE + '<path d="M28.4 37.6 Q32 40 35.6 37.4" class="k-thin"/>',
    ),
    "bea": dict(
        name="Bea", skin="skin2", shirt="bea",
        back="",
        collar='<path d="M27 48.6 L32 57.5 L37 48.6 Z" class="f-paper k-thin"/><path d="M17.5 52 C17.5 43.5 46.5 43.5 46.5 52" class="k-thick k-mute"/><rect x="13.6" y="48.5" width="7" height="9" rx="2.6" class="f-mute k-thin"/><rect x="43.4" y="48.5" width="7" height="9" rx="2.6" class="f-mute k-thin"/>',
        hair='<g class="f-hair2 k-thin"><circle cx="20.6" cy="25.6" r="4.2"/><circle cx="22.8" cy="19.6" r="4.8"/><circle cx="28.4" cy="15.6" r="5.2"/><circle cx="35" cy="15.2" r="5.2"/><circle cx="40.8" cy="18.8" r="4.9"/><circle cx="43.6" cy="24.6" r="4.2"/><circle cx="31.8" cy="19.8" r="4"/></g>',
        face=EYES + '<circle cx="27.4" cy="30.4" r="4.3" class="k-thin"/><circle cx="36.6" cy="30.4" r="4.3" class="k-thin"/><path d="M31.7 30 Q32 29 32.3 30" class="k-thin"/><path d="M24.8 24.8 Q27.4 24 30 24.8" class="k-thin"/><path d="M34 24.8 Q36.6 24 39.2 24.8" class="k-thin"/>' + NOSE + '<path d="M29.2 38 Q32 39.4 34.8 37.8" class="k-thin"/>',
    ),
    "rex": dict(
        name="Rex", skin="skin1", shirt="rex",
        back="",
        collar='<path d="M27 48.6 L32 56 L37 48.6 Z" class="f-paper k-thin"/><path d="M26.4 48.8 L30.4 59 L32 54" class="k-thin"/><path d="M37.6 48.8 L33.6 59 L32 54" class="k-thin"/>',
        hair='<path d="M19.6 27.4 C18 15.4 25 9.2 34 10 C40 10.6 46 13 47.2 18.4 C44.4 16.8 41.4 17.2 40.2 18.2 C44 20.2 45.6 23.6 44.6 27.4 C41 22.2 36 20.6 30 20.6 C25 20.6 21.6 23.2 19.6 27.4 Z" class="f-hair2 k-thin"/>',
        face=EYES + '<path d="M24.4 24.6 Q27.4 22 30.6 23.8" class="k-thin"/><path d="M33.4 23.8 Q36.6 22 39.6 24.6" class="k-thin"/>' + NOSE + '<path d="M25.8 36.4 Q32 44 38.2 36.4 Z" class="f-paper k-thin"/><path d="M26.6 37.4 L37.4 37.4" class="k-thin"/>',
    ),
    "meera": dict(
        name="Meera", skin="skin3", shirt="meera",
        back='<circle cx="32" cy="11.6" r="5.6" class="f-hair3 k-thin"/>',
        collar='<path d="M12 57 C22 51 36 58.5 52 51.5" class="k-thin"/><path d="M20 66 C25 58 33 56 44 59" class="k-thin"/>',
        hair='<path d="M19.6 29 C18.6 18.4 25 14.2 32 14.2 C39 14.2 45.4 18.4 44.4 29 C42 23.2 37 20.4 32 20.4 C27 20.4 22 23.2 19.6 29 Z" class="f-hair3 k-thin"/><circle cx="19.6" cy="35.6" r="1.3" class="f-a3s"/><circle cx="44.4" cy="35.6" r="1.3" class="f-a3s"/>',
        face=EYES + '<rect x="23.2" y="27.4" width="8.4" height="5.8" rx="1.8" class="k-thin"/><rect x="32.4" y="27.4" width="8.4" height="5.8" rx="1.8" class="k-thin"/><path d="M31.6 29.6 L32.4 29.6" class="k-thin"/><path d="M24.6 24.6 Q27.4 23.6 30.2 24.6" class="k-thin"/><path d="M33.8 24.6 Q36.6 23.6 39.4 24.6" class="k-thin"/>' + NOSE + '<path d="M27.8 37.4 Q32 40.6 36.2 37.4" class="k-thin"/>',
    ),
    "tomas": dict(
        name="Tomás", skin="skin2", shirt="tomas",
        back="",
        collar='<path d="M25.2 48.6 L29.2 53.6 L32 49.4 L34.8 53.6 L38.8 48.6" class="k-thin"/><path d="M14 58 L50 58" class="k-thin k-paper"/><path d="M22 52 L21 66 M42 52 L43 66" class="k-thin k-paper"/>',
        hair='<path d="M20 27.4 C19.4 17.4 25.6 14.2 32 14.2 C38.4 14.2 44.6 17.4 44 27.4 C42 21.6 38 19.6 32 19.6 C26 19.6 22 21.6 20 27.4 Z" class="f-hair1 k-thin"/><path d="M20.4 32.6 C20.8 42.8 26.8 46.6 32 46.6 C37.2 46.6 43.2 42.8 43.6 32.6 C41.4 37.8 37.2 39.4 32 39.4 C26.8 39.4 22.6 37.8 20.4 32.6 Z" class="f-hair1 k-thin"/>',
        face=EYES + '<path d="M24.6 26 Q27.4 25 30.2 26" class="k-thin"/><path d="M33.8 26 Q36.6 25 39.4 26" class="k-thin"/>' + NOSE + '<ellipse cx="32" cy="40.6" rx="3.4" ry="1.3" class="f-skin2"/>',
    ),
    "kai": dict(
        name="Kai", skin="skin4", shirt="kai",
        back="",
        collar='<path d="M10 56 L54 56" class="k-thin k-paper"/><path d="M8.5 61 L55.5 61" class="k-thin k-paper"/><path d="M27.6 48.8 C29 51.6 35 51.6 36.4 48.8" class="k-thin"/>',
        hair='<path d="M20 30 C19.6 25 20.4 22.4 22 21 L22.4 27 C21.4 28 20.8 29 20 30 Z" class="f-hair1"/><path d="M44 30 C44.4 25 43.6 22.4 42 21 L41.6 27 C42.6 28 43.2 29 44 30 Z" class="f-hair1"/><path d="M20.8 25.6 C20.6 16.8 27 12.4 34.2 12.8 C41.4 13.2 46.4 17 45.4 24.2 C43.4 21.6 38.6 19 33.4 19.8 C29 20.4 24.4 22.4 20.8 25.6 Z" class="f-hair4 k-thin"/><circle cx="44.4" cy="36.8" r="2.3" class="k-thin k-a3"/>',
        face=EYES + '<path d="M24.6 25.8 Q27.4 24.4 30.2 25.6" class="k-thin"/><path d="M33.8 25.6 Q36.6 24.4 39.4 25.8" class="k-thin"/>' + NOSE + '<path d="M27.2 36.4 Q32 42.4 36.8 36.4 Z" class="f-paper k-thin"/>',
    ),
}


# Details drawn over the torso of a full figure (person() coordinates: feet at 0, y up is negative).
TORSO = {
    'dev': '<path d="M-14 -131 C-8 -121 8 -121 14 -131" class="k-thin"/><path d="M-5 -124 L-6 -110 M5 -124 L6 -110" class="k-thin"/>',
    'bea': '<path d="M-17 -127 C-17 -150 17 -150 17 -127" class="k-thick k-mute"/><rect x="-22" y="-133" width="9" height="12" rx="3" class="f-mute k-thin"/><rect x="13" y="-133" width="9" height="12" rx="3" class="f-mute k-thin"/>',
    'rex': '<path d="M-8 -132 L0 -117 L8 -132 Z" class="f-paper k-thin"/><path d="M-11 -132 L-3 -100 L0 -114 M11 -132 L3 -100 L0 -114" class="k-thin"/>',
    'meera': '<path d="M-26 -121 C-10 -112 10 -127 26 -114" class="k-thin"/><path d="M-21 -97 C-6 -104 8 -95 22 -104" class="k-thin"/>',
    'tomas': '<path d="M-9 -132 L-4 -123 L0 -130 L4 -123 L9 -132" class="k-thin"/><path d="M-25 -100 L25 -100" class="k-thin k-paper"/><path d="M-12 -127 L-11 -67 M12 -127 L11 -67" class="k-thin k-paper"/>',
    'kai': '<path d="M-27 -110 L27 -110 M-26 -96 L26 -96 M-24 -82 L24 -82" class="k-thin k-paper"/>',
}


def _head_parts(key: str) -> str:
    c = CAST[key]
    skin = c["skin"]
    return (
        f'<ellipse cx="19.8" cy="31.5" rx="2.3" ry="3.3" class="f-{skin} k-thin"/>'
        f'<ellipse cx="44.2" cy="31.5" rx="2.3" ry="3.3" class="f-{skin} k-thin"/>'
        f'<ellipse cx="32" cy="30" rx="12.4" ry="14" class="f-{skin} k-thin"/>'
        f'{c["hair"]}{c["face"]}'
    )


def avatar_body(key: str, uid: str = "frame") -> str:
    """The inside of an avatar: a framed head-and-shoulders portrait on a 64x64 grid."""
    c = CAST[key]
    skin, shirt = c["skin"], c["shirt"]
    return (
        f'<defs><clipPath id="{uid}"><circle cx="32" cy="32" r="30.5"/></clipPath></defs>'
        '<circle cx="32" cy="32" r="30.5" class="f-soft"/>'
        f'<g clip-path="url(#{uid})">{c["back"]}'
        f'<path d="M27 40.5 L27 49 L37 49 L37 40.5 Z" class="f-{skin} k-thin"/>'
        f'<path d="M7 68 C8 54 17 48.5 32 48.5 C47 48.5 56 54 57 68 Z" class="f-{shirt} k-thin"/>'
        f'{c["collar"]}{_head_parts(key)}</g>'
        '<circle cx="32" cy="32" r="30.5" class="k-thin"/>'
    )


def avatar(key: str, cx: float, cy: float, size: float, uid: str) -> str:
    """An avatar placed on a larger figure, centred at (cx, cy), ``size`` across."""
    s = size / 64
    return f'<g transform="translate({cx - size / 2:.1f} {cy - size / 2:.1f}) scale({s:.3f})">{avatar_body(key, uid)}</g>'


def head(key: str) -> str:
    """Just the head (no frame, no shoulders), on the 64x64 grid."""
    c = CAST[key]
    return f'{c["back"]}{_head_parts(key)}'


def person(key: str, x: float, y: float, scale: float = 1.0, prop: str = "") -> str:
    """A standing figure whose feet touch (x, y). At scale 1 it is about 210 units tall.

    ``prop`` is extra SVG drawn in the figure's own coordinates (origin at the
    feet, y pointing down), for a laptop, a mug or a sign.
    """
    c = CAST[key]
    skin, shirt = c["skin"], c["shirt"]
    body = (
        # legs and shoes
        '<path d="M-14 -70 L-15 -8 L-4 -8 L-2 -70 Z" class="f-mute k-thin"/>'
        '<path d="M2 -70 L4 -8 L15 -8 L14 -70 Z" class="f-mute k-thin"/>'
        '<ellipse cx="-11" cy="-5" rx="10" ry="5" class="f-ink"/>'
        '<ellipse cx="11" cy="-5" rx="10" ry="5" class="f-ink"/>'
        # arms (behind the torso), hands
        '<path d="M-24 -128 C-36 -112 -40 -94 -38 -76 L-29 -75 C-30 -92 -27 -106 -19 -118 Z" class="f-{shirt} k-thin"/>'
        '<path d="M24 -128 C36 -112 40 -94 38 -76 L29 -75 C30 -92 27 -106 19 -118 Z" class="f-{shirt} k-thin"/>'
        '<circle cx="-33.5" cy="-71" r="6" class="f-{skin} k-thin"/>'
        '<circle cx="33.5" cy="-71" r="6" class="f-{skin} k-thin"/>'
        # torso
        '<path d="M-25 -129 C-30 -112 -26 -88 -20 -66 L20 -66 C26 -88 30 -112 25 -129 C14 -136 -14 -136 -25 -129 Z" class="f-{shirt} k-thin"/>'
    ).format(shirt=shirt, skin=skin)
    body += TORSO.get(key, "")
    neck = f'<path d="M-5 -142 L-5 -130 L5 -130 L5 -142 Z" class="f-{skin} k-thin"/>'
    k = 1.5  # cartoon proportions: a big head on a small body
    head_g = f'<g transform="translate({-32 * k:.1f} {-140 - 43 * k:.1f}) scale({k})">{head(key)}</g>'
    return (
        f'<g transform="translate({x:.1f} {y:.1f}) scale({scale:.3f})">'
        f"{body}{neck}{head_g}{prop}</g>"
    )


# ------------------------------------------------------------ hand-drawn lines


class Pen:
    """Draws slightly wobbly lines, deterministically (seeded)."""

    def __init__(self, seed: int = 7, wobble: float = 1.6):
        self.rng = random.Random(seed)
        self.wobble = wobble

    def _j(self) -> float:
        return self.rng.uniform(-self.wobble, self.wobble)

    def line_d(self, x1, y1, x2, y2) -> str:
        mx, my = (x1 + x2) / 2 + self._j(), (y1 + y2) / 2 + self._j()
        return f"M{x1:.1f} {y1:.1f} Q{mx:.1f} {my:.1f} {x2 + self._j() * 0.4:.1f} {y2 + self._j() * 0.4:.1f}"

    def line(self, x1, y1, x2, y2, cls="k") -> str:
        return f'<path d="{self.line_d(x1, y1, x2, y2)}" class="{cls}"/>'

    def rect_d(self, x, y, w, h) -> str:
        pts = [(x, y), (x + w, y), (x + w, y + h), (x, y + h)]
        d = f"M{pts[0][0] + self._j():.1f} {pts[0][1] + self._j():.1f}"
        for i in range(1, 5):
            ax, ay = pts[i - 1]
            bx, by = pts[i % 4]
            mx, my = (ax + bx) / 2 + self._j(), (ay + by) / 2 + self._j()
            d += f" Q{mx:.1f} {my:.1f} {bx + self._j() * 0.5:.1f} {by + self._j() * 0.5:.1f}"
        return d + " Z"

    def rect(self, x, y, w, h, cls="k") -> str:
        return f'<path d="{self.rect_d(x, y, w, h)}" class="{cls}"/>'

    def arrow(self, x1, y1, x2, y2, cls="k", bend=0.0, head=12) -> str:
        """A curved arrow; ``bend`` pushes the middle sideways (in units)."""
        dx, dy = x2 - x1, y2 - y1
        length = math.hypot(dx, dy) or 1
        nx, ny = -dy / length, dx / length
        mx, my = (x1 + x2) / 2 + nx * bend + self._j(), (y1 + y2) / 2 + ny * bend + self._j()
        shaft = f'<path d="M{x1:.1f} {y1:.1f} Q{mx:.1f} {my:.1f} {x2:.1f} {y2:.1f}" class="{cls}"/>'
        tx, ty = x2 - mx, y2 - my
        tl = math.hypot(tx, ty) or 1
        tx, ty = tx / tl, ty / tl
        wings = []
        for sgn in (1, -1):
            ang = math.radians(28) * sgn
            wx = x2 - head * (tx * math.cos(ang) - ty * math.sin(ang))
            wy = y2 - head * (tx * math.sin(ang) + ty * math.cos(ang))
            wings.append(f"M{x2:.1f} {y2:.1f} L{wx:.1f} {wy:.1f}")
        return shaft + f'<path d="{" ".join(wings)}" class="{cls}"/>'

    def circle_d(self, cx, cy, r, steps=10) -> str:
        pts = []
        start = self.rng.uniform(0, math.pi * 2)
        for i in range(steps + 1):
            a = start + 2 * math.pi * i / steps
            rr = r + self._j()
            pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
        d = f"M{pts[0][0]:.1f} {pts[0][1]:.1f}"
        for i in range(1, len(pts)):
            a0 = start + 2 * math.pi * (i - 0.5) / steps
            cxp = cx + (r / math.cos(math.pi / steps)) * math.cos(a0)
            cyp = cy + (r / math.cos(math.pi / steps)) * math.sin(a0)
            d += f" Q{cxp:.1f} {cyp:.1f} {pts[i][0]:.1f} {pts[i][1]:.1f}"
        return d


# ------------------------------------------------------------------- output


def text(x, y, s, cls="t", **attrs) -> str:
    extra = "".join(f' {k.replace("_", "-")}="{v}"' for k, v in attrs.items())
    return f'<text x="{x:.1f}" y="{y:.1f}" class="{cls}"{extra}>{html.escape(s)}</text>'


def lines(x, y, rows, cls="t", lh=28) -> str:
    return "".join(text(x, y + i * lh, r, cls) for i, r in enumerate(rows))


def write_svg(rel: str, width: int, height: int, title: str, body: str) -> Path:
    css = (FIGURES / "figure.css").read_text(encoding="utf-8").strip()
    doc = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" class="fig">\n'
        f"<title>{html.escape(title)}</title>\n<style>\n{css}\n</style>\n{body}\n</svg>\n"
    )
    path = FIGURES / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(doc, encoding="utf-8")
    return path


def write_avatars() -> None:
    for key, c in CAST.items():
        write_svg(f"cast/{key}.svg", 64, 64, c["name"], avatar_body(key))
