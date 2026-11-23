"""Draw an original top-to-bottom workflow; no external imagery."""
from pathlib import Path
from html import escape as e
R=Path(__file__).resolve().parents[1]
nodes=[
(100,150,'① 確認教學目標','做：確定讀者、主題與學習成果。','查：對象與深度是否合適？'),
(300,150,'② 查詢 Wiki 與來源','做：整理可用主張、限制與圖解。','查：主張有依據？計畫／假設／結果有區分？'),
(500,170,'③ 整理並確認大綱','做：安排10頁順序與每頁要回答的問題。','查：有無缺漏、重複？使用者是否確認？'),
(720,180,'④ 撰寫逐頁內容','做：寫標題、重點、圖解、來源與產出。','查：一頁一主旨？忠於 Wiki？沒有新增無據結論？'),
(950,150,'⑤ 生成 HTML 投影片','做：將逐頁稿排版，加入換頁、跳頁與全文模式。','查：圖文清楚？來源與回讀入口完整？'),
(1150,190,'⑥ 實際瀏覽與回歸檢查','查桌機／手機：溢出、遮擋、圖片與連結。','查操作：箭頭、鍵盤、首尾、跳頁、全文及列印。'),
(1400,150,'⑦ 使用者試讀與交付','做：依意見修正，保存成果與檢查紀錄。','查：是否看得懂、操作方便？未確認不寫已驗收。')]
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="1660" viewBox="0 0 1200 1660" role="img" aria-labelledby="title desc">','<title id="title">Wiki到投影片：由上往下的製作與檢查流程</title><desc id="desc">中央七階段由上往下。大綱不通過改大綱；證據不足返回來源；內容或介面失敗返回相應編輯，修改後再檢查。退回箭頭是規則，不表示每次都觸發。</desc>', '<defs><marker id="a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10" fill="#365744"/></marker><marker id="r" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10" fill="#a34e2b"/></marker></defs>', '<rect width="1200" height="1660" fill="#f7f4ec"/>','<g font-family="Microsoft JhengHei, sans-serif" fill="#203b32">','<text x="600" y="43" text-anchor="middle" font-size="30">從 Wiki 到教學投影片</text>']
for i,(y,h,title,line1,line2) in enumerate(nodes):
    fill='#e5eddf' if i in (2,5) else '#fffef9'
    parts.append(f'<rect x="220" y="{y}" width="780" height="{h}" rx="12" fill="{fill}" stroke="#8a9d7f" stroke-width="2"/>')
    for dy,text,size in [(37,title,26),(77,line1,20),(112,line2,20)]: parts.append(f'<text x="250" y="{y+dy}" font-size="{size}">{e(text)}</text>')
    if i==5:parts.append(f'<text x="250" y="{y+151}" font-size="20">不通過：只改對應部分，重測原問題與相關功能。</text>')
    if i<len(nodes)-1:
        ny=nodes[i+1][0]
        parts.append(f'<path d="M610 {y+h} V{ny-9}" fill="none" stroke="#365744" stroke-width="3" marker-end="url(#a)"/><text x="629" y="{(y+h+ny)//2+7}" font-size="17">通過</text>')
# Each return lane is outside the main reading spine.
parts+=['<path d="M220 580 H105 V520 H210" fill="none" stroke="#a34e2b" stroke-width="3" marker-end="url(#r)"/><text x="18" y="475" font-size="18" fill="#a34e2b">大綱需調整</text>',
'<path d="M1000 800 H1115 V375 H1010" fill="none" stroke="#a34e2b" stroke-width="3" marker-end="url(#r)"/><text x="1045" y="570" font-size="18" fill="#a34e2b">缺乏依據</text><text x="1045" y="600" font-size="18" fill="#a34e2b">回查來源</text>',
'<path d="M220 1250 H75 V795 H210" fill="none" stroke="#a34e2b" stroke-width="3" marker-end="url(#r)"/><text x="10" y="1000" font-size="18" fill="#a34e2b">文字錯誤</text><text x="10" y="1030" font-size="18" fill="#a34e2b">改逐頁稿</text>',
'<path d="M1000 1260 H1070 V1025 H1010" fill="none" stroke="#a34e2b" stroke-width="3" marker-end="url(#r)"/><text x="1080" y="1120" font-size="18" fill="#a34e2b">介面失敗</text><text x="1080" y="1150" font-size="18" fill="#a34e2b">改版面</text>',
'<text x="600" y="1596" text-anchor="middle" font-size="18">Loop：發現問題 → 回對應步驟修改 → 重測原問題與相關功能。</text>',
'</g></svg>']
(R/'assets/slides-workflow.svg').write_text('\n'.join(parts),encoding='utf-8')
print('Rendered original vertical workflow diagram.')
