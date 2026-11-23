# v1.0.6 定案與graph檢查

日期：2026-11-23。使用者明確定案v1.0.5簡報內容與排版，並授權本批發布。

- **正文不動**：data/research-slides.json及css/slides.css與v1.0.5相同；10頁教學內容、版型及節點不變。HTML只更新共用資源及graph入口的版本參數。
- **規則落實**：AGENTS.md第6節、docs/slides-workflow.md包含完整框線、同頁圖示唯一、固定PC頁框／標題、無內部捲動、概念圖與來源、可讀字級、圖下置中旁註與視覺均衡。每次改簡報前必讀。
- **graph重畫**：01–07由上往下，各階段工作／檢查／產物與退回目的地清楚。沒有副標題或底部小備註，只保留一句loop。原創SVG，PNG為2800×4452。
- **實際loop**：人工檢視發現退回線穿過標籤；加入標籤底色、重新生成SVG／PNG後目視及畫布文字邊界檢查通過。沒有假稱重新執行已定案大綱或碳交易實驗。
- **永久程式實測**：scripts/check-slides.py在1280×720、1366×768、1440×900、1920×1080及390×844共50頁通過。PC頁框／標題固定、內容及來源完整、無內部捲動、框線完整、圖示不重複、必要圖解載入。手機自然頁高。
- **操作與備援**：側箭頭、鍵盤、首尾、跳頁、答案滑鼠／鍵盤開合、全文、深層連結、列印、無JS及圖下置中解釋通過，無頁面JS錯誤。
- **靜態與目視**：19頁425個站內連結／資源／錨點通過；檢視50頁測試截圖縮圖及graph，字級／配置沿用已定案版，不以程式取代學術或美感判斷。

[機器量測與SHA-256](validation/slides-v1.0.6.json) · [正式規則](slides-workflow.md) · [graph PNG](../assets/slides-workflow.png)

v1.0.5檢查紀錄保留原樣：[人工報告](https://github.com/yangru413/Carbon-Trading-Research-Wiki/blob/v1.0.5/docs/slides-self-check-v1.0.5.md)、[量測JSON](https://github.com/yangru413/Carbon-Trading-Research-Wiki/blob/v1.0.5/docs/validation/slides-v1.0.5.json)。舊報告中的「待定案」反映當時狀態，本次使用者明確定案已記於此處。
