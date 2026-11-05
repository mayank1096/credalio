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
import dashgen
DCSS = re.sub(r'^body\{[^}]*\}\n', '', dashgen.CSS)
from kit import NOVA

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
PR = PR.replace('<div class="pr-head">', '<sc-if value="{{pr.guest}}" hint-placeholder-val="{{ true }}">\n<div class="pr-head">', 1)
i = PR.index('<div class="pr-tabs"'); PR = PR[:i] + '</sc-if>\nMEMBERHEAD\n' + PR[i:]
PR = PR.replace('<sc-if value="{{p.fit}}" hint-placeholder-val="{{ false }}"><a class="ds-btn pr-btn"', '<sc-if value="{{p.isCur}}" hint-placeholder-val="{{ false }}"><span class="pc-cur"><i>CKI</i>Your current plan</span></sc-if><sc-if value="{{p.fit}}" hint-placeholder-val="{{ false }}"><a class="ds-btn pr-btn"')
PR = PR.replace('<div class="pr-foot">', '<sc-if value="{{pr.isPath}}" hint-placeholder-val="{{ false }}"><p class="pc-note">Plans give you a monthly allowance. No plan pays for a whole path: DLP is used as you learn.</p></sc-if>\n<sc-if value="{{pr.guest}}" hint-placeholder-val="{{ true }}">\n<div class="pr-foot">')
PR = PR.replace('<sc-if value="{{pr.showTable}}"', '</sc-if>\n<sc-if value="{{pr.showTable}}"')
FC = block(L, '<section aria-labelledby="fc-h"')
DOOR = block(L, '<a class="ci-door ci-in"', 'a')
DOOR = DOOR.replace('<span class="ci-t">Bring your programs to Credalio.</span>', '<span class="ci-t">Learning for your organisation.</span>')
DOOR = DOOR.replace('Deliver programs, manage learners and educators, and issue verifiable credentials at scale.', 'Give teams, students or members access with central admin, AI settings and reporting. From 5,000 to 10,000 DLP per person, depending on your plan.')
DOOR = DOOR.replace('Partner with Credalio', 'Talk to Credalio')
LFOOT = block(L, '<footer class="lh-eng ft"', 'footer').replace('onSubmit="{{hero.onStart}}"', 'onSubmit="{{ftSub}}"')
def _fcm(css):
    out = []
    for m in re.finditer(r'@media \(max-width: 760px\)\{(.*?)\n\}', css, re.S):
        rules = [l for l in m.group(1).split('\n') if re.match(r'\.fc-(form|note|band|h2|sub|wrap)\b', l)]
        if rules: out.append('@media (max-width: 760px){\n' + '\n'.join(rules) + '\n}')
    return '\n'.join(out)
FC_M = _fcm(style(L))
FAQ_CSS = '\n'.join(l for l in style(CD).split('\n') if re.match(r'\.dt-(faq|fq|fh|fa|chev)|\.dt-fq-open', l))


NAVH = nav('Pricing')
NAVH = NAVH.replace('<a class="sx-link sx-login" href="#" style="font-weight: 600; color: #0B1433">Log in</a>\n<a class="sx-cta" href="#">Create account</a>', '<sc-if value="{{pr.guest}}" hint-placeholder-val="{{ true }}"><a class="sx-link sx-login" href="#" style="font-weight: 600; color: #0B1433">Log in</a>\n<a class="sx-cta" href="OnbWelcome.dc.html">Create account</a></sc-if><sc-if value="{{pr.member}}" hint-placeholder-val="{{ false }}"><a class="sx-dlp" href="Usage.dc.html" aria-label="{{pr.bal}} DLP available. View usage">' + coin() + '<b style="font-weight: 600">{{pr.bal}}<span class="pc-avl"> available</span></b></a><a class="sx-av" href="Dash-E.dc.html" aria-label="Your dashboard">AO</a></sc-if>')
CKI = ck(11, 3.4)
AVN = '<span class="nv-av" aria-hidden="true"><img src="' + NOVA + '" alt=""></span>'
MEMBERHEAD = """<sc-if value="{{pr.mine}}" hint-placeholder-val="{{ false }}">
<div class="pc-me">
<h1 class="pc-ph1">Your plan</h1>
<div class="nv-g">
<section class="ds-card nv-bal" aria-label="Your plan"><span class="hp-lab nv-lab">DLP available<span class="nv-st cb">{{pr.curName}}</span></span><span class="nv-big">""" + coin(True) + """{{pr.bal}}</span><span class="nv-sub">{{pr.curSub}}</span><div class="nv-acts"><a class="ds-ghost sm" href="Chk-TOP.dc.html">Get more DLP</a><a class="ds-link" href="Usage.dc.html">View usage</a></div></section>
<section class="lr-nova nova-card" aria-label="Your AI Coach">""" + AVN + """<div class="lr-nova-b"><span class="lr-nova-k">Nova · Your AI Coach</span><p>{{pr.nova}}</p></div></section>
</div>
<h2 class="pc-ph">{{pr.plansHead}}</h2>
</div>
</sc-if>
<sc-if value="{{pr.isPath}}" hint-placeholder-val="{{ false }}">
<div class="pc-me">
<a class="pc-back" href="PathDetail-Learner.dc.html">""" + '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 12H5"></path><path d="m11 18-6-6 6-6"></path></svg>' + """<span>Data Analyst path</span></a>
<div class="pc-path"><div><h1 class="pc-ph1">Choose a plan for your Data Analyst journey.</h1><p class="pc-p">You don’t need all of it today. DLP is used as you move through the path.</p></div>
<div class="lr-strip"><span class="lr-st"><small>Whole path</small><b>~3,800<i>DLP</i></b></span><span class="lr-st"><small>Your balance</small><b>200<i>DLP</i></b></span></div></div>
</div>
</sc-if>"""
PR = PR.replace('MEMBERHEAD', MEMBERHEAD).replace('CKI', CKI)
FAQS = [('Can I start for free?', 'Yes. Free gives you 200 DLP to explore Credalio, find your goal with your AI Coach and start eligible free learning.'), ('Do I need a card for Free?', 'No. You only add payment details if you choose Basic or Pro.'), ('What happens when I use all my DLP?', 'Your progress, projects and Backpack stay with you. Explore free learning, wait for your refresh, or upgrade to keep going.'), ('Does unused DLP roll over?', 'Not on Free. On Pro, unused DLP rolls over up to 18,000, with gradual decay from month four. Basic follows the Basic plan policy, which is being finalised.'), ('Are certificates included?', 'Certificates you earn from eligible learning go straight to your Digital Backpack.'), ('Are Professional Certifications included?', 'Certification learning uses your DLP like other learning. Any separate exam fee is shown on the certification page before you start.'), ('Does my plan include AI?', 'Yes. Every plan includes an AI Coach. You get more of it on Basic, and the most on Pro.'), ('What if a course needs more DLP than I have?', 'You can still start. Credalio shows what your balance covers, and you carry on when your allowance refreshes or you top up.'), ('Can my employer or university pay?', 'Yes. Organisations can give access through Credalio for Institutions, from 5,000 to 10,000 DLP per person.')]
CK = '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"></path></svg>'

CSS = r'''.pc-avl{font-weight:500;color:#5B6582}
.sx-dlp{height:36px;padding:0 12px 0 8px;border-radius:999px;background:#F5F8FF;border:1px solid #DCE5FB;display:flex;align-items:center;gap:8px;font-size:14px;font-weight:600;color:#0B1433;text-decoration:none;white-space:nowrap}
.sx-av{width:40px;height:40px;border-radius:999px;background:#DCE5FB;color:#1652F0;text-decoration:none;display:flex;align-items:center;justify-content:center;font-size:14px;font-weight:600}
.pc-cur{display:flex;align-items:center;justify-content:center;gap:8px;height:48px;border-radius:999px;background:#EAF0FF;color:#0E3BB8;font-size:14.5px;font-weight:600;margin-top:auto}
.pr-pro .pc-cur{background:rgba(255,255,255,.14);color:#FFFFFF}
.pc-cur i{width:20px;height:20px;border-radius:999px;background:#1652F0;color:#FFFFFF;display:flex;align-items:center;justify-content:center}
.pc-me{display:flex;flex-direction:column;gap:22px;margin-bottom:8px}
.pc-me .nv-g{grid-template-columns:400px minmax(0,1fr)}
.pc-me .lr-nova{margin:0;align-items:center}
.pc-me .lr-nova-a{width:auto}
.pc-ph{margin:18px 0 0;font-size:22px;font-weight:600;letter-spacing:-.4px}
.pc-back{display:inline-flex;align-items:center;gap:8px;align-self:flex-start;height:40px;padding:0 14px 0 10px;margin:0 0 0 -10px;border-radius:999px;color:#3A4566;font-size:14px;font-weight:500;text-decoration:none}
.pc-back:hover{background:#F5F8FF;color:#0B1433}
.pc-ph1{margin:4px 0 0;font-size:clamp(30px,3vw,40px);line-height:1.12;font-weight:600;letter-spacing:-.03em}
.pc-path{display:flex;align-items:flex-end;justify-content:space-between;gap:28px}
.pc-path .pc-p{margin-top:10px}
.pc-note{margin:0;text-align:center;font-size:13.5px;color:#5B6582}
.pc-roll{display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr);gap:48px;align-items:center}
.pc-rc{display:grid;grid-template-columns:minmax(0,1fr) auto minmax(0,1fr);gap:14px;align-items:center}
.pc-rc .nv-use{padding:22px 22px 20px}
.pc-rc .nv-l li{grid-template-columns:96px minmax(0,1fr) 60px;gap:12px}
.pc-rc .nv-l{margin-top:16px;gap:12px}
.pc-arr{width:40px;height:40px;border-radius:999px;background:#EAF0FF;color:#1652F0;display:flex;align-items:center;justify-content:center}
.nv-bar i.pc-rb{background:#9DB8F7}
.pc-ar{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:18px}
.pc-ar .lr-card,.pc-ar .pc-ai{padding:28px}
.pc-ar .lr-card{display:flex;flex-direction:column;gap:18px}
.pc-ar .lr-card .lr-cb{margin-top:0}
.pc-ar .lr-card > .ds-link{margin-top:0;padding-top:0}
.pc-ar .lr-card .pc-tiers span{background:#F7F9FD;border-color:#EEF1F7}
.pc-ai{display:flex;flex-direction:column;gap:14px;border-radius:20px;border:1.5px solid #DCE5FB}
.pc-ai .nv-av{width:52px;height:52px;box-shadow:0 0 0 3px #FFFFFF,0 0 0 4.5px #D6DDEE}
.pc-ai h3,.pc-ar .lr-card h3{margin:0;font-size:20px;font-weight:600;letter-spacing:-.3px}
.pc-ai p{margin:0;font-size:15px;line-height:1.55;color:#3A4566}
.pc-tiers{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px;margin-top:auto}
.pc-tiers span{display:flex;flex-direction:column;gap:2px;padding:12px 14px;border-radius:14px;background:rgba(255,255,255,.75);border:1.5px solid #FFFFFF;font-size:12.5px;color:#5B6582}
.pc-tiers b{font-size:14px;font-weight:600;color:#0B1433}
.pc-faq{max-width:860px;margin:0 auto}
.pc-faq .pc-sh{justify-content:center;text-align:center}
.pc-faq .pc-sh > div{display:flex;flex-direction:column;align-items:center}
.pc-faqf{margin:18px 0 0;text-align:center;font-size:14.5px;color:#5B6582}
.pc-sec{max-width:1312px;margin:0 auto;padding:0 48px 96px;box-sizing:border-box;font-family:'Google Sans',system-ui,sans-serif;color:#0B1433}
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
.pc-me .nv-g{grid-template-columns:minmax(0,1fr)}
.pc-avl{display:none}
.pc-path{flex-direction:column;align-items:stretch;gap:16px}
.pc-roll{grid-template-columns:minmax(0,1fr);gap:24px}
.pc-ar{grid-template-columns:minmax(0,1fr)}
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
.pc-rc{grid-template-columns:minmax(0,1fr)}
.pc-arr{justify-self:center;transform:rotate(90deg)}
.pc-tiers{grid-template-columns:minmax(0,1fr) minmax(0,1fr) minmax(0,1fr)}
.pc-tiers span{padding:10px}
.pc-ar .lr-card,.pc-ar .pc-ai{padding:22px 18px}
.pc-ph1{font-size:26px}
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
''' + NAVH + '''
''' + PR + '''

<sc-if value="{{pr.guest}}" hint-placeholder-val="{{ true }}">
<section class="pc-sec pc-ent" id="pc-ent" aria-label="Credalio for organisations"><div class="ci-doors">''' + DOOR + '''</div></section>

</sc-if>
<section class="pc-sec" aria-labelledby="pc-tu">
<div class="pc-top">
<div><span class="pc-k">DLP top-ups</span><h2 id="pc-tu" class="pc-h2">{{pr.topT}}</h2><p class="pc-p">Add DLP without changing your plan. Handy on Pro, or when you just need a little extra.</p></div>
<div class="cb-g">''' + TOPS + '''</div>
</div>
</section>

<sc-if value="{{pr.guest}}" hint-placeholder-val="{{ true }}">
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
</sc-if>

<sc-if value="{{pr.guest}}" hint-placeholder-val="{{ true }}">
<section class="pc-sec" aria-labelledby="pc-ro">
<div class="pc-roll">
<div><span class="pc-k">Rollover</span><h2 id="pc-ro" class="pc-h2">Life happens. Your learning can wait.''' + tip('On Pro, unused DLP rolls over up to 18,000. Gradual decay starts from month four. Basic follows the Basic plan policy, which is being finalised.') + '''</h2><p class="pc-p">On Pro, the DLP you don’t use this month carries into the next one.</p></div>
<div class="pc-rc">
<section class="ds-card nv-use" aria-label="Month one"><div class="nv-uh"><h2>September</h2><span class="nv-tot"><b>6,000</b> received</span></div><ul class="nv-l"><li><span class="nv-k">Used</span><span class="nv-bar"><i style="width: 67%"></i></span><b>4,000</b></li><li><span class="nv-k">Left over</span><span class="nv-bar"><i class="pc-rb" style="width: 33%"></i></span><b>2,000</b></li></ul></section>
<span class="pc-arr" aria-hidden="true"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"></path><path d="m13 6 6 6-6 6"></path></svg></span>
<section class="ds-card nv-use" aria-label="Month two"><div class="nv-uh"><h2>October</h2><span class="nv-tot"><b>8,000</b> available</span></div><ul class="nv-l"><li><span class="nv-k">New allowance</span><span class="nv-bar"><i style="width: 75%"></i></span><b>6,000</b></li><li><span class="nv-k">Rolled over</span><span class="nv-bar"><i class="pc-rb" style="width: 25%"></i></span><b>+2,000</b></li></ul></section>
</div>
</div>
</section>

<section class="pc-sec" aria-label="AI Coach and learning rewards">
<div class="pc-ar">
<section class="pc-ai nova-card" aria-labelledby="pc-ai">''' + AVN + '''<h3 id="pc-ai">Your AI Coach comes with you.</h3><p>Every plan includes an AI Coach. How much you can use it depends on your plan.</p>
<div class="pc-tiers"><span><b>Free</b>Basic access</span><span><b>Basic</b>Expanded</span><span><b>Pro</b>The most</span></div></section>
<section class="lr-card" aria-labelledby="pc-rw"><div class="lr-ch"><h3 id="pc-rw">Your learning can unlock more.''' + tip('Your plan pays for learning access. Rewards are a separate way to recognise qualifying learning and community activity.') + '''</h3><span class="ds-tag">Paid plans</span></div>
<div class="lr-cb"><span class="lr-ico">''' + dashgen.ic(dashgen.I['reward'], 22) + '''</span><div><h4>Learning Seasons</h4><p>On Basic and Pro, verified learning each season can earn rewards such as Marketplace Credits.</p></div></div>
<div class="pc-tiers"><span><b>Season LAS</b>Your activity score</span><span><b>Streak</b>Days in a row</span><span><b>Rewards</b>At season close</span></div>
<a class="ds-link" href="Dash-S3.dc.html">How rewards work''' + dashgen.ARR_S + '''</a></section>
</div>
</section>
</sc-if>

<section class="pc-sec pc-faq" aria-labelledby="pc-fq">
<div class="pc-sh"><div><span class="pc-k">FAQ</span><h2 id="pc-fq" class="pc-h2">Questions about plans and DLP</h2></div></div>
<div class="dt-faq">
<sc-for list="{{pr.faqs}}" as="f" hint-placeholder-count="6">
<div class="dt-fq {{f.cls}}"><button class="dt-fh" type="button" aria-expanded="{{f.exp}}" onClick="{{f.toggle}}">{{f.q}}<svg class="dt-chev" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"></path></svg></button><sc-if value="{{f.open}}" hint-placeholder-val="{{ false }}"><p class="dt-fa">{{f.a}}</p></sc-if></div>
</sc-for>
</div>
<p class="pc-faqf">Still stuck? <a class="ds-link" href="#">Contact support</a></p>
</section>

<sc-if value="{{pr.guest}}" hint-placeholder-val="{{ true }}">
''' + FC + '''
</sc-if>
''' + LFOOT + '''
</div>'''

def jsblock(name):
    i = L.index('class ' + name); j = L.index('\nclass ', i + 10)
    return L[i:j]
PART = L[L.index('class Part {'):L.index('function momentVals')]
PRICE = jsblock('PricePart').replace("this.state = { hours: 20, open: false };", "this.state = { hours: 20, open: true };")
PRICE = PRICE.replace("open: this.state.open ? 'true' : 'false',", "selCls: 'sel-' + fit, open: this.state.open ? 'true' : 'false',")
PRICE = PRICE.replace("pick: function () { self.setState({ hours: p.set }); } };", "href: ['OnbWelcome.dc.html', 'Chk-001.dc.html', 'Chk-001p.dc.html'][k], pick: function () { self.setState({ hours: p.set }); } };")

PRICE = PRICE.replace("this.state = { hours: 20, open: true };", "var md = (host.props || {}).mode || 'guest'; this.mode = md; this.state = { hours: { free: 2, basic: 20, pro: 60, path: 20 }[md] || 20, open: md === 'guest', faq: 0 };")
PRICE = PRICE.replace("var self = this, h = this.state.hours, fit = h <= 2 ? 0 : (h <= 20 ? 1 : 2);", "var self = this, md = this.mode, h = this.state.hours, fit = h <= 2 ? 0 : (h <= 20 ? 1 : 2), cur = { free: 0, basic: 1, pro: 2 }[md], mine = cur !== undefined, isPath = md === 'path'; var FITS = { path: ['You can start Stage 1 with your 200 DLP.', 'Covers about half the path each month. Stages 1 and 2 fit in one allowance.', 'Enough each month for the whole path, as you learn.'], free: ['Explore and start eligible learning.', 'Ten times your allowance. About 20 hours a month.', 'About 60 hours a month, with rollover up to 18,000.'], basic: ['Explore and start eligible learning.', 'Your plan today.', 'Three times your allowance, with rollover up to 18,000.'], pro: ['Explore and start eligible learning.', 'About 20 hours a month.', 'The most allowance each month, with rollover.'] }[md]; var HREF = isPath ? ['PathDetail-Learner.dc.html', 'Chk-006.dc.html', 'Chk-006p.dc.html'] : (mine ? ['#', 'Chk-007.dc.html', 'Chk-007p.dc.html'] : ['OnbWelcome.dc.html', 'Chk-001.dc.html', 'Chk-001p.dc.html']);")
PRICE = PRICE.replace("href: ['OnbWelcome.dc.html', 'Chk-001.dc.html', 'Chk-001p.dc.html'][k], pick:", "href: HREF[k], isCur: k === cur, desc: FITS ? FITS[k] : p.desc, cta: isPath ? (k === 0 ? 'Start with my 200 DLP' : 'Choose ' + p.label) : (mine ? (k < cur ? 'Change to ' + p.label : (k === 0 ? 'Change to Free' : 'Upgrade to ' + p.label)) : p.cta), pick:")
PRICE = PRICE.replace("tabCls: k === fit ? 'on' : '', sel: k === fit ? 'true' : 'false', fit: k === fit, nofit: k !== fit,", "tabCls: k === fit ? 'on' : '', sel: k === fit ? 'true' : 'false', fit: k === fit && k !== cur, nofit: k !== fit && k !== cur,")
PRICE = PRICE.replace("selCls: 'sel-' + fit,", """selCls: 'sel-' + fit, guest: md === 'guest', member: md !== 'guest', mine: mine, isPath: isPath,
      bal: { free: '80', basic: '1,460', pro: '4,250', path: '200' }[md] || '0', curName: ['Free', 'Basic', 'Pro'][cur] || '',
      curSub: { free: '200 DLP · refreshes 1 Oct', basic: '2,000 DLP a month · refreshes 12 Oct', pro: '6,000 DLP a month · refreshes 12 Oct' }[md] || '',
      nova: { free: 'At about 120 DLP a month, Free covers you for now. If you start a career path, Basic gives you far more room.', basic: 'You’ve used 540 DLP this month. At this pace, Basic lasts until your refresh on 12 October.', pro: 'You have plenty this month. If you ever run short before 12 October, a top-up is simpler than changing plans.' }[md] || '',
      plansHead: md === 'pro' ? 'Other plans' : 'Need more room to learn?', topT: md === 'pro' ? 'Need a little more before 12 October?' : 'Need a little more this month?',
      faqs: FAQ.map(function (f, i) { var open = self.state.faq === i; return { q: f[0], a: f[1], open: open, exp: open ? 'true' : 'false', cls: open ? 'dt-fq-open' : '', toggle: function () { self.setState({ faq: open ? -1 : i }); } }; }),""")
PRICE = PRICE.replace("constructor(host) { super(host);", "constructor(host) { super(host); this.host = host;")

FINAL = jsblock('FinalPart')

JS = '\nvar FAQ = ' + json.dumps(FAQS) + ';\n' + PART + PRICE + '\n' + FINAL + '''
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
  renderVals() { var o = {}; for (var k in this.parts) o[k] = this.parts[k].renderVals(); o.ftSub = function (e) { if (e && e.preventDefault) e.preventDefault(); }; return o; }
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
''' + BASE_CSS + style(L) + '\n' + KIT_CSS + '\n' + DCSS + '\n' + CSS + '\n' + FC_M + '''</style>
</helmet>
''' + BODY + '''
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{"mode":{"editor":"enum","options":["guest","free","basic","pro","path"],"default":"guest"},"$preview":{"width":1440,"height":4000}}'>''' + JS + '''</script>
</body>
</html>
'''

if __name__ == '__main__':
    open(OUT, 'w').write(HTML)
    print('wrote', OUT, len(HTML))
