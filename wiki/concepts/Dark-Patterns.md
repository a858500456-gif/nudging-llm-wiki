---
type: concept
title: Dark Patterns
domain: [HCI, IS]
tags: [dark-patterns, manipulation, ethics, consumer-protection]
created: 2026-11-24
updated: 2026-11-24
reviewed: false
---

# Dark Patterns

> 讓線上服務獲利的介面設計：透過強迫、引導或欺騙，讓使用者做出在充分知情、可以自由選擇時不會做的決定（[[Mathur2019-Dark-Patterns]] p.2）。這個詞由 Brignull 在 2010 年提出。

## 和 nudge 的差別
| | Nudge | Dark pattern |
|---|---|---|
| 為誰的利益 | 使用者自己（libertarian paternalism） | 服務提供者 |
| 是否保留選擇自由 | 是 | 不一定（restrictive、forced action） |
| 是否誠實 | 是 | 常常不是（deceptive、hides information） |
| 手法 | 預設、突顯、社會規範、提醒… | **同樣的手法**：預設、突顯、社會證明、稀缺 |

- 嚴格來說，不為使用者著想的「nudge」就不算 nudge（[[Jesse2021-Nudging-Recommender-Systems]] p.4）；但 Jesse & Jannach 的機制目錄也收錄了 "using visuals to deceit" 這類機制，可見界線在文獻中並不一致。

> [!note] 推論：同一個技術（例如預設選項）放在不同目的下，可能是 nudge 也可能是 dark pattern。判斷時要看：受益者是誰、資訊是否真實、使用者是否還能輕鬆選別的、使用者事後知道了會不會反對。

## 分類（[[Mathur2019-Dark-Patterns]]）
- **特徵五面向**：asymmetric、covert、deceptive、hides information、restrictive
- **7 大類、15 種**：Sneaking、Urgency、Misdirection、Social Proof、Scarcity、Obstruction、Forced Action
- **最常見**：low-stock message（632 個實例）、countdown timer（393）、activity message（313）、confirmshaming（169）

## 利用的認知偏誤
anchoring、bandwagon、default effect、framing、scarcity、sunk cost（[[Mathur2019-Dark-Patterns]] §3）；都屬於 System 1 的捷思（見 [[Heuristics]]）。

## 盛行率與生態系
- 約 11.1% 的熱門購物網站至少有一個；越熱門的網站越常見；183 個網站有明確欺騙行為（例如假倒數計時、假庫存）；22 家第三方公司提供現成工具（[[Mathur2019-Dark-Patterns]]）。

## 法規
欺騙性做法在美國（FTC Act §5）、歐盟（Unfair Commercial Practices Directive）違法；Trick Questions、Visual Interference 取得的同意不符合 GDPR（[[Mathur2019-Dark-Patterns]] §6.2）。

## 在哪些論文中出現
- [[Mathur2019-Dark-Patterns]]
- [[Jesse2021-Nudging-Recommender-Systems]]（倫理討論）

## 開放問題
- [[Unintended-Consequences-of-Nudges]]
- 使用者實際上覺得哪些 dark pattern 最過分？對行為的影響有多大？（[[Mathur2019-Dark-Patterns]] 列為未來研究）
- 生成式 AI 介面中會出現哪些新型 dark pattern？（見 [[Interface-Nudges-in-AI-Decision-Environments]]）

## 反向連結
以下頁面連到本頁（lint 自動補上的雙向連結）：
- [[Choice-Architecture]]
- [[Digital-Nudging]]
