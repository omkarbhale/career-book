"""Regenerate the cast avatars and the model sheet: python3 book/figures/_src/cast_figures.py"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
import figkit as fk  # noqa: E402

fk.write_avatars()

pen = fk.Pen(seed=11)
cells = [
    ("dev", "she/her", ["wants to build things", "laptop, teal hair clip"],
     '<g transform="translate(26 -96) rotate(-12)"><rect x="0" y="0" width="30" height="21" rx="2" class="f-paper k-thin"/><path d="M4 21 L-2 27 L30 27 L30 21" class="f-soft k-thin"/><circle cx="15" cy="10" r="3.4" class="f-a2"/></g>'),
    ("bea", "she/her", ["brilliant, hates selling", "headphones, glasses"], ""),
    ("rex", "he/him", ["aces every interview", "red blazer, big grin"], ""),
    ("meera", "she/her", ["has hired 200+ people", "a new mug every time"],
     '<g transform="translate(30 -82)"><path d="M0 0 L2 18 L16 18 L18 0 Z" class="f-a3 k-thin"/><path d="M18 4 C26 4 26 13 17 13" class="k-thin"/><path d="M5 -4 Q7 -8 5 -12 M11 -4 Q13 -8 11 -12" class="k-thin k-mute"/></g>'),
    ("tomas", "he/him", ["hiring manager \u2192 boss", "beard, flannel shirt"], ""),
    ("kai", "they/them", ["Dev\u2019s work friend", "lavender hair, hoop"], ""),
]
body = [fk.text(340, 44, "Model sheet: the cast", "t t-lg t-bold t-mid")]
for i, (key, pronouns, notes, prop) in enumerate(cells):
    col, row = i % 3, i // 3
    cx = 113 + col * 227
    feet = 350 + row * 410
    body.append(f'<ellipse cx="{cx}" cy="{feet - 4}" rx="48" ry="7" class="f-soft"/>')
    body.append(fk.person(key, cx, feet, 1.18, prop))
    body.append(fk.text(cx, feet + 36, fk.CAST[key]["name"], "t t-lg t-bold t-mid"))
    body.append(fk.text(cx, feet + 58, pronouns, "t t-sm t-mute t-mid"))
    body.append(fk.lines(cx, feet + 84, notes, "t t-sm t-mid", 22))
body.append(pen.line(60, 486, 620, 486, "k-thin k-dash k-mute"))
fk.write_svg(
    "cast/model-sheet.svg", 680, 880,
    "Model sheet showing the six recurring characters standing in two rows",
    "\n".join(body),
)
print("wrote cast figures")
