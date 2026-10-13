# fix005b: designer "it has to be a box" -> situation in a soft blue box (label, text, bold question) + tilted white AI-draft card.
import sys, os
f = os.path.join(sys.argv[1], 'CR-ORI-005.dc.html'); s = open(f, encoding='utf-8').read()
assert 'fix005b' not in s
s = s.replace('<div class="sc-top ob-in2"><p class="sc-lead">', '<div class="sc-top ob-in2"><p class="sc-lead"><span class="sc-k">The situation</span>', 1)
assert 'sc-k' in s
css = """
/* fix005b situation box */
.sc-top{margin-top:22px;padding:28px 32px;border-radius:22px;background:linear-gradient(135deg,#F5F8FF 0%,#EAF0FF 100%);border:1.5px solid #DCE5FB;grid-template-columns:minmax(0,1fr) 230px;gap:32px}
.sc-k{display:block;margin-bottom:10px;font-size:12.5px;font-weight:500;color:#1652F0}
.sc-lead{max-width:none}
.sc-top .sc-doc{transform:rotate(2deg);border-color:#FFFFFF;box-shadow:0 16px 34px rgba(22,82,240,.14)}
@media (max-width: 960px){.sc-top{grid-template-columns:minmax(0,1fr);gap:0;padding:18px;border-radius:18px;margin-top:16px}.sc-k{margin-bottom:8px}}
"""
i = s.rfind('</style>', 0, s.find('</helmet>')); s = s[:i] + css + s[i:]
open(f, 'w', encoding='utf-8').write(s); print('fix005b ok')
