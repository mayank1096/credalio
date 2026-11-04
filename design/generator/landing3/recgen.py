# Public Validation Record (TRST-006). Built from LIVE shared pieces, never redrawn:
#   CourseDetail.dc.html -> breadcrumb (cd-crumb), validation card (cd-val, gold seal, cd-checks, cd-vf)
#   Validation page      -> dl facts (vx-dl), step track (ko-path), cx-ticks
#   kit                  -> ds-ghost / ds-link / ds-tag / tip
# Usage: python3 recgen.py -> design/canvas3/project/Record.dc.html
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from kit import KIT_CSS, tip, ck
from shell import BASE_CSS, nav, FOOT
import pricegen, partgen, wow

P = os.path.join(HERE, '../../canvas3/project/')
OUT = P + 'Record.dc.html'
CDH = open(P + 'CourseDetail.dc.html').read()
style = pricegen.style

def pick(css, rx):
    """Rules whose selector matches rx, keeping their @media wrappers."""
    out, i, n = [], 0, len(css)
    def rules(body):
        res, j = [], 0
        while j < len(body):
            o = body.find('{', j)
            if o < 0: break
            c = body.find('}', o)
            sel = body[j:o].strip()
            if re.search(rx, sel): res.append(sel + '{' + body[o + 1:c] + '}')
            j = c + 1
        return res
    while i < n:
        o = css.find('{', i)
        if o < 0: break
        head = css[i:o].strip()
        if head.startswith('@media'):
            d, k = 1, o + 1
            while d:
                if css[k] == '{': d += 1
                elif css[k] == '}': d -= 1
                k += 1
            r = rules(css[o + 1:k - 1])
            if r: out.append(head + '{\n' + '\n'.join(r) + '\n}')
            i = k
        elif head.startswith('@'):
            d, k = 1, o + 1
            while d:
                if css[k] == '{': d += 1
                elif css[k] == '}': d -= 1
                k += 1
            i = k
        else:
            c = css.find('}', o)
            if re.search(rx, head): out.append(head + '{' + css[o + 1:c] + '}')
            i = c + 1
    return '\n'.join(out)

CDCSS = pick(style(CDH), r'\.cd-(val|vt|vd|checks|chk|vf|vid|crumb|seal)\b')
SEAL = re.search(r'<svg class="cd-seal".*?</svg>', CDH, re.S).group(0)
CHKI = re.search(r'<div class="cd-chk"><b>(<svg.*?</svg>)', CDH, re.S).group(1)
X = '<svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18"></path></svg>'
LINK = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1"></path><path d="M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"></path></svg>'

AREAS = [('Content', 'Subject Matter Validator', True), ('Learning design', 'Educational Validator', True), ('Assessment', 'Assessment Validator', True)]
NOT = ['Every learner gets a particular outcome', 'A job is guaranteed', 'The content can never go out of date', 'Future versions are validated automatically']
FACTS = [('Validation ID', 'VAL-CRD-004821'), ('Status', '<span class="ds-tag green">Credalio Validated</span>'), ('Tier', 'Gold'), ('Creator', 'Amara Okafor'), ('Learning type', 'Course'), ('Version validated', 'v2.1'), ('Completed', '24 September 2026')]

BODY = '''<div style="font-family: 'Google Sans', system-ui, sans-serif; color: #0B1433; background: #FFFFFF">
''' + nav('').replace('<a class="sx-cta" href="#">Create account</a>', '<a class="sx-cta" href="OnbWelcome.dc.html">Create account</a>') + '''
<main class="rc-wrap">
<nav class="cd-crumb" aria-label="Breadcrumb"><a href="Courses.dc.html">Courses</a><span aria-hidden="true">/</span><a href="CourseDetail.dc.html">Data Foundations</a><span aria-hidden="true">/</span><span>Validation Record</span></nav>
<header class="rc-head">
<div><span class="pc-k">Validation Record</span><h1 class="pc-ph1">Data Foundations: Spreadsheets to SQL</h1><p class="rc-by">Course by Amara Okafor</p></div>
<div class="rc-acts"><button type="button" class="ds-ghost sm rc-copy {{copyCls}}" onClick="{{copy}}"><sc-if value="{{copied}}" hint-placeholder-val="{{ false }}">''' + ck(14, 3) + '''</sc-if><sc-if value="{{notCopied}}" hint-placeholder-val="{{ true }}">''' + LINK + '''</sc-if><span>{{copyLabel}}</span></button><a class="ds-link" href="CourseDetail.dc.html">View the course →</a></div>
</header>
<div class="rc-grid">
<div class="rc-main">
<section class="cd-val" aria-label="Validation result" onMouseMove="{{holoMove}}" onMouseLeave="{{holoOut}}">
<span class="hl"><span class="hl-in">''' + SEAL + '''<span class="hl-sh"></span><span class="hl-gl"></span></span></span>
<div>
<div class="cd-vt">Gold Validated</div>
<div class="cd-vd">This version completed every review that applies to it.</div>
<div class="cd-checks">''' + ''.join('<div class="cd-chk"><b>%s%s</b><span>%s · Completed</span></div>' % (CHKI, t, r) for t, r, _ in AREAS) + '''</div>
<span class="hl-cap"><i></i>Holographic seal</span>
<div class="cd-vf"><span class="cd-vid">AI and Security &amp; Privacy reviews: not applicable''' + tip('These reviews are only added when the learning uses AI features or handles personal data.') + '''</span></div>
</div>
</section>
<section class="ds-card rc-card" aria-labelledby="rc-nm">
<h2 id="rc-nm" class="rc-h2">What validation doesn’t promise</h2>
<ul class="rc-not">''' + ''.join('<li><i>%s</i>%s</li>' % (X, t) for t in NOT) + '''</ul>
</section>
<section class="ds-card rc-card" aria-labelledby="rc-vh">
<h2 id="rc-vh" class="rc-h2">Version history''' + tip('After a major update, the new version is reviewed again and appears here with its own status.') + '''</h2>
<ol class="ko-path pt-path rc-path"><li class="pt-ok"><span class="ko-dot">''' + ck(13, 3) + '''</span><span><b>v2.1 · Validated <span class="ds-tag blue">Current</span></b><span>24 September 2026</span></span></li></ol>
</section>
</div>
<aside class="ds-card rc-facts" aria-label="Record details">
<dl class="rc-dl">''' + ''.join('<div><dt>%s</dt><dd>%s</dd></div>' % kv for kv in FACTS) + '''</dl>
<div class="rc-links"><a class="ds-link" href="Validation.dc.html">How validation works →</a><a class="rc-rep" href="#">Report a concern about this record</a></div>
</aside>
</div>
</main>
''' + FOOT + '''
</div>'''

CSS = CDCSS + r'''
.rc-wrap{max-width:1216px;margin:0 auto;padding:28px 48px 96px;box-sizing:border-box}
.rc-head{display:flex;align-items:flex-end;justify-content:space-between;gap:24px;margin-top:24px}
.rc-head .pc-ph1{margin-top:8px}
.rc-by{margin:8px 0 0;font-size:15px;color:#5B6582}
.rc-acts{display:flex;align-items:center;gap:18px;flex-shrink:0}
.rc-copy{display:inline-flex;align-items:center;gap:8px}
.rc-copy svg{color:#1652F0}
.rc-copy.on{border-color:#0F6B45;color:#0F6B45}
.rc-copy.on svg{color:#0F6B45}
.rc-grid{display:grid;grid-template-columns:minmax(0,1fr) 340px;gap:24px;align-items:start;margin-top:32px}
.rc-main{display:flex;flex-direction:column;gap:16px}
.cd-seal{width:76px;height:76px}
.rc-card{padding:26px 28px;border-radius:20px}
.rc-h2{margin:0;display:flex;align-items:center;font-size:18px;font-weight:600;letter-spacing:-.2px}
.rc-not{list-style:none;margin:16px 0 0;padding:0;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:12px 20px}
.rc-not li{display:flex;align-items:center;gap:10px;font-size:14.5px;color:#3A4566}
.rc-not i{width:20px;height:20px;border-radius:999px;background:#F1F3F8;color:#5B6582;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.rc-path{margin-top:18px}
.rc-path b{display:flex;align-items:center;gap:10px}
.rc-path b .ds-tag{font-size:12px !important;color:#0E3BB8 !important}
.rc-facts{position:sticky;top:96px;padding:8px 22px 20px;border-radius:20px}
.rc-dl{margin:0}
.rc-dl > div{padding:13px 0;border-top:1.5px solid #F0F2F8}
.rc-dl > div:first-child{border-top:0}
.rc-dl dt{font-size:12.5px;color:#8A93AD}
.rc-dl dd{margin:4px 0 0;font-size:15px;font-weight:600;color:#0B1433}
.rc-links{display:flex;flex-direction:column;align-items:flex-start;gap:10px;padding-top:16px;border-top:1.5px solid #F0F2F8}
.rc-rep{font-size:13.5px;color:#5B6582;text-decoration:underline;text-underline-offset:3px}
@media (max-width: 960px){
.rc-wrap{padding:16px 20px 72px}
.rc-head{flex-direction:column;align-items:flex-start;gap:14px}
.rc-grid{grid-template-columns:minmax(0,1fr);margin-top:22px}
.rc-main{display:contents}
.rc-facts{position:static;order:1}
.rc-main > *{order:2}
.rc-main > .cd-val{order:0}
.rc-grid{gap:16px}
.rc-dl{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);column-gap:16px}
.rc-dl > div:nth-child(2){border-top:0}
}
@media (max-width: 760px){
.rc-head .pc-ph1{font-size:26px}
.rc-acts{width:100%;justify-content:space-between}
.rc-card{padding:20px 18px}
.rc-not{grid-template-columns:minmax(0,1fr)}
.rc-facts{padding:4px 18px 18px}
.rc-rep{position:relative}
.rc-rep::after{content:'';position:absolute;inset:-12px -4px}
.cd-seal{width:52px;height:52px}
}
'''

JS = '''
class Component extends DCLogic {
''' + wow.HOLO_JS + '''
  constructor(props) { super(props); this.state = { copied: false }; }
  componentWillUnmount() { if (this.t) clearTimeout(this.t); }
  renderVals() {
    var self = this, on = this.state.copied;
    return { holoMove: function (e) { self.holoMove(e); }, holoOut: function () { self.holoOut(); }, copyLabel: on ? 'Link copied' : 'Copy record link', copyCls: on ? 'on' : '', copied: on, notCopied: !on,
      copy: function () { self.setState({ copied: true }); if (self.t) clearTimeout(self.t); self.t = setTimeout(function () { self.setState({ copied: false }); }, 2000); } };
  }
}
'''

HTML = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Validation Record</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500;600;700&amp;display=swap">
<style>
''' + BASE_CSS + KIT_CSS + '\n' + pricegen.CSS + '\n' + partgen.CSS + '\n' + CSS + '\n' + wow.HOLO_CSS + '''</style>
</helmet>
''' + BODY + '''
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":1440,"height":1080}}'>''' + JS + '''</script>
</body>
</html>
'''

if __name__ == '__main__':
    open(OUT, 'w').write(HTML)
    print('wrote', OUT, len(HTML))
