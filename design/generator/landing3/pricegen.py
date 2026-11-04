# Public pricing page (PRC-001..011). Built from LIVE shared pieces, never redrawn:
#   Landing.dc.html  -> pricing section (pr-*: slider, plan cards, compare table), institutions door (ci-in), final CTA (fc-*)
#   Checkout.dc.html -> top-up package tiles (cb-o, CR-CREIO-BUY design)
#   CertDetail.dc.html -> FAQ accordion (dt-faq)
#   Link 2 CR-WAL-OUT -> horizontal step track (ko-path) for "How DLP works"
# Usage: python3 pricegen.py -> design/canvas3/project/Pricing.dc.html
import os, re, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from kit import AURORA_JS, KIT_CSS, coin, credit, tip, btn, ck
from shell import BASE_CSS, nav, FOOT

P = os.path.join(HERE, '../../canvas3/project/')
OUT = P + 'Pricing.dc.html'
L = open(P + 'Landing.dc.html').read()
CD = open(P + 'CertDetail.dc.html').read()

def style(s): return re.search(r'<style>(.*?)</style>', s, re.S).group(1)
def block(s, start, tag='section'):
    i = s.index(start); d = 0; k = i
    while True:
        o = s.find('<' + tag, k + 1); c = s.find('</' + tag + '>', k + 1)
        if o != -1 and o < c: d += 1; k = o
        else:
            if d == 0: return s[i:c + len(tag) + 3]
            d -= 1; k = c

PR = block(L, '<section class="pr-sec"')
PR = PR.replace('<span style="font-size: 14px; font-weight: 500; color: #1652F0">Flexible learning</span>', '<span style="font-size: 14px; font-weight: 500; color: #1652F0">Pricing</span>')
PR = PR.replace('<h2 id="pr-h" class="pr-h2">Start free. Choose how far you want to go.</h2>', '<h1 id="pr-h" class="pr-h2">Start free. Choose how far you want to go.</h1>')
PR = PR.replace('<a class="ds-btn pr-btn" href="#">', '<a class="ds-btn pr-btn" href="{{p.href}}">').replace('<a class="{{p.ghCls}} pr-btn" href="#">', '<a class="{{p.ghCls}} pr-btn" href="{{p.href}}">')
PR = PR.replace('padding: 112px 48px;', 'padding: 56px 48px 96px;', 1)
PR = PR.replace('<table class="pr-table">', '<table class="pr-table {{pr.selCls}}">')
PR = PR.replace('<a class="ds-link" href="#">Explore Enterprise →</a>', '<a class="ds-link" href="#pc-ent">Explore Enterprise →</a>')
FC = block(L, '<section aria-labelledby="fc-h"')
DOOR = block(L, '<a class="ci-door ci-in"', 'a')
DOOR = DOOR.replace('<span class="ci-t">Bring your programs to Credalio.</span>', '<span class="ci-t">Learning for your organisation.</span>')
DOOR = DOOR.replace('Deliver programs, manage learners and educators, and issue verifiable credentials at scale.', 'Give teams, students or members access with central admin, AI settings and reporting. From 5,000 to 10,000 DLP per person, depending on your plan.')
DOOR = DOOR.replace('Partner with Credalio', 'Talk to Credalio')
FAQ_CSS = '\n'.join(l for l in style(CD).split('\n') if re.match(r'\.dt-(faq|fq|fh|fa|chev)|\.dt-fq-open', l))

CK = '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"></path></svg>'

CSS = r'''.pc-sec{max-width:1312px;margin:0 auto;padding:0 48px 96px;box-sizing:border-box;font-family:'Google Sans',system-ui,sans-serif;color:#0B1433}
.pc-sh{display:flex;align-items:flex-end;justify-content:space-between;gap:24px;margin-bottom:28px}
.pc-k{display:block;font-size:14px;font-weight:500;color:#1652F0}
.pc-h2{margin:8px 0 0;display:flex;align-items:center;font-size:36px;line-height:1.15;font-weight:600;letter-spacing:-.03em}
.pc-p{margin:10px 0 0;max-width:620px;font-size:17px;line-height:1.6;color:#4A5578}
.pc-ent .ci-doors{height:380px}
.pc-ent .ci-door{flex:1}
.pc-top{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.4fr);gap:40px;align-items:center;padding:32px 36px;border-radius:24px;border:1.5px solid #E6EAF3;background:#FFFFFF}
.pc-top .pc-h2{font-size:28px}
.pc-top .pc-p{font-size:15.5px}
.cb-g{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px}
.wf-o{position:relative;font-family:inherit;text-align:left;cursor:pointer;color:#0B1433;background:#FFFFFF;border:1.5px solid #E6EAF3;border-radius:16px;transition:border-color .2s ease,background .2s ease;text-decoration:none}
.wf-o:hover{border-color:#AFC1F5;background:#F5F8FF}
.cb-o{display:flex;flex-direction:column;align-items:flex-start;gap:2px;padding:18px 16px 16px}
.cb-o b{display:flex;align-items:center;gap:8px;font-size:22px;font-weight:600}
.cb-o b .dlp-c{width:22px;height:22px}
.cb-o > span{font-size:13px;color:#5B6582}
.cb-d{margin-top:8px;font-size:12.5px !important;color:#5B6582 !important;line-height:1.4}
.cb-pop{position:absolute;top:-11px;left:14px;height:22px;padding:0 10px;border-radius:999px;background:#FFF1CF;border:1.5px solid #F4D98E;color:#6B4E16;font-size:11.5px;font-weight:500;font-style:normal;display:inline-flex;align-items:center;white-space:nowrap}
.cb-go{margin-top:12px;font-size:14px;font-weight:600;color:#1652F0}
.pc-dlp{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:56px;align-items:start}
.pc-units{display:flex;flex-direction:column;gap:12px;margin-top:24px}
.pc-u{display:flex;align-items:center;gap:14px;padding:16px 18px;border-radius:18px;border:1.5px solid #E6EAF3;background:#FFFFFF}
.pc-u .dlp-c,.pc-u .cr-c{width:36px;height:36px;font-size:15px}
.pc-u b{display:block;font-size:16px;font-weight:600}
.pc-u small{display:block;margin-top:2px;font-size:14px;line-height:1.45;color:#4A5578}
.pc-scale{border-radius:22px;padding:28px;background:linear-gradient(160deg,#F5F8FF 0%,#FFFFFF 70%);border:1.5px solid #DCE5FB}
.pc-rate{display:flex;align-items:center;gap:12px;font-size:28px;font-weight:600;letter-spacing:-.02em}
.pc-rate .dlp-c{width:32px;height:32px}
.pc-rate span{color:#8A93AD;font-weight:500}
.pc-rows{list-style:none;margin:22px 0 0;padding:0;display:flex;flex-direction:column;gap:14px}
.pc-rows li{display:grid;grid-template-columns:64px minmax(0,1fr) 92px;align-items:center;gap:14px;font-size:14px;color:#3A4566}
.pc-rows b{font-weight:600;color:#0B1433}
.pc-rows i{display:block;height:10px;border-radius:999px;background:#F1F3F8;overflow:hidden}
.pc-rows i s{display:block;height:100%;border-radius:999px;background:#1652F0}
.pc-rows em{font-style:normal;text-align:right;font-size:13.5px;color:#5B6582}
.pc-free{margin-top:20px;font-size:14px;line-height:1.55;color:#4A5578}
.pc-how{margin-top:72px}
.ko-path{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr))}
.ko-path li{position:relative;display:flex;flex-direction:column;align-items:center;gap:14px;padding:0 16px;text-align:center}
.ko-path li:not(:last-child)::before{content:'';position:absolute;left:calc(50% + 22px);right:calc(-50% + 22px);top:13px;height:2px;border-radius:2px;background:#1652F0}
.ko-dot{width:28px;height:28px;flex-shrink:0;box-sizing:border-box;border-radius:50%;border:2px solid #1652F0;background:#FFFFFF;display:flex;align-items:center;justify-content:center;color:#1652F0;font-size:12.5px;font-weight:600}
.ko-path li:first-child .ko-dot{background:#1652F0;color:#FFFFFF}
.ko-path li > span:last-child{display:flex;flex-direction:column;gap:4px;align-items:center}
.ko-path b{font-size:16px;font-weight:600}
.ko-path li > span:last-child > span{font-size:14px;line-height:1.5;color:#4A5578;max-width:240px}
''' + FAQ_CSS + r'''
@media (max-width: 960px){
.pc-sec{padding:0 20px 72px}
.pc-sh{flex-direction:column;align-items:flex-start;gap:12px;margin-bottom:22px}
.pc-h2{font-size:28px}
.pc-p{font-size:15.5px}
.pc-ent .ci-doors{height:auto}
.pc-top{grid-template-columns:minmax(0,1fr);gap:22px;padding:24px 20px}
.pc-dlp{grid-template-columns:minmax(0,1fr);gap:32px}
.ko-path{grid-template-columns:minmax(0,1fr);gap:0}
.ko-path li{flex-direction:row;align-items:flex-start;text-align:left;gap:14px;padding:0 0 22px}
.ko-path li:last-child{padding-bottom:0}
.ko-path li:not(:last-child)::before{left:13px;right:auto;top:30px;bottom:2px;width:2px;height:auto}
.ko-path li > span:last-child{align-items:flex-start}
.pc-how{margin-top:48px}
}
@media (max-width: 760px){
.pc-h2{font-size:24px}
.pr-tablewrap{overflow:visible !important}
.pr-table{min-width:0 !important;width:100%}
.pr-table.sel-0 th:nth-child(3),.pr-table.sel-0 td:nth-child(3),.pr-table.sel-0 th:nth-child(4),.pr-table.sel-0 td:nth-child(4),.pr-table.sel-1 th:nth-child(2),.pr-table.sel-1 td:nth-child(2),.pr-table.sel-1 th:nth-child(4),.pr-table.sel-1 td:nth-child(4),.pr-table.sel-2 th:nth-child(2),.pr-table.sel-2 td:nth-child(2),.pr-table.sel-2 th:nth-child(3),.pr-table.sel-2 td:nth-child(3){display:none}
.pr-table td:last-child,.pr-table th:last-child{text-align:right}
.pc-top{border:0;padding:0;background:none;border-radius:0}
.pc-rate{font-size:20px;flex-wrap:wrap;gap:8px}
.pc-rate .dlp-c{width:26px;height:26px}
.pc-rows li{grid-template-columns:48px minmax(0,1fr) auto !important}
.pc-rows em{white-space:nowrap;font-size:12.5px}
.cb-g{grid-template-columns:minmax(0,1fr);gap:16px}
.cb-o{flex-direction:row;align-items:baseline;gap:10px;padding:16px 16px 14px}
.cb-o b{font-size:19px}
.cb-d,.cb-go{display:none}
.pc-scale{padding:22px 18px}
.pc-rows li{grid-template-columns:52px minmax(0,1fr) 80px;gap:10px}
}
'''

TOPS = ''.join('''<a class="wf-o cb-o" href="Chk-TOP.dc.html">%s<b>%s%s</b><span>DLP · price to be confirmed</span><span class="cb-d">About %d hours of learning</span><span class="cb-go">Get DLP →</span></a>''' % ('<em class="cb-pop">Most chosen</em>' if n == 1000 else '', coin(), '{:,}'.format(n), n // 100) for n in (500, 1000, 2500))

STEPS = [('Subscribe', 'Your monthly DLP lands in your account.'), ('Choose learning', 'Every eligible course shows how much DLP it needs.'), ('Learn', 'DLP is used as you open eligible learning.'), ('Keep going', 'Your allowance refreshes each month, with rollover on eligible plans.')]
HOW = ''.join('<li><span class="ko-dot">%d</span><span><b>%s</b><span>%s</span></span></li>' % (i + 1, t, d) for i, (t, d) in enumerate(STEPS))

BODY = '''<div style="font-family: 'Google Sans', system-ui, sans-serif; color: #0B1433; background: #FFFFFF">
''' + nav('Pricing') + '''
''' + PR + '''

<section class="pc-sec pc-ent" id="pc-ent" aria-label="Credalio for organisations"><div class="ci-doors">''' + DOOR + '''</div></section>

<section class="pc-sec" aria-labelledby="pc-tu">
<div class="pc-top">
<div><span class="pc-k">DLP top-ups</span><h2 id="pc-tu" class="pc-h2">Need a little more this month?</h2><p class="pc-p">Add DLP without changing your plan. Handy on Pro, or when you just need a little extra.</p></div>
<div class="cb-g">''' + TOPS + '''</div>
</div>
</section>

<section class="pc-sec" aria-labelledby="pc-dl">
<div class="pc-dlp">
<div>
<span class="pc-k">Your learning allowance</span>
<h2 id="pc-dl" class="pc-h2">What is DLP?''' + tip('DLP is a learning-access unit. It isn’t cash and it isn’t a token.') + '''</h2>
<p class="pc-p">Your plan gives you a monthly DLP allowance. You use it to open eligible courses, paths and certifications across Credalio.</p>
<div class="pc-units">
<div class="pc-u">''' + coin(True) + '''<div><b>DLP</b><small>Your learning allowance. Used to access eligible learning.</small></div></div>
<div class="pc-u">''' + credit(True) + '''<div><b>Marketplace Credits</b><small>A separate balance, used only where Credits are accepted.</small></div></div>
</div>
</div>
<div class="pc-scale">
<span class="pc-rate">''' + coin(True) + '''100 DLP <span>≈ 1 hour of learning</span></span>
<ul class="pc-rows">
<li><b>Free</b><i><s style="width: 3.3%"></s></i><em>200 · 2 hrs</em></li>
<li><b>Basic</b><i><s style="width: 33%"></s></i><em>2,000 · 20 hrs</em></li>
<li><b>Pro</b><i><s style="width: 100%"></s></i><em>6,000 · 60 hrs</em></li>
</ul>
<p class="pc-free">Free isn’t a trial that ends. You can still browse, plan with your AI Coach, keep your Backpack and use free learning.</p>
</div>
</div>
<div class="pc-how">
<div class="pc-sh"><div><span class="pc-k">How DLP works</span><h2 class="pc-h2">From allowance to learning.</h2></div></div>
<ol class="ko-path">''' + HOW + '''</ol>
</div>
</section>

''' + FC + '''
''' + FOOT + '''
</div>'''

def jsblock(name):
    i = L.index('class ' + name); j = L.index('\nclass ', i + 10)
    return L[i:j]
PART = L[L.index('class Part {'):L.index('function momentVals')]
PRICE = jsblock('PricePart').replace("this.state = { hours: 20, open: false };", "this.state = { hours: 20, open: true };")
PRICE = PRICE.replace("open: this.state.open ? 'true' : 'false',", "selCls: 'sel-' + fit, open: this.state.open ? 'true' : 'false',")
PRICE = PRICE.replace("pick: function () { self.setState({ hours: p.set }); } };", "href: ['OnbWelcome.dc.html', 'Chk-001.dc.html', 'Chk-001p.dc.html'][k], pick: function () { self.setState({ hours: p.set }); } };")
FINAL = jsblock('FinalPart')

JS = '\n' + PART + PRICE + '\n' + FINAL + '''
class Component extends DCLogic {
''' + AURORA_JS + '''
  constructor(props) {
    super(props);
    this.state = { v: 0 };
    this.parts = { pr: new PricePart(this), fc: new FinalPart(this) };
  }
  bump(now) {
    var self = this;
    if (now) { this.setState({ v: this.state.v + 1 }); return; }
    if (this.pend) return;
    this.pend = true;
    requestAnimationFrame(function () { self.pend = false; self.setState({ v: self.state.v + 1 }); });
  }
  componentDidMount() { this.aurScan(); for (var k in this.parts) if (this.parts[k].componentDidMount) this.parts[k].componentDidMount(); }
  componentWillUnmount() { if (this._aurMo) this._aurMo.disconnect(); for (var k in this.parts) if (this.parts[k].componentWillUnmount) this.parts[k].componentWillUnmount(); }
  renderVals() { var o = {}; for (var k in this.parts) o[k] = this.parts[k].renderVals(); return o; }
}
'''

HTML = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Pricing</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500;600;700&amp;display=swap">
<style>
''' + BASE_CSS + style(L) + '\n' + KIT_CSS + '\n' + CSS + '''</style>
</helmet>
''' + BODY + '''
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":1440,"height":4000}}'>''' + JS + '''</script>
</body>
</html>
'''

if __name__ == '__main__':
    open(OUT, 'w').write(HTML)
    print('wrote', OUT, len(HTML))
