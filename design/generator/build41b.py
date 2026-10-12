# build41b: designer 2026-10-12 — campus scene filler at the bottom of M1-L2 and the M1 check (K1–K3), and a warmer
# Module 1 welcome (M1-00): Nova greets you next to the Start button, scene at the bottom. Patches live files in <dir>.
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ori_m as O, cpx
P = sys.argv[1]
def rd(f): return open(os.path.join(P, f), encoding='utf-8').read()
def wr(f, s): open(os.path.join(P, f), 'w', encoding='utf-8').write(s)
for f in ['CR-ORI-M1-L2.dc.html', 'CR-ORI-M1-K.dc.html']:
    wr(f, O.add_scene(rd(f)))
s = rd('CR-ORI-M1-00.dc.html')
assert 'mo-hi' not in s
b0 = s.index('<a href="CR-ORI-M1-L1.dc.html" class="ds-btn mo-go mo-go-new ob-in2">'); b1 = s.index('</a>', b0) + 4
btn = s[b0:b1]
a = cpx.stage('Nova')
hi = ('<aside class="mo-hi" aria-label="Nova"><div class="mo-hi-t"><span class="mo-hi-b">Hi Ada, I’m Nova. This first module is a gentle start, and I’m here if anything’s unclear.</span>'
      + btn + '</div><span class="mo-hi-f" aria-hidden="true"><img src="/_blob/' + cpx.B['Nova'] + f'" alt="" style="left: -41px; top: -30px; width: 259px"></span></aside>')
s = s[:b0] + hi + s[b1:]
s = s.replace('<h1 class="lp-h1 ob-in">Welcome to Credalio</h1>', '<h1 class="lp-h1 ob-in">Welcome to Credalio</h1>', 1)
css = """
/* build41b warmer welcome */
.mo2-top{align-items:center}
.mo-hi{display:flex;align-items:center;gap:20px;flex-shrink:0}
.mo-hi-t{display:flex;flex-direction:column;align-items:flex-end;gap:14px;max-width:290px;margin-bottom:0}
.mo-hi-b{position:relative;padding:14px 16px;border-radius:18px 18px 4px 18px;background:#FFFFFF url(/_blob/d268046654a4206d2a726e62005bcc59) center / cover no-repeat;border:1.5px solid #E6EAF3;font-size:14px;line-height:1.5;color:#3A4566;box-shadow:0 10px 26px rgba(11,20,51,.06)}
.mo-hi-f{position:relative;width:168px;height:168px;border-radius:50%;overflow:hidden;flex-shrink:0;background:#EAF0FF;box-shadow:0 0 0 8px rgba(234,240,255,.6)}
.mo-hi-f img{position:absolute;max-width:none;height:auto;mix-blend-mode:multiply}
@media (max-width: 960px){
.mo-hi{width:100%;order:2}
.mo-hi-f{display:none}
.mo-hi-t{max-width:none;width:100%;align-items:stretch;margin:20px 0 0 0;gap:16px}
.mo-hi-b{border-radius:18px}
}
"""
i = s.rfind('</style>', 0, s.find('</helmet>')); s = s[:i] + css + s[i:]
wr('CR-ORI-M1-00.dc.html', O.add_scene(s))
print('build41b ok')
