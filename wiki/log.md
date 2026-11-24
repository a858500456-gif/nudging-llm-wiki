---
type: overview
title: Log
created: 2026-11-24
---

# Log

只能往後追加。查詢最近紀錄：`grep "^## \[" wiki/log.md | tail -5`

## [2026-11-24] schema | 建立知識庫
- 建立 AGENTS.md、目錄結構、index.md、log.md、overview.md、tools/pdf2md.py

## [2026-11-24] ingest | Valta2026-Technostress-Nudges
- 原始檔：raw/papers/Valta2026-Technostress-Nudges.pdf、raw/md/Valta2026-Technostress-Nudges.md（由使用者提供的本機 PDF 複製而來）
- 新建：papers/Valta2026-Technostress-Nudges、concepts/Technostress、concepts/Digital-Nudging、concepts/Cognitive-Effort、concepts/Digital-Mindset、concepts/Mediation-and-Moderation-Analysis、questions/Who-Benefits-More-From-Interface-Nudges、questions/Interface-Nudges-in-AI-Decision-Environments
- 更新：index、overview（新增 IS/HCI 分區）
- 矛盾／待確認：論文自己提出兩種相反的機制解釋（scaffolding 和 decision space optimization）；salience 操弄裡包含 "Lowest Total Price" 標籤，但三台車的總價其實相同（agent 推論）
- 其他：tools/pdf2md.py 改成優先使用 `import pymupdf`

## [2026-11-24] output | Valta2026-Technostress-Nudges 一般讀者導讀簡報
- 產出：outputs/slides/Valta2026-Technostress-Nudges.html（15 張，HTML 單檔，方向鍵切換）
- 引用：papers/Valta2026-Technostress-Nudges、concepts/Technostress、concepts/Digital-Nudging、concepts/Cognitive-Effort、concepts/Digital-Mindset、questions/Who-Benefits-More-From-Interface-Nudges、questions/Interface-Nudges-in-AI-Decision-Environments
- 備註：「間接效果約占四成」是由 Table 4 推算（0.163/0.439、0.219/0.580），簡報中已註明

## [2026-11-24] schema | 開放 assets/ 給 outputs 使用
- 經使用者同意：製作 outputs 時可以使用 assets/ 的小湯圓、朋友群插圖；**器官拷貝/ 不可以使用**；插圖複製到 outputs/slides/img/ 後內嵌進 HTML
- 修改 AGENTS.md §1、§1.1、§7.4、§10

## [2026-11-24] output | Valta2026-Technostress-Nudges 簡報加入插圖
- 加入小湯圓（主角）與朋友群（配角）共 16 張插圖，存放在 outputs/slides/img/，並內嵌進 HTML

## [2026-11-24] schema | 新增 HTML 簡報規範（AGENTS.md §7.5）
- 經使用者同意：日系可愛粉彩 × 手帳風、固定 16:9、圖文講義型（詳細數據放抽屜）、Huninn＋Zen Maru Gothic、圖貼相對路徑＋透明背景
- 共用主題 outputs/slides/theme/（kawaii.css、deck.js）；風格樣張 outputs/slides/_style-sample.html
- 新工具：tools/remove_white_bg.py（去背）、tools/bundle_slides.py（產生單檔版）
- 圖貼複製到 outputs/slides/assets/（tangyuan 24、friends 80 個檔案，含 3 張去背後的合照／總覽圖）

## [2026-11-24] output | Valta2026-Technostress-Nudges 簡報改用新主題
- outputs/slides/Valta2026-Technostress-Nudges.html（15 頁，6 頁附詳細數據抽屜）
- 單檔版：outputs/slides/dist/Valta2026-Technostress-Nudges.standalone.html
- 舊的 outputs/slides/img/ 已不再使用（刪除指令被擋下，待使用者手動刪除）

## [2026-11-24] output | 刪除舊的 outputs/slides/img/
- 使用者手動刪除；簡報、單檔版、樣張都不再引用

## [2026-11-24] output | 投影片製作 Graph 草稿 v0.2
- outputs/graph/slide-pipeline.md（Mermaid 流程圖＋節點與檢查說明，Obsidian 可直接看）
- outputs/graph/slide-pipeline.html（瀏覽器版，讀取 md 的流程圖）
- 已決定：中間產物存 outputs/slides/specs/{論文}/；只有大綱需要人工確認；重點檢查＝防爆版拆頁、圖貼情緒配對、數據公式完整
- 尚未定案，還沒寫進 AGENTS.md

## [2026-11-24] schema | 投影片製作 Graph v1.0 定案（AGENTS.md §7.6）
- outputs/graph/slide-pipeline.md 改為 v1.0，補上預設規格（12–16 頁、每頁 ≤4 區塊／≤180 字、情緒對照表位置、繳交內容）
- 新工具 tools/check_slides.py（material／outline／script／html 四種自動檢查）

## [2026-11-24] slides | Valta2026-Technostress-Nudges Stage 0
- 00-brief.md、01-material.md（33 則事實，3 則 ★）；Check 0 通過

## [2026-11-24] slides | Valta2026-Technostress-Nudges Stage 1
- 02-outline.md（16 頁，status: draft）；Check 1 通過；等待 Gate 1 使用者確認

## [2026-11-24] slides | Valta2026-Technostress-Nudges Gate 1
- 使用者核准大綱（16 頁），02-outline.md status: approved

## [2026-11-24] slides | Valta2026-Technostress-Nudges Stage 2
- outputs/slides/assets/stickers.md（圖貼情緒對照表）；03-script.md（16 頁）
- Check 2 第一次失敗：S10 的「差距約 0.6 分」是自行計算、不在素材包 → 退回 N2，改成 Cohen's d = 0.63／0.62 → 通過

## [2026-11-24] slides | Valta2026-Technostress-Nudges Stage 3
- 依腳本重做 outputs/slides/Valta2026-Technostress-Nudges.html（16 頁）；舊版移到 outputs/slides/_legacy/…no-graph.html
- Check 3-1（check_slides.py html）通過；Check 3-2（tools/check_layout.js）：圖片 0 失敗、溢出 0、遮擋 0

## [2026-11-24] slides | Valta2026-Technostress-Nudges Stage 4
- 單檔版 outputs/slides/dist/Valta2026-Technostress-Nudges.standalone.html

## [2026-11-24] ingest | Rhue2026-Local-Personalization
- 原始檔：raw/papers/Rhue2026-Local-Personalization.pdf（使用者提供的本機 PDF，EBSCO 下載）、raw/md/Rhue2026-Local-Personalization.md
- 新建：papers/Rhue2026-Local-Personalization、concepts/Personalization、concepts/Heuristics、concepts/Home-Bias、concepts/Rich-Get-Richer、concepts/Randomized-Experiments、questions/Unintended-Consequences-of-Nudges
- 更新：concepts/Digital-Nudging、concepts/Mediation-and-Moderation-Analysis、papers/Valta2026-Technostress-Nudges（互相連結）、index、overview
- 矛盾／待確認：Table 7 第 4 欄常數 42,4601 疑似排版錯誤；H3 只建立在 395 位捐款人上（agent 推論）

## [2026-11-24] ingest | Mertens2022-Nudging-Meta-Analysis、Jesse2021-Nudging-Recommender-Systems、Mathur2019-Dark-Patterns
- 來源：使用者同意後由 agent 下載；Mertens 取自日內瓦大學開放典藏（期刊正式版），Jesse 和 Mathur 取自 arXiv（含 BibTeX：raw/bib/）
- 挑選理由：和 Valta2026、Rhue2026 都有關聯的 nudging 論文（效果證據、推薦系統／個人化、倫理邊界）；Mills 2022 因找不到合法免費全文而未收錄
- 新建：3 篇論文頁；concepts/Choice-Architecture、concepts/Meta-Analysis、concepts/Recommender-Systems、concepts/Dark-Patterns；questions/Structure-vs-Information-Nudges
- 更新：concepts/Digital-Nudging、Heuristics、Personalization、Randomized-Experiments；questions/Unintended-Consequences-of-Nudges、Interface-Nudges-in-AI-Decision-Environments；papers/Valta2026、Rhue2026（互相連結）；index、overview
- 矛盾／待確認：Mertens「structure > information」vs Valta「default 和 salience 無差異」→ questions/Structure-vs-Information-Nudges；Mathur Table 1 的特徵符號在轉檔時遺失，只記錄內文明確的判斷

## [2026-11-24] lint | 收錄五篇後的健康檢查
- 26 頁；斷連結 0、孤兒頁 0、frontmatter 缺漏 0
- 單向連結 43 處 → 自動在目標頁的「反向連結」段落補上
- 待使用者注意：questions/Structure-vs-Information-Nudges（新矛盾）；所有新頁面 reviewed: false；Authors 仍無符合 2 篇以上的作者
