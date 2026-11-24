---
type: concept
title: Recommender Systems
domain: [AI, IS, HCI]
tags: [recommender-systems, personalization, digital-nudging]
created: 2026-11-24
updated: 2026-11-24
reviewed: false
---

# Recommender Systems（推薦系統）

> 自動篩選、排序要呈現給使用者的內容（商品、音樂、新聞），既是資訊過濾器，也會提供額外的相關建議（[[Jesse2021-Nudging-Recommender-Systems]] p.1）。

## 推薦就是一種 nudge
推薦系統決定哪些選項容易被看到，因此本身就構成了[[Choice-Architecture|選擇架構]]（[[Jesse2021-Nudging-Recommender-Systems]] p.1–2, Table 3）：
- 只呈現一部分選項 → **hiding**
- 排序 → **order effects**（positioning nudge）
- 依使用者客製 → **customized information**（見 [[Personalization]]）
- 「其他人也買了」→ **following the herd**、social influence
- 降低搜尋的力氣 → **change physical effort**、simplification

## 多重目標
- 推薦系統除了幫使用者找到喜歡的東西，也服務平台的目標（銷售、engagement）（[[Jesse2021-Nudging-Recommender-Systems]] p.1, p.5）。
- 可以在「照實推薦使用者喜歡的」之外，加上明確的 nudge 引導到「應該探索的」選項，例如在食譜推薦中突顯較健康的選項（p.3）。
- 若個人化推薦直接把某些選項過濾掉，就違反了選擇自由（p.5）。

## 實證摘要
- 推薦系統中研究過的 nudge 只有 18 種，最多的是 setting defaults 和 using visuals to increase salience；11 篇有測行為效果的研究中 8 篇有效（[[Jesse2021-Nudging-Recommender-Systems]] Table 4–5）。
- 靜態規則的個人化推薦（推薦住家附近）也會影響捐款流向，造成 [[Rich-Get-Richer]]（[[Rhue2026-Local-Personalization]]）。

## 在哪些論文中出現
- [[Jesse2021-Nudging-Recommender-Systems]]
- [[Rhue2026-Local-Personalization]]（個人化 email 推薦）

## 開放問題
- 個人化的 nudge（smart nudges）：依使用者和情境選擇 nudge 的種類和實作（[[Jesse2021-Nudging-Recommender-Systems]] p.21）
- 推薦系統中的 nudge 是否讓使用者覺得被操弄？目前沒有研究測過（同上 p.21–22）
- [[Interface-Nudges-in-AI-Decision-Environments]]

## 反向連結
以下頁面連到本頁（lint 自動補上的雙向連結）：
- [[Digital-Nudging]]
