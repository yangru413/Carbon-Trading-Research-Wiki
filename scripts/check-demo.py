"""Verify the local guide, original-document locators and inline card behavior."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import hashlib
import json
import re
import sys
import xml.etree.ElementTree as ET
import zipfile

ROOT=Path(__file__).resolve().parents[1]
class Document(HTMLParser):
    def __init__(self,path):
        super().__init__()
        self.path,self.ids,self.links,self.controls,self.paragraphs=path,set(),[],[],[]
        self.feed(path.read_text(encoding='utf-8'))
    def handle_starttag(self,tag,attrs):
        attrs=dict(attrs)
        if 'id' in attrs:
            assert attrs['id'] not in self.ids, f'duplicate ID: {self.path.name}: {attrs["id"]}'
            self.ids.add(attrs['id'])
        self.links.extend(attrs[key] for key in ('href','src') if key in attrs)
        if 'aria-controls' in attrs: self.controls.extend(attrs['aria-controls'].split())
        if tag=='p': self.paragraphs.append(attrs)

docs={p.name:Document(p) for p in ROOT.glob('*.html')}
checked=0
for name,doc in docs.items():
    for link in doc.links:
        url=urlsplit(link)
        if url.scheme or url.netloc: continue
        target=(ROOT/unquote(url.path)) if url.path else doc.path
        assert target.exists(),f'broken link: {name}: {link}'
        if url.fragment and target.suffix=='.html':
            assert url.fragment in docs[target.name].ids,f'broken anchor: {name}: {link}'
        checked+=1
    assert all(x in doc.ids for x in doc.controls),f'broken aria-controls: {name}'
topics=json.loads((ROOT/'data/topics.json').read_text(encoding='utf-8'))
for topic in topics:
    assert len(topic['extensions'])>=1
    if topic.get('href'): assert (ROOT/topic['href']).exists()
    for child in topic['extensions']:
        if child['status']=='ready': assert (ROOT/child['href']).exists()
        else: assert not child.get('href'),f'planned extension has fake link: {child["title"]}'

manifest=json.loads((ROOT/'data/plan-references.json').read_text(encoding='utf-8'))
if '--private-sources' in sys.argv:
    source=ROOT/manifest['source_file']
    assert source.is_file(),'Private source missing; use the public/static check without --private-sources'
    assert hashlib.sha256(source.read_bytes()).hexdigest()==manifest['source_sha256'],'CM03 version changed; review references'
    tree=ET.fromstring(zipfile.ZipFile(source).read('word/document.xml'))
    ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main','m':'http://schemas.openxmlformats.org/officeDocument/2006/math'}
    paragraphs=[''.join(n.text or '' for n in p.iter() if n.tag in (f"{{{ns['w']}}}t",f"{{{ns['m']}}}t")) for p in tree.findall('.//w:p',ns)]
    for key,ref in manifest['references'].items():
        text=paragraphs[ref['paragraph_index']]
        assert hashlib.sha256(text.encode('utf-8')).hexdigest()==ref['paragraph_sha256'],key
        assert text.startswith(ref['incipit']) or ' '.join(text.split()).startswith(ref['incipit']),key
    print(f'PASS: {len(manifest["references"])} private source paragraphs matched original CM03 version')
for name,doc in docs.items():
    for p in doc.paragraphs:
        if p.get('data-plan-ref'):
            assert all(key in manifest['references'] for key in p['data-plan-ref'].split(',')),name
plan_fragment=(ROOT/'content/cm03.html').read_text(encoding='utf-8')
for attrs,body in re.findall(r'<p([^>]*)>(.*?)</p>',plan_fragment,re.S):
    assert 'data-plan-ref=' in attrs or 'data-kind=' in attrs,body[:70]
for path in [ROOT/'content/start.html',ROOT/'content/carbon-basics.html',ROOT/'index.html',ROOT/'cm03.html',ROOT/'sources.html']:
    text=path.read_text(encoding='utf-8')
    assert not re.search(r'第\s*\d+\s*課|下一課預告|給第一天|新進研究者|菜鳥|試讀結束',text),path
for name in ('AGENTS.md','README.md','PROJECT_CONTEXT.md'):
    assert (ROOT/name).exists()
assert not (ROOT/'PROJECT_CONFIG.md').exists(),'Redundant configuration was not retired'
literature=json.loads((ROOT/'data/literature-sources.json').read_text(encoding='utf-8'))
pages=json.loads((ROOT/'data/pages.json').read_text(encoding='utf-8'))
slugs=[p['slug'] for p in pages]
assert len(set(slugs))==len(slugs),'Duplicate page registration'
for item in pages:
    assert (ROOT/'content'/f'{item["slug"]}.html').is_file()
    assert f'{item["slug"]}.html' in docs
for doc in docs.values():
    for p in doc.paragraphs:
        if p.get('data-cite'):
            assert all(key in literature for key in p['data-cite'].split(',')),doc.path.name
ga=(ROOT/'content/genetic-algorithm.html').read_text(encoding='utf-8')
for attrs,body in re.findall(r'<p([^>]*)>(.*?)</p>',ga,re.S):
    assert 'data-cite=' in attrs or 'data-plan-ref=' in attrs or 'data-kind=' in attrs or 'source-note' in attrs,body[:70]
figures=re.findall(r'<figure\b[^>]*>(.*?)</figure>',ga,re.S)
assert len(figures)>=2
for figure in figures:
    assert '<figcaption' in figure and '本站自製' in figure
for name in ('AGENTS.md','README.md','PROJECT_CONTEXT.md'):
    text=(ROOT/name).read_text(encoding='utf-8')
    # Retired filenames may be mentioned as history, never as a required input.
    assert not re.search(r'先讀[^\n]*再讀 PROJECT_CONFIG|完整讀取[^\n]*PROJECT_CONFIG',text),name
print(f'PASS: {len(docs)} pages; {checked} local links/assets/anchors; {len(topics)} topics with variable extension counts; GA source structure and page registry; public checks need no raw research files')

if '--browser' in sys.argv:
    sys.path.insert(0,str(ROOT/'.tools/vendor'))
    from playwright.sync_api import sync_playwright
    shots=ROOT/'.work/preview'
    shots.mkdir(parents=True,exist_ok=True)
    errors,results=[],[]
    with sync_playwright() as p:
        browser_name='Microsoft Edge'
        try:
            browser=p.chromium.launch(channel='msedge',headless=True)
        except Exception:
            # Fall back to an existing browser, never download one for QA.
            chrome=Path('C:/Program Files/Google/Chrome/Application/chrome.exe')
            if not chrome.exists(): raise
            browser=p.chromium.launch(executable_path=str(chrome),headless=True)
            browser_name='Google Chrome (installed; Edge startup failed)'
            print('Edge headless startup failed; checking with existing Chrome instead.')
        for width,height,mode in [(1440,1000,'desktop'),(768,1024,'tablet'),(390,844,'mobile')]:
            context=browser.new_context(viewport={'width':width,'height':height},device_scale_factor=1,reduced_motion='reduce')
            for filename in docs:
                page=context.new_page()
                page.on('pageerror',lambda err: errors.append(str(err)))
                page.goto((ROOT/filename).as_uri(),wait_until='load')
                page.evaluate('document.fonts.ready')
                assert page.locator('h1').count()==1,filename
                assert page.locator('.brand strong').inner_text()=='碳交易 Wiki'
                assert page.locator('.brand small').count()==0
                chrome=page.locator('.site-header,.site-footer').all_inner_texts()
                assert all('Theme 2' not in text and '分別標示' not in text for text in chrome)
                assert page.locator('nav[aria-label="主要導覽"] a[aria-current="page"]').count()==1,filename
                assert not page.evaluate('document.documentElement.scrollWidth > innerWidth'),f'overflow: {filename}/{mode}'
                await_images='async (xs)=>{xs.forEach(x=>x.loading="eager");await Promise.all(xs.map(x=>x.decode()));return xs.every(x=>x.naturalWidth>0)}'
                assert page.locator('img').evaluate_all(await_images),filename
                if filename=='index.html':
                    assert page.locator('h1').inner_text()=='碳交易 Wiki'
                    columns=page.locator('.topic-grid').evaluate('(x)=>getComputedStyle(x).gridTemplateColumns.split(" ").length')
                    assert columns=={'desktop':4,'tablet':2,'mobile':1}[mode]
                    assert page.locator('.topic-card').first.evaluate('(x)=>parseFloat(getComputedStyle(x).borderRadius)')==16
                    assert page.locator('.content-state').first.evaluate('(x)=>getComputedStyle(x).color')=='rgb(112, 112, 112)'
                    buttons=page.locator('.topic-expand')
                    assert buttons.count()==len(topics)
                    assert page.locator('[data-extension-child]:visible').count()==0
                    first=page.locator('#topic-overview .topic-expand')
                    next_card=page.locator('#topic-basics')
                    position='(x)=>({y:x.getBoundingClientRect().top+scrollY,x:x.getBoundingClientRect().left+scrollX})'
                    before=next_card.evaluate(position)
                    first.click()
                    assert first.get_attribute('aria-expanded')=='true'
                    assert page.locator('[data-extension-child="overview"]:visible').count()==3
                    after=next_card.evaluate(position)
                    assert after['y']>before['y']+30,f'cards did not move: {mode}'
                    main_box=page.locator('#topic-overview').bounding_box()
                    children=page.locator('[data-extension-child="overview"]')
                    boxes=[children.nth(i).bounding_box() for i in range(3)]
                    assert all(b['x']>=0 and b['x']+b['width']<=width+1 for b in boxes)
                    if columns==4:
                        assert all(abs(b['y']-main_box['y'])<2 for b in boxes),f'four-card row: {mode}'
                        assert next_card.bounding_box()['y']>main_box['y']+30,f'next row: {mode}'
                    else:
                        assert any(b['y']>main_box['y']+30 for b in boxes),f'no wrapping: {mode}'
                    first.click()
                    assert page.locator('[data-extension-child="overview"]:visible').count()==0
                    assert abs(next_card.evaluate(position)['y']-before['y'])<2
                    first.focus()
                    page.keyboard.press('Enter')
                    assert first.get_attribute('aria-expanded')=='true'
                    page.keyboard.press('Space')
                    assert first.get_attribute('aria-expanded')=='false'
                    # Multiple independent expansion groups; children remain in normal flow.
                    page.locator('#topic-datasets .topic-expand').click()
                    page.locator('#topic-methods .topic-expand').click()
                    assert page.locator('[data-extension-child="datasets"]:visible').count()==len(next(t for t in topics if t['id']=='datasets')['extensions'])
                    method_count=len(next(t for t in topics if t['id']=='methods')['extensions'])
                    assert page.locator('[data-extension-child="methods"]:visible').count()==method_count
                    assert not page.evaluate('document.documentElement.scrollWidth > innerWidth')
                    page.screenshot(path=str(shots/f'cards-expanded-{mode}.png'),full_page=True)
                    page.locator('[data-extension-child="datasets"] [data-extension-link]').click()
                    assert page.url.endswith('/transaction-log.html')
                    page.get_by_role('link',name='返回所屬章節 →',exact=True).click()
                    assert page.url.endswith('/sources.html#limits')
                    page.goto((ROOT/'index.html').as_uri(),wait_until='load')
                    page.locator('#topic-overview [data-topic-link]').click()
                    assert page.url.endswith('/start.html')
                    page.locator('[data-next-lesson]').click()
                    assert page.url.endswith('/carbon-basics.html')
                    page.locator('[data-prev-lesson]').click()
                    assert page.url.endswith('/start.html')
                if filename=='cm03.html':
                    # Every marked paragraph has its immediately adjacent source note.
                    missing=page.locator('p[data-plan-ref],p[data-kind]').evaluate_all('(xs)=>xs.filter(x=>!x.nextElementSibling?.matches("[data-source-annotation]")).length')
                    assert missing==0
                    detail=page.locator('.paragraph-source details').first
                    detail.locator('summary').click()
                    assert detail.get_attribute('open') is not None
                    assert 'CM03-f.docx' in detail.inner_text()
                if filename=='genetic-algorithm.html':
                    assert page.locator('.bibliography li').count()==3
                    assert page.locator('figure figcaption').count()==3
                    missing=page.locator('p[data-cite],p[data-plan-ref],p[data-kind]').evaluate_all('(xs)=>xs.filter(x=>!x.nextElementSibling?.matches("[data-source-annotation]")).length')
                    assert missing==0
                    page.get_by_role('link',name='返回求解方法與演算法 →',exact=True).click()
                    assert page.url.endswith('/index.html#topic-methods')
                    page.locator('#topic-methods .topic-expand').click()
                    page.get_by_role('link',name='基因演算法：表示、選擇與變異',exact=True).click()
                    assert page.url.endswith('/genetic-algorithm.html')
                page.goto((ROOT/filename).as_uri(),wait_until='load')
                page.locator('img').evaluate_all(await_images)
                page.screenshot(path=str(shots/f'{Path(filename).stem}-{mode}.png'),full_page=True)
                results.append({'page':filename,'viewport':mode,'overflow':False})
                page.close()
            context.close()
        fallback=browser.new_context(java_script_enabled=False,viewport={'width':390,'height':844})
        page=fallback.new_page()
        page.goto((ROOT/'index.html').as_uri(),wait_until='load')
        assert page.locator('[data-extension-child]:visible').count()==sum(len(t['extensions']) for t in topics)
        page.locator('#topic-overview [data-topic-link]').click()
        assert page.url.endswith('/start.html')
        fallback.close()
        motion=browser.new_context(viewport={'width':1440,'height':1000},reduced_motion='no-preference')
        page=motion.new_page()
        page.goto((ROOT/'index.html').as_uri(),wait_until='load')
        toggle=page.locator('#topic-overview .topic-expand')
        toggle.click()
        assert page.locator('.topic-grid').evaluate('(x)=>x.getAnimations({subtree:true}).length')>0
        page.evaluate('Promise.all(document.getAnimations().map(x=>x.finished.catch(()=>{})))')
        assert page.locator('[data-extension-child="overview"]:visible').count()==3
        toggle.click()
        toggle.click()
        page.evaluate('Promise.all(document.getAnimations().map(x=>x.finished.catch(()=>{})))')
        assert page.locator('[data-extension-child="overview"]:visible').count()==3
        page.screenshot(path=str(shots/'cards-four-columns-desktop.png'),full_page=True)
        page.emulate_media(reduced_motion='reduce')
        toggle.click()
        assert page.locator('.topic-grid').evaluate('(x)=>x.getAnimations({subtree:true}).length')==0
        motion.close()
        browser.close()
    assert not errors,errors
    report={'results':results,'page_errors':errors,'interaction_checks':['inline expansion pushes later cards','wrapping at three widths','collapse restores positions','independent expansions','keyboard Enter/Space','title navigation','child page and parent return','paragraph source disclosures','JavaScript disabled fallback']}
    report['browser']=browser_name
    (ROOT/'.work/demo-checks.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    print(f'PASS: {len(results)} browser page/viewport checks; inline flow/wrapping, keyboard, separate links, source disclosure, no-JS fallback; no page errors')
