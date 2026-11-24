---
type: paper
title: "Digital Nudging with Recommender Systems: Survey and Future Directions"
domain: [IS, HCI, AI]
tags: [digital-nudging, recommender-systems, taxonomy, survey, personalization]
created: 2026-11-24
updated: 2026-11-24
reviewed: false
authors: [Mathias Jesse, Dietmar Jannach]
year: 2021
venue: Computers in Human Behavior Reports 3, 100052
arxiv: "2011.03413"
doi: ""
source: "[[raw/papers/Jesse2021-Nudging-Recommender-Systems.pdf]]"
status: full
---

# Digital Nudging with Recommender Systems: Survey and Future Directions

> 一句話總結：推薦系統會挑選、排序要呈現的選項，本身就是一種 [[Digital-Nudging|digital nudge]]。作者透過系統性文獻回顧整理出 **87 種 nudging 機制**，提出四大類的新分類法，並發現其中只有 **18 種**在推薦系統中被研究過，剩下的 69 種是未來的研究空間。

- 作者：University of Klagenfurt（奧地利）
- 期刊：*Computers in Human Behavior Reports* 3, 100052（2021），開放取用；原始檔取自 arXiv 2011.03413v2（2021-01-13）

## 研究問題 (Problem)
- 推薦系統決定哪些資訊容易取得，因此影響決策；但**數位 nudging 和推薦系統過去大多被分開研究**（p.1–2）。
- 例如 HCI 領域的 nudging 回顧（Caraban et al. 2019）就沒有把推薦系統當成 nudge（p.2）。
- 目標：整理 nudging 機制、建立分類法、盤點推薦系統中已研究過的 nudge，並提出研究議程（p.3）。

## 核心方法 (Method)
- **定義**：digital nudging 是「用介面設計元素引導數位選擇環境中的行為」（Weinmann et al.）；Meske & Potthoff 的定義更廣，包含設計、資訊、互動元素，且**不限制選擇自由**（p.4）。
- **文獻搜尋**（p.5–6）：在 Web of Science、SpringerLink、IEEE Xplore、DOAJ、Emerald、ERIC/PubMed、Sage、INFORMS 搜尋 (Nudge OR Nudging OR Digital Nudge…) AND (Recommender…)；條件是 2008 年以後、描述 nudge、和推薦有關；再做 citation snowballing。得到 111 篇，去重並檢查相關性後留下 **63 篇**。

### 分類法（Figure 1, p.7；延伸 Münscher et al. 2016）
| 大類 | 說明 | 子類 |
|---|---|---|
| **Decision Information**（約一半的機制） | 改變呈現的資訊，不改變選項本身 | translate information、**increase salience**、make information visible、phrasing of information |
| **Decision Structure**（23 種） | 改變選項的安排 | change defaults、change option-related effort、change range or composition、change option consequences |
| **Decision Assistance**（8 種） | 協助使用者完成自己的目標 | provide reminders、facilitate commitment |
| **Social Decision Appeal**（11 種，新增） | 強調情感和社會意涵 | increase reputation of messenger、provide social reference point、instigate empathy |

- 共 13 個子類；新增的子類包括 increase salience、increase reputation of messenger、instigate empathy 等（p.8）。
- 和 [[Mertens2022-Nudging-Meta-Analysis]] 用的三類架構（同樣來自 Münscher et al.）相比，多了 social decision appeal，並把 salience 獨立出來。詳見 [[Choice-Architecture]]。

### 心理機制（§4, p.10–14）
- 文獻中提到 **58 種心理現象**（anchoring、default effect、loss aversion、framing、decoy effect、salience bias、scarcity…）。
- 但 87 種機制中只有 **22 種**有明確說明背後的心理理論 → 很多 nudge 是憑研究者經驗設計，而不是根據理論（p.12）。
- 例如 setting defaults 背後是 status quo bias、loss aversion、decision inertia（Table 2）。
- 同一個機制可能有多種實作方式、牽涉多種心理現象，所以效果很難直接歸因到單一機制（p.14）。

## 實驗與結果 (Experiments)
（本文是文獻回顧，沒有自己的實驗）

### 推薦系統本身就隱含的 nudge（Table 3, p.14–15）
只呈現一部分選項（hiding）、排序（ordering effects）、客製化資訊（customized information）、降低搜尋的力氣（change physical effort）、簡化（simplification）、呈現別人買過或喜歡過（following the herd、social influence）、強調屬性和優惠（increase salience of attributes/incentives）等，共 14 種。

### 已研究過的 nudge（Table 4–5, p.15–19）
- 16 篇實作並分析 nudge，另有 3 篇只提出設計；共研究過 **18 種機制**，最常見的是 **setting defaults** 和 **using visuals to increase salience**。
- 應用領域：路線規劃、電子商務最多。
- 樣本數：8 到約 20,933 人；排除兩個極端值後，平均 223 人、中位數 100 人。
- 有記錄研究期間的只有 1–2 個月；**只有兩篇（同一團隊）看長期效果**。
- 11 篇有測行為效果的研究中，**8 篇**至少有一種 nudge 有效，**3 篇**沒有顯著效果。

| 研究 | 結果 |
|---|---|
| Elsweiler et al. 2017（食譜，視覺 nudge） | 62.2% 的決策選了較健康的食譜 |
| Turland et al. 2015（安全網路） | 顏色突顯有效、排序無效；兩者合併效果最強 |
| Kammerer & Gerjets 2014（搜尋結果） | 清單排序有影響，但改成格狀排列後效果大幅降低 |
| Esposito et al. 2017（相容性警告） | 一般警告無效，情緒性措辭的警告有效 |
| Gena et al. 2019（新聞） | 從眾類 nudge 無效，負面框架有效 |
| Lee et al. 2011、Forwood et al. 2015、Bothos et al. 2016 | 沒有顯著效果 |

- Köcher et al. 2019：突顯某個選項不一定讓它被選更多，但會**間接**影響選擇（推薦大背包 → 大家平均選比較大的背包）→ 不能只看「被推的那個選項有沒有被選」（p.19–20）。

## 貢獻 (Contributions)
1. 87 種 nudging 機制的目錄和四大類分類法，並區分「機制」和「背後的心理現象」（p.3, §3–4）。
2. 指出推薦系統本身就是 nudge，以及推薦系統中 nudge 研究的缺口（69 種機制未被研究）（p.16）。
3. 研究議程（§5.3, p.20–22）：在推薦清單上加視覺突顯、預設選項、警告、小額誘因、即時推播、專家推薦、虛擬角色等；**個人化 nudge（smart nudges）**；以及檢查使用者是否覺得被操弄。

## 限制 (Limitations)
- 作者承認：有些研究沒用 nudging 這個詞，可能沒被搜尋到（p.16 註 6）。
- 本文不深入討論倫理（p.5），但指出：
  - 實務上 nudge 不一定為使用者著想（例如航空公司網站推銷不必要的加購），嚴格來說這不算 nudge（p.4）
  - 介面沒有完全中立的呈現方式（p.4）
  - 個人化推薦若直接過濾掉選項，就違反了選擇自由（p.5）
  - **沒有任何一篇研究檢查使用者是否覺得被操弄**（p.21–22）

> [!note] 推論：agent 觀察到、但論文沒有特別討論的地方
> - 這是 2021 年的回顧，搜尋時間更早；生成式 AI 推薦、對話式推薦出現後的研究都不在內。
> - 已研究的 18 種機制中，多數樣本小、時間短，「8/11 篇有效」不能當作效果大小的證據（沒有算效果量）；效果大小要參考 [[Mertens2022-Nudging-Meta-Analysis]]。
> - 作者把 nudging 和 persuasion 視為重疊的概念（p.5），這讓分類法中出現 "using visuals to deceit" 這類明顯有操弄性質的機制，界線比 Thaler & Sunstein 的原始定義寬鬆。

## 與其他論文的關係
- [[Valta2026-Technostress-Nudges]]：Valta 的兩種 nudge 正好是推薦系統中最常被研究的兩種（setting defaults、using visuals to increase salience）。Valta 用的 digital nudge 定義也來自 Weinmann et al. 和 Mirsch et al.
- [[Rhue2026-Local-Personalization]]：Rhue 的 local personalization email 在本文分類下屬於 customized information（decision information）；本文提出的「smart nudges」（個人化 nudge）正是 Rhue 研究的情境（agent 推論）。
- [[Mertens2022-Nudging-Meta-Analysis]]：兩篇都延伸 Münscher et al. 的分類；Mertens 提供效果量，本文提供更細的機制目錄。
- [[Mathur2019-Dark-Patterns]]：本文的 "using visuals to deceit"、limited time window、scarcity 等機制，在 Mathur 的分類中屬於 dark patterns。
- 基於（尚未收錄）：Weinmann et al. 2016、Mirsch et al. 2017、Schneider et al. 2018、Caraban et al. 2019、Münscher et al. 2016

## 相關概念
[[Digital-Nudging]]、[[Choice-Architecture]]、[[Recommender-Systems]]、[[Personalization]]、[[Heuristics]]

## 反向連結
以下頁面連到本頁（lint 自動補上的雙向連結）：
- [[Dark-Patterns]]
- [[Interface-Nudges-in-AI-Decision-Environments]]
- [[Unintended-Consequences-of-Nudges]]
