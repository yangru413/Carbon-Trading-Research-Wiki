# 第一批五篇來源與整合提案

查閱日：2026-11-21。狀態：已閱讀以下指定範圍，待批次確認後整合公開正文；尚非五篇已完成 ingest。來源含學術論文、條約、官方說明與研究資料文件，不全是論文。

## 1. 最佳化演算法的公平比較
Beiranvand, V., Hare, W., & Lucet, Y. (2017). Best practices for comparing optimization algorithms. *Optimization and Engineering, 18*, 815–848. https://doi.org/10.1007/s11081-017-9366-1

- 問題：如何避免演算法比較因目的、測試問題或評估選擇而誤導。
- 方法：文獻綜述與比較方法整理，不是新的配對演算法。
- 核讀：arXiv:1709.08242v1，PDF第1–5頁，§1–§3可見內容；副本已在私人 .work/sources/。
- 寫入：方法導讀與實驗評估，先交代比較目的與測試集。
- 限制：主要是序列單目標，不能直接當多目標指標規範。

## 2. 京都議定書：減量承諾與排放交易
United Nations. (1998). *Kyoto Protocol to the United Nations Framework Convention on Climate Change*. https://unfccc.int/resource/docs/convkp/kpeng.pdf

- 性質：條約文件，不是實驗論文；1998是所讀PDF封面出版年，與1997年通過不同。
- 問題：如何建立締約方的減量承諾與相關制度。
- 方法／機制：以法律條文定義承諾與交易原則，不是以演算法求配對。
- 核讀：封面、Article 3(1)；交易條款 Article 17 待下一階段精讀，不把尚未核讀部分寫成既定摘要。
- 寫入：碳交易歷史背景，說明國際減量承諾；交易機制段落需補核第17條。
- 限制：國家層次承諾不直接等於企業EUA交易；不能說京都是全球所有排放交易的起點。

## 3. EU ETS制度演進
European Commission. (2025, June 5). *Development of EU ETS (2005–2020).* https://climate.ec.europa.eu/areas-action/carbon-markets/eu-emissions-trading-system-eu-ets/development-eu-ets-2005-2020_en

- 性質：官方歷史說明，非條文本身，也非成效識別論文。
- 問題：制度如何建立，不同階段有何差異。
- 方法／內容：按階段說明制度；核讀 First steps、Phase 1–3及頁面更新日期。
- 寫入：EU ETS文章的歷史與2020樣本背景；第三期為2013–2020，改採歐盟統一總量、拍賣作為預設分配方式。
- 限制：法規細節仍須補對應年度法規原文，不以官方概述冒充法律全文。

## 4. EUTL研究資料庫
Abrell, J. (2024, November 6). *Database for the European Union Transaction Log* [Database documentation]. EUETS.INFO.

- 原檔：使用者提供 Description_EUTL_database.pdf，19頁，不公開原檔；文件指向 EUETS.INFO，尚未核對可下載同版的公開文件網址。
- 問題：EUTL帳戶、設施及移轉資料難以串接及使用。
- 方法：擷取、解析、清理資料；重建歷史帳戶關係；建立關聯式資料模型。
- 核讀：本機文字擷取第1–5頁、附錄A.2–A.4（第14–15頁）、表C.4–C.5（第18–19頁）。
- 寫入：資料清洗與欄位說明，解釋帳戶與設施不同、識別碼對照、交易區塊彙整與版本檢查。
- 限制：不是本機NOTESD同版欄位手冊；表中main=10與supplementary=0的說明，不能未核對編碼就直接認定NOTESD的10-0含義，更不能當已證明買賣成交。

## 5. 螞蟻系統原始研究
Dorigo, M., Maniezzo, V., & Colorni, A. (1996). Ant system: Optimization by a colony of cooperating agents. *IEEE Transactions on Systems, Man, and Cybernetics, Part B (Cybernetics), 26*(1), 29–41. https://doi.org/10.1109/3477.484436

- 所讀作者稿：https://faculty.washington.edu/paymana/swarm/dorigo96-itsmc.pdf （26個PDF頁面；頁碼不直接等於期刊頁碼）。
- 問題：如何以分散合作的人工代理搜尋組合最佳化方案。
- 方法：Ant System，以機率選擇、資訊素正回饋與啟發式資訊構造解；以旅行推銷員問題為主要示範。
- 核讀：摘要、Introduction，PDF第1–4頁；尚未核讀完整公式與實驗，不摘錄效能數字。
- 寫入：ACO入門，從螞蟻路徑比喻解釋合作搜尋；配對應用另明標本站示意。
- 限制：Ant System是早期方法，不能與所有ACO變體畫等號；未證明能直接解本研究的多目標碳交易模型。PDF載有著作權聲明，不重製原圖或公開全文。

## 共同整合方式
每篇建立可查閱文獻摘要、登錄來源、連結相關正文並補附近引用；保留實際核讀範圍。五篇確認後一批整合，再建置、檢查與記錄。這是首批五份來源，不代表每篇主題已達3–5篇引用。

## 真實查核與修正
- Scholarpedia兩個入口無法穩定讀取，改讀原始Ant System作者稿，不使用搜尋摘要當全文。
- 京都官方介紹逾時，改讀官方條約PDF；區分通過年份與PDF封面年份。
- 本機Abrell文件可讀，但公開同版網址尚未核定，保留限制。
