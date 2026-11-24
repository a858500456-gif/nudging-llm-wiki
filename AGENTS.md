# AGENTS.md — 論文 LLM Wiki 維護規範

本檔是這個知識庫的 schema。任何 LLM agent（Claude Code、Gemini、Codex…）進入此專案時，都必須先讀完本檔，並嚴格依照以下規則維護 wiki。本檔會隨使用經驗與使用者共同演進（見 §11）。

---

## 0. 專案目的

- 這是一個**廣泛領域的個人研究百科**，長期收錄 AI／LLM／數學相關的經典與最新論文。
- 做法參考 Karpathy 的 LLM Wiki：不是每次查詢才從原始論文重新檢索（RAG），而是由 agent **持續編譯並維護一份互相連結的 markdown wiki**。每加入一篇論文，知識就累積一次。
- 分工：
  - **使用者**：挑選論文、提出問題、決定方向、審閱內容。
  - **Agent**：摘要、交叉引用、歸檔、維護一致性、記錄 log，wiki 的所有內容都由 agent 撰寫。
- 使用者用 **Obsidian** 瀏覽（以專案根目錄為 vault）。

---

## 1. 目錄結構

```
LLM Wiki Notes/
├── AGENTS.md            # 本檔（schema）
├── CLAUDE.md            # 只引用 AGENTS.md，給 Claude Code 讀
├── raw/                 # 原始資料，不可修改（見 §1.1）
│   ├── papers/          # 論文 PDF：Vaswani2017-Transformer.pdf
│   ├── md/              # PDF 轉出的文字版：Vaswani2017-Transformer.md
│   ├── bib/             # BibTeX：Vaswani2017-Transformer.bib
│   ├── notes/           # 使用者自己的閱讀筆記（markdown）
│   └── images/          # 截圖、論文圖表、投影片素材
├── wiki/                # 由 agent 全權維護
│   ├── index.md         # 全站目錄（內容導向）
│   ├── log.md           # 時間序紀錄（只能往後追加）
│   ├── overview.md      # 領域地圖
│   ├── papers/          # 單篇論文頁
│   ├── concepts/        # 概念／方法／架構／理論
│   ├── tasks/           # 任務／Benchmark／資料集／評估指標
│   ├── comparisons/     # 綜合比較、文獻回顧、query 結果存檔
│   ├── questions/       # 未解問題、論文間矛盾、研究缺口
│   └── authors/         # 學者／研究機構
├── outputs/             # 由 wiki 產生的成品（HTML 簡報、圖表等）
│   └── slides/          # HTML 簡報（規範見 §7.5）
│       ├── theme/       # 共用主題 kawaii.css、deck.js
│       ├── assets/      # 簡報用圖貼（從 assets/ 複製、已去背）：tangyuan/、friends/
│       ├── dist/        # 內嵌所有圖片的單檔分享版（由 tools/bundle_slides.py 產生）
│       └── _style-sample.html   # 風格樣張，所有元件的參考範例
├── tools/               # 輔助腳本：pdf2md.py、remove_white_bg.py、bundle_slides.py
└── assets/              # 使用者的簡報插圖素材（只在製作 outputs 時使用，見 §1.1）
```

### 1.1 原始資料（raw/）的規則
- `raw/` 是**唯一的事實來源**。Agent 可以**新增**檔案（下載 PDF、轉檔、存 BibTeX），但**絕不修改或刪除**已存在的檔案。
- `assets/` 不屬於知識庫，是使用者的插圖素材，**只有在製作 `outputs/` 的成品（例如簡報）時才可以讀取和使用**：
  - 可以使用：`小湯圓拷貝/`（主角）、`朋友群拷貝/`（配角）、`角色總覽拷貝.png`
  - **不可以使用：`器官拷貝/`**
  - 使用時，把檔案**複製**到 `outputs/slides/assets/`（小湯圓放 `tangyuan/`、朋友群放 `friends/`，用英文資料夾名），簡報只引用這裡的檔案，不要直接引用根目錄 `assets/` 的路徑。
  - 圖貼**一律要透明背景**。單張角色圖本來就是透明的；白底的合照或總覽圖要先用 `python3 tools/remove_white_bg.py 輸入.png 輸出.png` 去背再使用。
  - 不修改、不刪除 `assets/` 裡的檔案，也不在 `wiki/` 頁面中連結它。

---

## 2. 語言與寫作風格

- 內文使用**繁體中文（台灣習慣用語）**：例如「資料集」而非「数据集」、「模型」、「訓練」、「效能」、「最佳化」、「程式碼」。
- **保留英文原文**的項目：技術術語、模型名稱、方法名稱、指標名稱、資料集名稱、論文標題。
  - 例：「Self-Attention 讓每個 token 都能直接關注序列中的其他位置」、「在 Ablation Study 中移除 positional encoding 後，BLEU 下降 2.1」。
  - 第一次在某頁出現、且有通行中文譯名的術語，可以寫成「注意力機制 (Attention)」，之後就統一用英文。
- **數學一律使用 LaTeX**：行內 `$...$`，獨立區塊 `$$...$$`（Obsidian 可直接渲染）。
- **必須保留**的技術細節（不要只寫成白話）：
  - 關鍵數學推導（至少保留核心步驟，不需要逐行抄錄）
  - Loss Function、目標函數
  - 演算法 pseudocode（用 ```` ```text ```` 程式碼區塊，或用 LaTeX 寫成 algorithm 格式）
  - 關鍵超參數與主要實驗數字
- 符號以**論文原文為準**；若和其他論文的符號衝突，在概念頁的「定義與符號」段落統一並註明對照。
- 文風：精簡、有資訊量、可以掃讀。多用條列和表格，避免空泛的形容詞。

---

## 3. 命名規則

| 類型 | 檔名格式 | 範例 |
|---|---|---|
| 論文頁 | `第一作者姓氏+年份-簡稱.md` | `wiki/papers/Vaswani2017-Transformer.md` |
| 論文原始檔 | 和論文頁同名 | `raw/papers/Vaswani2017-Transformer.pdf` |
| 概念／方法 | 英文名稱，單字之間用 `-` 連接 | `wiki/concepts/Self-Attention.md`、`wiki/concepts/LoRA.md` |
| 任務／資料集 | 官方名稱 | `wiki/tasks/MMLU.md`、`wiki/tasks/Machine-Translation.md` |
| 比較／綜述 | 描述性英文名稱 | `wiki/comparisons/Efficient-Attention-Variants.md` |
| 問題 | 描述性英文名稱 | `wiki/questions/Does-Scaling-Saturate.md` |
| 作者／機構 | 全名，用 `-` 連接 | `wiki/authors/Ashish-Vaswani.md`、`wiki/authors/Google-DeepMind.md` |

- **簡稱**：優先使用社群通稱（Transformer、BERT、LoRA、DPO）；如果沒有通稱，就取標題裡的 1–3 個關鍵字。
- **撞名**：同一位作者、同一年有兩篇論文時，用不同的簡稱區分；仍然無法區分時，在年份後加 `a`／`b`（`Hinton2006a-...`）。
- 檔名中不要出現空白、中文或 `/ : ? #` 等特殊字元。

---

## 4. 連結與 Frontmatter

### 4.1 連結
- wiki 內部一律使用 Obsidian 的 `[[WikiLink]]`，只寫檔名、不寫路徑：`[[Vaswani2017-Transformer]]`、`[[Self-Attention]]`。
- 顯示文字和檔名不同時，用 `[[Self-Attention|自注意力]]`。
- 連結原始資料：`[[raw/papers/Vaswani2017-Transformer.pdf]]`。
- **連結要雙向**：A 頁提到 B 時，B 頁的「相關」段落也要回連 A。
- 每個頁面至少要有 1 個連入連結（通常來自 `index.md` 或相關頁面），不可以有孤兒頁。

### 4.2 Frontmatter（所有 wiki 頁面都要有）
共通欄位：
```yaml
---
type: paper | concept | task | comparison | question | author | overview
title: 頁面標題
domain: [LLM]          # 可複選：AI、LLM、ML、CV、NLP、RL、Math、Theory…
tags: [attention, architecture]
created: 2026-11-24
updated: 2026-11-24
reviewed: false        # agent 建立或修改後一律設為 false；使用者審閱後改為 true
---
```
論文頁額外的欄位：
```yaml
authors: [Ashish Vaswani, Noam Shazeer, ...]
year: 2017
venue: NeurIPS 2017          # 或 arXiv preprint
arxiv: "1706.03762"
doi: ""
source: "[[raw/papers/Vaswani2017-Transformer.pdf]]"
status: full | skimmed       # full = 讀完全文；skimmed = 只讀了摘要／部分內容
```
- 標籤一律使用小寫英文，單字之間用 `-` 連接。新增標籤前，先檢查 `index.md` 和既有頁面裡是否已有同義的標籤。

---

## 5. 頁面類型與模板

### 5.1 論文頁（`wiki/papers/`）
```markdown
# {論文完整英文標題}

> 一句話總結：這篇論文做了什麼、為什麼重要。

## 研究問題 (Problem)
## 核心方法 (Method)
- 架構／演算法說明
- 關鍵公式（LaTeX）與 Loss Function
- Pseudocode（若有）
## 實驗與結果 (Experiments)
- 資料集／Benchmark：[[...]]
- 主要數字（附表格，標註出處的表號）
- Ablation Study 的重點
## 貢獻 (Contributions)
## 限制 (Limitations)
- 作者自己承認的限制
- > [!note] 推論：agent 觀察到、但論文沒有寫的限制
## 與其他論文的關係
- 基於：[[...]]　改進／挑戰：[[...]]　被後續工作沿用：[[...]]
## 相關概念
[[...]]、[[...]]
```

### 5.2 概念／方法頁（`wiki/concepts/`）
```markdown
# {概念名稱}
> 一句話定義。
## 定義與符號
## 直覺解釋
## 數學形式（LaTeX）
## 演進脈絡
| 年份 | 論文 | 改了什麼 |
## 變體與比較
## 在哪些論文中出現
## 開放問題
```

### 5.3 任務／Benchmark／資料集頁（`wiki/tasks/`）
```markdown
# {名稱}
> 測量什麼能力、資料規模、評估指標。
## 內容與格式
## 評估指標
## 各論文的結果
| 論文 | 模型 | 分數 | 設定（shot 數等） | 出處 |
## 已知問題（資料汙染、飽和、標註錯誤等）
```

### 5.4 比較／綜述頁（`wiki/comparisons/`）
用於跨論文的比較表、流派對比、query 結果存檔。必須包含：比較的維度、比較表、結論、引用的論文清單。

### 5.5 問題頁（`wiki/questions/`）
用於論文間的矛盾、未解問題、研究缺口。必須包含：問題陳述、各方說法（附出處）、目前看法、可以補讀哪些論文。

### 5.6 作者／機構頁（`wiki/authors/`）
**只有在同一位作者或機構出現在 2 篇以上已收錄的論文時才建立**，避免全自動流程產生大量只有一行的空頁。內容：研究方向、收錄的論文清單、代表性貢獻。

### 5.7 overview.md（領域地圖）
本知識庫沒有單一論點，`overview.md` 是一張**領域地圖**：依 domain 分區，列出每個分支的核心概念、代表論文、目前的研究前沿，以及跨領域的連結。每次 ingest 之後，檢查是否需要更新。

---

## 6. 引用與可信度規則（最重要）

全自動流程沒有人在中途把關，以下規則**不可省略**：

1. **每個事實主張都要附出處**，格式是 `（[[Vaswani2017-Transformer]] §3.2）` 或 `（… Table 2）`、`（… p.5）`。
2. **數字必須從原文抄錄**，不可以憑記憶或估計。來源只有摘要時，在 frontmatter 標 `status: skimmed`。
3. **區分三種聲音**：
   - 論文的內容 → 一般內文 + 出處
   - Agent 的推論或延伸 → `> [!note] 推論`
   - 使用者的想法（來自 `raw/notes/` 或對話）→ `> [!quote] 使用者筆記`
4. **遇到矛盾不覆寫**：新論文和既有內容衝突時，保留舊說法、加入新說法，兩邊互相連結，並在 `wiki/questions/` 建立或更新對應的問題頁。
5. **說法過時時標註而不刪除**：被後續研究推翻或取代的說法，用 `> [!warning] 已被取代：見 [[...]]` 標註。
6. 不確定的內容寫明「不確定」，不要猜測。

---

## 7. 工作流程

### 7.1 Ingest（加入新論文）— 預設全自動

**步驟 0：取得原始檔**
- **使用者在對話中提供 PDF**：存入 `raw/papers/{命名}.pdf`。如果 agent 拿不到檔案路徑，請使用者把檔案放進 `raw/papers/`。
- **使用者提供 arXiv 連結、ID 或 DOI**：
  ```bash
  curl -L "https://arxiv.org/pdf/{id}" -o "raw/papers/{命名}.pdf"
  curl -L "https://arxiv.org/bibtex/{id}" -o "raw/bib/{命名}.bib"
  ```
  非 arXiv 的 DOI：嘗試找開放取用的 PDF；找不到時，告知使用者需要手動下載。
- **使用者提供 markdown 筆記**：存入 `raw/notes/`。
- **使用者提供截圖或圖表**：存入 `raw/images/{論文簡稱}-{描述}.png`。

**步驟 1：轉檔**
```bash
python3 tools/pdf2md.py "raw/papers/{命名}.pdf"   # 輸出到 raw/md/{命名}.md，附頁碼標記
```
如果轉檔失敗，改用 `pdftotext -layout`，或直接讀 PDF。公式和圖表在轉檔時容易失真，關鍵公式要回到 PDF 原文核對。

**步驟 2：閱讀**：讀完全文（至少讀摘要、方法、實驗、結論）。重要的圖表要另外看圖。

**步驟 3：寫論文頁**：依照 §5.1 的模板。

**步驟 4：更新相關頁面**（通常 5–15 頁）：
- 新建或更新論文用到的概念頁、任務頁
- 在任務頁的結果表裡加入這篇論文的數字
- 補上雙向連結
- 作者或機構達到 2 篇論文時，建立作者頁
- 處理矛盾（§6.4）
- 有需要時更新 `overview.md`

**步驟 5：更新 `index.md` 和 `log.md`**（格式見 §8）。

**步驟 6：回報**：在對話中列出：
- 新建的頁面
- 修改的頁面
- 發現的矛盾或待確認事項
- 建議接著讀的論文（來自引用文獻或相關工作）

**批次 ingest**：可以一次處理多篇論文，但必須逐篇完成步驟 0–5，最後再一起回報。

### 7.2 Query（提問）
1. 先讀 `wiki/index.md` 找出相關頁面，再深入閱讀這些頁面；wiki 不夠用時，才回頭查 `raw/md/`。
2. 回答必須附上 wiki 頁面和論文出處。
3. 依問題選擇回答形式：條列、比較表、LaTeX 推導、Mermaid 圖。
4. **有保存價值的回答要存回 wiki**：跨論文的比較或分析存成 `wiki/comparisons/` 頁面，發現的新問題存到 `wiki/questions/`，並寫進 log。純粹的事實查詢不需要存檔。
5. 回答時發現 wiki 有錯誤或缺漏，順便修正並記錄。

### 7.3 Lint（健康檢查）— 使用者要求時執行
檢查並回報（能自動修的就直接修，需要判斷的列出來問使用者）：
- 孤兒頁（沒有任何連入連結）、斷掉的 `[[連結]]`
- 被提到多次、卻還沒有獨立頁面的概念
- 單向連結（缺少回連）
- 缺少出處的主張、frontmatter 不完整
- 頁面之間的矛盾、被取代卻沒有標註的說法
- `status: skimmed` 的論文清單（建議補讀全文）
- `reviewed: false` 的頁面數量
- 建議補讀的論文、值得研究的新問題

### 7.4 Output（產出成品）
簡報、圖表等成品放在 `outputs/`，內容必須來自 wiki，並標註引用了哪些頁面。產出後在 `log.md` 記一筆 `output`。
- HTML 簡報一律依照 §7.5 的規範製作。

### 7.5 HTML 簡報規範（日系可愛粉彩 × 手帳風）
所有論文簡報共用同一套風格。開始前先打開 `outputs/slides/_style-sample.html` 和 `theme/kawaii.css`，看過所有元件再動手。

**檔案與路徑**
- 簡報：`outputs/slides/{論文頁檔名}.html`，例如 `Valta2026-Technostress-Nudges.html`。
- `<head>` 依序引用 Google Fonts（Huninn、Zen Maru Gothic）和 `theme/kawaii.css`；`</body>` 前引用 `theme/deck.js`。**不要在簡報裡另外寫一套樣式**，需要新元件時加到 `theme/kawaii.css`，並同步更新樣張。
- 圖片一律用**相對路徑** `assets/tangyuan/…`、`assets/friends/…`，不使用 data URI，也不引用根目錄 `assets/`。
- 完成後執行 `python3 tools/bundle_slides.py outputs/slides/{檔名}.html`，產生 `dist/{檔名}.standalone.html` 單檔分享版。只修改原始檔，單檔版每次重新產生。
- 預覽：用 `.claude/launch.json` 的 `slides` 伺服器（`http://localhost:8765/`）。直接開檔案時，預覽視窗讀不到相對路徑的圖片。

**版面**
- 固定 16:9 畫布（1600×900），由 `deck.js` 等比縮放。結構是 `<div class="stage">` 內含多個 `<section class="slide">`。
- **圖文講義型**：畫面保持清爽，每頁 2–4 個重點區塊；完整數據、統計表、推導放進右下角的 `<details class="more">` 抽屜（`summary` 寫「詳細數據」或「詳細說明」）。
- 每頁左下角放 `<p class="cite">出處：wiki/… · 論文 §…</p>`。
- 每頁頂部固定是 `.kicker`（英文小標）＋ `h2`。

**配色與字型**
- 文字用咖啡色 `--ink`（取自角色描邊）。強調色取自五個角色：`cream` 小湯圓、`pink` 年糕貓、`honey` 布丁熊、`sky` 棉花雲、`mint` 書蟲。卡片、標籤、長條圖都用這五色。
- 中文用 Huninn（粉圓體），大數字和英文小標用 Zen Maru Gothic（`.num`、`.kicker`）。

**元件**（全部定義在 `theme/kawaii.css`）
| 元件 | 用途 |
|---|---|
| `.card` + 顏色 | 重點區塊。卡片上有 `.sticker.peek` 時，第一個子元素必須是 `.tag`，避免圖貼蓋到文字 |
| `.sticker` | 圖貼，自動加白色描邊和陰影；尺寸 `xs/s/m/l/xl`；`.peek` 從卡片右上角探頭，`.peek.left` 從左上角 |
| `.bubble` | 角色的對話泡泡，一句話講重點或吐槽；尾巴方向 `.to-left`、`.down`，預設指向右 |
| `.speaker` | 泡泡＋角色的組合 |
| `.sticky` | 便利貼（含紙膠帶），放補充說明或提醒 |
| `.chalkboard` | 小黑板，放 Takeaway、研究問題、總結金句 |
| `.hl` / `.circled` | 螢光筆底線、手繪圈圈，標出關鍵字或關鍵數字 |
| `.bars` | 圓角長條圖，寬度用 `style="--w:XX%"`，比例要和數值一致 |
| `.flow` | A → B → C 流程圖 |
| `table.cute` | 抽屜裡的統計表 |
| `.tag.observe` | 「🔍 閱讀觀察」：agent 自己的推論，對應 wiki 的 `[!note] 推論`，一定要和論文內容分開標示 |

**圖貼使用規則**
- 小湯圓是主角，代表讀者或受試者；朋友群是配角，負責講解或吐槽（書蟲適合講解研究、布丁熊適合反思和限制）。
- **表情要符合內容**：壓力、困擾用 sweat/angry/sad；成功、結果好用 cheer/happy/love；疑問、反思用 thinking；意外的發現用 surprised。
- 每頁 1–4 個圖貼，不要塞滿；圖貼不能蓋到文字或數字。
- 不使用 `器官拷貝/` 的任何圖。

**內容規則**
- 數字一律從 wiki 抄錄。自己推算的數字要在投影片上註明「推算」。
- 依照 §6 區分三種聲音：論文內容、agent 推論（`.tag.observe`）、使用者筆記。
- 最後一頁列出引用的 wiki 頁面和原始論文出處。

### 7.6 投影片製作 Graph（必須照這個流程做）
流程圖、節點和檢查的完整說明在 `outputs/graph/slide-pipeline.md`（v1.0）。**不可以跳過階段，也不可以直接從 wiki 做 HTML。**

| Stage | 節點產出（`outputs/slides/specs/{論文}/`） | 檢查 | 確認 |
|---|---|---|---|
| 0 素材準備 | `00-brief.md`、`01-material.md` | `check_slides.py material` | — |
| 1 大綱 | `02-outline.md` | `check_slides.py outline` | **Gate 1：一定要停下來等使用者確認** |
| 2 逐頁內容 | `03-script.md` | `check_slides.py script` | 自動 |
| 3 投影片 | `outputs/slides/{論文}.html` | `check_slides.py html`＋瀏覽器畫面檢查 | 自動 |
| 4 發布 | `dist/` 單檔版、`log.md` | — | — |

- 同一關連續失敗 3 次、或論文只讀過摘要時，停下來問使用者。
- 大綱確認後，在 `02-outline.md` 的 frontmatter 設 `status: approved`；Stage 2 只能讀已核准的大綱。
- 每個 Stage 完成時，在 `log.md` 記一筆 `## [日期] slides | {論文} Stage N`。

**中間檔格式**（`check_slides.py` 會依這個格式檢查）
- `01-material.md`：每則事實一行 `- [F01] 內容 ⟨src: papers/Valta2026-Technostress-Nudges §5.2⟩`；src 必須是存在的 wiki 頁面（`papers/`、`concepts/`、`questions/` 下的檔名）；agent 推論在行首加 `🔍`；關鍵發現在 ID 後加 `★`（例如 `[F17★]`），大綱必須用到所有 ★。
- `02-outline.md`：每頁一個 `## S01 標題` 區塊，底下有 `- 段落：`（開場／概念／方法／發現／反思／結論）、`- 重點：`（一句話）、`- 素材：F01, F02`。
- `03-script.md`：每頁一個 `## S01 標題` 區塊（自動拆頁用 `S05a`、`S05b`），欄位：`- 版型：`、`- 內文：`（可多行）、`- 數據：`、`- 抽屜：`、`- 圖貼：assets/…svg（表情）`、`- 台詞：`、`- 出處：`。數據欄的每個數字都要出現在 `01-material.md`。

---

## 8. index.md 與 log.md 格式

### index.md
依頁面類型分區，每頁一行：
```markdown
## Papers
- [[Vaswani2017-Transformer]] — 提出完全基於 Attention 的 seq2seq 架構 · 2017 · NeurIPS · #LLM
## Concepts
- [[Self-Attention]] — 序列內每個位置對所有位置計算加權和 · 被 5 篇論文引用
```
- 每次 ingest 都要更新。總頁數超過約 300 頁時，把 index 拆成 `index-papers.md` 等子目錄，主 index 只保留各區的連結；同時考慮導入搜尋工具（例如 qmd）。

### log.md
只能往後追加，每筆紀錄的標題都使用固定前綴，方便用 grep 查詢：
```markdown
## [2026-11-24] ingest | Vaswani2017-Transformer
- 新建：papers/Vaswani2017-Transformer, concepts/Self-Attention, ...
- 更新：tasks/WMT14, overview
- 矛盾／待確認：無

## [2026-11-25] query | Transformer 與 RNN 的計算複雜度比較
- 存檔：comparisons/Transformer-vs-RNN-Complexity

## [2026-11-30] lint | 
- 修正 3 個斷連結；待確認 2 項
```
查詢最近 5 筆：`grep "^## \[" wiki/log.md | tail -5`

---

## 9. 何時必須停下來詢問使用者

全自動是預設，但以下情況**必須先詢問**：
- 要**刪除、合併或重新命名**既有的 wiki 頁面
- 單次 ingest 預計會修改**超過 20 個**既有頁面
- 要修改本檔（AGENTS.md）
- 無法取得論文全文（只能讀摘要），而使用者沒有說只看摘要也可以
- 遇到無法判斷的重大矛盾（例如兩篇主要論文的核心結論互相衝突）

---

## 10. 禁止事項

- 修改或刪除 `raw/` 裡已存在的檔案；修改 `assets/`；使用 `assets/器官拷貝/`；在 outputs 以外的地方使用 `assets/`
- 捏造數字、引用或論文
- 在沒有標註的情況下，把 agent 的推論寫成論文的結論
- 覆寫矛盾的說法而不保留紀錄
- 建立沒有任何連入連結的孤兒頁
- 跳過 `index.md` 或 `log.md` 的更新

---

## 11. Schema 演進

- 本檔是可以修改的。使用者或 agent 發現規則不合用時，由 agent 提出修改建議，**經使用者同意後**才修改，並在 `log.md` 記錄 `## [日期] schema | 修改摘要`。
- 待觀察、尚未決定的事項：
  - 是否導入搜尋工具（qmd），預計 wiki 超過約 300 頁時評估
  - 是否需要 `datasets/` 從 `tasks/` 獨立出來
  - HTML 簡報規範（§7.5）是否需要調整，例如手機版排版
