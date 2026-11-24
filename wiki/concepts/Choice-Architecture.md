---
type: concept
title: Choice Architecture
domain: [IS, HCI, Theory]
tags: [choice-architecture, nudge, taxonomy, behavioral-economics]
created: 2026-11-24
updated: 2026-11-24
reviewed: false
---

# Choice Architecture（選擇架構）

> 人們做決定時所處的環境（實體、社會、心理），以及這個環境的設計方式。調整選擇架構、在不限制選擇自由的前提下引導行為，就是 nudge（[[Mertens2022-Nudging-Meta-Analysis]] p.2–3；[[Jesse2021-Nudging-Recommender-Systems]] p.4，引用 Thaler & Sunstein 2008）。

## 定義與符號
- **Libertarian paternalism**：nudge 應該幫助人做出比沒有 nudge 時更好的決定，而且不強迫（[[Jesse2021-Nudging-Recommender-Systems]] p.4）。
- **Bounded rationality**：人的時間、資訊、計算能力有限，常即時用捷思建構偏好，所以會受到呈現方式影響。這是 choice architecture 能發揮作用的原因（[[Mertens2022-Nudging-Meta-Analysis]] p.3；見 [[Heuristics]]）。
- 介面沒有完全中立的呈現方式：任何設計都會產生某種順序和視覺份量（[[Jesse2021-Nudging-Recommender-Systems]] p.4）。

## 分類法
兩篇都延伸 Münscher et al. (2016) 的三分法：

| 大類 | 針對的心理障礙 | 技術（Mertens） | Jesse & Jannach 的子類 | 整體效果 d（Mertens） |
|---|---|---|---|---|
| Decision information | 取得資訊的能力有限 | translation、visibility、social reference | translate、**increase salience**、make visible、phrasing | 0.38 |
| Decision structure | 評估比較選項的能力有限 | **default**、effort、composition、consequence | 同左 | **0.55** |
| Decision assistance | 注意力和自我控制有限 | reminder、commitment | 同左 | 0.31 |
| Social decision appeal | （Jesse & Jannach 新增）社會與情感 | （Mertens 歸在 social reference） | messenger reputation、social reference、instigate empathy | — |

（[[Mertens2022-Nudging-Meta-Analysis]] Table 1–2；[[Jesse2021-Nudging-Recommender-Systems]] Figure 1）

## 已收錄研究在分類中的位置
| 研究中的介入 | 類別 | 出處 |
|---|---|---|
| 預設選項（租車） | Decision structure：default | [[Valta2026-Technostress-Nudges]] |
| 視覺突顯（租車） | Decision information：visibility／increase salience | [[Valta2026-Technostress-Nudges]] |
| 推薦住家附近的專案（email） | Decision information：translation／customized information（提高個人切身性） | [[Rhue2026-Local-Personalization]]（agent 推論） |
| 推薦系統的排序、過濾 | Decision structure（order effects、hiding）＋decision information（customized） | [[Jesse2021-Nudging-Recommender-Systems]] Table 3 |
| Dark patterns：最貴的設為預設、假倒數、假庫存 | 同樣的手法被用來圖利網站 | [[Mathur2019-Dark-Patterns]] |

## 為什麼 structure 比較有效（Mertens 的解釋，作者自稱推測性）
1. 對資訊處理的要求較低：提供捷徑，不需要逐一評估。
2. 比較不受個人價值、目標的差異影響。
相對地，information 和 assistance 類介入在高認知負荷、時間壓力下更容易失效（[[Mertens2022-Nudging-Meta-Analysis]] p.7）。

> [!warning] 和個別研究不一致：[[Valta2026-Technostress-Nudges]] 中，default（structure）和 salience（information）降低壓力的效果沒有顯著差異。見 [[Structure-vs-Information-Nudges]]。

## 在哪些論文中出現
- [[Mertens2022-Nudging-Meta-Analysis]]
- [[Jesse2021-Nudging-Recommender-Systems]]
- [[Valta2026-Technostress-Nudges]]
- [[Mathur2019-Dark-Patterns]]

## 開放問題
- [[Structure-vs-Information-Nudges]]
- 同樣的選擇架構手法，什麼時候是 nudge、什麼時候是 [[Dark-Patterns|dark pattern]]？

## 反向連結
以下頁面連到本頁（lint 自動補上的雙向連結）：
- [[Digital-Nudging]]
- [[Recommender-Systems]]
