"""Render the reviewed page manuscript; standard library only, no publication."""
from pathlib import Path
from html import escape as e
import json
R=Path(__file__).resolve().parents[1]
data=json.loads((R/'data/research-slides.json').read_text(encoding='utf-8'))
slides=data['slides']
assert len(slides)==10
sections=[]
for i,s in enumerate(slides,1):
    for key in ('title','question','output','source','links'): assert s.get(key),(i,key)
    for link in s['links']:
        target=link['href'].split('#')[0]
        assert (R/'content'/target).is_file() or target in ('pareto.html','emobet.html','transaction-log.html'),link
    content=''
    if s.get('lead'): content+=f'<p class="slide-lead">{e(s["lead"])}</p>'
    if s.get('flow'):
        content+='<ol class="research-flow" aria-label="概念流程">'+''.join(f'<li>{e(x)}</li>' for x in s['flow'])+'</ol>'
    if s.get('loop'): content+=f'<p class="loop-caption">↺ {e(s["loop"])}</p>'
    if s.get('columns'):
        content+='<div class="slide-concepts" style="--cols:'+str(len(s['columns']))+'">'+''.join(f'<div><h3>{e(c["heading"])}</h3><p>{e(c["text"])}</p></div>' for c in s['columns'])+'</div>'
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
