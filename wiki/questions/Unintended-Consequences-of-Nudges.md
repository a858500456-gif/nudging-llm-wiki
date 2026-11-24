---
type: question
title: Unintended consequences of nudges and personalization
domain: [IS, HCI]
tags: [digital-nudging, personalization, equity, ethics]
created: 2026-11-24
updated: 2026-11-24
reviewed: false
---

# Nudge 和個人化有哪些意外的副作用？

## 問題陳述
nudge 和個人化通常用「平均行為有沒有變好」來評估，但同一個介入可能同時帶來其他後果：資源分配不均、被引導到特定選項、讓人覺得被操弄。

## 各方說法
| 副作用 | 證據 | 出處 |
|---|---|---|
| 資源集中到富裕社區 | local personalization 提高捐款，但捐款流向收入較高的地區和學校 | [[Rhue2026-Local-Personalization]] H3 |
| 效果因人而異，部分人沒有效果 | 靠朋友推薦捐款的人，只提高點擊、不提高捐款 | [[Rhue2026-Local-Personalization]] H2b |
| 可能引發反感 | 任務簡單或已有明確偏好時，nudge 可能被視為不必要的操弄（reactance） | [[Valta2026-Technostress-Nudges]] §2.2 |
| 約 15% 的 nudge 可能適得其反 | meta-analysis 的預測區間 [−0.48, 1.39] | [[Mertens2022-Nudging-Meta-Analysis]] |
| 手法被拿來圖利、欺騙 | 11.1% 熱門購物網站有 dark pattern；183 個網站有假倒數、假庫存等欺騙 | [[Mathur2019-Dark-Patterns]] |
| 沒有人測過使用者是否覺得被操弄 | 推薦系統的 nudge 研究都沒測這一點 | [[Jesse2021-Nudging-Recommender-Systems]] p.21–22 |
| 高風險情境需要透明度 | 高責任決策中，nudge 要搭配解釋，避免被認為過度簡化或操弄 | [[Valta2026-Technostress-Nudges]] §6.2 |

> [!note] 推論：Valta 實驗中的 salience nudge 寫著「Lowest Total Price」，但三台車總價相同（見 [[Valta2026-Technostress-Nudges]] 的推論段落）；這種「降低壓力但給了不精確資訊」的設計，正好落在 nudge 和 dark pattern 的灰色地帶。

## 目前看法
已收錄的研究都顯示：小小的介面或訊息改變就能有效改變感受或行為（整體 d = 0.45，見 [[Mertens2022-Nudging-Meta-Analysis]]），但**有效不代表沒有代價**：可能分配不均、適得其反，或被拿來欺騙使用者。評估 nudge 時應該同時看：個人感受、行為、資源分配、使用者是否知情。

## 可以補讀的方向
- ✅ 已收錄：nudge 效果的 meta-analysis（[[Mertens2022-Nudging-Meta-Analysis]]）、dark patterns（[[Mathur2019-Dark-Patterns]]）、推薦系統中的 nudging（[[Jesse2021-Nudging-Recommender-Systems]]）
- 個人化 nudge（Mills 2022〈Personalized nudging〉，找不到合法免費全文，尚未收錄）
- 使用者對 nudge 和 dark pattern 的感受與自主感

## 反向連結
以下頁面連到本頁（lint 自動補上的雙向連結）：
- [[Dark-Patterns]]
- [[Digital-Nudging]]
- [[Personalization]]
- [[Rich-Get-Richer]]
