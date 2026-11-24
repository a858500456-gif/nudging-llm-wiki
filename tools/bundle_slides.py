#!/usr/bin/env python3
"""Bundle a slide deck into one self-contained HTML file for sharing.

Usage: python3 tools/bundle_slides.py outputs/slides/Valta2026-Technostress-Nudges.html
Output: outputs/slides/dist/<name>.standalone.html

Inlines local stylesheets (<link href="theme/...">), scripts (<script src="theme/...">),
and images (src="assets/..." and data-walker="assets/..."), resolving paths relative
to the deck file. Remote URLs (e.g. Google Fonts) are left untouched.
The source deck keeps using relative paths; edit the source, then re-run this script.
"""
import base64
import mimetypes
import re
import sys
from pathlib import Path

mimetypes.add_type("image/svg+xml", ".svg")


def is_local(ref: str) -> bool:
    return not re.match(r"^(https?:|data:|//)", ref)


def data_uri(path: Path) -> str:
    mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    return f"data:{mime};base64,{base64.b64encode(path.read_bytes()).decode()}"


def bundle(src: Path) -> Path:
    base = src.parent
    html = src.read_text(encoding="utf-8")
    missing = []

    def css(m):
        href = m.group(1)
        if not is_local(href):
            return m.group(0)
        p = base / href
        if not p.exists():
            missing.append(href)
            return m.group(0)
        return f"<style>/* {href} */\n{p.read_text(encoding='utf-8')}\n</style>"

    def js(m):
        s = m.group(1)
        if not is_local(s):
            return m.group(0)
        p = base / s
        if not p.exists():
            missing.append(s)
            return m.group(0)
        return f"<script>/* {s} */\n{p.read_text(encoding='utf-8')}\n</script>"

    def attr(m):
        name, ref = m.group(1), m.group(2)
        if not is_local(ref):
            return m.group(0)
        p = base / ref
        if not p.exists():
            missing.append(ref)
            return m.group(0)
        return f'{name}="{data_uri(p)}"'

    html = re.sub(r'<link rel="stylesheet" href="([^"]+)">', css, html)
    html = re.sub(r'<script src="([^"]+)"></script>', js, html)
    html = re.sub(r'\b(src|data-walker)="([^"]+\.(?:svg|png|jpe?g|gif|webp))"', attr, html)
    if missing:
        sys.exit(f"missing files: {sorted(set(missing))}")

    out_dir = base / "dist"
    out_dir.mkdir(exist_ok=True)
    out = out_dir / f"{src.stem}.standalone.html"
    out.write_text(html, encoding="utf-8")
    print(f"wrote {out} ({out.stat().st_size // 1024} KB)")
    return out


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    bundle(Path(sys.argv[1]))
