"""Original educational SVG diagrams based on the cited Wiki examples."""
from pathlib import Path
from html import escape as e
R=Path(__file__).resolve().parents[1]
def svg(name,title,body,w=1000,h=300):
    text=f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="t d"><title id="t">{e(title)}</title><desc id="d">本站自製教學示意，非實證資料或文獻原圖。</desc><defs><marker id="a" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0 8 4 0 8" fill="#456648"/></marker></defs><rect width="100%" height="100%" rx="18" fill="#eef3e9"/><g font-family="Microsoft JhengHei,sans-serif" fill="#203b32">{body}</g></svg>'''
    (R/'assets'/name).write_text(text,encoding='utf-8')
def box(x,y,w,h,text,fill='#fffef9'):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{fill}" stroke="#a9bda0" stroke-width="2"/><text x="{x+w/2}" y="{y+h/2+8}" font-size="24" text-anchor="middle">{e(text)}</text>'
def text(x,y,s,size=22,color='#203b32',anchor='start'):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" text-anchor="{anchor}">{e(s)}</text>'
def arrow(x,y,x2,y2):return f'<path d="M{x} {y} L{x2} {y2}" fill="none" stroke="#456648" stroke-width="3" marker-end="url(#a)"/>'

b=text(65,37,'買方',19)+text(645,37,'賣方',19)
b+='<path d="M290 100 640 225M290 225 640 100" fill="none" stroke="#b5c3ab" stroke-width="2" stroke-dasharray="7 7"/>'
b+=arrow(290,100,635,100)+arrow(290,225,635,225)
for x,y,label in [(60,60,'企業甲'),(60,185,'企業乙'),(645,60,'企業丙'),(645,185,'企業丁')]:b+=box(x,y,230,80,label)
b+=text(470,160,'選擇交易對象',21,anchor='middle')
b+=text(60,295,'實線：一組示意配對　　虛線：其他候選關係',18)
svg('matching-example.svg','兩位買方與兩位賣方的候選配對',b,1000,330)

b=text(45,38,'親代',20)+text(390,38,'交配後代',20)+text(745,38,'限制檢查',20)
b+=box(35,65,230,65,'1100')+box(35,160,230,65,'0011')
b+=arrow(280,135,365,135)+text(325,180,'切點在第2位後',17,anchor='middle')
b+=box(385,65,230,65,'1111')+box(385,160,230,65,'0000')
b+=arrow(630,100,715,100)+arrow(630,195,715,195)
b+=box(730,65,235,65,'4項 → 不可行','#f6e7dc')+box(730,160,235,65,'0項 → 可行','#dfebd8')
b+=text(35,278,'示意限制：最多選兩項；產生後代不保證可行或更好。',20)
svg('ga-search-example.svg','基因演算法交配與限制檢查示意',b)

b=text(38,35,'逐步選路',20)
for x,y,label in [(90,90,'A'),(350,90,'B'),(350,230,'C'),(90,230,'D')]:
    b+=f'<circle cx="{x}" cy="{y}" r="25" fill="#fffef9" stroke="#8aa07b" stroke-width="2"/>'+text(x,y+8,label,23,anchor='middle')
b+='<path d="M115 90 325 90M350 115V205M325 230H115M90 205V115" fill="none" stroke="#456648" stroke-width="4" marker-end="url(#a)"/>'
b+='<path d="M110 110 330 210M110 210 330 110" stroke="#b2c1a8" stroke-width="2" stroke-dasharray="6 6"/>'
b+=arrow(420,155,500,155)
b+=box(525,55,420,70,'評估一條完整路線')+arrow(735,130,735,173)+box(525,185,420,70,'更新資訊素，再構造路線')
b+=text(35,290,'實線為一條候選巡迴；虛線為其他選項。選擇受資訊素與啟發式資訊影響。',18)
svg('aco-tour-example.svg','Ant System的路線構造與資訊素更新示意',b,1000,320)

b=text(35,35,'供給：乙最多10單位、丙最多5單位；甲需求12單位',22)
b+=box(35,65,420,70,'方案A：乙8 ＋ 丙4 ＝ 12','#dfebd8')+box(545,65,420,70,'方案B：乙11 ＋ 丙1 ＝ 12','#f6e7dc')
b+=text(55,180,'✓ 需求滿足，兩賣方均未超額',22)+text(565,180,'× 乙超過10單位上限',22)
b+=text(35,237,'可行性＝每一條限制都通過；總量相同，不代表兩個方案都可行。',21)
svg('feasibility-example.svg','同樣滿足需求但供給限制不同的兩個方案',b,1000,275)

for name,title,labels in [
('handoff-input.svg','第一年輸入資料示意',['企業代碼','指標定義','版本／時間']),
('handoff-records.svg','第二年研究紀錄示意',['資料規則','模型假設','候選解／評估']),
('handoff-rules.svg','第三年可追溯研究用途示意',['結果','規則解讀','假設與限制'])]:
    b=''
    for i,label in enumerate(labels):
        y=18+i*59
        b+=f'<rect x="35" y="{y}" width="250" height="45" rx="8" fill="#fffef9" stroke="#a9bda0"/>'+text(160,y+30,label,19,anchor='middle')
        if i<2:b+=arrow(160,y+45,160,y+56)
    svg(name,title,b,320,200)
# Narrow-screen compositions keep diagram text readable without horizontal scroll.
b=text(20,30,'買方',18)+text(220,30,'賣方',18)
b+='<path d="M130 80 220 170M130 170 220 80" fill="none" stroke="#b5c3ab" stroke-dasharray="5 5"/>'
b+=arrow(130,80,215,80)+arrow(130,170,215,170)
for x,y,label in [(20,50,'企業甲'),(20,140,'企業乙'),(225,50,'企業丙'),(225,140,'企業丁')]:b+=box(x,y,110,60,label)
b+=text(20,245,'實線：示意配對　虛線：其他候選',17)
svg('matching-example-mobile.svg','買賣方配對示意',b,360,275)
b=text(20,32,'親代',20)+box(20,50,140,60,'1100')+box(200,50,140,60,'0011')
b+=arrow(180,125,180,170)+text(200,155,'交配',18)
b+=text(20,200,'後代',20)+box(20,220,140,60,'1111')+box(200,220,140,60,'0000')
b+=arrow(90,290,90,340)+arrow(270,290,270,340)
b+=box(20,355,140,60,'不可行','#f6e7dc')+box(200,355,140,60,'可行','#dfebd8')
b+=text(90,450,'選4項',20,anchor='middle')+text(270,450,'選0項',20,anchor='middle')+text(20,490,'示意限制：最多選兩項。',18)
svg('ga-search-example-mobile.svg','交配後檢查後代可行性',b,360,525)
b=text(20,30,'構造一條候選路線',20)
for x,y,label in [(75,85,'A'),(285,85,'B'),(285,225,'C'),(75,225,'D')]:
    b+=f'<circle cx="{x}" cy="{y}" r="24" fill="#fffef9" stroke="#8aa07b"/>'+text(x,y+8,label,23,anchor='middle')
b+='<path d="M100 85H260M285 110V200M260 225H100M75 200V110" fill="none" stroke="#456648" stroke-width="3" marker-end="url(#a)"/><path d="M95 105 265 205M95 205 265 105" stroke="#b2c1a8" stroke-dasharray="5 5"/>'
b+=arrow(180,265,180,305)+box(25,325,310,65,'評估完整路線')+arrow(180,400,180,435)+box(25,450,310,65,'更新資訊素，再構造')
svg('aco-tour-example-mobile.svg','候選巡迴路線及資訊素更新',b,360,540)
b=text(20,32,'供給：乙最多10、丙最多5',20)+text(20,65,'需求：甲需要12單位',20)
b+=box(20,100,320,65,'A：乙8＋丙4＝12','#dfebd8')+text(25,205,'✓ 需求與供給限制均通過',19)
b+=box(20,255,320,65,'B：乙11＋丙1＝12','#f6e7dc')+text(25,360,'× 乙超過10單位上限',19)
b+=text(20,405,'總量相同，不一定都可行。',18)
svg('feasibility-example-mobile.svg','兩個方案的供需可行性比較',b,360,435)
print('Created seven original diagrams and four mobile compositions.')
