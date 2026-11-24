---
type: comparison
title: 5 篇論文怎麼看介面 nudge
domain: [IS, HCI, AI]
tags: [digital-nudging, comparison, synthesis]
created: 2026-11-24
updated: 2026-11-24
reviewed: false
---

# 5 篇論文怎麼看介面 nudge（綜合比較）

> Query 結果存檔：「把 5 篇放在一起看，介面 nudge 有多有效、在哪裡出現、有什麼代價？」這也是簡報 S15–S17 的依據。

## 比較表
| 論文 | 介入 | 類別（[[Choice-Architecture]]） | 結果變數 | 主要發現 |
|---|---|---|---|---|
| [[Valta2026-Technostress-Nudges]] | 預設選項、視覺突顯 | 結構、資訊 | 主觀壓力 | 兩者都降低壓力（d ≈ 0.63），彼此沒有差異 |
| [[Rhue2026-Local-Personalization]] | 推薦住家附近的 email | 資訊（🔍 推論） | 點擊、捐款、資金流向 | 點擊 +24%、捐款 +36%，但錢流向富裕社區 |
| [[Mertens2022-Nudging-Meta-Analysis]] | 455 個 nudge 效果量 | 三類都有 | 行為 | 整體 d = 0.45；結構 0.55 > 資訊 0.38 > 協助 0.31 |
| [[Jesse2021-Nudging-Recommender-Systems]] | 推薦系統中的 nudge | 四類（新增社會訴求） | 文獻回顧 | 87 種機制，推薦系統只研究過 18 種 |
| [[Mathur2019-Dark-Patterns]] | 購物網站的 dark patterns | 同樣的手法被用來圖利 | 盛行率 | 1,818 個，11.1% 網站，183 個有欺騙 |

## 綜合結論
1. **有效，但效果因類型和結果而異**：行為上「改變結構」最有效，但對主觀壓力，Valta 的實驗沒有看到差異 → [[Structure-vs-Information-Nudges]]。
2. **無所不在**：推薦系統本身就是 nudge，個人化讓 nudge 因人而異（Jesse、Rhue）。
3. **有代價**：可能造成分配不公（[[Rich-Get-Richer]]），或越界成為 [[Dark-Patterns]]。判斷原則：為誰的利益、資訊是否真實 → [[Unintended-Consequences-of-Nudges]]。

## 用途
- 簡報 `outputs/slides/Valta2026-Technostress-Nudges.html` 的 S15–S17（Graph 第二次執行，素材 F34–F43）
