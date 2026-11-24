#!/usr/bin/env python3
"""Convert a paper PDF in raw/papers/ to text markdown in raw/md/, with page markers.

Usage: python3 tools/pdf2md.py raw/papers/Vaswani2017-Transformer.pdf [more.pdf ...]

Each page is prefixed with `<!-- page N -->` so the agent can cite (… p.N).
Never overwrites an existing output file (raw/ is append-only).
Requires PyMuPDF (`import fitz`); falls back to `pdftotext -layout` if unavailable.
"""
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "raw" / "md"


def extract_pages(pdf: Path) -> list[str]:
    try:
        import pymupdf as fitz  # PyMuPDF (new name)
    except ImportError:
        try:
            import fitz  # PyMuPDF (legacy name)
        except ImportError:
            fitz = None
    if fitz is None:
        if not shutil.which("pdftotext"):
            sys.exit("Need PyMuPDF (pip install pymupdf) or pdftotext (brew install poppler).")
        text = subprocess.run(
            ["pdftotext", "-layout", str(pdf), "-"], check=True, capture_output=True, text=True
        ).stdout
        return text.split("\f")
    with fitz.open(pdf) as doc:
        return [page.get_text("text") for page in doc]


def convert(pdf: Path) -> None:
    out = OUT_DIR / (pdf.stem + ".md")
    if out.exists():
        print(f"skip (exists): {out.relative_to(ROOT)}")
        return
    pages = extract_pages(pdf)
    body = [f"# {pdf.stem}\n", f"> 自動轉檔自 raw/papers/{pdf.name}；公式與表格可能失真，請以 PDF 為準。\n"]
    for i, text in enumerate(pages, 1):
        if text.strip():
            body.append(f"\n<!-- page {i} -->\n\n{text.strip()}\n")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out.write_text("".join(body), encoding="utf-8")
    print(f"wrote: {out.relative_to(ROOT)} ({len(pages)} pages)")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    for arg in sys.argv[1:]:
        p = Path(arg).resolve()
        if not p.is_file():
            sys.exit(f"not found: {arg}")
        convert(p)
