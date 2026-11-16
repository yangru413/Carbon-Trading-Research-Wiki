raise SystemExit('Retired migration: use README.md and scripts/build-demo.py; no files changed.')
"""One-time migration of derived content and creation of checked source locators."""
from pathlib import Path
import hashlib
import json
import re
import zipfile
import xml.etree.ElementTree as ET

root = Path(__file__).resolve().parents[1]
# Preserve the existing dataset explanation while moving it out of Python strings.
html = (root / 'sources.html').read_text(encoding='utf-8')
main = re.search(r'<main\b[^>]*>(.*?)</main>', html, re.S).group(1)
main = re.sub(r'<aside class="reference-banner">.*?</aside>', '', main, flags=re.S)
main = main.replace('有轉移紀錄，<br>就有實際成交價嗎？', '研究資料：<br>資料集、欄位與使用限制')
main = main.replace('資料來源', '研究資料').replace('資料與來源', '研究資料')
main = main.replace('先看表頭，再決定研究用途', 'CSV 欄位與研究用途')
main = main.replace('每項主張，都有回頭路', '參考文件與連結')
main = main.replace('這一版，先把研究說清楚', '整理範圍與限制')
main = main.replace('只讀取兩份', '讀取兩份').replace('先問對問題', '待釐清的研究問題')
main = main.replace('先提供三頁可導覽成品：首頁、CM03 第二年導讀、資料與來源。', '提供研究指南與計畫、資料查閱內容。')
main = re.sub(r'<p>依使用者最新決定，.*?</p>', '<p>本版整理研究脈絡、碳交易基礎、計畫解讀與研究資料；其餘章節及延伸項目依內容狀態標示。</p>', main, flags=re.S)
main = re.sub(r'<p>目前提供首頁、研究起點、第 1 課，.*?</p>', '<p>本版整理研究脈絡、碳交易基礎、計畫解讀與研究資料；其餘章節及延伸項目依內容狀態標示。</p>', main, flags=re.S)
main = main.replace('完整八頁、更多文獻導讀、PDF 專案說明與 GitHub Pages 公開部署尚未完成；進一步完善及推送、發布前，先與使用者討論確認。', '完整主線、補充專文、PDF 專案說明及公開部署尚未完成。')
main = main.replace('本示範版', '本版').replace('示範版範圍', '整理範圍')
main = re.sub(r'<div class="reading-card">.*?</div>', '<div class="reading-card"><h3>相關章節</h3><a href="cm03.html#questions">CM03 模型與資料的待釐清事項 →</a></div>', main, flags=re.S)
main = main.replace('</article>', '[[extensions:datasets]]</article>')
(root / 'content/sources.html').write_text('<main id="main" class="wrap">'+main+'</main>', encoding='utf-8')

ns = {'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main', 'm':'http://schemas.openxmlformats.org/officeDocument/2006/math'}
source = root / 'CM03-f.docx'
tree = ET.fromstring(zipfile.ZipFile(source).read('word/document.xml'))
paragraphs = [''.join(n.text or '' for n in p.iter() if n.tag in (f"{{{ns['w']}}}t",f"{{{ns['m']}}}t")) for p in tree.findall('.//w:p',ns)]
definitions = [
    ('scope','Summary and What to Do in this Project','相關本研究的國科會計畫有:'),
    ('year1','Theme 1 概述','Theme 1 analyzes the theories'),
    ('year2','Theme 2 概述','The ET problem does not only concern'),
    ('year3','Theme 3 概述','To resolve hierarchical and real number nature'),
    ('products','§3.2.1 ET problem','Two types of permits are sold'),
    ('roles','§3.2.1 ET problem','In this study, the corporates that purchase permits'),
    ('binary','§3.2.1 ET problem','1. Initially, it is formulated as the transportation-like problem.'),
    ('supply','§3.2.1 ET problem','Suppose that the entity'),
    ('amount','§3.2.1 ET problem','If xij denotes the amount of permit'),
    ('reputation','§3.2.1 ET problem','Furthermore, the selection of the idea energy receivers'),
    ('four','§3.2.1 ET problem','With the consideration of multiple object functions:'),
    ('pareto','§3.2.1 ET problem','Over the years, researchers have been interested'),
    ('emobet','§3.2.2 The EMO based ET (EMOBET) approach','To solve the advanced ET problem,'),
    ('encoding','§3.2.2 Representation','Representation: A chromosome is encoded'),
    ('vectors','§3.2.2 Adaptive reference vector update','To fit the irregular Pareto front shape,'),
    ('vector-parameters','§3.2.2 Adaptive reference vector update','In this study, the parameters θg'),
    ('comparison','§3.2.3 The experiment and performance comparison','The following five methods are compared'),
    ('ablation','§3.2.3 The experiment and performance comparison','The following two experiments are implemented'),
    ('difficulty','第二年預計可能遭遇之困難及解決途徑','The four objective functions presented in the proposal'),
    ('hrs','§3.3.4 The deliverables of the hierarchical RS approach','The deliverables of the HRS support:'),
]
refs = {}
for key, section, start in definitions:
    hits = [(i,p) for i,p in enumerate(paragraphs) if p.startswith(start)]
    assert len(hits) == 1, (key,len(hits))
    index, text = hits[0]
    # Short searchable incipit; exact paragraph hash validates the private original.
    incipit = ' '.join(text.split()[:12])
    refs[key] = {'section':section,'incipit':incipit,'paragraph_index':index,
                 'paragraph_sha256':hashlib.sha256(text.encode('utf-8')).hexdigest()}
(root/'data').mkdir(exist_ok=True)
(root/'data/plan-references.json').write_text(json.dumps({'source_file':source.name,'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'references':refs},ensure_ascii=False,indent=2),encoding='utf-8')
print(f'Migrated dataset explanation; verified {len(refs)} unique CM03 locators against original document.')
