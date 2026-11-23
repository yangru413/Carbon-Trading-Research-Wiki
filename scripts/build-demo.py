"""Build the local research guide. Standard library only; never publishes."""
from pathlib import Path
from html import escape
import json
import re

ROOT = Path(__file__).resolve().parents[1]
TOPICS = json.loads((ROOT/'data/topics.json').read_text(encoding='utf-8'))
REFS = json.loads((ROOT/'data/plan-references.json').read_text(encoding='utf-8'))
LITERATURE = json.loads((ROOT/'data/literature-sources.json').read_text(encoding='utf-8'))
TOPIC_BY_ID = {t['id']: t for t in TOPICS}
DATE = '2026-11-16'
EXTERNAL = {
    'eu-ets': ('歐盟執委會：About the EU ETS', 'https://climate.ec.europa.eu/areas-action/carbon-markets/about-eu-ets_en'),
    'rvea': ('Cheng 等人（2016）：大學典藏書目，僅核對名稱與書目', 'https://openresearch.surrey.ac.uk/esploro/outputs/journalArticle/A-Reference-Vector-Guided-Evolutionary-Algorithm/99513096002346'),
}
def e(text):
    return escape(str(text), quote=True)

def header(current):
    links = [('home','index.html','研究指南'),('cm03','cm03.html','CM03 計畫'),('sources','sources.html','研究資料')]
    nav = ''.join(f'<a href="{url}"'+(' aria-current="page"' if key==current else '')+f'>{label}</a>' for key,url,label in links)
    return f'<a class="skip" href="#main">跳至主要內容</a><header class="site-header"><div class="wrap header-inner"><a class="brand" href="index.html" aria-label="碳交易 Wiki 首頁"><span class="brand-mark" aria-hidden="true">C</span><span><strong>碳交易 Wiki</strong></span></a><nav class="nav" aria-label="主要導覽">{nav}</nav></div></header>'

def footer():
    return '<footer class="site-footer"><div class="wrap footer-inner"><p>碳交易 Wiki</p><p>更新・2026-11-16</p><a href="sources.html#scope">整理範圍與限制</a></div></footer>'

def extension_card(item, owner, index):
    card_id=f'extension-{owner}-{index}'
    ready=item.get('status')=='ready'
    title=f'<a href="{e(item["href"])}" data-extension-link>{e(item["title"])}</a>' if ready else f'<span>{e(item["title"])}</span>'
    return f'<article id="{card_id}" class="subcard" data-extension-child="{owner}"><span class="subcard-type">延伸閱讀・{e(TOPIC_BY_ID[owner]["title"])}</span><h3>{title}</h3><p>{e(item["summary"])}</p><span class="content-state">'+('已有內容' if ready else '待整理・未開放')+'</span></article>'

def topic_cards():
    cards=[]
    for t in TOPICS:
        owner=t['id']
        title=f'<a href="{e(t["href"])}" data-topic-link>{e(t["title"])}</a>' if t.get('href') else f'<span>{e(t["title"])}</span>'
        controls=' '.join(f'extension-{owner}-{i}' for i in range(len(t['extensions'])))
        cards.append(f'<article class="topic-card" id="topic-{owner}" data-topic="{owner}"><div class="card-top"><span class="tag">'+('計畫原文解讀' if owner=='plan' else '研究主題')+f'</span><span class="card-number">{e(t["order"])}</span></div><h2>{title}</h2><button class="topic-expand" type="button" aria-expanded="true" aria-controls="{controls}" aria-label="{e(t["title"])}：展開或收合延伸閱讀"><span class="topic-summary">{e(t["summary"])}</span><span class="topic-needs">{e(t["needs"])}</span><span class="expand-label">收合延伸閱讀（{len(t["extensions"])}） −</span></button><span class="content-state">'+('章節可查閱' if t.get('href') else '章節整理中')+'</span></article>')
        cards.extend(extension_card(item,owner,i) for i,item in enumerate(t['extensions']))
    return '<div class="topic-grid" id="topics">'+''.join(cards)+'</div>'

def extension_shelf(owner):
    t=TOPIC_BY_ID[owner]
    items=[]
    for x in t['extensions']:
        title=f'<a href="{e(x["href"])}">{e(x["title"])}</a>' if x.get('href') else e(x['title'])
        items.append(f'<li><h3>{title}</h3><p>{e(x["summary"])}</p><span class="content-state">'+('已有內容' if x.get('href') else '待整理・未開放')+'</span></li>')
    return '<aside class="extension-shelf" aria-label="延伸閱讀"><h2>延伸閱讀</h2><p class="extension-context">相關章節：'+e(t['title'])+'。各項補充可按研究需要查閱；待整理項目不提供空白連結。</p><ul class="extension-list">'+''.join(items)+'</ul></aside>'

def annotations(html):
    def replace(match):
        attrs, body=match.groups()
        keys=re.search(r'data-plan-ref="([^"]+)"', attrs)
        kind=re.search(r'data-kind="([^"]+)"',attrs)
        ext=re.search(r'data-external="([^"]+)"',attrs)
        cite=re.search(r'data-cite="([^"]+)"',attrs)
        location=re.search(r'data-location="([^"]+)"',attrs)
        if not (keys or kind or cite):
            return match.group(0)
        kind=kind.group(1) if kind else ('external' if cite and not keys else 'summary')
        labels={'summary':'計畫摘要','interpretation':'本站解讀','example':'示意範例','external':'外部來源','editorial':'編輯說明'}
        label=labels[kind]
        paragraph='<p'+attrs+'>'+body+'</p>'
        locators=[]
        sections=[]
        if keys:
            for key in keys.group(1).split(','):
                ref=REFS['references'][key]
                sections.append(ref['section'])
                locators.append(f'<li><strong>{e(ref["section"])}</strong><br>段落起句：<q lang="en">{e(ref["incipit"])}</q></li>')
        externals=''
        if ext:
            title,url=EXTERNAL[ext.group(1)]
            externals=f'<a href="{e(url)}">{e(title)}</a>；查詢 {DATE}。'
        if cite:
            for key in cite.group(1).split(','):
                source=LITERATURE[key]
                externals+=f'<a href="#ref-{e(key)}">{e(source["authors"])}（{e(source["year"])}）</a>；'
            if location:
                externals+=e(location.group(1))+'。'
        if keys:
            summary='；'.join(dict.fromkeys(sections))
            details=f'<details><summary>原文定位</summary><div>原始文件：{e(REFS["source_file"])}<ul>{"".join(locators)}</ul>起句用於本機文件搜尋；非全文轉載。{externals}</div></details>'
            note=f'<div class="paragraph-source" data-source-annotation><span>{label}｜{e(summary)}</span>{details}</div>'
        else:
            text={'example':'本站自製教學情境，非計畫數據或實驗結果。','editorial':'網站範圍或閱讀說明，非計畫原文主張。','external':externals,'interpretation':'本站依下列來源整理的解讀：'+externals}.get(kind,'本站整理。')
            note=f'<div class="paragraph-source" data-source-annotation><span>{label}｜{text}</span></div>'
        return paragraph+note
    return re.sub(r'<p([^>]*)>(.*?)</p>',replace,html,flags=re.S)

def process(body):
    body=re.sub(r'\[\[extensions:([a-z]+)\]\]',lambda m: extension_shelf(m.group(1)),body)
    def bibliography(match):
        items=[]
        for key in match.group(1).split(','):
            source=LITERATURE[key]
            doi=f' DOI：<a href="https://doi.org/{e(source["doi"])}">{e(source["doi"])}</a>。' if source.get('doi') else ''
            if source.get('apa'):
                items.append(f'<li id="ref-{e(key)}">{e(source["apa"])}<br><a href="{e(source["url"])}">原始來源／版本入口</a><br><small>實際查閱：{e(source["read_scope"])}<br>用途：{e(source["supports"])}<br>查詢：{e(source["accessed"])}</small></li>')
                continue
            items.append(f'<li id="ref-{e(key)}"><strong>{e(source["authors"])}（{e(source["year"])}）</strong>。<cite>{e(source["title"])}</cite>。{e(source["publication"])}。{doi}<br><a href="{e(source["url"])}">原始來源／作者公開版本</a><br><small>實際查閱：{e(source["read_scope"])}<br>用途：{e(source["supports"])}<br>查詢：{e(source["accessed"])}</small></li>')
        return '<ol class="bibliography">'+''.join(items)+'</ol>'
    body=re.sub(r'\[\[bibliography:([a-z0-9,\-]+)\]\]',bibliography,body)
    return annotations(body)

def page(filename,title,description,body,current):
    html=f'<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="description" content="{e(description)}"><meta name="theme-color" content="#203b32"><title>{e(title)}｜碳交易 Wiki</title><link rel="icon" href="assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="css/style.css"><link rel="stylesheet" href="css/learning.css"><link rel="stylesheet" href="css/wiki.css"><link rel="stylesheet" href="css/visuals.css"><script src="js/wiki.js" defer></script></head><body>{header(current)}{process(body)}{footer()}</body></html>'
    if 'academic-article' in body:
        html=html.replace('</head>','<link rel="stylesheet" href="css/article.css"></head>')
    if 'class="wrap presentation"' in body:
        html=html.replace('</head>','<link rel="stylesheet" href="css/slides.css"><script src="js/slides.js" defer></script></head>')
        html=html.replace('更新・2026-11-16','更新・2026-11-23')
    (ROOT/filename).write_text(html,encoding='utf-8')

if (ROOT/'data/research-slides.json').exists():
    import runpy
    runpy.run_path(str(ROOT/'scripts/render-research-slides.py'),run_name='__main__')
home=(ROOT/'content/index.html').read_text(encoding='utf-8').replace('[[topic-cards]]',topic_cards())
page('index.html','碳交易 Wiki','研究主題卡片、閱讀順序與可展開的延伸閱讀。',home,'home')

for item in json.loads((ROOT/'data/pages.json').read_text(encoding='utf-8')):
    stem=item['slug']
    assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',stem),f'Invalid page slug: {stem}'
    assert item['nav'] in ('home','cm03','sources'),f'Unknown navigation group: {stem}'
    page(stem+'.html',item['title'],item['description'],(ROOT/'content'/f'{stem}.html').read_text(encoding='utf-8'),item['nav'])

# Reuse reviewed material as dedicated extension pages, rather than creating empty destinations.
plan=(ROOT/'content/cm03.html').read_text(encoding='utf-8')
datasets=(ROOT/'content/sources.html').read_text(encoding='utf-8')
for filename,title,parent,parent_title,prerequisite,raw,section_id in [
    ('pareto.html','Pareto 支配與方案比較','cm03.html#pareto','CM03 計畫解讀・Pareto 與權重','交易配對與多個目標的概念',plan,'pareto'),
    ('emobet.html','EMOBET 的概念流程','cm03.html#methods','CM03 計畫解讀・方法','候選方案、配對與多目標的概念',plan,'methods'),
    ('transaction-log.html','交易 log 欄位與紀錄粒度','sources.html#limits','研究資料・欄位與研究用途','帳戶、移轉與單位種類的概念',datasets,'limits'),
]:
    section=re.search(r'<section id="'+section_id+r'">(.*?)</section>',raw,re.S).group(1)
    section=re.sub(r'^<h2>.*?</h2>','',section,flags=re.S)
    body=f'<main id="main" class="wrap extension-page"><div class="lesson-position"><a href="{parent}">← 返回所屬章節：{parent_title}</a><span>延伸閱讀</span></div><header class="article-hero"><span class="tag">延伸閱讀</span><h1>{title}</h1><div class="meta"><span>相關概念：{prerequisite}</span><span>更新：{DATE}</span></div></header><article class="prose extension-prose">{section}<nav class="lesson-pager" aria-label="返回主線"><a class="button" href="{parent}">返回所屬章節 →</a><a href="index.html#route">研究指南</a></nav></article></main>'
    page(filename,title,title+'，依現有計畫解讀與資料說明整理。',body,'sources' if filename=='transaction-log.html' else 'cm03')
print(f'Built {len(list(ROOT.glob("*.html")))} local HTML pages. No source upload, Git push or publication.')
