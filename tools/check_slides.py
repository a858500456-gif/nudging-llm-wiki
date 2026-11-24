#!/usr/bin/env python3
"""Automatic checks for the slide-making graph (outputs/graph/slide-pipeline.md).

Usage: python3 tools/check_slides.py {material|outline|script|html} PAPER
  e.g. python3 tools/check_slides.py outline Valta2026-Technostress-Nudges

Reads outputs/slides/specs/PAPER/{00-brief,01-material,02-outline,03-script}.md
and outputs/slides/PAPER.html. Prints every problem found; exit code 1 if any.
Formats are defined in AGENTS.md §7.6.
"""
import html as htmllib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
SLIDES = ROOT / "outputs" / "slides"
SECTIONS = ["開場", "概念", "方法", "發現", "反思", "結論"]
MAX_CHARS = 180          # 內文字數上限（不含抽屜）
MAX_BULLETS = 4 * 4      # 最多 4 個區塊 × 每區塊 4 個條列

FACT_RE = re.compile(r"^- \[(F\d+)(★)?\] (.+?) ⟨src: ([^\s⟩]+)[^⟩]*⟩\s*$")
NUM_RE = re.compile(r"\d+(?:[.,]\d+)?")


def specs(paper):
    return SLIDES / "specs" / paper


def read(path):
    if not path.exists():
        return None
    return path.read_text(encoding="utf-8")


def frontmatter(text):
    m = re.match(r"---\n(.*?)\n---", text, re.S)
    out = {}
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                out[k.strip()] = v.strip()
    return out


def blocks(text, id_re=r"S\d\d[a-z]?"):
    """Split '## S01 標題' blocks -> list of (id, title, {field: value})."""
    out = []
    parts = re.split(rf"^## ({id_re}) (.+)$", text, flags=re.M)
    for i in range(1, len(parts), 3):
        sid, title, body = parts[i], parts[i + 1].strip(), parts[i + 2]
        fields, cur = {}, None
        for line in body.splitlines():
            m = re.match(r"^- ([^：:]{1,6})[：:]\s*(.*)$", line)
            if m:
                cur = m.group(1)
                fields[cur] = m.group(2).strip()
            elif cur and line.strip() and not line.startswith("#"):
                fields[cur] += "\n" + line.strip()
        out.append((sid, title, fields))
    return out


def norm_num(s):
    return s.replace(",", "")


def paper_of(src, material_text):
    """The paper this material pack is about (from its frontmatter)."""
    return frontmatter(material_text).get("paper", "")


def material_facts(paper, problems):
    text = read(specs(paper) / "01-material.md")
    if text is None:
        problems.append("找不到 01-material.md")
        return {}, ""
    facts = {}
    for n, line in enumerate(text.splitlines(), 1):
        if not line.startswith("- ["):
            continue
        m = FACT_RE.match(line)
        if not m:
            problems.append(f"01-material.md 第 {n} 行格式不符（需要 [Fxx] 內容 ⟨src: 頁面 §章節⟩）")
            continue
        fid, star, body, src = m.groups()
        if fid in facts:
            problems.append(f"{fid} 重複")
        src_page = read(WIKI / f"{src}.md")
        if src_page is None:
            problems.append(f"{fid} 的出處 wiki/{src}.md 不存在")
        elif "🔍" not in body:
            # 數字必須照抄 wiki：出處頁或論文頁裡要找得到同一個數字（agent 推論🔍除外）
            paper_page = read(WIKI / "papers" / f"{paper_of(src, text)}.md") or ""
            pool = norm_num(src_page + paper_page)
            for num in NUM_RE.findall(body):
                if norm_num(num) not in pool:
                    problems.append(f"{fid} 的數字 {num} 在 wiki/{src}.md 找不到")
        facts[fid] = {"star": bool(star), "body": body}
    return facts, text


def check_material(paper):
    p = []
    page = read(WIKI / "papers" / f"{paper}.md")
    if page is None:
        p.append(f"找不到論文頁 wiki/papers/{paper}.md")
    elif frontmatter(page).get("status") != "full":
        p.append("論文頁不是 status: full（只讀過摘要）→ 停下來問使用者")
    if read(specs(paper) / "00-brief.md") is None:
        p.append("找不到 00-brief.md")
    facts, _ = material_facts(paper, p)
    if not facts:
        p.append("素材包沒有任何事實")
    if facts and not any(f["star"] for f in facts.values()):
        p.append("素材包沒有標記任何 ★ 關鍵發現")
    return p, f"{len(facts)} 則事實，{sum(f['star'] for f in facts.values())} 則 ★"


def page_range(paper):
    brief = read(specs(paper) / "00-brief.md") or ""
    m = re.search(r"頁數範圍\s*\|\s*(\d+)\s*[–-]\s*(\d+)", brief)
    return (int(m.group(1)), int(m.group(2))) if m else (12, 16)


def check_outline(paper):
    p = []
    facts, _ = material_facts(paper, [])
    text = read(specs(paper) / "02-outline.md")
    if text is None:
        return ["找不到 02-outline.md"], ""
    bl = blocks(text, r"S\d\d")
    lo, hi = page_range(paper)
    if not lo <= len(bl) <= hi:
        p.append(f"頁數 {len(bl)} 不在 {lo}–{hi} 頁範圍內")
    used, last_sec = set(), -1
    for sid, title, f in bl:
        sec = f.get("段落", "")
        if sec not in SECTIONS:
            p.append(f"{sid} 的段落「{sec}」不是 {'/'.join(SECTIONS)} 之一")
        else:
            if SECTIONS.index(sec) < last_sec:
                p.append(f"{sid} 的段落「{sec}」順序倒退（故事線要依序）")
            last_sec = max(last_sec, SECTIONS.index(sec))
        point = f.get("重點", "")
        if not point:
            p.append(f"{sid} 沒有重點")
        elif "\n" in point or point.count("。") > 1:
            p.append(f"{sid} 的重點超過一句話")
        ids = re.findall(r"F\d+", f.get("素材", ""))
        if not ids:
            p.append(f"{sid} 沒有引用素材")
        for i in ids:
            if i not in facts:
                p.append(f"{sid} 引用的 {i} 不在素材包裡")
        used.update(ids)
    for sec in SECTIONS:
        if not any(f.get("段落") == sec for _, _, f in bl):
            p.append(f"故事線缺少「{sec}」段落")
    for fid, f in facts.items():
        if f["star"] and fid not in used:
            p.append(f"關鍵發現 {fid}★ 沒有出現在大綱裡")
    status = frontmatter(text).get("status", "")
    return p, f"{len(bl)} 頁，status: {status}"


def sticker_files(value):
    return re.findall(r"assets/[\w\-/]+\.(?:svg|png)", value or "")


def check_script(paper):
    p = []
    outline = read(specs(paper) / "02-outline.md")
    text = read(specs(paper) / "03-script.md")
    if outline is None or text is None:
        return ["找不到 02-outline.md 或 03-script.md"], ""
    if frontmatter(outline).get("status") != "approved":
        p.append("大綱還沒經過 Gate 1 核准（status 不是 approved）")
    _, mat_text = material_facts(paper, [])
    mat_nums = {norm_num(n) for n in NUM_RE.findall(mat_text)}
    out_ids = [sid for sid, _, _ in blocks(outline, r"S\d\d")]
    bl = blocks(text)
    base_ids = [re.sub(r"[a-z]$", "", sid) for sid, _, _ in bl]
    for sid in out_ids:
        if sid not in base_ids:
            p.append(f"大綱的 {sid} 在腳本裡不見了")
    for sid in dict.fromkeys(base_ids):
        if sid not in out_ids:
            p.append(f"腳本的 {sid} 不在大綱裡")
    prev = set()
    for sid, title, f in bl:
        for need in ("版型", "內文", "圖貼", "出處"):
            if not f.get(need):
                p.append(f"{sid} 缺少「{need}」")
        body = f.get("內文", "")
        chars = len(re.sub(r"[\s\-*•|：:，。、（）()「」]", "", body))
        if chars > MAX_CHARS:
            p.append(f"{sid} 內文 {chars} 字，超過 {MAX_CHARS} 字 → 拆頁")
        if body.count("\n") + 1 > MAX_BULLETS:
            p.append(f"{sid} 內文行數太多 → 拆頁")
        for n in NUM_RE.findall(f.get("數據", "")):
            if norm_num(n) not in mat_nums:
                p.append(f"{sid} 數據裡的 {n} 不在素材包裡")
        files = sticker_files(f.get("圖貼"))
        for fp in files:
            if not (SLIDES / fp).exists():
                p.append(f"{sid} 的圖貼 {fp} 不存在")
        cur = set(files)
        if cur & prev:
            p.append(f"{sid} 和上一頁重複使用圖貼 {', '.join(sorted(cur & prev))}")
        prev = cur
    return p, f"{len(bl)} 頁（大綱 {len(out_ids)} 頁）"


def strip_tags(s):
    return re.sub(r"\s+", " ", htmllib.unescape(re.sub(r"<[^>]+>", " ", s))).strip()


def check_html(paper):
    p = []
    script = read(specs(paper) / "03-script.md")
    page = read(SLIDES / f"{paper}.html")
    if script is None or page is None:
        return ["找不到 03-script.md 或投影片 HTML"], ""
    sections = re.findall(r'<section class="slide[^"]*">(.*?)</section>', page, re.S)
    bl = blocks(script)
    if len(sections) != len(bl):
        p.append(f"投影片有 {len(sections)} 頁，腳本有 {len(bl)} 頁")
    for (sid, title, f), sec in zip(bl, sections):
        text = strip_tags(sec)
        head = re.search(r"<h[12][^>]*>(.*?)</h[12]>", sec, re.S)
        head_txt = strip_tags(head.group(1)).replace(" ", "") if head else ""
        if title.replace(" ", "") != head_txt:
            p.append(f"{sid} 標題不一致：腳本「{title}」／HTML「{head_txt}」")
        flat = norm_num(text)
        for n in NUM_RE.findall(f.get("數據", "")):
            if norm_num(n) not in flat:
                p.append(f"{sid} 腳本數據 {n} 沒有出現在投影片上")
        for fp in sticker_files(f.get("圖貼")):
            if fp not in sec:
                p.append(f"{sid} 腳本指定的圖貼 {fp} 沒有用在這一頁")
        if 'class="cite"' not in sec and "資料來源" not in sec and sid != "S01":
            p.append(f"{sid} 沒有出處")
    for ref in re.findall(r'(?:src|data-walker|href)="([^"]+)"', page):
        if re.match(r"^(https?:|data:|#|//)", ref):
            continue
        if not (SLIDES / ref).exists():
            p.append(f"檔案不存在：{ref}")
    return p, f"{len(sections)} 頁"


CHECKS = {"material": check_material, "outline": check_outline, "script": check_script, "html": check_html}

if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] not in CHECKS:
        sys.exit(__doc__)
    stage, paper = sys.argv[1], sys.argv[2]
    problems, summary = CHECKS[stage](paper)
    print(f"[{stage}] {paper}：{summary}")
    if problems:
        for x in problems:
            print("  ❌", x)
        sys.exit(1)
    print("  ✅ 全部通過")
