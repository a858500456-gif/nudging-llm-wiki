---
type: paper
title: "Designing away technostress: Digital interface nudges, cognitive effort, and digital mindset in complex decision environments"
domain: [IS, HCI]
tags: [technostress, digital-nudging, interface-design, cognitive-effort, digital-mindset, online-experiment]
created: 2026-11-24
updated: 2026-11-24
reviewed: false
authors: [Maximilian Valta, Christian Maier, Yannick Hildebrandt]
year: 2026
venue: Information & Management 63 (2026) 104421
arxiv: ""
doi: "10.1016/j.im.2026.104421"
source: "[[raw/papers/Valta2026-Technostress-Nudges.pdf]]"
status: full
---

# Designing away technostress: Digital interface nudges, cognitive effort, and digital mindset in complex decision environments

> 一句話總結：在一個刻意設計得很混亂的租車決策介面上，加入 **Default-Setting** 或 **Salience-Framing** 兩種 [[Digital-Nudging|digital interface nudge]]，就能降低使用者感受到的 hindrance [[Technostress]]，部分是透過降低 [[Cognitive-Effort|perceived cognitive effort]] 達成；而 [[Digital-Mindset]] 越高的人，降幅越大。重點在於：任務本身的客觀複雜度沒有被移除，只是改變了複雜度「被呈現與處理」的方式。

- 作者：Maximilian Valta、Christian Maier（University of Bamberg，Chair of IS, Health and Society in the Digital Age）、Yannick Hildebrandt（University of Bamberg，Chair of IS Management）
- 期刊：*Information & Management*，2026，Open Access（CC BY）
- 收稿 2025-10-31，接受 2026-08-21

## 研究問題 (Problem)

- Technostress 研究已經承認「IS 設計」是可以用來緩解壓力的手段，但**沒有具體指出是哪些介面層級的機制**，可以在互動當下改變使用者的壓力評估（[[Valta2026-Technostress-Nudges]] §1, p.1）。
- 既有的設計導向研究不是停留在概念層次（「介面要更簡單」），就是主張大幅重新設計（簡化介面、刪減功能）。這些做法隱含「要降低 technostress 就必須移除複雜度」的假設，沒有解釋**如何在介面中重新組織複雜度**（§1, p.1）。
- 背景數據：線上交易的放棄率接近 70%，每年約造成 2,600 億美元的營收損失（§1, p.1，引用 Baymard Institute 2024）。
- **Research Question**：digital interface nudging 原則如何影響使用者在複雜數位決策任務中感受到的 hindrance technostressors？digital mindset 又如何影響這個關係？（§1, p.2）

## 核心方法 (Method)

### 研究模型與假設
研究模型見 Fig. 2（p.5）。自變數是兩種 nudge（各自和控制組比較），中介變數是 perceived cognitive effort，調節變數是 digital mindset（second-order construct，由四個 thinking pattern 反映），依變數是 perceived hindrance technostressors（HTS）。

| 假設 | 內容 | 結果 |
|---|---|---|
| H1 | Default-setting nudge 降低 perceived HTS | 支持 |
| H2 | Salience-framing nudge 降低 perceived HTS | 支持 |
| H3a | Digital mindset 調節 default-setting → HTS（mindset 越高，HTS 降得越多） | 支持 |
| H3b | Digital mindset 調節 salience-framing → HTS | 支持 |
| H4a | Cognitive effort 中介 default-setting → HTS | 支持（partial mediation） |
| H4b | Cognitive effort 中介 salience-framing → HTS | 支持（partial mediation） |

（§3, p.5–6；§5, p.9–10）

**兩種 nudge 在理論上的差異**（§2.2, p.3；§3, p.6）：
- **Default-setting**：預先選好一個選項，使用者可以改，用「簡化選擇 (choice simplification)」來降低 effort。
- **Salience-framing**：用視覺提示（icon、版面、顏色）讓和任務相關的資訊更顯眼，用「引導注意力 (attentional guidance)」來降低 effort，不改變選項集合。這裡指的是**介面層級的視覺突顯**，不是 gain-loss 那類 message framing。

**為什麼 mindset 高的人效果更大**（作者的論證，§3, p.6）：mindset 高的人會看到更大的 problem-solution space，想比較更多選項和資料，所以實際面對的複雜度更高。nudge 幫他們刪減掉的複雜度也就更多。

### 實驗流程（Fig. 3, p.7）
1. **Pre-experiment**：訪談 12 人（6 女 6 男，23–64 歲），找出租車網站中引發 hindrance technostress 的因素：IS 設計不清楚、保險條款與費用不明、任務指示不清、單頁資訊量過大、add-on 選項太複雜（§4.1, p.6）。
2. **Stress validation**（12 人）：
   - 客觀指標：用 MentalBioScreen K3 量測皮膚電導 (skin conductance, EDA)。實驗中平均 10.64 µS，填問卷時 6.46 µS，在沒有刻意加入壓力源的對照網站上 8.99 µS。
   - 主觀指標：perceived stress 在實驗中為 4.77，在對照網站為 3.74（§4.1, p.6–7）。
3. **主實驗**（線上，三組 between-subjects 隨機分派）：
   - 情境：扮演員工，替主管預訂一趟 10 天、每天約 200 英里、異地還車、需要全險的商務租車，主管事後會檢查選擇是否恰當（模擬 accountability）。
   - 從 3 台車 × 3 種保險中各選一個，需要同時考慮 6 個屬性。資訊刻意寫得混亂：附加費用是否適用不明確、年齡限制前後不一致、里程上限和超額費用不同。
   - **三台車在考慮全部 6 個屬性後總價相同 → 沒有客觀上的正確答案**。實驗目的不是操弄使用者選哪台車，而是看壓力感受（§4.2, p.7）。
   - 兩種 nudge 分開測試（不組合），以確保 internal validity（§4.2, p.7）。
   - Nudge 依照 digital nudge design method（analysis → design → implementation & evaluation）設計（§4.2, p.7）。

| 條件 | 操弄方式 | N |
|---|---|---|
| Default-setting nudge | 預選其中一個選項 | 70 |
| Salience-framing nudge | 用「Lowest Total Price」「Great Deal」標籤、TrustPilot 評分等視覺提示突顯其中一個選項 | 73 |
| Control | 只有基本的文字和圖片 | 71 |

（Table 2, Fig. 4, p.8）

### 測量
- Hindrance technostressors：14 題（Maier et al. 2021），α = 0.931
- Digital mindset：14 題（Hildebrandt & Beimborn 2024），α = 0.734，四個維度見 [[Digital-Mindset]]
- Perceived cognitive effort：7 題，改編自 Cooper-Martin 1994、Heitmann et al. 2007，α = 0.711
- 全部採 7-point Likert 量表（Appendix Table 5, p.13–14；§4.2, p.8）

### 樣本與資料清理（Appendix Table 6, p.14）
MTurk，approval rate ≥ 95%：

| 篩選步驟 | 排除 | 剩下 |
|---|---|---|
| 初始回覆 | — | 655 |
| 沒通過 4 題 attention check 中的任一題 | 233 | 422 |
| 完成時間 < 3 分鐘 | 163 | 259 |
| 作答變異太小（SD < 0.80）或有固定作答模式 | 39 | 220 |
| 離群值 | 6 | **214** |

- 樣本：平均年齡 35.75 歲（SD 11.55），女性 49.5%，58.4% 有學士學位，每天平均使用 IT 6.36 小時（Table 3, p.8）。
- GPower 3.1：N ≈ 150、medium effect size 時 power > 0.8（§4.2, p.8）。

### 分析方法
- SEM（IBM SPSS Amos 28）＋ one-way ANOVA（SPSS 28.0）（§5, p.8）
- 中介：5000 次 bootstrap、bias-corrected CI（§5.4, p.10）
- 調節：digital mindset 先做 mean-centering，再用 simple slope 分析 ±1 SD（§5.3, p.10）
- 統計方法說明見 [[Mediation-and-Moderation-Analysis]]

## 實驗與結果 (Experiments)

### 測量模型
- 所有 loading > 0.707；CR > 0.7、AVE > 0.5；RMSEA = 0.04、CFI = 0.95、TLI = 0.93（§5.1, p.8–9）
- Digital mindset 四個一階維度對二階因素的 loading 介於 0.787–0.882（Fig. 5, p.9）
- Common method bias：用 common latent factor 檢驗，loading 的差異都 < 0.20（§5.1, p.9）

### H1、H2：直接效果（§5.2, p.9–10）
One-way ANOVA：$F(2, 211) = 8.57,\ p < 0.001$

| 條件 | HTS 平均 (SD) | Cohen's d（相對控制組） |
|---|---|---|
| Default-setting | 4.87 (1.03) | −0.63 |
| Salience-framing | 4.84 (1.15) | −0.62 |
| Control | 5.47 (0.87) | — |

- 兩種 nudge 之間**沒有顯著差異**（mean diff = 0.03, p = 0.87, 95% CI [−0.33, 0.39]）。
- 迴歸的 total effect $c$：default-setting $\beta = -0.439$（p < .01）、salience-framing $\beta = -0.580$（p < .001）。作者強調，salience 的係數看起來比較大，但**沒有正式檢定哪一個比較好**（§5.2, p.10）。

### H3：Digital mindset 的調節效果（§5.3, p.10；Fig. 6）
- 交互作用項：default × mindset $\beta = -0.278$（p < .01）、salience × mindset $\beta = -0.307$（p < .01）

| Simple slope | Low mindset (−1 SD) | High mindset (+1 SD) |
|---|---|---|
| Default-setting → HTS | $\beta = -0.195$, p = .041 | $\beta = -0.515$, p < .001 |
| Salience-framing → HTS | $\beta = -0.260$, p = .012 | $\beta = -0.645$, p < .001 |

- **mindset 低的人也有顯著效果**，只是幅度比較小。所以 mindset 影響的是「效果有多大」，不是「有沒有效果」。
- 探索性的事後分析（Appendix Table 8, p.14–15）：調節效果主要來自 **generative**（default: −0.238, p = .039；salience: −0.336, p = .016）和 **combinatorial**（−0.270, p = .028；−0.252, p = .048）。**data-driven** 和 **risk-affine** 都不顯著。

### H4：Cognitive effort 的中介效果（§5.4, p.10；Table 4, p.11）
- a-path：default → effort $\beta = -0.323$、salience → effort $\beta = -0.434$（均為 p < .01）
- b-path：effort → HTS $\beta = 0.504$（p < .01）

| | Total effect $c$ | Direct effect $c'$ | Indirect effect $ab$（95% CI） |
|---|---|---|---|
| Default-setting | −0.439** | −0.276** | −0.163 [−0.23, −0.05] |
| Salience-framing | −0.580*** | −0.361** | −0.219 [−0.29, −0.08] |

→ **Partial mediation**：nudge 一部分直接降低 HTS，一部分透過降低 cognitive effort 間接降低 HTS。

> [!note] 推論：用 Fig. 5 的數字驗算，$a \times b$：$-0.323 \times 0.504 \approx -0.163$、$-0.434 \times 0.504 \approx -0.219$，和表中的 indirect effect 一致；$c' + ab$：$-0.276 + (-0.163) = -0.439$、$-0.361 + (-0.219) = -0.580$，也和 total effect 一致。

### Sensitivity analysis（§5.1, p.9；Appendix Tables 9–10, p.15）
擔心「操弄—中介—結果」三者的題目在概念上重疊（HTS 量表裡有「資訊不清楚」「資訊太多」這類題目），所以拿掉這些題目，剩 6 題（α = 0.823, CR = 0.866, AVE = 0.519）重新分析。效果的模式不變，只是變小了：

| | $c$ | $c'$ | $ab$（95% CI） |
|---|---|---|---|
| Default-setting | −0.291** | −0.184* | −0.107 [−0.17, −0.03] |
| Salience-framing | −0.387*** | −0.241** | −0.146 [−0.21, −0.05] |

### 敘述統計（Appendix Table 7, p.14）
HTS 平均 5.06（SD 1.06），cognitive effort 平均 5.30（1.23）；digital mindset 四個維度的平均落在 5.45–5.58。HTS 和 cognitive effort 的相關 r = 0.569。

## 貢獻 (Contributions)
1. **Technostress 研究**：把「IS 設計」具體化成一個可以改變的介面層級機制，回應 Tarafdar et al. (2019) 所說的 "appropriate IS design"。壓力不只取決於複雜度本身，也取決於**複雜度如何透過介面被遇到** (how complexity is encountered)（§6.1.1, p.11）。
2. **Digital nudging 研究**：把結果變數從行為（選了什麼、有沒有採用）擴展到**知覺層面的壓力**（如何經驗這次選擇），從 "what users choose" 延伸到 "how users experience choice under complexity"（§6.1.2, p.11）。
3. **Digital mindset**：首次提供證據，顯示 digital mindset 是一個 user-level scope condition（§6.1.3, p.11–12）。

## 限制 (Limitations)
作者自己承認的限制（§6.3, p.12–13）：
- 兩種 nudge 分開測試，沒有檢驗組合起來的效果（additive／synergistic／conflicting），建議未來用 factorial design。
- 主實驗只用主觀量表；生理指標（EDA）只在 pretest 使用。
- Cognitive effort 量表混合了「主動投入的程度」和「感受到的困難度」，無法區分 nudge 是真的降低了認知需求，還是只改變了主觀感受。
- 只有單一、一次性的租車任務；長期反覆使用可能出現 habituation（習慣化），需要 longitudinal 和 field study。
- MTurk 樣本無法代表組織中的使用者，選擇也沒有真實的金錢或組織後果，ecological validity 有限。
- Digital mindset 之外的特質（personal innovativeness with IT、computer self-efficacy）還沒有比較。
- 作者也承認：無法區分 cognitive effort 來自任務複雜度、資訊特性，還是介面的處理負擔（§6.1.1, p.11）。

> [!note] 推論：agent 觀察到、但論文沒有特別討論的地方
> - **資料清理的排除率約 67%**（655 → 214），其中「完成時間 < 3 分鐘」就排除了 163 人。這樣的排除比例在 MTurk 研究中不算罕見，但留下來的可能是比較認真、投入的受試者，會影響外推性。
> - **Digital mindset 和 HTS 呈正相關**（四個維度 r = 0.218–0.430，Table 7）：mindset 越高的人，整體感受到的 hindrance 越高。這和作者「mindset 高的人看到更大的決策空間 → 更複雜」的論證一致，但論文沒有直接討論這個主效果。
> - **Salience-framing 的操弄內容不只是視覺突顯**：Fig. 4 中包含 "Lowest Total Price"、"Great Deal" 標籤和 TrustPilot 評分，等於也提供了 social proof 和價格資訊。這和作者定義的「純介面層級 salience，不是 message framing」之間可能有落差，而且三台車的總價其實相同，「Lowest Total Price」這個標籤在事實上值得商榷。
> - 兩種 nudge 都只突顯或預選「某一個」選項，所以「降低壓力」和「被引導到特定選項」可能混在一起，論文沒有報告各組最後選了哪台車。

## 與其他論文的關係
- 基於（尚未收錄）：Maier et al. 2021（challenge/hindrance stressors 量表，JAIS）、Tarafdar et al. 2019（technostress trifecta，ISJ）、Ragu-Nathan et al. 2008、Weinmann et al. 2016 和 Mirsch et al. 2017（digital nudging）、Hildebrandt & Beimborn 2024（digital mindset 量表）
- 被後續工作沿用：_尚無_
- 相關（同為小幅介面／訊息改變影響決策）：[[Rhue2026-Local-Personalization]]，Valta 看個人壓力感受、Rhue 看行為與資源分配
- 效果量對照：[[Mertens2022-Nudging-Meta-Analysis]]（default d = 0.62 最強；但本研究 default 和 salience 沒有差異 → [[Structure-vs-Information-Nudges]]）
- 本研究的兩種 nudge 是推薦系統中最常研究的兩種機制：[[Jesse2021-Nudging-Recommender-Systems]]
- 「Lowest Total Price」標籤的問題可用 dark pattern 的 deceptive 特徵檢視：[[Mathur2019-Dark-Patterns]]
- 開放問題：[[Who-Benefits-More-From-Interface-Nudges]]、[[Interface-Nudges-in-AI-Decision-Environments]]、[[Unintended-Consequences-of-Nudges]]

## 相關概念
[[Technostress]]、[[Digital-Nudging]]、[[Cognitive-Effort]]、[[Digital-Mindset]]、[[Mediation-and-Moderation-Analysis]]

## 反向連結
以下頁面連到本頁（lint 自動補上的雙向連結）：
- [[Choice-Architecture]]
- [[Heuristics]]
- [[Meta-Analysis]]
- [[Randomized-Experiments]]
