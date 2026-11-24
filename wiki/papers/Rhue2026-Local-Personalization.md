---
type: paper
title: "A Field Experiment in Local Personalization for Charitable Crowdfunding"
domain: [IS, HCI]
tags: [personalization, heuristics, home-bias, social-influence, field-experiment, crowdfunding, equity]
created: 2026-11-24
updated: 2026-11-24
reviewed: false
authors: [Lauren Rhue, Atiya Avery, Jessica Clark]
year: 2026
venue: MIS Quarterly 50(1), 397–412 (Research Note)
arxiv: ""
doi: "10.25300/MISQ/2025/19044"
source: "[[raw/papers/Rhue2026-Local-Personalization.pdf]]"
status: full
---

# A Field Experiment in Local Personalization for Charitable Crowdfunding

> 一句話總結：在 DonorsChoose 對近 16 萬名捐款人做隨機實地實驗，發現把 email 改成推薦「捐款人住家附近」的專案（local personalization），能提高點擊和捐款，**即使這些人過去沒有地方偏好**；但對靠朋友推薦而捐款的人只提高點擊、不提高捐款，而且這種做法會把錢導向**較富裕、和捐款人相似的社區**，形成 [[Rich-Get-Richer|rich-get-richer]] 效應。

- 作者：Lauren Rhue、Jessica Clark（University of Maryland）、Atiya Avery（Auburn University）
- 期刊：*MIS Quarterly* 50(1)，2026 年 3 月，Research Note

## 研究問題 (Problem)
- 捐款人面對大量專案、無法逐一評估，會依賴 [[Heuristics|捷思 (heuristics)]]，最常見的兩種是 [[Home-Bias|home bias]]（偏好在地）和 social influence（偏好朋友推薦）（[[Rhue2026-Local-Personalization]] p.2）。
- 過去研究多半分開研究這兩種捷思，或假設它們互相強化；但兩者可能指向不同選擇（例如捐給遠方的朋友）（p.2–3）。
- 平台的 [[Personalization|個人化]]通常假設「過去行為預測未來偏好」(revealed preference)，但對沒有在地捐款紀錄的人，啟動 home bias 是否仍有效，並不清楚（p.2, p.4）。
- 三個研究問題（p.2）：
  1. local personalization 對過去沒有支持在地專案的人有沒有效？
  2. 對過去因社會連結而捐款的人，效果有什麼不同？
  3. 對捐款分布和平台的公益使命有什麼影響？

## 核心方法 (Method)

### 假設（p.4）
| 假設 | 內容 | 結果 |
|---|---|---|
| H1a | local personalization 提高曾捐非在地專案者的 engagement | 支持 |
| H1b | local personalization 提高曾捐非在地專案者的捐款機率 | 支持 |
| H2a | 對所有人（含曾受社會影響者）都提高 engagement | 部分支持 |
| H2b | 只對沒有社會影響紀錄的人提高捐款機率 | 支持 |
| H3 | local personalization 造成 rich-get-richer，資金集中到較富裕地區 | 支持 |

### 實驗設計（p.5–7）
- 合作平台：DonorsChoose（美國 K-12 公立學校老師募集教室資源；累計募得超過 15 億美元、支持超過 89,000 所學校）。
- 時間：2021 年 10 月；追蹤收到 email 後一週的行為。
- 母體：匿名資料庫超過 200,000 名捐款人中，**最近一次捐款是非在地**（帳單郵遞區號 ≠ 最近支持的郵遞區號）的 159,941 人。
- 隨機分派兩種個人化 email（Table 1）：

| 條件 | 推薦哪裡的專案 | N |
|---|---|---|
| Local personalization（處理組） | 帳單地址（住家）附近 | 79,894 |
| Default personalization（控制組，平台原本做法） | 最近一次捐款的學校附近 | 80,047 |

- 兩封 email 只差在地名（主旨、預覽文字、內文、landing page 都一致替換），其他內容完全相同。
- 測量：open rate、click rate（engagement）；donation rate、donation amount（捐款）。整體平均 open 約 28%、click 5%、donation 0.2%。
- Prior home bias 的代理變數：帳單地與最近捐款地的距離；prior social influence 的代理變數：第一次捐款是否來自老師的推薦連結（referral，平均 0.649）。
- 郵遞區號層級的人口資料（收入、房價、人口、種族組成）來自美國 Census。
- Randomization check：兩組在 referral（0.651 vs 0.648, p = 0.2697）、距離、收入、人口等都沒有顯著差異（Table 3）。
- 分析：t-test（隨機分派下足以推論因果）、logistic regression、OLS。

### 主要模型
距離調節（logistic，Table 5）：
$$\Pr(DV_i) = \alpha + \beta_1 \text{LocalPers}_i + \beta_2 \text{Distance}_i + \beta_3 (\text{LocalPers}_i \times \text{Distance}_i) + \epsilon_i$$

Rich-get-richer（OLS，Table 7，只看透過 email 捐款的 395 人）：
$$\text{MedianIncome}_i = \alpha + \beta_1 \text{LocalPers}_i + \beta_2 \text{LocalIncome}_i + \beta_3 \text{Referral}_i + \beta_4 (\text{LocalPers}_i \times \text{LocalIncome}_i) + \epsilon_i$$

社區相似度（Table 10）：把郵遞區號的收入、人口、種族、地理特徵做成標準化向量，計算
$$\cos(\mathbf{A},\mathbf{B}) = \frac{\mathbf{A}\cdot\mathbf{B}}{\lVert\mathbf{A}\rVert\,\lVert\mathbf{B}\rVert},\qquad d(\mathbf{A},\mathbf{B}) = \sqrt{\textstyle\sum_i (A_i - B_i)^2}$$

## 實驗與結果 (Experiments)

### H1：整體效果（Table 4, p.8）
| | N | Open | Click | Donation |
|---|---|---|---|---|
| Default | 80,047 | 0.277 | 0.0436 | 0.00209 |
| Local | 79,894 | 0.282* | 0.0542*** | 0.00285*** |
| p | | 0.024 | < 0.001 | 0.002 |

- Click 提高 24%、donation 提高 36%（p.8）。
- Logistic：local personalization 對 open β = 0.025*、click β = 0.228***、donation β = 0.314**（Table 5）。
- **距離交互作用為正**（click 0.0001**、donation 0.001***）：過去捐得越遠的人，local personalization 效果越大 → 對「沒有 home bias 紀錄」的人反而有效（p.9）。

### H2：依社會影響分組（Table 6, p.9–10）
| | Referred：Default | Referred：Local | Non-referred：Default | Non-referred：Local |
|---|---|---|---|---|
| N | 52,091 | 51,781 | 27,956 | 28,113 |
| Open | 0.269 | 0.272（n.s.） | 0.292 | 0.300* |
| Click | 0.039 | 0.047*** | 0.052 | 0.067*** |
| Donation | 0.0012 | 0.0015（n.s.） | 0.004 | 0.005** |

- 被推薦而來的捐款人：local personalization 只提高點擊，**不提高捐款**；而且這群人在兩種條件下的回應率都比較低（p.10）。

### H3：Rich-get-richer（p.10–13）
- 收到 local email 而捐款的人，捐給的地區中位數家戶收入高出 **$7,710–$10,146**（p < .001）；交互作用 b = 0.285***：捐款人所在地越富裕，這個效果越強（Table 7, Figure 2）。
- 捐給「高收入學校」（免費／減價午餐比例 < 40%）的 odds 提高 **67%–96%**（b = 0.674–0.796, p < .01），不受 referral 調節（Table 8）。
- 捐款地點分布（Table 9）：

| | N | 捐給自己社區 | 捐給最近支持過的地區 | 其他地區 |
|---|---|---|---|---|
| Local | 229 | 93（41%） | 26（11%） | 110（48%） |
| Default | 167 | 37（22%） | 58（35%） | 72（43%） |

- 捐款人的住家社區平均收入高於最近支持過的地區（約 $66,000 vs $51,000）。
- 即使捐到「其他地區」，local 組捐的社區在人口特徵上也更像捐款人自己的社區（cosine similarity 0.634 vs 0.498, p = 0.0019）→ 與 homophily（同質相吸）機制一致（Table 10, p.12–13）。

## 貢獻 (Contributions)
1. **捷思的層級**：比較 home bias 和 social influence 的獨立與交互效果；人際信任（social influence）似乎比地理接近更強，沒有社會線索的人更容易被地理框架影響（p.13）。
2. **個人化與社會公平**：個人化通常被視為提升相關性的手段，本研究顯示以捷思為基礎的目標設定會產生**分配上的副作用**（rich-get-richer），而且延伸到人口特徵相似的社區（p.13）。
3. **實務**：靜態屬性（住家位置）勝過行為目標（捐款紀錄），挑戰「過去行為最能預測未來」的個人化假設；建議輪替或混合多種個人化策略以兼顧公平（p.13–14）。

## 限制 (Limitations)
作者承認（p.14）：
- 從行為反應推論捷思，沒有自陳的理由
- 沒有測試其他捷思（例如名字相似）
- 人口資料只到郵遞區號層級，無法分析個人的種族、年齡
- 沒有直接測試減緩不公平的策略
- 只看 home bias，其他捷思也可能影響捐款流向

> [!note] 推論：agent 觀察到、但論文沒有特別討論的地方
> - **捐款事件非常少**：16 萬人中只有約 395 人透過 email 捐款，H3 的所有分析都建立在這 395 人（部分模型 385、389 人）上，和前面 16 萬人的 engagement 分析統計力差很多。
> - **「Local」和「Default」都是個人化**，比較的是兩種推薦規則，不是「有沒有 nudge」；所以結論是「哪種框架更有效」，不能直接推到「個人化 vs 不個人化」。
> - Table 7 第 4 欄的常數寫成 `42,4601`，看起來是排版錯誤（第 2 欄是 42,098）。
> - Social influence 的代理變數是「第一次捐款是否來自老師推薦連結」，和 H2 討論的「最近一次非在地捐款是因為朋友」不完全是同一件事。

## 與其他論文的關係
- 和 [[Valta2026-Technostress-Nudges]] 的關係：兩篇都是用一個**很小的介面／訊息改變**（預設選項、視覺突顯、email 裡的地名）去影響使用者的決策過程。Valta 看的是**使用者自己的壓力感受**（偏正面），Rhue 看的是**行為和社會分配**（同時有正面與副作用）。
  > [!note] 推論：Rhue 的 local personalization 可以視為一種以 home bias 為槓桿的框架型 nudge（論文本身沒有用 nudge 這個詞），兩篇合起來點出 nudge 研究的兩種結果變數：個人感受 vs 群體分配。
- 基於（尚未收錄）：Kahneman 2011（dual-process）、Lin & Viswanathan 2016（home bias）、Burtch et al. 2014、Lambrecht & Tucker 2013（targeting）、Merton 1968（Matthew effect）
- 其他相關收錄：[[Mertens2022-Nudging-Meta-Analysis]]（prosocial 領域 d = 0.44；information 類介入受個人價值影響）、[[Jesse2021-Nudging-Recommender-Systems]]（個人化推薦作為 nudge、smart nudges）、[[Mathur2019-Dark-Patterns]]（social proof 與從眾偏誤）
- 開放問題：[[Unintended-Consequences-of-Nudges]]

## 相關概念
[[Personalization]]、[[Heuristics]]、[[Home-Bias]]、[[Rich-Get-Richer]]、[[Randomized-Experiments]]、[[Digital-Nudging]]

## 反向連結
以下頁面連到本頁（lint 自動補上的雙向連結）：
- [[Choice-Architecture]]
- [[Recommender-Systems]]
