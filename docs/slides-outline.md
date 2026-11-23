# 簡報重製：大綱與階段檢查

日期：2026-11-23。使用者在前一輪大綱後要求「照這個流程再做一次投影片」，本批據此執行，不另造一次逐頁人工確認紀錄。

## 1. 目標確認
讀者：初入研究者與接手學生。主題：碳交易配對研究如何進行。
閱讀後應能說明研究步驟、分辨觀測與假設、解釋GA／ACO角色，並知道結果要如何檢查。
範圍：教學而非實證報告，沒有新研究結果；保留10頁、固定兩側換頁、跳頁、全文閱讀與列印。

## 2. Wiki證據盤點
先讀 research-methodology、start、sources、genetic-algorithm、ant-colony-optimization 與既有簡報，再對照下列來源頁。
五份已整合來源供相關頁使用；GA沿用既有Eiben／Whitley，四目標與年度關係用CM03原文定位。
制度、指標、成交、移轉、模擬與實證不得混用。沒有依據的新主張刪除或明示本站教學示例。

## 3. 已確認大綱的實作版本
| 頁 | 主題 | 學習問題 | Wiki來源 | 預定圖解 |
| --- | --- | --- | --- | --- |
| 1 | 研究全貌 | 研究什麼、步驟怎麼連起來？ | research-methodology | 問題→資料→模型→方法→評估 |
| 2 | 碳交易基本概念 | 配額、移轉與減排有何不同？ | carbon-basics、eu-ets-history | 既有配額示意 |
| 3 | 配對與多目標 | 決定什麼、如何判斷更好？ | cm03#objectives、pareto | 四目標與取捨文字對照 |
| 4 | 資料與清理 | 資料能提供什麼、怎麼檢查？ | sources、reading-eutl-database | 原始資料→對照→清理→樣本 |
| 5 | 模型與假設 | 如何連接決策、目標與限制？ | cm03#questions、sources#price | 輸入→決策→限制→評估 |
| 6 | GA | 如何改動候選方案？ | genetic-algorithm | 選擇→交配／突變→評估→迭代 |
| 7 | ACO | 如何構造方案、與GA哪裡不同？ | ant-colony-optimization、reading-ant-system | 可行選擇→構造→評估→更新 |
| 8 | 實驗評估 | 如何公平比較與解釋結論？ | research-methodology、reading-benchmarking、cm03 | 可行性／表現／結論範圍 |
| 9 | 跨年度銜接 | 需要接什麼、留下什麼？ | start、research-methodology | 前一年→第二年→第三年 |
| 10 | 流程回顧 | 哪裡退回、重查什麼？ | research-methodology、sources、cm03 | 研究流程加具體退回規則 |

大綱檢查：順序由基礎走到評估；每頁一個主要問題。GA／ACO分開，避免擠在同頁；第10頁不新增主題，而回顧流程及退回條件。大綱通過後才建立逐頁內容檔 data/research-slides.json。

## 4. 流程規則
文字缺依據→回Wiki查來源；文字過長→改逐頁稿；版面／操作錯誤→改HTML/CSS/JS後重測；學術疑義→保留待確認，不讓程式替代判斷。
只有測試真的失敗才記錄為發生過的loop；下列圖中的退回箭頭是工作規則，不表示每條都在本次觸發。
