#!/usr/bin/env python3
"""Make the white background of an illustration PNG transparent.

Usage: python3 tools/remove_white_bg.py INPUT.png OUTPUT.png [--threshold 235]

Only near-white pixels *connected to the image border* are removed (flood fill),
so white/cream areas enclosed by a character's outline are kept.
Edge pixels next to the removed area get partial alpha to avoid a white halo.
"""
import argparse
from collections import deque

from PIL import Image


def remove_bg(src: str, dst: str, threshold: int = 235) -> None:
    im = Image.open(src).convert("RGBA")
    w, h = im.size
    px = im.load()

    def is_bg(x, y):
        r, g, b, a = px[x, y]
        return a == 0 or min(r, g, b) >= threshold

    bg = bytearray(w * h)
    q = deque()
    for x in range(w):
        for y in (0, h - 1):
            if is_bg(x, y) and not bg[y * w + x]:
                bg[y * w + x] = 1
                q.append((x, y))
    for y in range(h):
        for x in (0, w - 1):
            if is_bg(x, y) and not bg[y * w + x]:
                bg[y * w + x] = 1
                q.append((x, y))
    while q:
        x, y = q.popleft()
        for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= nx < w and 0 <= ny < h and not bg[ny * w + nx] and is_bg(nx, ny):
                bg[ny * w + nx] = 1
                q.append((nx, ny))

    for y in range(h):
        for x in range(w):
            i = y * w + x
            r, g, b, a = px[x, y]
            if bg[i]:
                px[x, y] = (r, g, b, 0)
                continue
            # feather: light pixels touching the background become semi-transparent
            touching = any(
                0 <= nx < w and 0 <= ny < h and bg[ny * w + nx]
                for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))
            )
            if touching:
                lightness = min(r, g, b)
                if lightness > 160:
                    alpha = int(a * (255 - lightness) / (255 - 160))
                    px[x, y] = (r, g, b, max(0, min(a, alpha)))
    im.save(dst)
    print(f"wrote {dst}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("dst")
    ap.add_argument("--threshold", type=int, default=235)
    a = ap.parse_args()
    remove_bg(a.src, a.dst, a.threshold)
