# build40c: RDY-001d follows the standard outcome order, centred (designer: "success screen ... tick on center and text too").
# emblem -> pill -> H1 -> sub -> path card -> CTA, all centred; payout row stays below. Applies on top of build40b.
import re, sys, os
f = os.path.join(sys.argv[1], 'CR-RDY-001.dc.html'); s = open(f, encoding='utf-8').read()
assert 'rdd-c' not in s, 'already applied'
m = re.search(r'<section class="ds-card rdd-hero ob-in" aria-labelledby="rdd-h">.*?</section>', s, re.S)
h = m.group(0)
cta = re.search(r'<a href="CR-HOME-EXP\.dc\.html" class="ds-btn rdd-go">.*?</a>', h, re.S).group(0)
path = re.search(r'<ol class="rdd-path ob-in2".*?</ol>', h, re.S).group(0)
top = re.search(r'<div class="rdd-l">(.*?)<a href="CR-HOME-EXP', h, re.S).group(1)
new = ('<section class="rdd-hero rdd-c ob-in" aria-labelledby="rdd-h">' + top + '<div class="ds-card rdd-card">' + path + '</div>' + cta + '</section>')
s = s[:m.start()] + new + s[m.end():]
css = """
/* build40c centred outcome order */
.rdd-hero.rdd-c{display:flex;flex-direction:column;align-items:center;text-align:center;margin:36px auto 0 auto;padding:0;max-width:560px;background:transparent;border:0;box-shadow:none;gap:0}
.rdd-c .rdd-sub{margin-left:auto;margin-right:auto}
.rdd-card{margin-top:28px;width:100%;max-width:420px;box-sizing:border-box;padding:22px 24px;text-align:left}
.rdd-c .rdd-path{padding:0;border:0}
.rdd-c .rdd-path::before{left:11px;top:14px;bottom:14px}
.rdd-c .rdd-go{margin-top:28px}
.rdd-c + .rd-grid{max-width:780px;margin:44px auto 0 auto}
@media (max-width: 960px){
.rdd-hero.rdd-c{margin-top:28px}
.rdd-card{padding:18px}
.rdd-c .rdd-go{width:100%;justify-content:space-between;margin-top:24px}
.rdd-c .rdd-path::before{top:14px}
.rdd-c + .rd-grid{margin-top:36px}
}
"""
i = s.rfind('</style>', 0, s.find('</helmet>')); s = s[:i] + css + s[i:]
open(f, 'w', encoding='utf-8').write(s); print('build40c ok')
