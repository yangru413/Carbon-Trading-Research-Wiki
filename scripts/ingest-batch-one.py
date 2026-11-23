"""Apply the approved first source batch. Run once; never modifies raw sources."""
from pathlib import Path
from html import escape as e
import json

R=Path(__file__).resolve().parents[1]
D='2026-11-23'
def read(p): return (R/p).read_text(encoding='utf-8-sig')
def write(p,t): (R/p).write_text(t,encoding='utf-8')
def dump(p,v): write(p,json.dumps(v,ensure_ascii=False,indent=2)+'\n')

records=[
dict(key='benchmark2017',slug='reading-benchmarking',title='最佳化演算法如何公平比較？',authors='Beiranvand, V., Hare, W., & Lucet, Y.',year='2017',original='Best practices for comparing optimization algorithms',publication='Optimization and Engineering, 18, 815–848',doi='10.1007/s11081-017-9366-1',url='https://arxiv.org/abs/1709.08242v1',scope='arXiv:1709.08242v1，PDF第1–5頁，§1–§3；未讀完整篇。',problem='演算法的比較如何避免受到測試選擇與實驗設計誤導？',method='文獻綜述與比較方法整理，並非提出新求解器。',finding='先定比較目的，再選測試問題、執行實驗與分析；不同方法需使用相同測試集及評估尺度。',location='§1.2–§3；PDF第3–5頁',limit='主要討論序列單目標最佳化，不足以定義完整多目標評估。',parent='research-methodology.html',relation='用於安排研究步驟與實驗檢查；不由此指定碳價、權重或宣稱GA優於ACO。'),
dict(key='kyoto1998',slug='reading-kyoto-protocol',title='京都議定書：減量承諾與交易原則',authors='United Nations',year='1998',original='Kyoto Protocol to the United Nations Framework Convention on Climate Change',publication='United Nations；條約文件，所讀PDF封面版次',url='https://unfccc.int/resource/docs/convkp/kpeng.pdf',scope='封面、Article 3(1)、Article 17（PDF第4、16頁）；不是完整法律評註。',problem='締約方如何承擔減量義務，以及交易在履行義務中扮演何種角色？',method='法律條文規範承諾與參與條件，並非演算法或實驗研究。',finding='第17條允許附件B締約方為履行第3條承諾參與排放交易，並要求交易補充國內行動。',location='Article 3(1)、17；PDF第4、16頁',limit='1998是所讀PDF封面年份，議定書1997年通過；締約方機制不能直接當企業EUA交易規則。',parent='carbon-basics.html',relation='說明國際減量制度背景，不將京都誤寫成所有碳交易的唯一源頭。'),
dict(key='ets-history2025',slug='reading-eu-ets-history',title='EU ETS：制度階段如何影響研究',authors='European Commission',year='2025',original='Development of EU ETS (2005–2020)',publication='Directorate-General for Climate Action；June 5更新',url='https://climate.ec.europa.eu/areas-action/carbon-markets/eu-emissions-trading-system-eu-ets/development-eu-ets-2005-2020_en',scope='First steps、Phase 1–3及頁面更新日；官方歷史說明，非法律全文。',problem='不同年份的制度背景為何不能混用？',method='以歷史階段整理制度建立與改革，沒有使用因果估計或求解演算法。',finding='2003年採納指令、2005年啟動；第三期2013–2020改為歐盟統一總量，以拍賣為預設分配方式。',location='First steps、Phase 3 (2013–2020)',limit='2020樣本屬第三期；法律細節仍需核對當時有效條文，不能由概述推定全部交易資格。',parent='eu-ets-history.html',relation='將制度期間納入資料篩選與模型假設的檢查。'),
dict(key='abrell2024',slug='reading-eutl-database',title='EUTL資料如何整理成研究資料庫？',authors='Abrell, J.',year='2024',original='Database for the European Union Transaction Log',publication='EUETS.INFO；November 6資料庫說明',url='https://euets.info/',scope='使用者提供2024-11-06版19頁PDF：第1–5、14–15、18–19頁；網站為計畫入口，非已核定同版PDF連結。',problem='公開EUTL資訊分散，帳戶、設施與移轉難以串接。',method='下載、解析與清理資料，重建歷史帳戶關係，建立關聯式資料模型。',finding='交易資料需處理帳戶識別碼對照；最終表依日期、帳戶、原始交易ID及單位／交易類別彙整區塊。',location='§1、附錄A.3–A.4；PDF第3、14–15頁',limit='這是研究資料庫的處理方法，不是NOTESD同版欄位手冊；不能直接套代碼或把移轉視為成交。',parent='sources.html',relation='提供欄位對照、版本與資料粒度檢查的依據，不代表本機全檔已清洗。'),
dict(key='ant1996',slug='reading-ant-system',title='Ant System：人工螞蟻如何合作搜尋？',authors='Dorigo, M., Maniezzo, V., & Colorni, A.',year='1996',original='Ant system: Optimization by a colony of cooperating agents',publication='IEEE Transactions on Systems, Man, and Cybernetics, Part B (Cybernetics), 26(1), 29–41',doi='10.1109/3477.484436',url='https://faculty.washington.edu/paymana/swarm/dorigo96-itsmc.pdf',scope='作者稿PDF第1–7頁：摘要、§I–III；未完成實驗結果審閱，PDF頁與期刊頁不同。',problem='如何以合作的簡單代理搜尋組合最佳化方案？',method='Ant System：依資訊素及啟發式資訊機率構造解，完成後評估並更新資訊素；主要以TSP說明。',finding='搜尋包含構造、評估、更新與重複；已走訪城市的記錄協助維持合法路徑。',location='§II–III；作者稿PDF第5–7頁',limit='早期Ant System不等於所有ACO變體；TSP方法未直接驗證碳交易多目標配對。',parent='ant-colony-optimization.html',relation='作為ACO入門依據，配對改寫必須另外設計可行選擇、評分與限制處理。')]

lit=json.loads(read('data/literature-sources.json'))
pages=json.loads(read('data/pages.json'))
def register(slug,title,description):
    if not any(p['slug']==slug for p in pages): pages.append(dict(slug=slug,title=title,description=description,nav='home'))
def p(text,key=None,loc='',kind=None):
    attrs=(f' data-cite="{key}" data-location="{e(loc)}"' if key else '')+(f' data-kind="{kind}"' if kind else '')
    return f'<p{attrs}>{text}</p>'
def shell(title,body,back='index.html#route',tag='研究方法'):
    return f'<main id="main" class="wrap"><div class="lesson-position"><a href="{back}">← 返回相關主題</a></div><header class="article-hero"><span class="tag">{tag}</span><h1>{title}</h1><div class="meta"><span>更新：{D}</span></div></header><article class="prose">{body}<nav class="lesson-pager"><a href="{back}">返回相關主題</a><a href="literature.html">文獻索引 →</a></nav></article></main>'
for r in records:
    key=r['key']
    lit[key]=dict(authors=r['authors'],year=r['year'],title=r['original'],publication=r['publication'],url=r['url'],read_scope=r['scope'],supports=r['finding'],accessed=D,apa=f"{r['authors']} ({r['year']}). {r['original']}. {r['publication']}. "+('https://doi.org/'+r['doi'] if r.get('doi') else r['url']))
    if r.get('doi'): lit[key]['doi']=r['doi']
    b='<section><h2>原文題目與研究問題</h2>'+p(e(r['original']),kind='editorial')+p(r['problem'],key,r['location'])+'</section>'
    for heading,field in [('用什麼方法','method'),('本次核讀重點','finding'),('適用限制','limit')]: b+=f'<section><h2>{heading}</h2>'+p(r[field],key,r['location'])+'</section>'
    b+='<section><h2>與本研究的關係</h2>'+p('本站解讀：'+r['relation'],key,r['location'],'interpretation')+'</section><section><h2>閱讀範圍</h2>'+p(e(r['scope']),kind='editorial')+'</section><section><h2>APA書目與出處</h2>[[bibliography:'+key+']]</section>'
    write('content/'+r['slug']+'.html',shell(r['title'],b,r['parent'],'文獻摘要'))
    register(r['slug'],r['title'],r['problem'])

b='<section><h2>先說清楚要比較什麼</h2>'+p('演算法比較要先釐清目的，再選擇測試問題、執行實驗與分析報告。','benchmark2017','§1.2–§3')+p('本站建議：將研究問題寫成「在明定供需與資格下，哪些配對安排可行，且如何比較其取捨？」這是研究整理框架，不是計畫新增的正式模型。',kind='interpretation')+'</section>'
b+='<section><h2>從問題走到可檢查的實驗</h2><ol><li>界定商品、參與者與決策內容。</li><li>對照模型需要與資料實際可提供的欄位。</li><li>明列目標、限制與缺失資料假設。</li><li>選擇可表示此問題的求解方法。</li><li>用共同測試情境與評估方式比較。</li><li>報告限制與可交付的結果。</li></ol>'+p('本站整理：上述步驟結合本站既有制度、資料與模型頁；比較部分依 Beiranvand 等人（2017）。小樣本可先用於流程檢查，不能直接推論市場整體表現。','benchmark2017','§2–§3','interpretation')+'</section>'
b+='<section><h2>跨年度銜接</h2>'+p('CM03以第一年的企業永續分析、第二年交易配對與第三年規則研究形成脈絡。','benchmark2017','僅支持比較方法；跨年度安排見下段計畫定位','interpretation')
# Cross-year facts must use plan, never the benchmarking paper.
b=b.replace(p('CM03以第一年的企業永續分析、第二年交易配對與第三年規則研究形成脈絡。','benchmark2017','僅支持比較方法；跨年度安排見下段計畫定位','interpretation'),'<p data-plan-ref="year1,year2,year3">CM03以第一年的企業永續分析、第二年交易配對與第三年規則研究形成脈絡。</p>')
b+=p('本站交接建議：先確認可取得的企業識別對照、永續指標定義、版本與可用時間；第二年留下模型假設、資料處理規則、候選解與評估記錄。這是建議清單，不代表第一年已交付或第三年已採用。',kind='interpretation')+'</section><section><h2>延伸閱讀</h2><a href="reading-benchmarking.html">論文：公平比較的問題、方法與限制</a> · <a href="sources.html">研究資料</a> · <a href="genetic-algorithm.html">GA</a> · <a href="ant-colony-optimization.html">ACO</a></section><section><h2>來源</h2>[[bibliography:benchmark2017]]</section>'
write('content/research-methodology.html',shell('碳交易配對研究如何進行',b,'start.html'))
register('research-methodology','碳交易配對研究如何進行','研究問題、資料、模型、方法與評估的連接。')

b='<section><h2>先理解制度期間</h2>'+p('EU ETS於2005年啟動；2013–2020為第三期，採歐盟統一總量並以拍賣為預設分配方式。','ets-history2025','First steps；Phase 3')+p('本站解讀：分析2020樣本應先對照第三期規則；新制度不能無條件回套。官方歷史介紹不是完整法規，本頁尚不提供交易資格的法律判定。','ets-history2025','Phase 3','interpretation')+'</section><section><h2>研究如何使用</h2>'+p('本站整理：資料版本、研究期間與適用規則應共同記錄；再確認配額種類與帳戶資格。法律原文與更多來源尚待補充。',kind='interpretation')+'<a href="reading-eu-ets-history.html">官方文件摘要</a> · <a href="carbon-basics.html">碳交易基礎</a></section><section><h2>來源</h2>[[bibliography:ets-history2025]]</section>'
write('content/eu-ets-history.html',shell('EU ETS：制度階段與研究期間',b,'carbon-basics.html','制度背景'))
register('eu-ets-history','EU ETS：制度階段與研究期間','理解2020資料所處制度階段與法律查核限制。')

b='<section><h2>從螞蟻比喻理解搜尋</h2>'+p('蟻群最佳化（Ant Colony Optimization, ACO）的早期Ant System讓人工螞蟻逐步構造方案，依資訊素與啟發式資訊機率選擇，再更新搜尋記憶。','ant1996','§I–III；作者稿PDF第2–7頁')+'</section><section><h2>輸入、輸出與步驟</h2>'+p('原文以旅行推銷員問題（Traveling Salesman Problem, TSP）說明：輸入城市與距離，輸出尋得的巡迴路線。初始化 → 構造合法路線 → 評估長度 → 更新資訊素 → 重複。','ant1996','§II–III')+'</section><section><h2>微應用：把選擇看成配對</h2>'+p('本站自製示意：買方甲可向賣方乙或丙購買，先排除不符合資格或供給的選項，再逐步組成方案。資訊素可作搜尋記憶的比喻；這不是已實作的碳交易ACO，沒有指定價格、權重或效果。',kind='example')+'</section><section><h2>適用限制與研究關係</h2>'+p('原文的合法巡迴路徑不等於碳交易的供需可行性。配對使用前仍須另定表示法、評分與限制處理；不能將TSP效果直接當碳交易成效。','ant1996','§II–III','interpretation')+'<a href="reading-ant-system.html">原始論文摘要</a> · <a href="genetic-algorithm.html">比較閱讀：GA</a> · <a href="research-methodology.html">研究方法</a></section><section><h2>來源與閱讀限制</h2>'+p('本頁是首批來源整合的入門稿，目前僅一篇來源，未滿主要文章3–5篇要求；詳細機制與應用待補。',kind='editorial')+'[[bibliography:ant1996]]</section>'
write('content/ant-colony-optimization.html',shell('蟻群最佳化：合作搜尋與配對示意',b,'index.html#topic-methods'))
register('ant-colony-optimization','蟻群最佳化：合作搜尋與配對示意','ACO入門、原始方法與配對應用界線。')

def insert(file,marker,html):
    s=read(file); assert marker in s,file
    write(file,s.replace(marker,html+marker,1).replace('更新：2026-11-16','更新：'+D))
insert('content/start.html','[[extensions:overview]]','<section><h2>如何進行研究</h2>'+p('本站導讀：由研究問題走到資料、模型與實驗。先看研究步驟，再按主題查閱方法與文獻。',kind='editorial')+'<a href="research-methodology.html">研究方法與評估路徑 →</a> · <a href="literature.html">文獻摘要索引 →</a></section>')
insert('content/carbon-basics.html','[[extensions:basics]]','<section><h2>國際減量承諾與交易背景</h2>'+p('京都議定書第17條將排放交易置於履行減量承諾的框架，並規定交易補充國內行動；不表示購買配額本身就完成實際減排。','kyoto1998','Article 17；PDF第16頁')+'<a href="reading-kyoto-protocol.html">條約摘要與限制</a> · <a href="eu-ets-history.html">EU ETS制度階段</a><h3>來源</h3>[[bibliography:kyoto1998]]</section>')
insert('content/sources.html','[[extensions:datasets]]','<section><h2>資料清理：先對照識別碼與粒度</h2>'+p('Abrell的資料建置包含擷取、清理、帳戶關係重建與資料模型；交易區塊依日期、帳戶、原始交易ID及單位／類型彙整。','abrell2024','§1、附錄A.3–A.4；PDF第3、14–15頁')+p('本站檢查建議：先留存版本與原始欄位，再比較列數、交易ID及彙整數量。不能直接刪除重複ID，或把Abrell代碼表當作NOTESD同版規格。','abrell2024','附錄A.3–A.4','interpretation')+'<a href="reading-eutl-database.html">資料文件的方法與限制 →</a><h3>來源</h3>[[bibliography:abrell2024]]</section>')
insert('content/genetic-algorithm.html','[[bibliography:ea2002,whitley2005,deb2000]]','<section><h2>比較閱讀</h2><a href="ant-colony-optimization.html">ACO：從構造方案理解另一種搜尋方式</a> · <a href="research-methodology.html">比較方法前先確定研究目的</a></section>')

b='<section><h2>第一批來源</h2>'+p('已整合的五份來源包含學術論文、條約、官方歷史說明與研究資料文件。每頁明示實際閱讀範圍；不是全部全文讀完，也不代表各主題引用數已齊備。',kind='editorial')+'<ul>'+''.join(f'<li><a href="{r["slug"]}.html">{e(r["original"])}</a>（{r["year"]}）</li>' for r in records)+'</ul></section>'
write('content/literature.html',shell('文獻摘要與來源索引',b,'index.html#route','文獻索引'))
register('literature','文獻摘要與來源索引','按題目查閱研究問題、方法、用途與限制。')
dump('data/pages.json',pages);dump('data/literature-sources.json',lit)
topics=json.loads(read('data/topics.json'))
for t in topics:
    if t['id']=='overview': t['extensions'][0].update(title='研究如何進行：問題、資料與實驗',href='research-methodology.html',status='ready',parent='start.html')
    if t['id']=='basics': t['extensions'][2].update(href='eu-ets-history.html',status='ready',parent='carbon-basics.html')
    if t['id']=='methods': t['extensions'].append(dict(title='蟻群最佳化：合作搜尋與配對示意',summary='原始Ant System概念、步驟與研究應用限制。',href='ant-colony-optimization.html',status='ready',parent='index.html#topic-methods'))
dump('data/topics.json',topics)
insert('content/index.html','  <section class="section" id="route">','  <section class="section"><h2>研究導讀</h2><p>沿研究問題、資料、模型與實驗理解研究如何進行。</p><a class="button" href="research-methodology.html">閱讀研究導讀 →</a> <a href="#route">按主題查閱</a> · <a href="literature.html">文獻索引</a></section>\n')
print('Integrated five sources; created nine registered pages; updated existing articles and navigation.')
