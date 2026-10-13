# scene5: designer 2026-10-13 — swap main scene v4 for v5 (same layout; organization = three people at an info board,
# validator ~58px further left). Moves the validator fade rect / floor glow and its mobile pan. usage: python3 scene5.py <dir>
import os, sys, re
P = sys.argv[1]
OLD, NEW = '/_blob/35f92c519316f253dc620c3c4b2d859c', '/_blob/c6a3cfeead45b159745cbe37bd22bc3f'
out = []
for f in sorted(os.listdir(P)):
    if not f.endswith('.dc.html'): continue
    p = os.path.join(P, f); s = open(p, encoding='utf-8').read()
    if OLD not in s: continue
    s = s.replace(OLD, NEW)
    s = s.replace('<rect x="1288" y="110" width="227"', '<rect x="1223" y="110" width="199"')
    s = s.replace('<ellipse cx="1401" cy="624" rx="93"', '<ellipse cx="1322" cy="624" rx="80"')
    s = s.replace('"validate": -48,', '"validate": -37,')
    s = s.replace('a learner, a creator, a validator and an organization team"', 'a learner, a creator, a validator and an organization team at a planning board"')
    open(p, 'w', encoding='utf-8').write(s); out.append(f)
print('scene5', len(out)); print(' '.join(out))
