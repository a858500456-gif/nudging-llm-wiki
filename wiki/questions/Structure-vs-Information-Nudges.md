---
type: question
title: Are decision-structure nudges really stronger than information nudges?
domain: [IS, HCI]
tags: [choice-architecture, digital-nudging, contradiction]
created: 2026-11-24
updated: 2026-11-24
reviewed: false
---

# 改變選項結構的 nudge，真的比改變資訊呈現的 nudge 有效嗎？

## 問題陳述（矛盾）
- [[Mertens2022-Nudging-Meta-Analysis]]：跨 455 個效果量，decision structure（d = 0.55，其中 default d = 0.62）**一致**強於 decision information（d = 0.38）。
- [[Valta2026-Technostress-Nudges]]：default-setting（structure）和 salience-framing（information）降低壓力的效果**沒有顯著差異**（mean diff = 0.03, p = .87）；迴歸係數甚至是 salience 看起來較大（−0.580 vs −0.439，但未檢定）。

## 可能的解釋
| 解釋 | 說明 | 依據 |
|---|---|---|
| 結果變數不同 | Mertens 只看**行為**；Valta 看的是**主觀壓力**。default 改變行為很有效，但降低壓力不一定比讓資訊更清楚有效 | 兩篇的方法差異（agent 推論） |
| 介入的分類不純 | Valta 的 salience 組除了視覺突顯，還有「Lowest Total Price」標籤、TrustPilot 評分（社會證明），混合了 information 和 social reference | [[Valta2026-Technostress-Nudges]] Fig. 4（agent 推論） |
| 單一研究的統計力 | Valta 每組約 70 人，要檢測兩個 nudge 之間的小差異統計力不足 | [[Valta2026-Technostress-Nudges]] §5.2 的 95% CI [−0.33, 0.39] 很寬 |
| 情境 | Mertens 指出 information 類介入在高認知負荷下更容易失效，但 Valta 的任務正是高負荷，卻沒有看到差異 | [[Mertens2022-Nudging-Meta-Analysis]] p.7 |

## 目前看法
還無法下結論。兩篇在「結果變數」和「介入的純度」上都不同，不能算是正面衝突；比較合理的說法是：**行為改變上 structure 較強，對主觀感受的影響目前證據不足**。

## 可以補讀的方向
- 以主觀感受（壓力、滿意度、自主感）為結果變數的 nudge 研究或 meta-analysis
- 對 Mertens 的批評與再分析（Szaszi et al. 2022、Maier et al. 2022 PNAS letters，尚未收錄）
- 直接比較 default 和 salience 的大樣本實驗

## 反向連結
以下頁面連到本頁（lint 自動補上的雙向連結）：
- [[Choice-Architecture]]
- [[Digital-Nudging]]
