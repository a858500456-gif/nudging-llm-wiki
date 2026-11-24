---
type: paper
title: "Dark Patterns at Scale: Findings from a Crawl of 11K Shopping Websites"
domain: [HCI, IS, AI]
tags: [dark-patterns, manipulation, consumer-protection, web-measurement, nudging, clustering]
created: 2026-11-24
updated: 2026-11-24
reviewed: false
authors: [Arunesh Mathur, Gunes Acar, Michael J. Friedman, Elena Lucherini, Jonathan Mayer, Marshini Chetty, Arvind Narayanan]
year: 2019
venue: Proc. ACM Hum.-Comput. Interact. 3 (CSCW), Article 81
arxiv: "1907.07032"
doi: "10.1145/3359183"
source: "[[raw/papers/Mathur2019-Dark-Patterns.pdf]]"
status: full
---

# Dark Patterns at Scale: Findings from a Crawl of 11K Shopping Websites

> 一句話總結：用自動爬蟲模擬購物流程，掃描約 11K 個熱門英文購物網站的 53K 個商品頁，找到 **1,818 個 [[Dark-Patterns|dark pattern]]**（15 種、7 大類），出現在約 **11.1%** 的網站；其中 183 個網站有明確的欺騙行為，越熱門的網站越常用；還有 22 家第三方公司把 dark pattern 當成現成服務在賣。

- 作者：Princeton University（Mathur、Acar、Friedman、Lucherini、Mayer、Narayanan）、University of Chicago（Chetty）
- 發表：*Proc. ACM HCI* 3 (CSCW), Article 81（2019 年 11 月）；原始檔取自 arXiv 1907.07032v2

## 研究問題 (Problem)
- **Dark patterns**：讓線上服務獲利的介面設計，透過**強迫、引導或欺騙**，讓使用者做出在充分知情、可以自由選擇時不會做的決定（[[Mathur2019-Dark-Patterns]] p.2）。
- 過去的研究只有分類（多半根據軼事或使用者投稿），缺少**大規模的盛行率證據**，也沒有系統性說明不同 dark pattern 如何傷害使用者（p.2, p.5）。

## 核心方法 (Method)

### Dark pattern 特徵分類法（§3, p.5–6）
五個面向：
| 面向 | 問題 | 例子 |
|---|---|---|
| Asymmetric | 介面是否讓選項的份量或負擔不對等？ | 「接受 cookie」按鈕很大，「拒絕」藏起來 |
| Covert | 介面的作用是否對使用者隱藏？ | decoy effect（誘餌選項） |
| Deceptive | 是否透過不實陳述、誤導或隱瞞造成錯誤信念？ | 號稱限時、但重新整理就重來的折扣 |
| Hides Information | 是否隱藏或延後必要資訊？ | 結帳最後才出現額外費用 |
| Restrictive | 是否限制可選的選項？ | 只能用社群帳號註冊 |

利用的認知偏誤：anchoring、bandwagon（從眾）、default effect、framing、scarcity bias、sunk cost fallacy（p.6）。

### 資料蒐集與分析（§4, Fig. 1）
1. **網站清單**：Alexa Top Sites 361,102 個網站 → 用 Webshrinker 分類出 46,569 個購物網站（在 500 個人工標註樣本上，準確率 94%，Alexa 自己的分類器只有 89%）→ 用 polyglot 篩出 19,455 個英文購物網站（2018 年 8 月）。
2. **找商品頁**：Selenium 爬蟲＋logistic regression URL 分類器（五折交叉驗證準確率 83%），每站最多 5 個商品頁 → 從 **11,286** 個網站取得 **53,180** 個商品頁。
3. **模擬購買流程**：以 OpenWPM 為基礎的 checkout crawler，選規格、加入購物車、看購物車、結帳；抽樣 100 頁中有 66 頁成功走到結帳頁。爬完約 90 小時。
4. **頁面切割**：把頁面切成文字區塊（segments），並用 Mutation Summary 捕捉動態更新（例如倒數計時）→ 約 1,300 萬個 segments，去重後約 130 萬個。
5. **分群**：Bag of Words（詞彙量 10,133）→ PCA 取 3 個成分（解釋 > 95% 變異）→ **HDBSCAN** 階層密度分群（min_cluster_size = 10）→ 10,277 群。
6. **人工檢查**：第一輪篩到 1,768 群；兩位研究者對 200 群獨立標註，Cohen's kappa = **0.74**，討論解決分歧後由一人檢查其餘群。
7. **檢查欺騙行為**：對動態型 dark pattern（例如倒數計時）每 4 小時回訪一次、連續 5 天，把截圖串成影片判斷是否造假。

## 實驗與結果 (Experiments)

### 盛行率（Table 1, §5）
- **1,818** 個 dark pattern，在 **1,254** 個網站（約 **11.1%**）上；因為只分析文字、只看商品頁到結帳頁，這是**下限**。
- **越熱門的網站越常出現**：Spearman's ρ = −0.62, p < 0.0001（Alexa 排名數字越小越熱門）。

| 類別 | 類型（實例數 / 網站數） | 利用的偏誤 |
|---|---|---|
| Sneaking | Sneak into Basket（7/7）、Hidden Costs（5/5）、Hidden Subscription（14/13） | default effect、sunk cost |
| Urgency | **Countdown Timer（393/361）**、Limited-time Message（88/84） | scarcity |
| Misdirection | Confirmshaming（169/164）、Visual Interference（25/24）、Trick Questions（9/9）、Pressured Selling（67/62） | framing、anchoring、default |
| Social Proof | Activity Message（313/264）、Testimonials（12/12） | bandwagon |
| Scarcity | **Low-stock Message（632/581）**、High-demand Message（47/43） | scarcity |
| Obstruction | Hard to Cancel（31/31） | — |
| Forced Action | Forced Enrollment（6/6） | — |

- 例子：Pressured Selling 把最貴的商品設為**預設選項**；Visual Interference 把「不要收行銷信」的選項變成灰色，看起來像不能點；Confirmshaming 把拒絕按鈕寫成讓人羞愧的話。

### 欺騙行為（§5）
- 共 **234** 個欺騙性實例，在 **183** 個網站上。
- 欺騙性倒數計時：**157** 個實例、140 個網站（時間到了就重來，或時間到了優惠還在）。
- 欺騙性活動通知：29 個實例、20 個網站；欺騙性低庫存訊息：17 個實例、17 個網站（有的每次載入頁面都隨機產生庫存數字）。

### 第三方生態系（§5, Table 2）
- **22** 家第三方公司提供 Social Proof 活動通知等功能，出現在 1,066 個購物網站、7,769 個 Alexa 前一百萬網站上。
- 有些公司**公開宣傳造假功能**（例如 Boost 的「Fake it till you make it」頁面、可以建立假訂單的 WooCommerce 外掛）；Shopify 曾暫時下架讓網站輸入假銷售資料的 Sales Pop 外掛。

## 貢獻 (Contributions)
1. 可以在網路規模上找出 dark pattern 的自動化方法（爬蟲、分群），程式和資料集公開（p.3）。
2. 第一份大規模的 dark pattern 盛行率資料（p.3）。
3. 以五個特徵面向＋認知偏誤描述 dark pattern 如何運作的分類法（p.5–6）。
4. 政策意涵（§6.2）：
   - 欺騙性做法在美國（FTC Act Section 5）和歐盟（Unfair Commercial Practices Directive）都明確違法
   - Sneaking 類可能違反歐盟 Consumer Rights Directive
   - Trick Questions 和 Visual Interference 取得的同意不符合 GDPR「自由、知情、主動」的要求
5. 對使用者的工具：可以做成標示 dark pattern 的瀏覽器外掛或網站評分（§6.1）。

## 限制 (Limitations)
作者承認（§6.4）：
- 只分析文字，**沒有分析純視覺的 dark pattern**（字體大小、顏色）
- 有些類型處在灰色地帶，專家和使用者的看法可能不同（例如免運截止倒數）
- 偏誤和 dark pattern 的對應可能更複雜，而且每個人的易受影響程度不同
- 爬蟲有失敗；只爬商品頁和結帳頁，漏掉首頁、搜尋、註冊、購買後的 upselling
- 沒有測量 dark pattern 對使用者行為的實際影響（列為未來研究）

> [!note] 推論：agent 觀察到、但論文沒有特別討論的地方
> - 這是 2018 年的資料，網站生態和法規（例如 EU Digital Services Act）之後都有變化，盛行率數字不能直接用在現在。
> - PDF 轉文字時，Table 1 的特徵符號（Always／Sometimes／Never）遺失了，所以本頁只記錄內文明確寫出的特徵判斷，沒有逐格抄錄。

## 與其他論文的關係
- [[Valta2026-Technostress-Nudges]]：Valta 實驗中的 salience nudge 寫著「Lowest Total Price」，但三台車總價相同；用本文的分類，這可能符合 **deceptive**（不實陳述）的特徵，雖然實驗目的是降低壓力而不是獲利（agent 推論）。另外，Valta 用的兩種 nudge（預設選項、視覺突顯），和本文的 Pressured Selling（把最貴的設為預設）、Visual Interference（用視覺引導）用的是**同一種手法**，差別在於為誰的利益服務。
- [[Rhue2026-Local-Personalization]]：Rhue 的個人化沒有欺騙或隱藏，但同樣利用捷思（home bias）；本文的 social proof、bandwagon 和 Rhue 的 social influence 是相近的心理機制。
- [[Jesse2021-Nudging-Recommender-Systems]]：Jesse 的 nudging 機制目錄中，limited time window、make resources scarce、using visuals to deceit 等，在本文中都被歸為 dark patterns。
- [[Mertens2022-Nudging-Meta-Analysis]]：Mertens 的 decision structure（預設、選項組合）效果最強，而本文顯示同樣的結構手法也最常被拿來操弄（agent 推論）。
- 基於（尚未收錄）：Brignull 2010（dark patterns 一詞的提出）、Gray et al. 2018、Calo（market manipulation）、Kahneman（dual-process）

## 相關概念
[[Dark-Patterns]]、[[Digital-Nudging]]、[[Heuristics]]、[[Choice-Architecture]]、[[Unintended-Consequences-of-Nudges]]

## 反向連結
以下頁面連到本頁（lint 自動補上的雙向連結）：
- [[Interface-Nudges-in-AI-Decision-Environments]]
