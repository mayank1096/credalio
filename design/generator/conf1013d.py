# conf1013d: ONB-003v (email confirmed) had its own older rain-from-the-top confetti; swap it for the shared
# confetti.py v3 burst (from the H1), so every success screen moves the same way. usage: python3 conf1013d.py <dir>
import os, re, sys
from confetti import CONF, add_css
p = os.path.join(sys.argv[1], 'CR-ONB-003v.dc.html'); s = open(p, encoding='utf-8').read()
assert 'cfFall' in s, 'already patched'
s = re.sub(r'@keyframes cfFall\{.*?\n\.cf\{[^\n]*\n@media \(prefers-reduced-motion: reduce\)\{\.cf\{display:none\}\}\n', '', s, count=1, flags=re.S)
s, n = re.subn(r'<div aria-hidden="true" style="position: absolute; left: 0; top: 0; width: 100%; height: 100%; overflow: hidden; pointer-events: none; z-index: 4">\s*(?:<span class="cf"[^>]*></span>\s*)+</div>\n?', '', s, count=1); assert n == 1
h = '<h1 class="ob-h1 ob-in" style="'; assert s.count(h) == 1
s = s.replace(h, h + 'position: relative; ', 1)
s = s.replace('>Your email is confirmed.</h1>', '>' + CONF + '<span style="position: relative; z-index: 1">Your email is confirmed.</span></h1>', 1)
s = add_css(s); assert 'cfFall' not in s
open(p, 'w', encoding='utf-8').write(s); print('ok')
