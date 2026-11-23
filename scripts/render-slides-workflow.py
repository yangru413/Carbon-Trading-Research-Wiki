"""Render the approved top-to-bottom production graph as original SVG artwork."""
from pathlib import Path
from html import escape

R = Path(__file__).resolve().parents[1]
stages = [
    ('確認教學目標', [
        '做：確認讀者、主題、深度與學習成果。',
        '查：初學者能理解嗎？內容聚焦研究如何進行嗎？',
        '留：已確認的目標與範圍。']),
    ('查詢 Wiki 與來源', [
        '做：先查索引，再讀正文、引用與相關圖解。',
        '查：主張有依據？事實、計畫、假設與結果有區分？',
        '查：圖片來源、可公開權限與數據身分清楚？',
        '留：可用主張、來源、限制與缺口。']),
    ('整理並確認大綱', [
        '做：安排頁序、每頁主旨與教學問題。',
        '查：有無缺漏或重複？使用者確認後才寫逐頁稿。',
        '留：大綱；未通過就留在本階段調整。']),
    ('撰寫逐頁內容', [
        '做：寫解釋、例子、圖解、引用與每頁結論。',
        '查：忠於 Wiki，解釋足夠；不增添無據結論。',
        '查：演算法等抽象概念有示意圖、依據及假設。',
        '查：整理結論用「懶人包」，研究交付用「產出成果」。',
        '留：逐頁稿；依據不足回 02，內容不足在此補寫。']),
    ('生成 HTML 與排版', [
        '做：依稿生成 HTML；保留換頁、跳頁與 Wiki 入口。',
        '查：節點有完整框線、貼切圖示；同頁圖示不重複。',
        '查：固定頁框及標題；圖文錯開，不以加圖撐高頁面。',
        '查：沒有頁內捲動區；答案展開可延長整頁。',
        '查：字級適中、圖說貼近圖片；圖文間距及留白均衡。',
        '查：過空先補必要解釋／重排，再補有來源授權的圖。',
        '留：HTML；解釋不足回 04，版面問題在此修正。']),
    ('實際瀏覽與回歸檢查', [
        '查桌機：四種 PC 尺寸完整顯示，換頁標題不跳。',
        '查手機：不水平溢出，沒有任何內部捲動容器。',
        '查圖文：圖像完整、字可讀、框線／圖示／來源正確。',
        '查操作：箭頭、鍵盤、跳頁、答案開合與連結。',
        '查備援：全文、列印、深層連結與無 JavaScript。',
        '留：截圖與量測；人工再核對內容、圖解及視覺平衡。',
        '不通過：回 04 修內容或回 05 修介面，再重測此處。']),
    ('使用者試讀、定案與發布', [
        '做：使用者試讀；問題依性質回 02／04／05 修正。',
        '查：重做 06，使用者明確定案後才標示已驗收。',
        '做：保存版本與檢查紀錄，依當批授權推送 GitHub。',
        '查：公開簡報與圖片的版本、內容與本機一致。'])
]
width = 1400
x, box_width = 220, 960
y = 100
nodes = []
for title, lines in stages:
    h = 86 + len(lines) * 34
    nodes.append((y, h, title, lines))
    y += h + 54
height = y + 24
parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
    '<title id="title">從 Wiki 到教學投影片</title>',
    '<desc id="desc">七階段由上往下。每階段列出工作、檢查及產物。內容失敗回04；介面失敗回05；缺乏依據回02。修改後重做06。橘色箭頭是條件式退回規則，不表示每次都觸發。</desc>',
    '<defs><marker id="forward" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10" fill="#365744"/></marker><marker id="return" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10" fill="#a34e2b"/></marker></defs>',
    f'<rect width="{width}" height="{height}" fill="#f7f4ec"/>',
    '<g font-family="Microsoft JhengHei, sans-serif" fill="#203b32">',
    '<text x="700" y="53" font-size="36" text-anchor="middle">從 Wiki 到教學投影片</text>']
for i, (top, h, title, lines) in enumerate(nodes):
    fill = '#e8efe2' if i in (2, 5) else '#fffef9'
    parts += [f'<rect x="{x}" y="{top}" width="{box_width}" height="{h}" rx="17" fill="{fill}" stroke="#9aaf8d" stroke-width="2"/>',
        f'<text x="{x+28}" y="{top+46}" font-size="31" font-weight="600" fill="#58734e">{i+1:02d}</text>',
        f'<text x="{x+104}" y="{top+46}" font-size="29" font-weight="600">{escape(title)}</text>']
    for j, line in enumerate(lines):
        parts.append(f'<text x="{x+28}" y="{top+88+j*34}" font-size="24">{escape(line)}</text>')
    if i < len(nodes)-1:
        bottom = top+h
        parts.append(f'<path d="M700 {bottom+4} V{nodes[i+1][0]-9}" fill="none" stroke="#365744" stroke-width="3" marker-end="url(#forward)"/><text x="722" y="{bottom+33}" font-size="19" fill="#58734e">通過</text>')

def return_path(start, target, lane, labels, label_x, label_y):
    parts.append(f'<path d="M{start[0]} {start[1]} H{lane} V{target[1]} H{target[0]}" fill="none" stroke="#a34e2b" stroke-width="3" marker-end="url(#return)"/>')
    parts.append(f'<rect x="{label_x-8}" y="{label_y-27}" width="190" height="72" rx="8" fill="#f7f4ec"/>')
    for j, label in enumerate(labels):
        parts.append(f'<text x="{label_x}" y="{label_y+j*31}" font-size="23" fill="#a34e2b">{escape(label)}</text>')

return_path((1180, nodes[3][0]+92), (1190, nodes[1][0]+90), 1260,
            ['依據不足', '回 02 閱讀'], 1210, nodes[2][0]+70)
return_path((220, nodes[5][0]+120), (210, nodes[3][0]+95), 60,
            ['內容／解釋不足', '回 04 修改'], 18, nodes[4][0]+42)
return_path((1180, nodes[5][0]+205), (1190, nodes[4][0]+140), 1315,
            ['版面／操作失敗', '回 05 修改'], 1205, nodes[4][0]+235)
parts += [f'<text x="700" y="{height-28}" text-anchor="middle" font-size="24">Loop：發現問題 → 回對應步驟修改 → 重測原問題與受影響項目。</text>', '</g></svg>']
(R/'assets/slides-workflow.svg').write_text('\n'.join(parts)+'\n', encoding='utf-8')
print(f'Rendered approved vertical graph: {width} x {height}.')
