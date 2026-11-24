---
type: paper
title: "The effectiveness of nudging: A meta-analysis of choice architecture interventions across behavioral domains"
domain: [IS, HCI, Theory]
tags: [nudge, choice-architecture, meta-analysis, behavior-change, publication-bias]
created: 2026-11-24
updated: 2026-11-24
reviewed: false
authors: [Stephanie Mertens, Mario Herberz, Ulf J. J. Hahnel, Tobias Brosch]
year: 2022
venue: PNAS 119(1), e2107346118
arxiv: ""
doi: "10.1073/pnas.2107346118"
source: "[[raw/papers/Mertens2022-Nudging-Meta-Analysis.pdf]]"
status: full
---

# The effectiveness of nudging: A meta-analysis of choice architecture interventions across behavioral domains

> 一句話總結：匯整 214 篇研究、455 個效果量、約 215 萬名受試者，[[Choice-Architecture|choice architecture]]（nudge）整體能改變行為，效果小到中等（Cohen's d = 0.45）；其中**改變選項結構**（例如預設選項）的效果最強，**食物**領域最容易被影響、**財務**領域最難；但文獻有發表偏誤，真實效果可能更小。

- 作者：University of Geneva（Swiss Center for Affective Sciences、心理系）
- 期刊：*PNAS* 119(1)，2022（2021-12-30 線上刊出），CC BY-NC-ND 開放取用
- 原始檔取自日內瓦大學開放典藏的期刊正式版

## 研究問題 (Problem)
過去的 meta-analysis 多半只看單一技術或單一領域，所以不知道（[[Mertens2022-Nudging-Meta-Analysis]] p.3）：
1. 某些 choice architecture 技術是否比其他技術更有效？
2. 某些行為領域是否更容易被影響？
3. 技術的效果是否因領域而不同？
4. 效果是否受地點、對象等情境因素影響？

## 核心方法 (Method)

### 理論框架：三種心理障礙 → 三類介入（Table 1, p.4；依 Münscher et al. 的分類）
| 心理障礙 | 介入類別 | 技術 |
|---|---|---|
| 取得決策資訊的能力有限 | **Decision information**：讓資訊更容易取得、理解、更切身 | translation（轉換或重新框架資訊）、visibility（讓資訊看得見，例如營養標示）、social reference（社會規範資訊） |
| 評估和比較選項的能力有限 | **Decision structure**：改變選項的安排或決策形式 | default（預設選項）、effort（調整選擇的費力程度）、composition（選項的範圍或分組）、consequence（小額誘因或社會後果） |
| 注意力和自我控制有限 | **Decision assistance**：協助自我調節 | reminder（提醒）、commitment（承諾機制） |

詳見 [[Choice-Architecture]]。

### 文獻蒐集與納入條件（p.9–10）
- 資料庫：PsycINFO、PubMed、PubPsych、ScienceDirect，關鍵字 nudge OR "choice architecture" × 實證研究詞；另外找回顧文章的參考文獻、政府行為科學單位的報告，以及未發表研究（ProQuest 論文、學術郵件清單）。搜尋到 2019 年 6 月為止，共 9,606 篇。
- 納入條件：隨機對照實驗、行為結果（真實或假設情境）、以個人為分析單位、英文發表；**排除和經濟誘因、教育計畫等其他介入合併的研究**。
- 最後樣本：214 篇、455 個效果量、N = 2,149,683（單篇 N 從 14 到 813,990）。資料和程式碼公開在 OSF。

### 分析（詳見 [[Meta-Analysis]]）
- 效果量：Cohen's d，正值代表往介入期望的方向改變。
- 三層次 meta-analytic model（效果量嵌套在研究中），再用 mixed-effects 模型檢驗調節變數。
- 異質性：$\tau^2$、$I^2$；發表偏誤：funnel plot、Egger's test、加權函數的敏感度分析。

## 實驗與結果 (Experiments)

### 整體效果（p.4–5）
- **d = 0.45**, 95% CI [0.39, 0.52], t(340) = 14.38, p < .001，屬於小到中等效果。
- 移除離群值後 d = 0.42 [0.37, 0.46]；leave-one-out 的 d 介於 0.43–0.46。
- 異質性非常高：$\tau^2 = 0.23$、$I^2 = 99.67\%$；個別效果量從 −0.69 到 4.69。
- 95% 預測區間 [−0.48, 1.39] → **約 15% 的介入可能會適得其反**（backfire）。

### 發表偏誤（p.5）
- Egger's test：效果量和標準誤正相關（b = 2.28, 95% CI [1.31, 3.25], p < .001）→ 小樣本研究偏向報告正面結果。
- 假設中度偏誤：d 從 0.42 降到 **0.31**（降幅 26.79%）；假設嚴重偏誤：降到 **0.03**（但 funnel plot 只部分支持這個假設）。
- 作者結論：整體結論不變，但真實效果可能比估計的小。

### 依類別與技術（Table 2, Fig. 4）
| 類別／技術 | k | d | 95% CI |
|---|---|---|---|
| **Decision information** | 130 | 0.38 | [0.29, 0.47] |
| · Translation | 50 | 0.31 | [0.18, 0.43] |
| · Visibility | 31 | 0.36 | [0.26, 0.45] |
| · Social reference | 49 | 0.40 | [0.29, 0.51] |
| **Decision structure** | 227 | **0.55** | [0.45, 0.64] |
| · Default | 132 | **0.62** | [0.50, 0.73] |
| · Effort | 23 | 0.43 | [0.19, 0.67] |
| · Composition | 53 | 0.55 | [0.22, 0.88] |
| · Consequence | 19 | 0.43 | [0.29, 0.58] |
| **Decision assistance** | 98 | 0.31 | [0.23, 0.39] |
| · Reminder | 69 | 0.30 | [0.20, 0.39] |
| · Commitment | 29 | 0.30 | [0.13, 0.46] |

- Structure > information（b = 0.17, p = .02）；structure > assistance（b = 0.24, p < .001）；information 和 assistance 沒有差異（p = .25）。
- 這個「structure 最強」的模式在每個領域都成立（structure 的 d 介於 0.33–0.86）。

### 依行為領域（Table 2, Fig. 5）
| 領域 | k | d | 95% CI |
|---|---|---|---|
| Food | 111 | **0.72** | [0.49, 0.95] |
| Prosocial | 66 | 0.44 | [0.29, 0.59] |
| Environment | 76 | 0.43 | [0.32, 0.54] |
| Health | 84 | 0.34 | [0.22, 0.45] |
| Other | 73 | 0.29 | [0.05, 0.54] |
| Finance | 45 | **0.25** | [0.12, 0.37] |

### 情境因素（Table 2, p.6）
- 地點（美國內外）、對象（成人 vs 兒童青少年）、實驗類型（實驗室、artifactual field、framed field、natural field）**都沒有顯著影響**。
- 只有發表年份有影響：越新的研究報告的效果越小（t(339) = −3.44, p < .001）。

## 貢獻 (Contributions)
1. 第一個跨技術、跨領域、跨情境的大規模 nudge meta-analysis；d = 0.45 和教育宣導、經濟誘因等傳統介入相當（p.6）。
2. 用三種心理障礙的框架比較介入類別，發現 **decision structure 一致最強**。作者的解釋（p.7，作者自己說「有點推測性」）：
   - structure 類介入對資訊處理的要求較低，提供捷徑，不需要逐一評估
   - information 和 assistance 類介入要和個人的價值、目標連結，因此更受**個人差異**影響，在高認知負荷或時間壓力下更容易失效
3. 領域差異：低成本、低長期後果、習慣性的決策（食物）最容易被影響；高影響的決策（財務）最難（p.7–8）。

## 限制 (Limitations)
作者承認（p.8）：
- 只看以個人為單位的研究，排除家戶、班級、組織層級的研究
- 異質性極高，大部分仍無法解釋；應研究收入、社經地位、領域知識、數字能力、態度等調節變數
- 主要用 nudge 和 choice architecture 當關鍵字，可能漏掉 2008 年以前的研究
- 有中度發表偏誤，未來研究要注意樣本數規劃
- 個人化、針對易受影響族群（兒童、低收入家庭）的介入要特別注意倫理

> [!note] 推論：agent 觀察到、但論文沒有特別討論的地方
> - **排除組合式介入**讓每種技術的效果可以分開估計，但真實世界的 nudge 常是組合使用（Valta 也只測單一 nudge），所以結果可能低估或高估實務上的效果。
> - 他人的批評（Szaszi et al., PNAS 2022 letter，**尚未收錄、未讀全文**）認為發表偏誤比作者假設的更嚴重；這和本文自己的敏感度分析（嚴重偏誤時 d = 0.03）一致，代表「nudge 平均有多有效」仍有爭議。

## 與其他論文的關係
- [[Valta2026-Technostress-Nudges]]：Valta 的 default-setting 屬於 decision structure（本文 d = 0.62，最強的技術）；salience-framing 比較接近 decision information 的 visibility。但 Valta 發現兩者效果**沒有顯著差異**，和本文「structure > information」的整體模式不同 → 見 [[Structure-vs-Information-Nudges]]。
- [[Rhue2026-Local-Personalization]]：local personalization 改變的是資訊的**個人切身性**（translation／personal relevance），屬於 decision information；捐款屬於 prosocial 領域（本文 d = 0.44）。本文說 information 類介入受個人價值影響較大，正好和 Rhue 發現「靠朋友推薦捐款的人不受影響」的異質性一致（agent 推論）。
- 本文提到的個人差異調節（收入、知識、態度）呼應 Valta 的 [[Digital-Mindset]] 調節效果。
- 基於（尚未收錄）：Thaler & Sunstein 2008《Nudge》、Münscher et al.（分類架構）、Johnson & Goldstein（器官捐贈預設）、Allcott（能源社會規範）

## 相關概念
[[Choice-Architecture]]、[[Digital-Nudging]]、[[Meta-Analysis]]、[[Heuristics]]、[[Randomized-Experiments]]

## 反向連結
以下頁面連到本頁（lint 自動補上的雙向連結）：
- [[Jesse2021-Nudging-Recommender-Systems]]
- [[Mathur2019-Dark-Patterns]]
- [[Personalization]]
- [[Unintended-Consequences-of-Nudges]]
