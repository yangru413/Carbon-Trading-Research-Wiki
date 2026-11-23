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
    'document':'<path d="M5 3h10l4 4v14H5ZM14 3v5h5M8 12h8M8 16h8"/>'
}
def node_icon(label):
    groups=[('leaf',('永續','聲譽')),('folder',('資料','欄位','樣本','版本','第一年')),('refresh',('資訊素','更新','記憶')),('shuffle',('交配','突變')),('model',('模型','決策','限制','構造','選項')),('people',('族群','親代','配對','買方','賣方','第二年')),('chart',('評估','目標','表現','比較','利潤','成本')),('check',('可行','結論','第三年')),('search',('問題','方法','搜尋'))]
    kind=next((name for name,words in groups if any(w in label for w in words)),'document')
    return '<svg class="node-icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false" fill="none" stroke="currentColor" stroke-width="1.65" stroke-linecap="round" stroke-linejoin="round">'+ICON_PATHS[kind]+'</svg>'
sections=[]
for i,s in enumerate(slides,1):
    for key in ('title','question','output','source','links'): assert s.get(key),(i,key)
    for link in s['links']:
        target=link['href'].split('#')[0]
        assert (R/'content'/target).is_file() or target in ('pareto.html','emobet.html','transaction-log.html'),link
    content=''
    if s.get('lead'): content+=f'<p class="slide-lead">{e(s["lead"])}</p>'
    if s.get('flow'):
        content+='<ol class="research-flow" aria-label="概念流程">'+''.join(f'<li>{node_icon(x)}<span>{e(x)}</span></li>' for x in s['flow'])+'</ol>'
    if s.get('loop'): content+=f'<p class="loop-caption">↺ {e(s["loop"])}</p>'
    if s.get('columns'):
        content+='<div class="slide-concepts" style="--cols:'+str(len(s['columns']))+'">'+''.join(f'<div><h3>{node_icon(c["heading"])}<span>{e(c["heading"])}</span></h3><p>{e(c["text"])}</p></div>' for c in s['columns'])+'</div>'
    points='<ul class="slide-points">'+''.join(f'<li>{e(x)}</li>' for x in s.get('points',[]))+'</ul>'
    if s.get('image'):
        assert (R/s['image']).is_file()
        content+=f'<div class="slide-columns"><div>{points}</div><figure><img src="{e(s["image"])}" alt="{e(s["alt"])}"><figcaption>{e(s["caption"])}</figcaption></figure></div>'
    else: content+=points
    if s.get('quiz'):
        content+=f'<details class="slide-check"><summary>{e(s["quiz"]["question"])}</summary><p>{e(s["quiz"]["answer"])}</p></details>'
    tag='h1' if i==1 else 'h2'
    links=' · '.join(f'<a href="{e(x["href"])}">{e(x["label"])}</a>' for x in s['links'])
    sections.append(f'''<section class="slide" id="slide-{i}" aria-labelledby="title-{i}" data-manuscript-page="{i}">
      <span class="slide-category">{i:02d} / {e(s['topic'])}</span><{tag} id="title-{i}">{e(s['title'])}</{tag}>
      <p class="teaching-question">{e(s['question'])}</p>
      {content}
      <p class="slide-output"><strong>這一步留下：</strong>{e(s['output'])}</p>
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
print('Rendered 10 teaching pages from the reviewed manuscript.')
