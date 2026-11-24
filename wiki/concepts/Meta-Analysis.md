---
type: concept
title: Meta-Analysis
domain: [Math, Theory]
tags: [statistics, meta-analysis, effect-size, publication-bias, research-method]
created: 2026-11-24
updated: 2026-11-24
reviewed: false
---

# Meta-Analysis（統合分析）

> 把許多研究的效果量合併，估計整體效果、效果的變異，以及什麼因素會調節效果。

## 定義與符號
- **效果量 Cohen's d**：兩組平均差除以合併標準差
$$d = \frac{\bar X_T - \bar X_C}{s_p},\qquad s_p = \sqrt{\frac{(n_T-1)s_T^2 + (n_C-1)s_C^2}{n_T+n_C-2}}$$
  慣例：0.2 小、0.5 中、0.8 大。
- **Random-effects model**：假設每個研究的真實效果 $\theta_i$ 本身就不同
$$y_i = \theta_i + \varepsilon_i,\quad \theta_i \sim \mathcal N(\mu, \tau^2),\quad \varepsilon_i \sim \mathcal N(0, v_i)$$
  $\mu$ 是平均效果，$\tau^2$ 是研究間的真實變異。
- **三層次模型**：同一篇論文的多個效果量彼此相關，所以分成「效果量 ⊂ 研究」兩層隨機效果（[[Mertens2022-Nudging-Meta-Analysis]]）。
- **異質性 $I^2$**：總變異中有多少比例是真實差異，而不是抽樣誤差。
- **預測區間**：下一個新研究的真實效果可能落在哪裡，大約是 $\mu \pm 1.96\sqrt{\tau^2 + SE(\hat\mu)^2}$；它比信賴區間寬得多。

## 發表偏誤（Publication bias）
- **Funnel plot**：效果量對標準誤作圖；沒有偏誤時應該左右對稱。
- **Egger's test**：迴歸效果量和標準誤，斜率顯著代表小樣本研究偏向報告大效果。
- **敏感度分析**：假設不同程度的偏誤，看估計值會降多少。

## 實例
[[Mertens2022-Nudging-Meta-Analysis]]：
- 455 個效果量、214 篇、N = 2,149,683；整體 $d = 0.45$ [0.39, 0.52]
- $\tau^2 = 0.23$、$I^2 = 99.67\%$；預測區間 [−0.48, 1.39] → 約 15% 的介入可能適得其反
- Egger's test b = 2.28；中度偏誤假設下 d 降到 0.31，嚴重偏誤假設下降到 0.03

> [!note] 推論：$I^2$ 接近 100% 時，「平均效果 d = 0.45」本身的意義有限。更重要的訊息是：nudge 的效果高度取決於技術、領域和情境，平均值無法預測個別介入會不會有效。

## 和單一實驗的關係
- 單一實驗的效果量（例如 [[Valta2026-Technostress-Nudges]] 的 d = −0.63）可以和 meta-analysis 的分布對照，判斷它算大還是小。
- 但 meta-analysis 的結果變數多是**行為**，Valta 的結果變數是**主觀壓力**，不能直接比較（agent 推論）。

## 在哪些論文中出現
- [[Mertens2022-Nudging-Meta-Analysis]]

## 開放問題
- 發表偏誤到底多嚴重？Mertens 的敏感度分析範圍很大（d 從 0.31 到 0.03），批評者認為偏誤更嚴重（未收錄）。
