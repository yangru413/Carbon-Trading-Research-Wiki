"""Validate the HTML teaching deck with an installed browser; never publishes."""
from pathlib import Path
import json,sys,hashlib
from datetime import datetime,timezone
R=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(R/'.tools/vendor'))
from playwright.sync_api import sync_playwright
out=R/'.work/preview';out.mkdir(parents=True,exist_ok=True)
results=[]
manuscript=json.loads((R/'data/research-slides.json').read_text(encoding='utf-8'))['slides']
assert len(manuscript)==10
with sync_playwright() as p:
    b=p.chromium.launch(channel='msedge',headless=True)
    for width,height in [(1440,1000),(390,844)]:
        context=b.new_context(viewport={'width':width,'height':height},reduced_motion='reduce')
        page=context.new_page();errors=[]
        page.on('pageerror',lambda error:errors.append(str(error)))
        page.goto((R/'research-slides.html').as_uri())
        assert page.locator('#slide-prev,#slide-next').count()==0
        for i in range(10):
            page.select_option('#slide-select',str(i))
            assert page.locator('.slide:visible').count()==1
            assert page.locator('#slide-status').inner_text()==f'{i+1} / 10'
            assert not page.evaluate('document.documentElement.scrollWidth>innerWidth'),(width,i)
            assert page.locator('img:visible').evaluate_all('(xs)=>xs.every(x=>x.complete&&x.naturalWidth>0)')
            assert page.locator(f'#slide-{i+1} h1,#slide-{i+1} h2').inner_text()==manuscript[i]['title']
            assert page.locator(f'#slide-{i+1} .slide-source a').count()>=1
            assert page.locator(f'#slide-{i+1} .slide-output').count()==1
            nodes=page.locator(f'#slide-{i+1} .research-flow li, #slide-{i+1} .slide-concepts > div')
            for node in nodes.all():
                assert node.locator('svg.node-icon').count()==1
                assert node.evaluate('(n)=>["Top","Right","Bottom","Left"].every(x=>parseFloat(getComputedStyle(n)["border"+x+"Width"])>0)'),(width,i,'incomplete node frame')
            page.screenshot(path=str(out/f'slides-{width}-{i+1}.png'),full_page=True)
            results.append({'width':width,'slide':i+1,'overflow':False})
        page.select_option('#slide-select','0')
        assert page.locator('#side-prev').is_disabled()
        page.locator('#side-next').click()
        assert page.locator('#slide-status').inner_text()=='2 / 10'
        page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
        box=page.locator('#side-prev').bounding_box()
        assert box and 0<=box['y']<height-40
        page.locator('#side-prev').click()
        assert page.locator('#slide-status').inner_text()=='1 / 10'
        page.locator('h1').click()
        page.keyboard.press('ArrowRight');assert page.locator('#slide-status').inner_text()=='2 / 10'
        page.keyboard.press('End');assert page.locator('#side-next').is_disabled()
        page.keyboard.press('Home');assert page.locator('#side-prev').is_disabled()
        page.select_option('#slide-select','4');page.locator('summary').click()
        assert page.locator('details').get_attribute('open') is not None
        page.locator('#view-all').click();assert page.locator('.slide:visible').count()==10
        assert not page.locator('.deck-side-nav').is_visible()
        page.locator('#view-all').click();assert page.locator('.slide:visible').count()==1
        page.goto((R/'research-slides.html').as_uri()+'#slide-7')
        assert page.locator('#slide-status').inner_text()=='7 / 10'
        page.emulate_media(media='print');assert page.locator('.slide:visible').count()==10
        assert not errors,errors
        context.close()
    context=b.new_context(java_script_enabled=False)
    page=context.new_page();page.goto((R/'research-slides.html').as_uri())
    assert page.locator('.slide:visible').count()==10
    b.close()
files=['data/research-slides.json','content/research-slides.html','research-slides.html','css/slides.css','js/slides.js','scripts/check-slides.py','scripts/render-research-slides.py','assets/slides-workflow.svg','assets/slides-workflow.png']
report={'version':(R/'VERSION').read_text(encoding='utf-8').strip(),'tested_at_utc':datetime.now(timezone.utc).isoformat(),'browser':'Microsoft Edge','results':results,'keyboard':True,'no_js':True,'print':True,'deep_link':True,'interaction_checks':['fixed side buttons after scroll','first/last boundaries','no duplicate bottom buttons','select navigation','question reveal','all-page view','manuscript titles match','source links and output on each slide'],'page_errors':[],'hash_policy':'SHA-256: text uses LF-normalized bytes for Git/Windows portability; PNG uses original bytes','sha256':{f:hashlib.sha256((R/f).read_bytes() if f.endswith('.png') else (R/f).read_bytes().replace(b'\r\n',b'\n')).hexdigest() for f in files}}
(R/'.work/slides-checks.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
if '--draft' not in sys.argv:
    public=R/'docs/validation';public.mkdir(exist_ok=True)
    (public/f'slides-v{report["version"]}.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('PASS: 20 slide/viewport checks; keyboard, select, reveal, all-page view, deep link, print and no-JS fallback; no page errors.')
