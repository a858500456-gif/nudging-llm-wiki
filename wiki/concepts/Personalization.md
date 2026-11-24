---
type: concept
title: Personalization
domain: [IS, HCI]
tags: [personalization, targeting, recommender, platform-design]
created: 2026-11-24
updated: 2026-11-24
reviewed: false
---

# Personalization

> 依照使用者的行為或人口資料（例如過去紀錄、所在地），量身調整內容和推薦，以提高相關性和回應（[[Rhue2026-Local-Personalization]] p.3，引用 Zhang 2011、Xiao & Yue 2021）。

## 定義與符號
- **Engagement**：使用者和內容的互動，例如打開、點擊 email（[[Rhue2026-Local-Personalization]] p.3）。
- **Behavioral targeting**：用過去行為推測偏好，背後是 revealed preference（Samuelson 1948）的邏輯：過去做什麼，未來就會做什麼。
- **Attribute-based targeting**：用靜態屬性（例如住家位置）決定推薦內容。

## 直覺解釋
個人化不只是「推薦你可能喜歡的東西」，它也會**啟動特定的捷思**：推薦住家附近的專案，會喚起「幫助自己社區」的 [[Home-Bias|home bias]]，即使你以前沒有這種傾向（[[Rhue2026-Local-Personalization]]）。

## 演進脈絡
| 年份 | 論文 | 改了什麼 |
|---|---|---|
| 2026 | [[Rhue2026-Local-Personalization]] | 實地實驗顯示：靜態屬性（住家位置）的個人化勝過行為目標（捐款紀錄），但會造成 [[Rich-Get-Richer]] 的分配副作用 |

## 變體與比較
- Local personalization vs default personalization（推薦最近支持過的地區）：前者 click 提高 24%、donation 提高 36%（[[Rhue2026-Local-Personalization]] Table 4）。
- 效果會因使用者過去的捷思而不同：靠朋友推薦捐款的人只提高點擊，不提高捐款（[[Rhue2026-Local-Personalization]] Table 6）。

## 和 nudge 的關係
> [!note] 推論：個人化訊息透過「選擇呈現什麼」改變決策，但不限制選項、不給經濟誘因，符合 [[Digital-Nudging]] 的定義；差別在於它是**因人而異**的。nudge 研究和個人化研究在這裡交會。

## 風險
- 以捷思為基礎的個人化可能強化既有不平等（[[Rhue2026-Local-Personalization]] p.13）。
- 緩解方向：輪替或混合多種目標規則、加入公平性考量（[[Rhue2026-Local-Personalization]] p.13–14，引用 Gao et al. 2023）。

## 和推薦系統、nudge 文獻的連結
- 推薦系統的客製化資訊（customized information）就是一種 nudging 機制；文獻提出「smart nudges」：依使用者和情境個人化 nudge 本身（[[Jesse2021-Nudging-Recommender-Systems]] p.21，見 [[Recommender-Systems]]）。
- Mertens 提醒：針對個人差異設計的介入要注意倫理，避免傷害較易受影響的族群（[[Mertens2022-Nudging-Meta-Analysis]] p.8）。

## 在哪些論文中出現
- [[Rhue2026-Local-Personalization]]
- [[Jesse2021-Nudging-Recommender-Systems]]

## 開放問題
- [[Unintended-Consequences-of-Nudges]]
- 動態、演算法式的推薦系統，是否也會出現同樣的分配效應？（Rhue 的實驗是靜態規則）
