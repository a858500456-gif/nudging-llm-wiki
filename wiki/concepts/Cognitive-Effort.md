---
type: concept
title: Cognitive Effort
domain: [IS, HCI]
tags: [cognitive-effort, decision-making, cognitive-load]
created: 2026-11-24
updated: 2026-11-24
reviewed: false
---

# Cognitive Effort

> 使用者在介面中尋找、解讀、比較資訊時，主觀上感受到的心智負擔（[[Valta2026-Technostress-Nudges]] §3, p.5，引用 cognitive effort theory [40]）。

## 定義與符號
- **Perceived cognitive effort**：這裡指的是**主觀感受到的決策負擔**，不是區分 intrinsic／extraneous load 的 cognitive load 成分（[[Valta2026-Technostress-Nudges]] §4.2, p.8；§6.1.1, p.11）。

## 直覺解釋
資訊越分散、越模糊、要比較的屬性越多，就越吃力；越吃力，就越容易覺得系統在妨礙你，也就是 hindrance [[Technostress]]。

## 在因果鏈中的角色
$$\text{Interface nudge} \xrightarrow{\ a\ <\ 0\ } \text{Perceived cognitive effort} \xrightarrow{\ b\ >\ 0\ } \text{Hindrance technostressors}$$

- [[Valta2026-Technostress-Nudges]] §5.4：$a_{\text{default}} = -0.323$、$a_{\text{salience}} = -0.434$、$b = 0.504$，屬於 partial mediation（統計方法見 [[Mediation-and-Moderation-Analysis]]）

## 測量
7 題，改編自 Cooper-Martin (1994)、Heitmann et al. (2007)，例如 "I thought very hard about which rental car and insurance to pick."、"I had to make a decision based on complex information."（[[Valta2026-Technostress-Nudges]] Appendix Table 5，α = 0.711）

> [!warning] 測量上的限制
> 這份量表混合了「主動投入的程度」和「感受到的任務困難度」兩種概念，所以無法區分介面設計是**真的降低了認知需求**，還是**只改變了主觀感受**（[[Valta2026-Technostress-Nudges]] §6.3, p.13）。作者建議未來使用分開的量表，並搭配行為或生理的過程指標。

> [!note] 推論：量表裡有幾題（例如 "I was careful about..."、"I concentrated a lot..."）比較像在測「投入程度」而不是「負擔」。如果 nudge 讓人「比較不用心」，分數也會下降，所以這個構念的解讀要小心。

## 在哪些論文中出現
- [[Valta2026-Technostress-Nudges]]

## 開放問題
- 降低的是實際的認知負荷還是主觀感受？可以用眼動、反應時間、EDA 等過程指標區分。

## 反向連結
以下頁面連到本頁（lint 自動補上的雙向連結）：
- [[Interface-Nudges-in-AI-Decision-Environments]]
