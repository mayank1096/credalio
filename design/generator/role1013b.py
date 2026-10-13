# role1013b: designer "the image resets" — ONB-002's scene must look identical to Main's so it feels continuous:
# same desktop size (min(50vh, 33.33vw)), same mobile box (720x240, margin-top 8, Main pans), and the role
# highlight shows instantly (no cd-fade fade-in). usage: python3 role1013b.py <dir>
import os, sys
p = os.path.join(sys.argv[1], 'CR-ONB-002.dc.html'); s = open(p, encoding='utf-8').read()
i = s.find('<div class="ob-illus" aria-hidden="true"'); j = s.find('</div>', i); blk = s[i:j]
assert 'height: min(40vh, 33.33vw)' in blk
nb = blk.replace('height: min(40vh, 33.33vw)', 'height: min(50vh, 33.33vw)').replace('<svg class="cd-fade" ', '<svg ')
s = s[:i] + nb + s[j:]
a = '.ob-illus{position:relative !important;flex-shrink:0;align-self:flex-start;height:170px !important;width:510px !important;order:2;margin-top:4px;'
assert s.count(a) == 1
s = s.replace(a, '.ob-illus{position:relative !important;flex-shrink:0;align-self:flex-start;height:240px !important;width:720px !important;order:2;margin-top:8px;')
a = "{'learn': 106, 'create': 60, 'validate': -27, 'institution': -88}"
assert s.count(a) == 1
s = s.replace(a, "{'learn': 147, 'create': 83, 'validate': -37, 'institution': -122}")
open(p, 'w', encoding='utf-8').write(s); print('ok')
