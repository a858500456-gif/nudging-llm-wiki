---
type: concept
title: Mediation and Moderation Analysis
domain: [Math, IS]
tags: [statistics, mediation, moderation, sem, research-method]
created: 2026-11-24
updated: 2026-11-24
reviewed: false
---

# Mediation and Moderation Analysis

> **中介 (Mediation)** 回答「X 透過什麼影響 Y」，**調節 (Moderation)** 回答「X 對 Y 的效果在什麼條件下比較強或比較弱」。這是 IS 和行為研究中最常見的兩種機制分析。

## 定義與符號
- $X$：自變數（例如實驗操弄，用 dummy 編碼：處理組 = 1，控制組 = 0）
- $M$：中介變數
- $W$：調節變數
- $Y$：依變數

## 數學形式

### 中介（簡單中介模型）
$$
\begin{aligned}
Y &= i_1 + c\,X + \varepsilon_1 && \text{(total effect } c\text{)}\\
M &= i_2 + a\,X + \varepsilon_2 && (a\text{-path})\\
Y &= i_3 + c'\,X + b\,M + \varepsilon_3 && (\text{direct effect } c',\ b\text{-path})
\end{aligned}
$$
- **Indirect effect** $= a \times b$；在 OLS 線性模型中，$c = c' + ab$
- **顯著性檢定**：$ab$ 的抽樣分配不是常態，所以用 **bootstrap**（例如重抽 5000 次）建立信賴區間，**CI 不包含 0 就算顯著**。
- **Full mediation**：$ab$ 顯著，且 $c'$ 不顯著；**Partial mediation**：$ab$ 和 $c'$ 都顯著。

### 調節（交互作用）
$$Y = i + b_1 X + b_2 W + b_3 (X \times W) + \varepsilon$$
- $b_3$ 顯著，代表 $X$ 的效果會隨著 $W$ 改變。$X$ 的條件效果為 $\theta_{X \to Y}(W) = b_1 + b_3 W$。
- **Mean-centering**：先把 $W$ 減去平均值，讓 $b_1$ 的意思變成「$W$ 在平均水準時 $X$ 的效果」，也可以減少 $X$ 和 $X \times W$ 的共線性。
- **Simple slope 分析**：把 $W = \bar W \pm 1\,SD$ 代入，分別看 $X$ 的效果。

## 實例
[[Valta2026-Technostress-Nudges]] 同時使用兩種分析：
- 中介：$X$ = nudge、$M$ = [[Cognitive-Effort|perceived cognitive effort]]、$Y$ = hindrance [[Technostress]]。default-setting：$a = -0.323,\ b = 0.504,\ ab = -0.163$，95% CI [−0.23, −0.05]，$c' = -0.276$ → partial mediation。
- 調節：$W$ = [[Digital-Mindset]]（先 mean-centering），simple slope ±1 SD：default-setting 在 low mindset 時 $-0.195$、在 high mindset 時 $-0.515$。

## 相關的檢驗
- **Common method bias (CMB)**：當自變數和依變數都來自同一份自陳問卷時可能產生的偏誤。可以用程序上的補救（例如實驗操弄、分開測量），或統計檢驗（common latent factor：loading 的差異 < 0.20）處理（[[Valta2026-Technostress-Nudges]] §5.1）。
- **Measurement model 的常用門檻**：loading > 0.707、CR > 0.7、AVE > 0.5、RMSEA < 0.06、CFI > 0.95（[[Valta2026-Technostress-Nudges]] §5.1 使用的標準；RMSEA 和 CFI 的門檻是一般慣例，原文只寫 "established guidelines"）

## 在哪些論文中出現
- [[Valta2026-Technostress-Nudges]]
- 另見 [[Randomized-Experiments]]（實驗設計與異質性分析）

## 開放問題
- 實驗中，$M$ 和 $Y$ 都是自陳量表，而且是同時測量的，中介的因果推論有限，需要時間上的分隔或直接操弄 $M$。
