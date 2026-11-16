# PROJECT_CONTEXT.md — 執行狀態與交接

更新：2026-11-16。本文件記錄決策、授權與待辦，不是研究證據。開發準則見 AGENTS.md，操作見 README.md。

## 最新決策與授權
- 2026-11-16 最新授權：使用者要求推送至指定 GitHub 倉庫並部署 GitHub Pages。首次發布以 main 分支根目錄為來源；原始 CSV／DOCX／PDF、工具與暫存排除。先前「不發布／僅本機」為歷史批次限制，本次授權已取代。發布範圍包含目前網站圖文與必要維護文件；後續擴充仍先討論。
- 圖像與延伸卡片最新決策：以電腦閱讀為主，首頁加入 AI 主題插畫，研究脈絡與 CM03 放入原檔 Figure 1／2，碳交易、Pareto、GA 補自製概念圖並附依據。計畫原圖僅本機預覽，公開重製權限待確認。延伸不固定三項：碳交易基礎與演算法各四項，研究資料與實驗各兩項，其他按實質內容安排。
- 最新介面調整：網站改名「碳交易 Wiki」、不加副標題，移除指定的頁首頁尾研究口號；卡片圓角矩形，桌機四欄、平板兩欄、手機單欄；灰色狀態字，展開淡入與排列位移動畫（尊重減少動態偏好）。研究正文與來源規則維持。
- 使用中性、白話的繁體中文研究指南；核心維持 CM03 第二年 Theme 2 多目標碳交易配對。
- 首頁方案 B：標題換頁，內文展開至少三張延伸子卡片；插入正常排列、推移後方卡片並換行，未完成項目不設假連結。
- CM03 本文逐段追溯原文章節與起句；歧義不自行修補。資料集與資料庫區稱「研究資料」。
- 最新核准：精簡 AGENTS.md 為本專案新增／修改頁面的開發憲法，整理 README 與交接；取消獨立 PROJECT_CONFIG.md，研究細節保存於 docs/research-notes.md；提供自行撰寫 Word／PDF 指南。
- 本批另核准新增基因演算法文章，證明文件可支持擴充；所有圖文須交代來源，說明查證範圍與規則。
- 每批先報估時與影響；本批完成後停止。不推送、不公開發布、不製作 Word／PDF，後續完善先討論。

## 目前成果
- 已推送 GitHub 並啟用 Pages： https://yangru413.github.io/Carbon-Trading-Research-Wiki/ 。2026-11-16 已實測 22 個公開頁面／資源 HTTP 200，公開瀏覽器的四欄卡片、圖片、動畫、GA 文章與返回路徑及手機寬度通過；詳見 docs/deployment-report.md。
- 9 個靜態頁面：首頁、研究脈絡、碳交易基礎、CM03、研究資料、Pareto、EMOBET、交易 log、基因演算法。
- content/ 是正文；data/pages.json 登記文章；data/topics.json 管理卡片；data/plan-references.json 管理 CM03 定位；data/literature-sources.json 管理外部文獻與閱讀範圍。
- 基因演算法文章包含逐段來源、自製流程圖、可重算的四位元限制式範例與書目。不是碳交易實驗，也不是 EMOBET 正式實作。
- AGENTS 已精簡；README 提供四個內容檔案的新增流程。舊 PROJECT_CONFIG 已退役，研究內容完整保存於備查，不要求新增頁面時全部閱讀。
- CM03 已核對 20 個原文段落定位與指紋；商品、變數、編碼長度、REVA／RVEA 差異仍待確認。
- 本批詳細證據見 docs/ga-page-proof.md；歷史紀錄見 docs/revision-report.md，舊頁數／三層架構已被本批更新。

## 原始資料與工具
- 原始素材 CM03-f.docx、Description_EUTL_database.pdf、ESD.csv、NOTESD.csv、about_eutl_log.txt 均不修改、不公開。EUTL_url.txt 與 RAG Notebook 目前未見。
- Abrell 文件為 2024-11-06 的 19 頁研究資料庫說明，不是本機 CSV 同版官方欄位手冊。CSV 只檢查表頭與前三筆：ESD 65 欄、NOTESD 67 欄，未做全檔分析或價格配對。
- NOTESD 約 1.51 GB；抽樣含 ERU，不能稱全檔純 EUA。早期文字異常未確認是否為編碼問題。
- Python：C:/Users/yuhua/anaconda3/python.exe。Playwright 在 .tools/vendor；使用既有 Edge，必要時既有 Chrome，不下載新瀏覽器。
- 正常使用 scripts/build-demo.py 與 scripts/check-demo.py；prepare-revision.py、reorganize-guidance.py 是已退役遷移腳本，不重跑。verify-ga-example.py 獨立核算教學範例。
- 公開倉庫：https://github.com/yangru413/Carbon-Trading-Research-Wiki 。Pages 已部署並驗證；後續新增內容依當批授權處理。

## 尚未完成
- 其餘主線與待整理延伸；未做碳交易最佳化實驗，也沒有實證效能結果。
- 使用者審閱本批成果；引文是否支持主張仍需人工判斷。
- 首次 GitHub 推送、Pages 部署與公開網址測試已完成；後續研究內容擴充先討論。
- Word／PDF 由使用者撰寫，docs/submission-guide.md 提供綱要。

自動檢查通過不代表整站完成學術審查或完整作業交付。
