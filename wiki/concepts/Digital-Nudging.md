---
type: concept
title: Digital Nudging
domain: [IS, HCI]
tags: [digital-nudging, choice-architecture, interface-design]
created: 2026-11-24
updated: 2026-11-24
reviewed: false
---

# Digital Nudging

> 在數位介面中，以可預期的方式引導使用者注意力與決策的設計元素。主要目的是讓使用者受益，**不限制選項，也不提供經濟誘因**（[[Valta2026-Technostress-Nudges]] §1, p.2，引用 Weinmann et al. 2016）。

## 定義與符號
- **Choice architecture（選擇架構）**：選項如何被安排、呈現與預設。nudge 就是對選擇架構的調整。
- **Digital interface nudge**：嵌入在 UI 裡的微觀設計元素，影響使用者如何注意、處理和選擇選項（[[Valta2026-Technostress-Nudges]] §2.2, p.3）。
- 數位 nudge 和線下 nudge 的差別：介面可以動態地組織資訊、增加或刪除互動步驟、分配視覺上的顯著程度，直接影響使用者感受到的 cognitive effort（同上）。

## 常見類型
salience-framing、default-setting、social norms、loss aversion、anchoring（[[Valta2026-Technostress-Nudges]] §2.2, p.3）

### Default-Setting Nudge（預設選項）
- 預先選好一個選項，使用者沒有主動更改就會套用。
- 機制：**choice simplification**，減少需要主動做的決定、降低 decision fatigue，也帶來熟悉感（[[Valta2026-Technostress-Nudges]] §2.2, p.3）。
- 適用情境：重複性高、風險比較低的設定決策，例如 dashboard 的預設報表檢視、workflow 的標準簽核路徑、員工入口網站預選的方案組合（[[Valta2026-Technostress-Nudges]] §6.2, p.12）。

### Salience-Framing Nudge（顯著性突顯）
- 用視覺提示（icon、版面、顏色、標籤）讓和任務相關的資訊更顯眼，**不改變選項集合**。
- 機制：**attentional guidance**，降低尋找、解讀和比較資訊的成本，節省 working memory（[[Valta2026-Technostress-Nudges]] §2.2, §3）。
- 和 gain-loss 等語言上的 message framing 是不同的概念（同上）。
- 適用情境：需要整合分散資訊的比較任務；在 AI 介面中，可以用來突顯 confidence indicator、風險資訊、資料來源（[[Valta2026-Technostress-Nudges]] §6.2, p.12）。

## 效果的邊界條件
（[[Valta2026-Technostress-Nudges]] §2.2, p.3）
- **最有效**：任務複雜、選項多、有時間壓力或需要負責 (accountability)、知覺風險高的時候
- **效果較弱，甚至引發 reactance（反抗）**：任務簡單、選項少、使用者已經有明確偏好，讓 nudge 顯得像不必要的操弄
- **個人差異**：need for cognition、need for uniqueness（[[Valta2026-Technostress-Nudges]] §2.2）；[[Digital-Mindset]]（[[Valta2026-Technostress-Nudges]] §5.3）
- 高風險、高責任的情境需要搭配解釋和透明度，避免讓人覺得被過度簡化或操弄（[[Valta2026-Technostress-Nudges]] §6.2）

## 研究的結果變數
- 傳統：行為結果（採用、遵從、購買決策）
- [[Valta2026-Technostress-Nudges]]：擴展到**知覺層面的壓力**。default-setting 和 salience-framing 都能降低 hindrance [[Technostress]]，效果量相近（d ≈ −0.62 ~ −0.63），兩者沒有顯著差異。

## 設計方法
Digital nudge design method：analysis（定義目標）→ design（設計 nudge）→ implementation & evaluation（[[Valta2026-Technostress-Nudges]] §4.2，引用 [65]）

## 和個人化的關係
> [!note] 推論：[[Rhue2026-Local-Personalization]] 的 local personalization（email 推薦住家附近的專案）不限制選項、不給誘因，只改變呈現什麼，可視為一種以 [[Home-Bias|home bias]] 為槓桿的框架型 nudge；論文本身沒有用 nudge 這個詞。它提醒我們 nudge 也有分配上的副作用（[[Rich-Get-Richer]]）。

## 整體效果有多大
- 跨 455 個效果量的 meta-analysis：整體 d = 0.45；default 最強（d = 0.62），改變選項結構的介入一致強於改變資訊呈現的介入；但有發表偏誤，約 15% 的介入可能適得其反（[[Mertens2022-Nudging-Meta-Analysis]]）。完整分類見 [[Choice-Architecture]]。

## 推薦系統與 dark patterns
- 推薦系統的篩選和排序本身就是 nudge；文獻中有 87 種 nudging 機制，推薦系統只研究過 18 種（[[Jesse2021-Nudging-Recommender-Systems]]，見 [[Recommender-Systems]]）。
- 同樣的手法（預設、突顯、稀缺、社會證明）若為平台利益而欺騙使用者，就是 [[Dark-Patterns|dark pattern]]；約 11.1% 的熱門購物網站有 dark pattern（[[Mathur2019-Dark-Patterns]]）。

## 在哪些論文中出現
- [[Valta2026-Technostress-Nudges]]
- [[Rhue2026-Local-Personalization]]（相關：個人化訊息作為 nudge）
- [[Mertens2022-Nudging-Meta-Analysis]]
- [[Jesse2021-Nudging-Recommender-Systems]]
- [[Mathur2019-Dark-Patterns]]（反面：dark patterns）

## 綜合比較
- [[Five-Papers-on-Nudging]]

## 開放問題
- 多個 nudge 組合使用時，效果是相加、相乘還是互相衝突？（[[Valta2026-Technostress-Nudges]] §6.3）
- 長期反覆接觸後會不會 habituation（習慣化）？（同上）
- [[Interface-Nudges-in-AI-Decision-Environments]]
- [[Unintended-Consequences-of-Nudges]]
- [[Structure-vs-Information-Nudges]]

## 反向連結
以下頁面連到本頁（lint 自動補上的雙向連結）：
- [[Heuristics]]
- [[Personalization]]
- [[Who-Benefits-More-From-Interface-Nudges]]
