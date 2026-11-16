"""Read original sources without modifying them; write private derived notes."""
from pathlib import Path
import sys
import zipfile
import xml.etree.ElementTree as ET
import csv
import json

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / '.tools/vendor'))
from pypdf import PdfReader

out = ROOT / '.work'
out.mkdir(exist_ok=True)
ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
      'm': 'http://schemas.openxmlformats.org/officeDocument/2006/math'}
with zipfile.ZipFile(ROOT / 'CM03-f.docx') as archive:
    tree = ET.fromstring(archive.read('word/document.xml'))
    paragraphs = []
    for i, p in enumerate(tree.findall('.//w:p', ns)):
        text = ''.join(n.text or '' for n in p.iter() if n.tag in
                       (f"{{{ns['w']}}}t", f"{{{ns['m']}}}t"))
        paragraphs.append(f'[P{i}] {text}')
    (out / 'cm03-extracted.txt').write_text('\n'.join(paragraphs), encoding='utf-8')
reader = PdfReader(ROOT / 'Description_EUTL_database.pdf')
pdf_text = '\n\n'.join(f'[PDF page {i+1}]\n{page.extract_text()}'
                       for i, page in enumerate(reader.pages))
(out / 'eutl-extracted.txt').write_text(pdf_text, encoding='utf-8')
schemas = {}
for name in ('ESD.csv', 'NOTESD.csv'):
    with (ROOT / name).open(encoding='utf-8-sig', newline='') as handle:
        rows = csv.reader(handle)
        header = next(rows)
        sample = [next(rows) for _ in range(3)]
    schemas[name] = {'bytes': (ROOT / name).stat().st_size,
                     'columns': header, 'column_count': len(header),
                     'sample_row_lengths': [len(r) for r in sample],
                     'price_named_columns': [c for c in header if 'PRICE' in c.upper()]}
(out / 'csv-schema.json').write_text(json.dumps(schemas, ensure_ascii=False, indent=2), encoding='utf-8')
print(f'CM03: {len(paragraphs)} paragraphs; EUTL: {len(reader.pages)} pages')
print(json.dumps({k: {a: b for a, b in v.items() if a != 'columns'} for k, v in schemas.items()}, ensure_ascii=False))
print(pdf_text[:26000])
