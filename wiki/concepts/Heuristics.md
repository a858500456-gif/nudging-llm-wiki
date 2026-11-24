---
type: concept
title: Heuristics
domain: [IS, HCI, Theory]
tags: [heuristics, dual-process, decision-making, behavioral-economics]
created: 2026-11-24
updated: 2026-11-24
reviewed: false
---

# Heuristics（捷思）

> 簡化決策的心智捷徑：靠聯想或情緒線索快速判斷，而不是逐一分析所有選項（[[Rhue2026-Local-Personalization]] p.3，引用 Kahneman 2011）。

## 定義與符號
- **Dual-process theory**：System 1 快速、直覺；System 2 緩慢、深思。捷思屬於 System 1（[[Rhue2026-Local-Personalization]] p.3）。
- **Homophily（同質相吸）**：傾向和相似的人往來；地理接近、相似背景、社會連結都是「相似」的訊號，能提高信任、降低不確定性（[[Rhue2026-Local-Personalization]] p.3，引用 Kossinets & Watts 2006）。

## 直覺解釋
選項太多、資訊不完整時，人不會（也做不到）全部比較，而是抓一個好用的線索來決定：「這是我家附近的」「這是朋友推薦的」。

## 常見類型
| 捷思 | 說明 | 出處 |
|---|---|---|
| [[Home-Bias]] | 偏好支持在地的對象 | [[Rhue2026-Local-Personalization]] |
| Social influence | 偏好支持社會連結推薦的對象，以信任作為線索 | [[Rhue2026-Local-Personalization]] |
| 預設效應 | 沒有主動改變就接受預設選項（default-setting nudge 的基礎） | [[Valta2026-Technostress-Nudges]]、[[Digital-Nudging]] |

## 捷思的層級
- 人際信任（social influence）的影響似乎比地理接近更強；沒有強烈社會線索的人，更容易被地理框架影響（[[Rhue2026-Local-Personalization]] p.13）。

## 和 nudge 的關係
> [!note] 推論：nudge 的運作原理就是**利用或配合捷思**：預設選項利用「懶得改」，視覺突顯利用「注意力被顯眼的東西吸走」，local personalization 利用 home bias。所以 nudge 的效果和風險，都和捷思的性質綁在一起。

## 被拿來操弄的時候
- Dark patterns 利用 anchoring、bandwagon、default、framing、scarcity、sunk cost 等偏誤（[[Mathur2019-Dark-Patterns]] §3）。
- 文獻中提到 58 種和 nudge 有關的心理現象，但 87 種 nudging 機制中只有 22 種明確說明背後的理論（[[Jesse2021-Nudging-Recommender-Systems]] §4）。
- 高影響的決策（財務）比低影響、習慣性的決策（食物）更不受捷思影響（[[Mertens2022-Nudging-Meta-Analysis]] p.7–8）。

## 在哪些論文中出現
- [[Rhue2026-Local-Personalization]]
- [[Valta2026-Technostress-Nudges]]（以 choice architecture 的形式間接出現）
- [[Mertens2022-Nudging-Meta-Analysis]]
- [[Jesse2021-Nudging-Recommender-Systems]]
- [[Mathur2019-Dark-Patterns]]

## 開放問題
- 引導使用者用更深思的方式決策（System 2），能不能減少捷思帶來的不平等？（[[Rhue2026-Local-Personalization]] p.14 提出的未來方向）

## 反向連結
以下頁面連到本頁（lint 自動補上的雙向連結）：
- [[Choice-Architecture]]
- [[Dark-Patterns]]
