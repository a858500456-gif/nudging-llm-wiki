---
title: 投影片製作 Graph（v1.0）
status: final
updated: 2026-11-24
---

# 投影片製作 Graph（v1.0，已定案）

> 老師的要求：先整理大綱 → 大綱確認 → 再做投影片逐頁內容 → 最後依此做成投影片。要設計成 graph，想清楚各階段要做的、如何檢查。
> 瀏覽器版：`outputs/graph/slide-pipeline.html`，直接讀取本檔的流程圖，只要改這裡就好

## 已決定的事
- 中間產物存成獨立的 Markdown 檔：`outputs/slides/specs/{論文}/`
- 人工確認關卡**只有 Gate 1（大綱）**；大綱定案後，Stage 2、3 自動跑完，遇到問題才停下來問
- 重點自動檢查：防爆版自動拆頁、圖貼情緒配對且不重複、數據與公式完整

## 流程圖

```mermaid
flowchart TD
  START(["📥 輸入：論文、受眾、預計時長"])

  subgraph S0["Stage 0：素材準備（Context Retrieval）"]
    N0["N0 收集素材<br/>讀論文頁＋沿 wiki 連結取一層<br/>→ 01-material.md"]
    C0{"🔍 Check 0<br/>每則事實有出處？<br/>論文讀過全文？"}
  end

  subgraph S1["Stage 1：大綱（Outline）"]
    N1["N1 產生大綱<br/>故事線＋每頁一句重點<br/>→ 02-outline.md"]
    C1{"🔍 Check 1<br/>故事線完整？<br/>每頁只有一個重點？<br/>頁數在範圍內？"}
    G1(["🙋 Gate 1：你確認大綱"])
  end

  subgraph S2["Stage 2：逐頁內容腳本（Slide Script）"]
    N2["N2 撰寫逐頁內容<br/>文字、數據、抽屜、元件、圖貼、台詞<br/>→ 03-script.md"]
    C21{"🔍 Check 2-1<br/>每頁都對得上大綱？"}
    C22{"🔍 Check 2-2<br/>數據、公式、作者年份<br/>和 wiki 一致？"}
    C23{"🔍 Check 2-3<br/>放得進 16:9？"}
    C24{"🔍 Check 2-4<br/>圖貼情緒配對<br/>且不重複？"}
  end

  subgraph S3["Stage 3：投影片（HTML）"]
    N3["N3 依腳本製作 HTML<br/>套用 theme ＋ assets"]
    C31{"🔍 Check 3-1<br/>和腳本一致？<br/>頁數、標題、數字"}
    C32{"🔍 Check 3-2<br/>畫面檢查<br/>路徑、溢出、遮擋"}
  end

  subgraph S4["Stage 4：發布"]
    N4["N4 產生單檔版<br/>寫進 log.md"]
  end

  ASK(["⚠️ 停下來問你"])
  RULE["規則：同一關連續失敗 3 次<br/>就停下來問你"]
  DONE(["✅ 完成"])

  START --> N0 --> C0
  C0 -- "❌ 缺出處" --> N0
  C0 -- "❌ 只讀過摘要" --> ASK
  C0 -- "✅ 通過" --> N1
  N1 --> C1
  C1 -- "❌ 自動修正" --> N1
  C1 -- "✅ 通過" --> G1
  G1 -- "✏️ 要求修改" --> N1
  G1 -- "✅ 大綱定案" --> N2
  N2 --> C21
  C21 -- "❌ 補上或刪掉" --> N2
  C21 -- "✅" --> C22
  C22 -- "❌ 補回數據" --> N2
  C22 -- "✅" --> C23
  C23 -- "❌ 自動拆成兩頁" --> N2
  C23 -- "✅" --> C24
  C24 -- "❌ 換圖貼" --> N2
  C24 -- "✅" --> N3
  N3 --> C31
  C31 -- "❌ 照腳本改" --> N3
  C31 -- "✅" --> C32
  C32 -- "❌ 版面問題" --> N3
  C32 -- "❌ 內容放不下" --> N2
  C32 -- "✅" --> N4 --> DONE
  RULE -.-> ASK

  classDef step fill:#fff3e3,stroke:#5b4a42,stroke-width:2px,color:#5b4a42
  classDef check fill:#fff2a6,stroke:#5b4a42,stroke-width:2px,color:#5b4a42
  classDef gate fill:#ffe3ec,stroke:#ee8aa8,stroke-width:3px,color:#5b4a42
  classDef term fill:#dcf1d6,stroke:#6fb37f,stroke-width:2px,color:#5b4a42
  classDef warn fill:#ffe3ec,stroke:#5b4a42,stroke-width:2px,stroke-dasharray:5 4,color:#5b4a42
  class N0,N1,N2,N3,N4 step
  class C0,C1,C21,C22,C23,C24,C31,C32 check
  class G1 gate
  class START,DONE term
  class ASK,RULE warn
```

## 各節點說明

| 節點 | 輸入 | 做什麼 | 產出 |
|---|---|---|---|
| N0 收集素材 | 論文頁 | 讀 `wiki/papers/` 論文頁，沿 `[[連結]]` 讀一層相關的概念頁、問題頁，整理成事實清單，每則附出處 | `01-material.md` |
| N1 產生大綱 | `01-material.md` | 排出故事線（開場 → 概念 → 方法 → 發現 → 反思 → 結論），每頁寫標題、一句重點、引用哪些素材 | `02-outline.md` |
| N2 撰寫逐頁內容 | 定案的 `02-outline.md` | 每頁寫內文、數據、抽屜內容、用哪個元件、圖貼和表情、對話泡泡台詞、出處 | `03-script.md` |
| N3 製作 HTML | `03-script.md` | 照腳本套用 `theme/` 和 `assets/`，不自行增減內容 | `{論文}.html` |
| N4 發布 | HTML | 執行 `bundle_slides.py` 產生單檔版，寫進 `log.md` | `dist/…standalone.html` |

## 各檢查說明

| 檢查 | 怎麼檢查 | 沒通過時 |
|---|---|---|
| Check 0 | 素材每一則都有 wiki 頁面和論文章節；論文頁 `status: full` | 缺出處 → 回 N0 補；只讀過摘要 → 停下來問你 |
| Check 1 | 故事線每一段都有頁；每頁只有一個重點；頁數在範圍內；素材裡的關鍵發現都有用到 | 回 N1 自動修正 |
| Gate 1 | **你確認大綱** | 附修改意見 → 回 N1 |
| Check 2-1 | 大綱的每一頁在腳本裡都有、重點沒跑掉、沒有多出來的頁（自動拆頁的 5a/5b 算同一頁） | 回 N2 |
| Check 2-2 | 數字、LaTeX 公式、作者年份逐一和 wiki 比對，關鍵數據不能在簡化時被拿掉 | 回 N2 補回 |
| Check 2-3 | 每頁區塊數、字數不超過上限；超過就拆成兩頁，不犧牲細節、也不讓文字溢出 | 回 N2 拆頁 |
| Check 2-4 | 依照圖貼情緒對照表，表情要符合內容；同一張圖貼不連續重複使用 | 回 N2 換圖貼 |
| Check 3-1 | HTML 的頁數、標題、數字和腳本一致 | 回 N3 照腳本改 |
| Check 3-2 | 圖片路徑存在；在瀏覽器執行 `tools/check_layout.js`，檢查溢出、圖貼遮擋文字 | 版面問題 → 回 N3；內容放不下 → 回 N2 |
| 共通規則 | 同一關連續失敗 3 次 | 停下來問你 |

## 預設規格（v1.0 定案時決定）
- **大綱預設**：受眾＝一般讀者（沒讀過論文的同學）、報告約 15 分鐘、**12–16 頁**；在 `00-brief.md` 可以覆寫
- **故事段落**：開場 → 概念 → 方法 → 發現 → 反思 → 結論，每一段至少 1 頁
- **每頁上限**（Check 2-3）：畫面上最多 **4 個內容區塊**、內文最多約 **180 個中文字**（不含抽屜）、每張卡片最多 **4 個條列**；超過就拆頁
- **圖貼情緒對照表**：`outputs/slides/assets/stickers.md`
- **繳交內容**：流程圖＋實際跑一次的全部產出（`specs/` 的中間檔、投影片、單檔版）
- **檢查工具**：`python3 tools/check_slides.py {stage} {論文}`，stage 為 `material`、`outline`、`script`、`html`
