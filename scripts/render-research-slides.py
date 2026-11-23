"""Render the reviewed page manuscript; standard library only, no publication."""
from pathlib import Path
from html import escape as e
import json
R=Path(__file__).resolve().parents[1]
data=json.loads((R/'data/research-slides.json').read_text(encoding='utf-8'))
slides=data['slides']
assert len(slides)==10
# Original code-native line icons; decorative, with no added visible labels.
ICON_PATHS={
    'folder':'<path d="M3 7V5a1 1 0 0 1 1-1h5l2 2h9a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V7Z"/><path d="M3 9h18"/>',
    'model':'<rect x="3" y="3" width="6" height="6" rx="1"/><rect x="15" y="15" width="6" height="6" rx="1"/><path d="M9 6h9v9M6 9v9h9"/>',
    'chart':'<path d="M4 3v17h17M8 16v-5M13 16V7M18 16v-8"/>',
    'search':'<circle cx="10" cy="10" r="6"/><path d="m15 15 6 6"/>',
    'people':'<circle cx="9" cy="7" r="3"/><path d="M3 20v-3a6 6 0 0 1 12 0v3M16 4a3 3 0 0 1 0 6M18 13a5 5 0 0 1 3 5v2"/>',
    'shuffle':'<path d="M3 6h3c5 0 5 12 10 12h5M18 15l3 3-3 3M3 18h3c2 0 3-2 4-4M14 8c1-1 2-2 3-2h4M18 3l3 3-3 3"/>',
    'check':'<rect x="4" y="3" width="16" height="18" rx="2"/><path d="m8 12 3 3 6-6"/>',
    'leaf':'<path d="M20 3C8 3 3 7 4 14c1 6 9 6 12 2 3-4 4-8 4-13ZM4 21 15 9"/>',
    'refresh':'<path d="M20 8A8 8 0 0 0 6 5L3 8M3 3v5h5M4 16a8 8 0 0 0 14 3l3-3M21 21v-5h-5"/>',
    'document':'<path d="M5 3h10l4 4v14H5ZM14 3v5h5M8 12h8M8 16h8"/>',
    'target':'<circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="3"/><path d="M12 1v3M12 20v3M1 12h3M20 12h3"/>',
    'compass':'<circle cx="12" cy="12" r="9"/><path d="m16 8-2 6-6 2 2-6Z"/>',
    'wallet':'<rect x="3" y="5" width="18" height="15" rx="2"/><path d="M17 11h4v5h-4a2.5 2.5 0 0 1 0-5ZM3 8h18M6 5V3h11"/>',
    'trend':'<path d="M3 20V4M3 20h18M6 15l5-5 4 2 6-7M16 5h5v5"/>',
    'link':'<path d="m10 7 2-2a5 5 0 0 1 7 7l-2 2M14 17l-2 2a5 5 0 0 1-7-7l2-2M8 16l8-8"/>',
    'archive':'<rect x="3" y="3" width="18" height="5" rx="1"/><path d="M5 8v13h14V8M9 12h6"/>',
    'ruler':'<path d="m3 16 13-13 5 5L8 21ZM12 7l2 2M8 11l2 2M4 15l2 2"/>',
    'fingerprint':'<path d="M5 11a7 7 0 0 1 14 0M8 12a4 4 0 0 1 8 0v4M11 12v4c0 3-1 4-2 5M5 14v2M19 14v4M8 14v3M14 12v6l1 3"/>',
    'filter':'<path d="M3 4h18l-7 8v7l-4 2v-9Z"/>',
    'database':'<ellipse cx="12" cy="5" rx="8" ry="3"/><path d="M4 5v14c0 4 16 4 16 0V5M4 12c0 4 16 4 16 0"/>',
    'question':'<circle cx="12" cy="12" r="9"/><path d="M9 8a3 3 0 0 1 6 1c0 2-3 2-3 4M12 17h.01"/>',
    'shield':'<path d="m12 2 8 3v6c0 5-8 11-8 11S4 16 4 11V5ZM8 11l3 3 5-6"/>',
    'calculator':'<rect x="5" y="2" width="14" height="20" rx="2"/><path d="M8 6h8M8 11h1M12 11h1M16 11h.01M8 15h1M12 15h1M16 15h.01M8 19h1M12 19h1M16 19h.01"/>',
    'route':'<circle cx="5" cy="4" r="2"/><circle cx="19" cy="20" r="2"/><path d="M5 6v7a4 4 0 0 0 8 0V9a3 3 0 0 1 6 0v9"/>',
    'scope':'<path d="M9 3H3v6M15 3h6v6M3 15v6h6M21 15v6h-6"/><circle cx="12" cy="12" r="3"/>',
    'branch':'<circle cx="5" cy="4" r="2"/><circle cx="5" cy="20" r="2"/><circle cx="19" cy="5" r="2"/><path d="M5 6v12M7 16c7 0 12-3 12-9"/>',
    'flask':'<path d="M9 2h6M10 2v7L4 19a2 2 0 0 0 2 3h12a2 2 0 0 0 2-3L14 9V2M7 16h10"/>',
    'folder-search':'<path d="M12 20H4V5h5l2 2h9v4"/><circle cx="16" cy="16" r="4"/><path d="m19 19 3 3"/>',
    'balance':'<path d="M12 3v18M5 21h14M3 7h18M6 7l-4 8h8ZM18 7l-4 8h8Z"/>'
}
def node_icon(label,kind=None):
    groups=[('leaf',('永續','聲譽')),('folder',('資料','欄位','樣本','版本','第一年')),('refresh',('資訊素','更新','記憶')),('shuffle',('交配','突變')),('model',('模型','決策','限制','構造','選項')),('people',('族群','親代','配對','買方','賣方','第二年')),('chart',('評估','目標','表現','比較','利潤','成本')),('check',('可行','結論','第三年')),('search',('問題','方法','搜尋'))]
    kind=kind or next((name for name,words in groups if any(w in label for w in words)),'document')
    return '<svg class="node-icon" data-icon="'+kind+'" viewBox="0 0 24 24" aria-hidden="true" focusable="false" fill="none" stroke="currentColor" stroke-width="1.65" stroke-linecap="round" stroke-linejoin="round">'+ICON_PATHS[kind]+'</svg>'
def figure(d):
    assert (R/d['src']).is_file(),d['src']
    mobile=''
    if d.get('mobile'):
        assert (R/d['mobile']).is_file()
        mobile=f'<source media="(max-width:750px)" srcset="{e(d["mobile"])}">'
    return f'<figure class="teaching-diagram"><picture>{mobile}<img src="{e(d["src"])}" alt="{e(d["alt"])}"></picture><figcaption>{e(d["caption"])}</figcaption></figure>'
sections=[]
for i,s in enumerate(slides,1):
    for key in ('title','question','output','source','links'): assert s.get(key),(i,key)
    for link in s['links']:
        target=link['href'].split('#')[0]
        assert (R/'content'/target).is_file() or target in ('pareto.html','emobet.html','transaction-log.html'),link
    content=''
    if s.get('lead'): content+=f'<p class="slide-lead">{e(s["lead"])}</p>'
    if s.get('flow'):
        content+='<ol class="research-flow" aria-label="概念流程">'+''.join(f'<li>{node_icon(x,s.get("flow_icons",[None]*len(s["flow"]))[n])}<span>{e(x)}</span></li>' for n,x in enumerate(s['flow']))+'</ol>'
    if s.get('loop'): content+=f'<p class="loop-caption">↺ {e(s["loop"])}</p>'
    if s.get('columns'):
        items=[]
        for n,c in enumerate(s['columns']):
            illustration=f'<img class="handoff-image" src="{e(c["image"])}" alt="{e(c["heading"])}的交接材料示意">' if c.get('image') else ''
            items.append(f'<div><h3>{node_icon(c["heading"],s.get("column_icons",[None]*len(s["columns"]))[n])}<span>{e(c["heading"])}</span></h3>{illustration}<p>{e(c["text"])}</p></div>')
        content+='<div class="slide-concepts" style="--cols:'+str(len(s['columns']))+'">'+''.join(items)+'</div>'
        if s.get('diagram_note'): content+=f'<p class="diagram-note">{e(s["diagram_note"])}</p>'
    points='<ul class="slide-points">'+''.join(f'<li>{e(x)}</li>' for x in s.get('points',[]))+'</ul>'
    if s.get('image'):
        assert (R/s['image']).is_file()
        content+=f'<div class="slide-columns"><div>{points}</div><figure><img src="{e(s["image"])}" alt="{e(s["alt"])}"><figcaption>{e(s["caption"])}</figcaption></figure></div>'
    else: content+=points
    if s.get('diagram'):content+=figure(s['diagram'])
    if s.get('quiz'):
        content+=f'<details class="slide-check"><summary><span class="quiz-label">想一想</span><span class="quiz-question">{e(s["quiz"]["question"])}</span><span class="quiz-action"><span class="quiz-show">點我看答案 ＋</span><span class="quiz-hide">收起答案 −</span></span></summary><div class="quiz-answer"><strong>參考答案</strong><p>{e(s["quiz"]["answer"])}</p></div></details>'
    tag='h1' if i==1 else 'h2'
    links=' · '.join(f'<a href="{e(x["href"])}">{e(x["label"])}</a>' for x in s['links'])
    sections.append(f'''<section class="slide {e(s.get('class',''))}" id="slide-{i}" aria-labelledby="title-{i}" data-manuscript-page="{i}">
      <span class="slide-category">{i:02d} / {e(s['topic'])}</span><{tag} id="title-{i}">{e(s['title'])}</{tag}>
      <p class="teaching-question">{e(s['question'])}</p>
      {content}
      <p class="slide-output"><strong>{e(s['output_label'])}：</strong>{e(s['output'])}</p>
      <footer class="slide-source">{e(s['source'])}<br>{links}</footer>
    </section>''')
body='''<main id="main" class="wrap presentation">
  <div class="deck-toolbar"><a href="index.html">← 碳交易 Wiki</a><span>教學簡報 · 10頁</span><button type="button" id="view-all" hidden>展開全文</button></div>
  <noscript><p>目前顯示完整簡報；啟用JavaScript可逐頁閱讀。</p></noscript>
  <nav class="deck-side-nav" aria-label="畫面兩側換頁" hidden><button id="side-prev" class="side-prev" type="button" aria-label="上一頁" title="上一頁">‹</button><button id="side-next" class="side-next" type="button" aria-label="下一頁" title="下一頁">›</button></nav>
  <div class="slides">'''+ '\n'.join(sections)+'''</div>
  <nav class="deck-controls" aria-label="簡報換頁" hidden><label>跳到 <select id="slide-select" aria-label="選擇簡報頁面"></select></label><span id="slide-status" aria-live="polite" aria-atomic="true"></span></nav>
  <p class="deck-hint">點兩側箭頭或左右方向鍵換頁 · Home／End到首尾 · 展開全文可閱讀或列印全部頁面 · <a href="assets/slides-workflow.svg">查看簡報製作流程圖</a></p>
</main>'''
(R/'content/research-slides.html').write_text(body+'\n',encoding='utf-8')
notes=['# 教學簡報逐頁稿','','由data/research-slides.json生成；圖解與數字為已標示來源的教學示意。','']
for i,s in enumerate(slides,1):
    notes += [f'## P{i} {s["title"]}','','教學問題：'+s['question'],'']
    if s.get('lead'):notes += [s['lead'],'']
    if s.get('flow'):notes += ['流程：'+' → '.join(s['flow']),'']
    for c in s.get('columns',[]):notes += ['- '+c['heading']+'：'+c['text']]
    for item in s.get('points',[]):notes += ['- '+item]
    if s.get('diagram'):notes += ['', '圖解：'+s['diagram']['src'],'圖說：'+s['diagram']['caption']]
    if s.get('quiz'):notes += ['', '練習題：'+s['quiz']['question'],'答案：'+s['quiz']['answer']]
    notes += ['',s['output_label']+'：'+s['output'],'','來源：'+s['source'],'','Wiki：'+'；'.join(x['href'] for x in s['links']),'']
(R/'docs/slides-manuscript.md').write_text('\n'.join(notes).rstrip()+'\n',encoding='utf-8')
print('Rendered 10 teaching pages from the reviewed manuscript.')
