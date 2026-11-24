---
type: concept
title: Randomized Experiments (Online & Field)
domain: [IS, Math]
tags: [research-method, experiment, causal-inference, ab-testing]
created: 2026-11-24
updated: 2026-11-24
reviewed: false
---

# Randomized Experiments（線上實驗與實地實驗）

> 把受試者隨機分到不同條件，讓條件之間唯一的系統性差異就是介入本身，因此可以推論因果。

## 兩種常見形式
| | 線上（情境）實驗 | 實地實驗（field experiment） |
|---|---|---|
| 情境 | 研究者設計的模擬任務 | 真實平台、真實行為 |
| 受試者知情 | 知道自己在做實驗 | 通常不知道 |
| 能測什麼 | 可以問卷測量感受、中介變數 | 主要是行為（點擊、購買、捐款） |
| 外部效度 | 較低 | 較高 |
| 例子 | [[Valta2026-Technostress-Nudges]]：MTurk 上的租車任務，N = 214 | [[Rhue2026-Local-Personalization]]：DonorsChoose 的 email，N = 159,941 |

## 關鍵步驟
- **Randomization check（平衡檢查）**：確認各組在介入前的特徵沒有差異（[[Rhue2026-Local-Personalization]] Table 3）。
- **分析**：隨機分派成功時，簡單的組間比較（t-test、ANOVA）就足以估計平均處理效果；再用迴歸加入交互作用看異質性（[[Rhue2026-Local-Personalization]] p.7；[[Valta2026-Technostress-Nudges]] §5.2）。
- **資料品質**：線上實驗常用注意力檢查、完成時間篩選（[[Valta2026-Technostress-Nudges]] Appendix Table 6）。

## 異質性分析
- 用調節變數看效果「對誰比較大」：Valta 用數位思維（[[Mediation-and-Moderation-Analysis]]），Rhue 用過去捐款距離和是否來自推薦。

> [!note] 推論：兩篇的設計剛好互補：Valta 能測到「為什麼有效」（中介：費腦程度），但情境是假的；Rhue 是真實行為和大樣本，但只能從行為推論心理機制。

## 實驗類型會影響效果嗎？
- Meta-analysis 中，實驗室、artifactual field、framed field、natural field 實驗的 nudge 效果沒有顯著差異（d 約 0.43–0.52）（[[Mertens2022-Nudging-Meta-Analysis]] Table 2），但作者也提到只看實地實驗的其他 meta-analysis 估計值較小。

## 在哪些論文中出現
- [[Valta2026-Technostress-Nudges]]
- [[Rhue2026-Local-Personalization]]
- [[Mertens2022-Nudging-Meta-Analysis]]（以隨機對照實驗作為納入條件）
