# 最新版簡報自我檢查報告：v1.0.0

檢查日：2026-11-23（台灣時間）。對象：research-slides.html、其來源稿、樣式／互動及最新graph。這是AI與程式自檢，不是第三方認證、完整學術審查或讀者理解成效實驗。

## 1. 可核對的結果
| 檢查 | 本次實際結果 | 證據 |
| --- | --- | --- |
| 來源稿生成 | 成功生成10頁，再建置19頁網站 | scripts/render-research-slides.py、scripts/build-demo.py |
| 全站靜態 | 19頁、416個站內連結／資源／錨點通過 | scripts/check-demo.py |
| 全站瀏覽器 | 19頁×桌機／平板／手機＝57組通過，無頁面JS錯誤 | validation/site-v1.0.0.json |
| 簡報專用 | 10頁×1440×1000與390×844兩種視窗＝20組通過 | validation/slides-v1.0.0.json |
| 逐頁稿一致性 | 10頁標題對應JSON，每頁都有來源入口及產出 | scripts/check-slides.py的實際斷言 |
| 排版／圖像 | 20組無橫向溢出，可見圖片解碼通過 | 同上；目視資料見下方 |
| 操作 | 兩側箭頭、捲動後按鈕、首尾停用、鍵盤、跳頁、答題展開、全文、網址定位、列印及無JS通過 | JSON的interaction_checks及布林結果 |
| Graph精簡 | 移除副標題及最底備註，保留一句loop；SVG與PNG重新輸出並目視 | assets/slides-workflow.svg／png |

執行命令：
```powershell
python scripts/render-slides-workflow.py
python scripts/export-workflow-png.py
python scripts/build-demo.py
python scripts/check-demo.py
python scripts/check-slides.py
python scripts/check-demo.py --browser
```
實際使用本機Anaconda Python及已安裝的Microsoft Edge，沒有下載新瀏覽器。簡報JSON保留實際UTC測試時間，對應台灣日期2026-11-23；完整值以JSON為準。

## 2. 我如何依graph執行？
本案的graph是「使用者與AI按階段執行的工作流程」，**不是LangGraph等引擎自動跑圖**。證據是各階段分開保存的產物、實際工具結果及修正紀錄，不能用一張圖證明每條退回線都發生過。

| 節點 | 實際工作與產物 | 狀態／界線 |
| --- | --- | --- |
| ① 目標 | 訪談讀者與研究方法主軸，整理需求 | 已確認；完整需求見requirements-summary.md |
| ② Wiki與來源 | 讀取導讀、資料、GA／ACO與來源摘要，區分提案、示意與結果 | 已按本批需要核對，不是全站逐段學術審查 |
| ③ 大綱 | 先保存slides-outline.md，10頁順序來自使用者要求照流程執行的前次大綱 | 有執行授權，不捏造另一次人工逐頁簽核 |
| ④ 逐頁稿 | 先建立data/research-slides.json及slides-manuscript.md，列問題、內容、來源與產出 | AI內容核對完成；使用者未逐頁學術驗收 |
| ⑤ HTML | render-research-slides.py由稿產生片段，建置器生成正式頁面 | 已完成；避免正文與簡報各自手填而不同步 |
| ⑥ 實測 | 重跑本報告上列靜態、全站及簡報專用測試 | 本次通過，JSON含時間與SHA-256 |
| ⑦ 試讀 | 使用者曾實際提出換頁與冗餘操作回饋，修正後重測；本批獲版本發布授權 | 尚無正式讀者理解測量，不以發布授權冒充教學內容驗收 |

## 3. 哪些loop有真正發生？
| 發現 | 修改 | 重查的具體內容 | 紀錄 |
| --- | --- | --- | --- |
| Wiki手機長書目溢出 | CSS允許長網址換行 | 原手機頁及全站視窗是否還有橫向溢出 | wiki-log ingest段，最終57組再通過 |
| 簡報標題焦點外框 | 修非互動標題樣式 | 版面及鍵盤仍可操作 | slides-proof與wiki-log |
| 必須捲到底才能換頁 | 固定兩側箭頭 | 捲動後箭頭在視窗內、點擊換頁、首尾停用 | check-slides.py；最新版重跑通過 |
| 上下頁按鈕冗餘 | 刪底部按鈕與舊JS依賴 | 舊按鈕不存在，側邊／鍵盤仍正常 | check-slides.py有明確斷言 |
| 生成器誤判Pareto來源頁 | 改衍生頁辨識 | 重建成功後再驗證新產物，不把舊HTML通過當新版本通過 | slides-proof graph重製段 |
| SVG直接截圖逾時 | 改HTML容器輸出 | PNG存在、圖文箭頭目視正常 | export-workflow-png.py及graph圖片 |

這些案例證明「問題 → 對應修正 → 再檢查」有執行；未觸發的例如文獻矛盾退回，不宣稱已跑過。

## 4. 如何避免只憑口頭說通過？
- [機器結果](validation/slides-v1.0.0.json)保存測試時間、20組視窗結果、操作檢查及9個檔案的SHA-256，包含逐頁稿、HTML、CSS、JS、生成器、測試程式及graph兩種檔案。
- 另逐檔重算雜湊核對一致，讓測試結果能對應本次準備提交的版本。文字檔依報告hash_policy先統一LF換行，避免Windows與Git換行轉換產生假差異；PNG用原始位元組。此SHA-256是版本識別，不是學術正確性證明。
- [桌機截圖](validation/slides-1440-1.png)與[手機截圖](validation/slides-390-7.png)可直接查看；私人工作區另保留所有20頁／視窗截圖。已有各頁總覽目視與重點頁細看，不能說每個像素均經人工檢查。
- 提交後用Git標籤v1.0.0定位同一版本；測試腳本可重新執行，不依賴未公開的研究原檔。

## 5. 尚未證明的事
沒有證明完整研究模型正確、GA／ACO有效、所有文獻全文已讀、全站每段主張已完成學術審查、所有外部網址永遠可用，或所有讀者都能看懂。定期更新未排程；更多來源與真實照片也未完成。本版以作業必要成果及可核對的執行紀錄為範圍。
