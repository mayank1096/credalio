# fix005: designer 2026-10-13 "this design looks bad" (CR-ORI-005 situation card). Navy box -> calm lead (question in bold) + light
# AI-draft card on the right; no "The situation" label, no repeated "What should happen?" heading. usage: python3 fix005.py <dir>
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ori_m as O
f = os.path.join(sys.argv[1], 'CR-ORI-005.dc.html'); s = open(f, encoding='utf-8').read()
assert 'sc-top' not in s
s, n = re.subn(r'<div class="sc-sit ob-in2">\s*<span class="sc-l">The situation</span>\s*<p>A creator uses AI to generate an entire lesson\. What must happen before it is submitted for validation\?</p>\s*(<div class="sc-doc".*?</div>)\s*</div>',
               lambda m: '<div class="sc-top ob-in2"><p class="sc-lead">A creator uses AI to generate an entire lesson. <b>What must happen before it goes to validation?</b></p>' + m.group(1) + '</div>', s, count=1, flags=re.S)
assert n
s, n = re.subn(r'<h2 class="sc-q ob-in3">What should happen\?</h2>\s*', '', s, count=1); assert n
css = """
/* fix005 calm situation */
.sc-top{margin-top:14px;display:grid;grid-template-columns:minmax(0,1fr) 248px;gap:40px;align-items:center}
.sc-lead{margin:0;font-size:17px;line-height:1.6;color:#3A4566;max-width:520px}
.sc-lead b{display:block;margin-top:6px;font-weight:600;color:#0B1433}
.sc-top .sc-doc{transform:none;padding:16px;border-radius:16px;border:1.5px solid #E6EAF3;box-shadow:0 12px 30px rgba(11,20,51,.06);gap:8px}
.sc-top + .kc-opts{margin-top:32px}
@media (max-width: 960px){.sc-top{grid-template-columns:minmax(0,1fr);gap:0;margin-top:12px}.sc-lead{font-size:15.5px}.sc-top + .kc-opts{margin-top:24px}}
"""
i = s.rfind('</style>', 0, s.find('</helmet>')); s = s[:i] + css + s[i:]
if 'lp-scene' not in s: s = O.add_scene(s)
open(f, 'w', encoding='utf-8').write(s); print('fix005 ok')
