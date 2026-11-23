# PROJECT_CONTEXT.md — 執行狀態與交接

更新：2026-11-23。本文件記錄決策、授權與待辦，不是研究證據。開發準則見 AGENTS.md，操作見 README.md。

## v1之後的本機視覺調整（尚未發布）
- 依使用者要求，簡報所有流程及概念節點改完整圓角外框與自製線條圖示；不加節點數字、不新增小標或內容。逐字文字比對及data/research-slides.json雜湊確認不變。
- 大張graph圈號改01–07，原有主線／檢查文字保留；沒有恢復已刪的副標題與底部備註。
- 20組簡報桌機手機與操作檢查、19頁416個站內連結檢查通過；新增逐節點完整邊框／單一圖示斷言。機器結果留.work/slides-checks.json，未覆蓋v1.0.0公開驗證紀錄。
- 本批未推送、不移動v1.0.0標籤。

## 第一版基準與本批授權（優先於下方歷史狀態）
- 使用者要求截至目前所有可公開成果定為第一版，以Git管理版本並推送GitHub；使用v1.0.0標籤，保留先前提交歷史。原始研究檔、.work與.tools仍不公開。
- 已完成完整需求摘要 docs/requirements-summary.md、反思 docs/workflow-reflection.md、最新版自檢 docs/slides-self-check-v1.0.0.md及公開驗證JSON／兩張截圖。
- graph已刪副標題及最底備註，只保留主標題與一句loop。19頁416站內連結、全站57組及簡報20組瀏覽器檢查通過；驗證檔案SHA-256一致。
- 額外3–5篇引用等補強依使用者要求暫緩，不列為v1已達成。未做研究最佳化或完整學術審查。
- Git提交／遠端狀態以版本紀錄與本批交付為準；下方「未發布」為先前批次歷史。

## 2026-11-21 本批進度（優先於下方歷史批次）
### 2026-11-23 更新（取代下方未整合狀態）
- 最新graph重製：按已確認10頁大綱，先保存 docs/slides-outline.md，再寫 data/research-slides.json／docs/slides-manuscript.md，核對後生成HTML。新增直向製作流程圖 assets/slides-workflow.svg／png，20組桌機手機測試通過，待使用者試讀，未發布。
- 最新介面：底部重複上一頁／下一頁已移除，只留兩側固定箭頭、跳頁選單與頁碼；20組簡報驗證通過。
- 簡報新增畫面左右固定換頁箭頭，避免必須捲到頁尾；桌機／手機與捲動後換頁驗證通過。
- 最新：依使用者要求完成10頁教學HTML簡報 research-slides.html，首頁有入口；沿用既有兩張自製示意圖，未新增外部素材。全站19頁／410站內連結通過；簡報20組桌機手機與操作檢查通過。詳見 docs/slides-proof.md。此項取代下方「簡報未完成」，未發布。
- 使用者確認執行第一批五來源 ingest；已完成五篇文獻摘要、研究方法／EU ETS／ACO文章及文獻索引，共新增9頁，全站18頁。
- 研究脈絡、碳交易基礎、研究資料與GA頁已補連結或內容；首頁具研究導讀／主題查閱雙入口。
- 五來源均有閱讀範圍、APA書目及跨頁整合；京都第17條與Ant System方法段補讀，未宣稱完整全文審查。
- 建置與靜態檢查通過：18頁、378個站內連結／資源／錨點；新增頁有入站連結，無 .work 資源連結。瀏覽器結果另見本批紀錄。
- 仍缺各主要文章3–5篇完整支持，EU ETS法律原文及ACO其他文獻待補；HTML簡報、素材與完整語意lint未完成，未發布。
- 最新使用者決策：改為一次五篇集中討論後整合；取代逐篇停下詢問。第一批閱讀與整合提案在 docs/source-batch-01.md；尚未整合公開正文，未計五篇完成 ingest。
- 需求訪談完成，使用者要求開始執行；已重寫 AGENTS.md，改為 LLM Wiki 知識維護規範。
- 雙入口：研究導讀＋主題查閱；改造方案見 docs/wiki-rework-plan.md，實際操作紀錄見 docs/wiki-log.md。
- 本批完成規則與架構，尚未新 ingest、改正文、下載素材或生成簡報；不將既有引用自動計入本次五篇要求。
- 初期逐篇閱讀並討論後整合；穩定後可同主題批次。定期更新頻率未定，尚無排程。
- 下一步提出來源候選並開始第一篇閱讀討論。推送與發布尚未獲本批授權。

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
