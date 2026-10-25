"""Figure handling: validate a standalone SVG and turn it into inline markup.

Figures are authored as standalone ``.svg`` files that open on their own. Each
file carries a copy of the canonical figure stylesheet
(``book/figures/figure.css``) in a ``<style>`` element, so it renders with
light-theme fallbacks when viewed alone. When the build inlines a figure it
drops that copy (the site stylesheet already holds the same rules, driven by
the theme tokens), prefixes every id so figures cannot collide on one page,
and adds the accessible name from the chapter's alt text.
"""

from __future__ import annotations

import re
import xml.etree.ElementTree as ET

SVG_NS = "http://www.w3.org/2000/svg"
XLINK_NS = "http://www.w3.org/1999/xlink"
ET.register_namespace("", SVG_NS)
ET.register_namespace("xlink", XLINK_NS)

FORBIDDEN = {"script", "foreignObject", "image", "iframe", "a", "audio", "video", "canvas"}
COLOUR_ATTRS = ("fill", "stroke", "stop-color", "flood-color", "lighting-color", "color")
ALLOWED_PAINT = {"none", "currentcolor", "transparent", "inherit"}
COLOUR_IN_STYLE_RE = re.compile(r"#[0-9a-fA-F]{3,8}\b|rgba?\(|hsla?\(|\b(?:black|white|red|green|blue|gray|grey)\b")


def _local(tag: str) -> str:
    return tag.split("}", 1)[1] if "}" in tag else tag


def normalise_css(css: str) -> str:
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    return re.sub(r"\s+", " ", css).strip()


def check_svg(text: str, where: str, canonical_css: str) -> list[str]:
    """Problems with a source SVG, as messages (empty when it is fine)."""
    problems = []
    try:
        root = ET.fromstring(text)
    except ET.ParseError as exc:
        return [f"{where}: not well-formed XML ({exc})"]
    if _local(root.tag) != "svg":
        return [f"{where}: the root element must be <svg>"]
    vb = root.get("viewBox", "")
    if len(vb.split()) != 4:
        problems.append(f"{where}: the <svg> needs a viewBox=\"0 0 W H\"")
    if "fig" not in root.get("class", "").split():
        problems.append(f"{where}: the <svg> needs class=\"fig\"")
    styles = [el for el in root.iter() if _local(el.tag) == "style"]
    if len(styles) != 1 or normalise_css(styles[0].text or "") != normalise_css(canonical_css):
        problems.append(
            f"{where}: its <style> must be an exact copy of book/figures/figure.css "
            "(run: python3 tools/build.py --sync-figure-style)"
        )
    for el in root.iter():
        name = _local(el.tag)
        if name in FORBIDDEN:
            problems.append(f"{where}: <{name}> is not allowed in figures")
        for attr, value in el.attrib.items():
            a = _local(attr)
            if a.startswith("on"):
                problems.append(f"{where}: event handler attribute {a!r} is not allowed")
            if a in COLOUR_ATTRS and value.strip().lower() not in ALLOWED_PAINT and not value.startswith("url(#"):
                problems.append(
                    f"{where}: <{name} {a}=\"{value}\"> hard-codes a colour; use a class from figure.css"
                )
            if a == "style" and COLOUR_IN_STYLE_RE.search(value):
                problems.append(f"{where}: <{name} style=...> hard-codes a colour; use a class from figure.css")
            if a in ("font-family",):
                problems.append(f"{where}: <{name}> sets font-family; use the text classes from figure.css")
            if a == "href" and not value.startswith("#"):
                problems.append(f"{where}: <{name}> links to {value!r}; figures may only reference their own ids")
    return problems


def inline_svg(text: str, prefix: str, label: str, decorative: bool = False) -> str:
    """Inline-ready markup for a checked SVG.

    A ``decorative`` SVG (an avatar next to a speaker's name) is hidden from
    assistive technology instead of being given an accessible name.
    """
    root = ET.fromstring(text)
    ids = {el.get("id") for el in root.iter() if el.get("id")}
    for el in list(root.iter()):
        for child in list(el):
            if _local(child.tag) in ("style", "title", "desc"):
                el.remove(child)
    for el in root.iter():
        if el.get("id"):
            el.set("id", f"{prefix}-{el.get('id')}")
        for attr in list(el.attrib):
            value = el.attrib[attr]
            if _local(attr) == "href" and value.startswith("#") and value[1:] in ids:
                el.set(attr, f"#{prefix}-{value[1:]}")
            elif "url(#" in value:
                el.set(attr, re.sub(r"url\(#([^)]+)\)", lambda m: f"url(#{prefix}-{m.group(1)})" if m.group(1) in ids else m.group(0), value))
    vb = root.get("viewBox").split()
    for drop in ("width", "height"):
        root.attrib.pop(drop, None)
    root.set("width", vb[2])
    root.set("height", vb[3])
    root.set("focusable", "false")
    if decorative:
        root.set("aria-hidden", "true")
    else:
        root.set("role", "img")
        root.set("aria-labelledby", f"{prefix}-title")
        title = ET.Element(f"{{{SVG_NS}}}title", {"id": f"{prefix}-title"})
        title.text = label
        root.insert(0, title)
    return ET.tostring(root, encoding="unicode", short_empty_elements=True)


def svg_text_content(text: str) -> str:
    """All human-readable text in an SVG (for the placeholder check)."""
    try:
        root = ET.fromstring(text)
    except ET.ParseError:
        return ""
    parts = []
    for el in root.iter():
        if _local(el.tag) in ("text", "tspan", "title", "desc"):
            parts.append(el.text or "")
    return " ".join(parts)


def sync_style(text: str, canonical_css: str) -> str:
    """Replace (or add) the figure's <style> block with the canonical CSS."""
    block = "<style>\n" + canonical_css.strip() + "\n</style>"
    if re.search(r"<style[^>]*>.*?</style>", text, flags=re.S):
        return re.sub(r"<style[^>]*>.*?</style>", lambda m: block, text, count=1, flags=re.S)
    return re.sub(r"(<svg\b[^>]*>)", lambda m: m.group(1) + "\n" + block, text, count=1)
