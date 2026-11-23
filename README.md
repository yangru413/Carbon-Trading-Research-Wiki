# 碳交易 Wiki

目前版本：**v1.0.5**（2026-11-23）。第一個正式基準v1.0.0保留不動；版本見 `VERSION`，變更見 [CHANGELOG](CHANGELOG.md)。

- [完整需求摘要](docs/requirements-summary.md)：包含歷史要求、最新決策與暫緩項目。
- [第一版流程自檢報告](docs/slides-self-check-v1.0.0.md)：graph各階段產物、真實loop、測試與SHA-256證據。
- [逐頁修改與v1.0.1檢查](docs/slides-self-check-v1.0.1.md)：圖示、圖解、練習題與逐頁要求的驗證。
- [固定頁框與v1.0.2檢查](docs/slides-self-check-v1.0.2.md)：各頁尺寸、標題位置及換頁穩定性。
- [工作流程反思](docs/workflow-reflection.md)：出問題節點、檢查前移與作業三題。

以 CM03 第二年 Theme 2 為重心的繁體中文研究指南，連結碳交易基礎、配對模型、多目標、研究資料、求解及實驗。白話解釋保留學術限制；計畫摘要、本站解讀與示例分開標示。

## 1. 使用與文件分工

2026-11-23 首批 LLM Wiki 整合已加入「研究導讀＋主題查閱」雙入口與文獻摘要索引。實際來源、閱讀範圍、更新與驗證見 [維護紀錄](docs/wiki-log.md)；第一批五份來源已整合，不代表各主題3–5篇文獻或整份作業完成。`scripts/ingest-batch-one.py` 為一次性已執行遷移，請勿重跑，日常仍用下方建置流程。

教學簡報重製版依 [大綱](docs/slides-outline.md) → [逐頁稿](docs/slides-manuscript.md) → HTML製作。逐頁內容來源為 `data/research-slides.json`，建置時 `scripts/render-research-slides.py` 產生 `content/research-slides.html`，請改JSON而非直接改該片段。製作流程圖在 `assets/slides-workflow.svg`／`.png`；PNG可供使用者放入Word報告。

直接開啟 `index.html`，或在 VS Code 右鍵選 **Open with Live Server**。主題標題進章節，卡片內文展開／收合延伸子卡片；後續卡片推移並換行。未完成內容不設假連結，停用 JavaScript 時延伸全部顯示。

網站不設副標題；圓角卡片在桌機每列四張、平板兩張、手機一張。展開使用簡潔動畫，系統設定減少動態時停用；內容狀態以灰色呈現。

- **AGENTS.md**：本網站新增／修改頁面的開發憲法，包含格式、圖文來源、技術限制與檢查。
- **README.md**：實際操作、檔案位置、資料限制及可照做的新增流程。
- **PROJECT_CONTEXT.md**：進度、當前授權、驗證結果與待辦，不是研究證據。

原 PROJECT_CONFIG.md 已取消；研究專屬細節保留於 [研究設定備查](docs/research-notes.md)，其中舊授權／期限只作歷史記錄，最新工作範圍以 PROJECT_CONTEXT.md 為準。

## 2. 檔案位置

```text
content/                 正文 HTML 片段，不含共用頁首頁尾
data/pages.json          獨立正文頁登錄：slug、標題、摘要、導覽群組
data/topics.json         首頁主題與延伸項目、連結及狀態
data/plan-references.json CM03 原文定位與版本指紋
data/literature-sources.json 外部文獻、查閱範圍及主張用途
css/                     共用版型與卡片樣式
js/wiki.js               卡片展開互動
scripts/build-demo.py     靜態建置與共用頁首頁尾
scripts/check-demo.py     靜態、引用結構及可選瀏覽器／原檔檢查
docs/                    維護、來源查閱與驗證報告
*.html                   建置產物，可直接瀏覽；不要直接改稿
```

首頁正文在 `content/index.html`，卡片由資料產生。既有 Pareto、EMOBET、交易 log 延伸頁重用對應章節片段，由建置程式產生；一般新文章不必仿照這種抽取方式，使用下面的獨立正文登錄即可。

## 3. 新增一頁：以基因演算法為例

開始前依 AGENTS.md 回報估時，確認主題與核准範圍。新增頁面通常只需下列四個內容檔，不必改共用 UI 或互動程式。

### A. 查重與蒐集來源

檢查 `data/topics.json`、`data/pages.json` 與既有正文，確認沒有重複文章。直接查閱原始論文、作者版本或官方文件，記下作者、年份、題名、章節、網址、取得日期、實際讀取範圍及主張對照。

來源記於 `data/literature-sources.json`，來源鍵例如 `ea2002`。讀摘要就寫「僅摘要」，不要聲稱全文已讀；文獻查閱紀錄與未採用線索見 [GA 新增驗證](docs/ga-page-proof.md)。

### B. 建立正文

建立 `content/genetic-algorithm.html`。參考既有文章的 `<main id="main" class="wrap">`、`article-hero`、`prose`、來源及返回入口；不要複製共用 `<head>`、頁首或頁尾。

正文最低內容：標題、性質、摘要、所屬主題、更新日期、白話概念、正式名詞、方法與限制、研究關係、附近引用及完整書目。演算法另列輸入／輸出／流程；公式解釋變數、範圍與單位。所有圖文都交代來源或原創身分。

本專案可使用以下來源標記，建置會在段落旁產生來源註記：

```html
<p data-cite="ea2002" data-location="§2、§5.1">有文獻依據的白話整理。</p>
<p data-plan-ref="emobet">CM03 原文的摘要。</p>
<p data-kind="interpretation" data-plan-ref="emobet">依原文提出的本站解讀。</p>
<p data-kind="example">本站自製示意，不是真實研究數據。</p>
```

`data-plan-ref` 必須是已核對的定位鍵；新原文段落要建立新定位，不任意借用舊鍵。多個鍵用逗號分開。`data-cite` 指向外部文獻，可搭配 `data-location` 記實際章節；`[[bibliography:ea2002,whitley2005]]` 產生文章書目。

圖表使用 `<figure>` 與 `<figcaption>`，標作者／自製或改繪、依據、假設與授權；自製表格在標題／圖說交代。引用不代表可直接重製論文圖片。標題、卡片摘要與導覽承接所屬正文來源，不為 UI 文字捏造學術文獻。

### C. 登錄頁面

在 `data/pages.json` 加入：

```json
{
  "slug": "genetic-algorithm",
  "title": "基因演算法：表示、選擇與變異",
  "description": "GA 的基本機制、示意例子及其與 CM03 的關係。",
  "nav": "home"
}
```

`slug` 對應正文檔與輸出網址；不得重複或任意更名。`nav` 選既有 `home`、`cm03` 或 `sources`，代表目前頁首所屬群組。

### D. 建立可找到的入口

在 `data/topics.json` 的 `methods` 主題 `extensions` 加入或更新項目：

```json
{
  "title": "基因演算法：表示、選擇與變異",
  "href": "genetic-algorithm.html",
  "summary": "基本流程、可行性示意與 CM03 的研究連結。",
  "status": "ready",
  "parent": "index.html#topic-methods"
}
```

`ready` 才能帶有效 `href`；未完成用 `planned` 且不設連結。延伸數量按內容調整，不鎖定三項：演算法與法規可四至五項，研究資料、實驗等重複內容可合併一至兩項。文章上下提供返回所屬主題的實際連結。

### E. 建置、檢查、回報

```powershell
python scripts/build-demo.py
python scripts/check-demo.py
```

這兩步只需要 Python 標準函式庫，不需要研究原檔、API key 或後端。瀏覽器檢查是選配：

```powershell
python scripts/check-demo.py --browser
```

需要既有 Playwright 與 Edge（或已安裝 Chrome 備援）；本機工具目前在 `.tools/vendor`。缺少瀏覽器工具時可先做靜態檢查，但不得聲稱瀏覽器測試通過。

只有本機具有 CM03 原檔時，再做原文指紋核對：

```powershell
python scripts/check-demo.py --private-sources
```

檢查項目包含連結、頁面登錄、引用鍵、卡片狀態、排版、展開、返回與引用顯示。人工仍需核對主張與來源是否相符。完成後更新 PROJECT_CONTEXT.md，列出來源、實際驗證與限制；未經授權不推送或發布。

## 4. 研究素材與必要限制

| 素材 | 用途與界線 |
| --- | --- |
| CM03-f.docx | 原始研究計畫。第二年四目標、EMOBET、比較及評估安排的依據；不是已完成成果 |
| Description_EUTL_database.pdf | Jan Abrell（2024-11-06）研究資料庫說明，共19頁；不是兩份原始CSV的同版欄位規格 |
| ESD.csv／NOTESD.csv | 原始研究資料。只檢查表頭與少量樣本，未做全檔分析；不能整份視為純 EUA 成交資料 |
| about_eutl_log.txt | 隨附說明，擷取日與筆數檔名年份有差異，需核對版本 |

EUTL 移轉不等於買賣成交，不保證有價格；日期不直接當議價時點。區分交易列、交易ID、單位種類與數量。價格須交代商品／合約、口徑、幣別、單位、頻率、時區、來源與可觀察時點，避免前視偏誤。資料缺口、代理值與假設必須標記。

CM03 的商品範圍、二元配對／交易量符號、染色體長度及 REVA／RVEA 名稱有待釐清處；不擅自補成唯一模型。目標權重、參考向量權重與屬性權重不可混用。第一年與第三年作研究脈絡，不取代第二年主線。

原始檔、公司／帳戶資訊、`.tools/`、`.work/` 不公開，原檔唯讀。未見的 EUTL_url.txt 與 RAG Notebook 不視為已讀；RAG 教材不是碳交易證據，本版不需 RAG、LLM API、登入、付費服務或後端。詳細設定保留在 [研究備查](docs/research-notes.md)。

## 5. 發布與交付

Repository：<https://github.com/yangru413/Carbon-Trading-Research-Wiki>。

GitHub Pages：<https://yangru413.github.io/Carbon-Trading-Research-Wiki/>。

使用者已於 2026-11-16 授權首次推送與部署。Pages 使用 `main` 分支根目錄，`.nojekyll` 保留原生靜態檔案。後續改稿先執行建置及檢查，再依當批授權提交／推送；GitHub Pages 會隨分支更新重新部署。只上傳確認過的網站與維護文件，不使用 `git add .` 盲目上傳。原始研究資料及本機工具不公開。

完整作業需 Repository、可瀏覽網站、AGENTS.md 與 PDF 說明。Word／PDF 由使用者自行製作；[簡短撰寫指南](docs/submission-guide.md) 只提供大綱。未提供的評分條件不自行假定。網站沒有執行最佳化或驗證研究成效。
