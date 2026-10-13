# inbox1013: designer 2026-10-13 — ONB-003b "Check your inbox" gets its own illustration (person cheering + envelope
# with tick, `design/illustrations/check-inbox.webp`, blob 57c3bf77…, 2000x667) instead of the main scene + role overlays.
# Same frame as ONB-003v (ob-illus-img, top mask, mobile pan). usage: python3 inbox1013.py <dir>
import os, re, sys
p = os.path.join(sys.argv[1], 'CR-ONB-003b.dc.html'); s = open(p, encoding='utf-8').read()
assert 'check-inbox' not in s and '57c3bf77' not in s
new = ('<div class="ob-illus ob-illus-img" aria-hidden="true" style="position: absolute; left: 50%; bottom: 0; height: clamp(160px, calc(100vh - 485px), min(40vh, 33.33vw)); aspect-ratio: 2000 / 667; transform: translateX(-50%); --pan: 40px; overflow: hidden; z-index: 1; -webkit-mask-image: linear-gradient(to bottom, transparent 0, #000 14%); mask-image: linear-gradient(to bottom, transparent 0, #000 14%)">\n'
       '<img src="/_blob/57c3bf77e5ea45493691feb0c503b6d5" alt="" data-src="check-inbox" style="position: absolute; left: 0; top: 0; width: 100%; height: 100%; display: block">\n</div>\n')
s, n = re.subn(r'<div class="ob-illus" aria-hidden="true".*?\n</div>\n', new, s, count=1, flags=re.S); assert n == 1
if '.ob-illus-img{width:auto' not in s:
    i = s.rfind('</style>', 0, s.find('</helmet>')); s = s[:i] + '@media (max-width: 960px){.ob-illus-img{width:auto !important}}\n' + s[i:]
open(p, 'w', encoding='utf-8').write(s); print('ok')
