"""Recompute the original teaching example; this is not a GA benchmark."""
from itertools import product
from pathlib import Path
import re

coefficients=(8,6,5,3)
def score(bits): return sum(c*int(x) for c,x in zip(coefficients,bits))
def feasible(bits): return sum(map(int,bits))<=2
parent_a,parent_b='1100','0011'
children=(parent_a[:2]+parent_b[2:],parent_b[:2]+parent_a[2:])
mutation=parent_a[:1]+'0'+parent_a[2:]
assert children==('1111','0000')
assert mutation=='1000'
examples=dict(zip(('A','B','C','D','M'),(parent_a,parent_b,*children,mutation)))
root=Path(__file__).resolve().parents[1]
text=(root/'content/genetic-algorithm.html').read_text(encoding='utf-8')
for key,bits in examples.items():
    row=re.search(r'<tr data-example-id="'+key+r'">(.*?)</tr>',text,re.S).group(1)
    cells=re.findall(r'<td>(.*?)</td>',row)
    assert cells==[bits,str(score(bits)),str(sum(map(int,bits))),'是' if feasible(bits) else '否'],(key,cells)
all_bits=[''.join(map(str,x)) for x in product((0,1),repeat=4)]
valid=[x for x in all_bits if feasible(x)]
best=max(map(score,valid))
optima=[x for x in valid if score(x)==best]
assert len(valid)==11 and best==14 and optima==['1100']
print('PASS: 5 article rows recomputed; 16 states enumerated, 11 feasible; unique optimum 1100, score 14. Not a GA performance experiment.')
