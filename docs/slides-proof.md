# HTML 教學簡報製作與檢查

## 2026-11-23 graph重製版（優先於下方初版）
- 先整理 docs/slides-outline.md，依使用者「照這個流程再做一次」執行，保留原10頁順序。
- 再寫 data/research-slides.json 與可讀的 docs/slides-manuscript.md，逐頁包含問題、主旨、圖解、來源、產出；核對Wiki後才生成HTML。逐頁稿是AI核對，不冒充使用者逐頁確認。
- scripts/render-research-slides.py 由建置器呼叫，來源稿、產物不再各自手填；底部重複按鈕不再出現，兩側箭頭保持。
- 大綱及製作graph：assets/slides-workflow.svg／png，中央由上往下；每階段列要做的事及檢查，退回箭頭標明改稿或介面，不把研究graph與製作graph混用。
- 真實失敗：生成器一開始把Pareto衍生頁當作content原稿，導致建置失敗。改成識別既有衍生頁，再成功建置。失敗後舊HTML的靜態通過不算新版本通過，後續重新建置及檢查。
- PNG輸出直接開SVG截圖逾時，改用HTML容器輸出成功；此是輸出工具問題，不是論文內容矛盾。
- 重製版20組桌機／手機檢查通過：逐頁標題與稿一致、各頁來源與產出存在、無橫向溢出、圖片解碼、無JS錯誤；保留鍵盤、箭頭、跳頁、全文、列印、直接定位及無JS測試。圖文總覽與桌機第1／3頁、流程圖經目視核對。
- 尚待使用者試讀驗收；沒有新增學術來源、沒有重新執行碳交易最佳化，未推送發布。

日期：2026-11-23。成果：research-slides.html；正文 content/research-slides.html；樣式 css/slides.css；操作 js/slides.js。由 scripts/build-demo.py 建置，首頁已有入口，未推送發布。

## 從 Wiki 到簡報
| 頁 | 教學內容 | Wiki 知識來源 |
| --- | --- | --- |
| 1 | 閱讀目標與研究主線 | research-methodology.html |
| 2 | 配額、交易與減排的區分 | carbon-basics.html、eu-ets-history.html |
| 3 | 研究問題與四目標 | cm03.html#objectives |
| 4 | 資料可提供與仍缺少的資訊 | sources.html、reading-eutl-database.html |
| 5 | 欄位、模型及假設檢核 | sources.html#price、cm03.html#questions |
| 6 | GA概念與微示例 | genetic-algorithm.html |
| 7 | ACO概念與適用界線 | ant-colony-optimization.html、reading-ant-system.html |
| 8 | 可行性與公平比較 | research-methodology.html、reading-benchmarking.html |
| 9 | 跨年度銜接建議 | start.html、research-methodology.html |
| 10 | 概念回顧與深入入口 | Wiki導讀及文獻索引 |

每頁有來源或本站整理身分及返回Wiki連結，完整書目與閱讀範圍由文章與摘要頁提供。未從新來源添加研究結論；沒有碳交易實驗結果。

## 素材
只沿用 assets/allowance-exchange.svg、assets/ga-crossover.svg，均為既有本站自製示意，依據及假設保留在頁內與Wiki原圖說；未抓取外部新聞影像，未重製論文原圖。ACO流程為HTML文字示意，非文獻原圖。

## 驗證與實際修正
- 建置19頁；全站410個站內連結／資源／錨點通過。
- scripts/check-slides.py：1440×1000與390×844各檢查10頁，共20組；無橫向溢出、圖片解碼正常、無JavaScript錯誤。
- 測試方向鍵、Home／End、上一頁／下一頁邊界、跳頁、答案展開、全文模式、網址直接進第7頁、列印顯示全部10頁、停用JS顯示全文。
- 人工目視桌機第2頁、手機第7頁，發現換頁後標題有瀏覽器預設焦點外框；移除非互動標題外框，按鈕／連結焦點保留，再跑20組測試通過。
- 截圖與機器結果留私人 .work/preview/slides-*.png、.work/slides-checks.json；不當成公開研究資料。

## 限制
6分鐘為編排預估，未做受試者閱讀測量。教學內容仍需使用者審閱；自動測試不等於學術審查。未發布；Word／PDF由使用者製作。
