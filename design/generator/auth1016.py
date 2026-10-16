"""Designer 2026-10-16: one illustration (auth-scene.webp) behind every sign-up form and log-in page.
Patches LIVE CR-ONB-003 (create account; replaces its own illustration) and CR-ONB-003c (password; replaces the campus scene).
The CR-LOG sources pick the scene up from CR-ONB-003c when log1016.py is re-run.
Usage: python3 auth1016.py <canvas/project dir>"""
import os, re, sys
P = sys.argv[1]
NEW = '/_blob/2f4b6a89779043fb2ec851f8050aa46a'
SCENE_CSS = ('.ob-scene{position:absolute;left:0;right:0;bottom:0;height:min(48vh,44vw);background:url(%s) 50%% 100%% / cover no-repeat;z-index:-1;pointer-events:none}\n'
             '@media (max-width: 760px){.ob-scene{height:190px;background-size:auto 100%%;background-position:50%% 100%%}}\n'
             # short laptop screens: a soft white glow behind the form so the figures fade out under it
             "@media (max-height: 800px) and (min-width: 961px){.ob-main::before{content:'';position:absolute;left:50%%;top:-24px;bottom:-56px;width:min(820px,92vw);transform:translateX(-50%%);background:radial-gradient(closest-side,#FFFFFF 74%%,rgba(255,255,255,0));z-index:-1;pointer-events:none}}") % NEW
def rd(f): return open(os.path.join(P, f)).read()
def wr(f, s): open(os.path.join(P, f), 'w').write(s)

s = rd('CR-ONB-003c.dc.html')
s, n = re.subn(r'\.ob-scene\{[^\n]*\n@media \(max-width: 760px\)\{\.ob-scene\{[^\n]*\}\}', SCENE_CSS, s)
assert n == 1; wr('CR-ONB-003c.dc.html', s)

s = rd('CR-ONB-003.dc.html')
assert NEW not in s
s, n = re.subn(r'<div class="ob-illus ob-illus-img".*?</div>\n', '', s, flags=re.S); assert n == 1
s = s.replace('</style>', '.ob-root{isolation:isolate}\n' + SCENE_CSS + '\n</style>', 1)
s, n = re.subn(r'(<div class="ob-root"[^>]*>\n)', r'\1<div class="ob-scene" aria-hidden="true"></div>\n', s); assert n == 1
wr('CR-ONB-003.dc.html', s)
print('patched CR-ONB-003, CR-ONB-003c')
