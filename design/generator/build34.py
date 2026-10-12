# build34: CR-AI-001a (Copilot Act: apply changes, over LIVE COURSE-OV-001), CR-AI-003 (Copilot history, over LIVE DASH-NEW),
# CR-SEARCH-002 (global search results, Studio page), CR-HELP one source variants home / article (= HELP-001 / HELP-002).
# usage: python3 build34.py <dir>  (run in a scratch copy: build17 re-runs on import; copy back only the files printed at the end)
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build17 as B
from tipx import tip, TIP_CSS
P, rd, wr, ic, I, ARR = B.P, B.rd, B.wr, B.ic, B.I, B.ARR
OUT = []
X = ic('<path d="M7 7l10 10M17 7 7 17"></path>', 18, 2.2)
HIST = ic('<path d="M3 12a9 9 0 1 0 3-6.7L3 8"></path><path d="M3 3v5h5"></path><path d="M12 7v5l3 2"></path>', 18, 2)
SEND = ic('<path d="M12 19V5"></path><path d="m5 12 7-7 7 7"></path>', 18, 2.4)
CTX = ic('<rect x="3" y="4" width="18" height="16" rx="3"></rect><path d="M3 9h18"></path>', 14, 2)
BACK = ic('<path d="M19 12H5"></path><path d="m11 6-6 6 6 6"></path>', 18, 2.2)
PLUS = ic('<path d="M12 5v14M5 12h14"></path>', 16, 2.4)
CHEVR = ic('<path d="m9 6 6 6-6 6"></path>', 16, 2.2)
SRCH = ic('<circle cx="11" cy="11" r="7"></circle><path d="m20 20-3.5-3.5"></path>', 20, 2)
UP = ic('<path d="M7 10v11"></path><path d="M14 4.5 13 10h6a2 2 0 0 1 2 2.3l-1.3 7A2 2 0 0 1 17.7 21H7V10l4.6-6.3a1.6 1.6 0 0 1 2.4.8z"></path>', 16, 2)
DOWN = ic('<path d="M17 14V3"></path><path d="M10 19.5 11 14H5a2 2 0 0 1-2-2.3l1.3-7A2 2 0 0 1 6.3 3H17v11l-4.6 6.3a1.6 1.6 0 0 1-2.4-.8z"></path>', 16, 2)
wm = rd('CR-AI-001-Mobile.dc.html')
def mobw(n, src_imp, h=844):
    t = wm.replace('CR-AI-001 mobile', n + ' mobile').replace('<dc-import name="CR-AI-001"', src_imp)
    t = re.sub(r'hint-size="390px,\d+px"', f'hint-size="390px,{h}px"', t)
    t = re.sub(r'width: 390px; height: \d+px;', f'width: 390px; height: {h}px;', t, count=1)
    t = re.sub(r'"\$preview":\{"width":390,"height":\d+\}', f'"$preview":{{"width":390,"height":{h}}}', t)
    wr(n + '-Mobile.dc.html', t); OUT.append(n + '-Mobile.dc.html')
def nova(px):
    return (f'<span class="cp-av" aria-hidden="true" style="width: {px}px; height: {px}px"><img src="/_blob/b8f0756720795e1bd3b02e9c2655cb25" alt="" '
            'style="position: absolute; left: -87.50%; top: -57.81%; width: 294.06%; max-width: none; height: auto; mix-blend-mode: multiply"></span>')
a1 = rd('CR-AI-001.dc.html')
i = a1.find('/* CR-AI-001 Copilot panel */'); PCSS = a1[i:a1.find('</style>', i)]
def with_panel(base, panel, css, title):
    s = rd(base)
    assert s.count('</x-dc>') == 1
    s = s.replace('</x-dc>', panel + '\n</x-dc>', 1)
    k = s.rfind('</style>', 0, s.find('</helmet>'))
    s = s[:k] + PCSS + css + s[k:]
    return re.sub(r'<title>.*?</title>', f'<title>{title}</title>', s, count=1)
HEAD = ('<header class="cp-h">' + nova(40) + '<span class="cp-n"><b>Nova</b><span>Your Copilot</span></span>'
        '<a href="CR-AI-003.dc.html" class="cp-ib" aria-label="Past conversations">' + HIST + '</a>'
        '<a href="#" class="cp-ib" aria-label="Close">' + X + '</a></header>')
COMPOSER = ('<label class="cp-in"><span class="sr-only">Ask Nova</span><input placeholder="Ask Nova anything…"><button type="button" class="cp-go" aria-label="Send">' + SEND + '</button></label>')

# ======================= CR-AI-001a · Act: apply changes =======================
OUTC = ['Write SQL queries that filter and aggregate business data', 'Join tables to answer questions across sources', 'Present a recommendation backed by data']
act = ('<div class="cp-ov" aria-hidden="true"></div><aside class="cp" role="dialog" aria-label="Nova, your Copilot"><div class="cp-fx" aria-hidden="true"></div>' + HEAD +
       '<div class="cp-b"><span class="cp-ctx">' + CTX + 'Looking at Data Analysis with SQL</span>'
       '<div class="cp-me"><p>Add measurable outcomes to this course.</p></div>'
       '<div class="cp-m">' + nova(28) + '<div class="cp-col"><div class="cp-bub"><p>Here are three your learners can show they’ve reached. Nothing changes until you apply.</p></div>'
       '<div class="ac"><span class="ac-h">Adds 3 learning outcomes</span><ul class="ac-l">' + ''.join(f'<li><span class="ac-p">{PLUS}</span>{o}</li>' for o in OUTC) + '</ul>'
       '<div class="ac-f"><a href="#" class="ds-btn ac-go"><span>Apply changes</span></a><a href="#" class="ac-x">Not now</a></div></div></div></div></div>'
       '<footer class="cp-f">' + COMPOSER + '<span class="cp-cost"><i aria-hidden="true"></i>Applying uses about 400 Creio</span></footer></aside>')
ACSS = """
/* CR-AI-001a act card */
.cp-me{align-self:flex-end;max-width:82%;padding:12px 16px;border-radius:18px 18px 6px 18px;background:#1652F0;color:#FFFFFF}
.cp-me p{margin:0;font-size:14.5px;line-height:1.5}
.cp-col{display:flex;flex-direction:column;gap:10px;min-width:0;flex:1}
.ac{padding:16px 16px 14px 16px;border-radius:18px;border:1.5px solid #D6DDEE;background:#FFFFFF;box-shadow:0 10px 26px rgba(11,20,51,.06)}
.ac-h{display:block;font-size:14.5px;font-weight:600}
.ac-l{list-style:none;margin:12px 0 0 0;padding:0;display:flex;flex-direction:column;gap:10px}
.ac-l li{display:flex;align-items:flex-start;gap:10px;font-size:14px;line-height:1.45;color:#3A4566}
.ac-p{width:22px;height:22px;flex-shrink:0;border-radius:50%;background:#E7F5EE;color:#0F6B45;display:flex;align-items:center;justify-content:center}
.ac-p svg{width:13px;height:13px}
.ac-f{margin-top:16px;padding-top:14px;border-top:1.5px solid #F0F2F8;display:flex;align-items:center;gap:6px}
.ac-go{height:42px;padding:0 20px;font-size:14.5px}
.ac-x{height:42px;padding:0 14px;display:inline-flex;align-items:center;border-radius:999px;font-size:14.5px;font-weight:600;color:#3A4566;text-decoration:none}
.ac-x:hover{background:#F1F3F8}
@media (max-width: 960px){.ac-f{flex-direction:column;align-items:stretch}.ac-go{justify-content:center}.ac-x{justify-content:center}}
"""
wr('CR-AI-001a.dc.html', with_panel('CR-COURSE-OV-001.dc.html', act, ACSS, 'Credalio · Nova · Apply changes')); OUT.append('CR-AI-001a.dc.html')
mobw('CR-AI-001a', '<dc-import name="CR-AI-001a"', 844)

# ======================= CR-AI-003 · Copilot history =======================
HS = [('Improving SQL learning outcomes', 'Data Analysis with SQL', '28 Sep'), ('Understanding validation feedback', 'Case VAL-00928', '25 Sep'),
      ('Planning the January cohort', 'Applied AI Program', '18 Sep'), ('Choosing what to create', 'Dashboard', '2 Sep')]
hist = ('<div class="cp-ov" aria-hidden="true"></div><aside class="cp" role="dialog" aria-label="Past conversations with Nova"><div class="cp-fx" aria-hidden="true"></div>'
        '<header class="cp-h ch-h"><a href="CR-AI-001.dc.html" class="cp-ib" aria-label="Back to conversation">' + BACK + '</a><span class="cp-n"><b>Past conversations</b></span>'
        '<a href="#" class="cp-ib" aria-label="Close">' + X + '</a></header>'
        '<div class="ch-b"><ul class="ch-l">' + ''.join(f'<li><a href="CR-AI-001.dc.html" class="ch-r"><span class="ch-t"><b>{t}</b><span>{o} · {d}</span></span>{CHEVR}</a></li>' for t, o, d in HS) + '</ul>'
        '<span class="ch-n">Kept for 90 days.' + tip('Delete any conversation from its menu. Nova never shares them.', 'dn') + '</span></div>'
        '<footer class="cp-f"><a href="CR-AI-001.dc.html" class="ds-btn ch-new"><span>New conversation</span></a></footer></aside>')
HCSS = TIP_CSS + """
/* CR-AI-003 history */
.ch-h{padding-left:12px}
.ch-b{position:relative;flex-grow:1;overflow-y:auto;padding:8px 14px 20px 14px}
.ch-l{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:4px}
.ch-r{display:flex;align-items:center;gap:12px;padding:14px 12px;border-radius:14px;color:#0B1433;text-decoration:none}
.ch-r:hover{background:#F5F8FF}
.ch-r > svg{color:#8A93AD;flex-shrink:0}
.ch-t{flex-grow:1;min-width:0;display:flex;flex-direction:column;gap:3px}
.ch-t b{font-size:15px;font-weight:600}.ch-t span{font-size:13px;color:#5B6582}
.ch-n{display:flex;align-items:center;gap:4px;margin:14px 12px 0 12px;font-size:12.5px;color:#8A93AD}
.ch-new{justify-content:center;height:48px;font-size:15px}
"""
wr('CR-AI-003.dc.html', with_panel('CR-DASH-NEW.dc.html', hist, HCSS, 'Credalio · Nova · Past conversations')); OUT.append('CR-AI-003.dc.html')
mobw('CR-AI-003', '<dc-import name="CR-AI-003"', 844)

# ======================= CR-SEARCH-002 · results for "SQL" =======================
def hl(t):
    return re.sub(r'(SQL)', r'<mark>\1</mark>', t)
GR = [('Learning experiences', 'book', [('Data Analysis with SQL', 'Course · Published · Gold validated', 'CR-COURSE-OV-001.dc.html'), ('Advanced SQL for Analysts', 'Course · Published', '#')]),
      ('Content', 'doc', [('SQL joins', 'Chapter 3 · Data Analysis with SQL', '#'), ('SQL assessment', 'Chapter 5 quiz · 10 questions', '#')]),
      ('People', 'user', [('Mary Okafor', 'Co-creator · Data Analysis with SQL', '#'), ('Jane Adeyemi', 'Learner · Data Analysis with SQL', 'CR-LRN-002.dc.html')]),
      ('Validation', 'val', [('Case VAL-00928 · Data Analysis with SQL', '1 clarification open', 'CR-VAL-MC-002.dc.html')]),
      ('Discussions', 'chat', [('Understanding LEFT JOIN', 'Data Analysis with SQL · Chapter 3', 'CR-DISC-002.dc.html')]),
      ('Help', 'sup', [('How Credalio validates technical courses', 'Validation guide', 'CR-HELP-002.dc.html')])]
n_all = sum(len(g[2]) for g in GR)
tabs = f'<button type="button" class="sr-tb on">All <em>{n_all}</em></button>' + ''.join(f'<button type="button" class="sr-tb">{g} <em>{len(r)}</em></button>' for g, _, r in GR)
groups = ''.join(f'<section class="sr-g" aria-label="{g}"><span class="hp-lab">{g}</span><ul>' + ''.join(
    f'<li><a href="{h}" class="sr-r"><span class="hp-ic">{ic(I[i], 19)}</span><span class="sr-t"><b>{hl(t)}</b><span>{hl(d)}</span></span>{CHEVR}</a></li>' for t, d, h in r) + '</ul></section>' for g, i, r in GR)
main_sr = ('<main class="ds-main hp">\n<div class="hp-head ob-in"><div><h1 class="ds-h1 sr-h1">Results for “SQL”' + tip('You only see what you have access to.') + '</h1></div></div>'
           '<div class="sr-tabs ob-in2" role="tablist" aria-label="Filter results">' + tabs + '</div>'
           '<div class="ds-card sr ob-in3">' + groups + '</div>\n</main>')
css_sr = TIP_CSS + """
.sr-h1{display:flex;align-items:center;gap:10px}.sr-h1 .tip{margin-top:4px}
.sr-tabs{display:flex;gap:8px;overflow-x:auto;scrollbar-width:none;padding-bottom:2px}.sr-tabs::-webkit-scrollbar{display:none}
.sr-tb{flex-shrink:0;display:inline-flex;align-items:center;gap:8px;height:40px;padding:0 16px;border-radius:999px;border:1.5px solid #E6EAF3;background:#FFFFFF;font-family:inherit;font-size:14px;font-weight:500;color:#3A4566;cursor:pointer}
.sr-tb em{font-style:normal;font-size:12.5px;color:#8A93AD}
.sr-tb.on{background:#EAF0FF;border-color:#1652F0;color:#0E3BB8}.sr-tb.on em{color:#1652F0}
.sr{margin-top:18px;padding:8px 28px 18px 28px}
.sr-g{padding:18px 0 6px 0}
.sr-g + .sr-g{border-top:1.5px solid #F0F2F8}
.sr-g ul{list-style:none;margin:8px 0 0 0;padding:0;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:4px 24px}
.sr-r{display:flex;align-items:center;gap:14px;padding:10px 10px 10px 0;border-radius:14px;color:#0B1433;text-decoration:none}
.sr-r:hover .sr-t b{color:#1652F0}
.sr-r > svg{color:#CBD3E6;flex-shrink:0}
.sr-t{flex-grow:1;min-width:0;display:flex;flex-direction:column;gap:2px}
.sr-t b{font-size:15px;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.sr-t > span{font-size:13.5px;color:#5B6582;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.sr mark{background:#FFF1CF;color:inherit;border-radius:3px;padding:0 1px}
@media (max-width: 960px){
.sr-tabs{margin:0 -16px;padding:0 16px 2px 16px}
.sr-tb{height:38px;padding:0 14px;font-size:13.5px}
.sr{margin-top:14px;padding:2px 16px 10px 16px}
.sr-g{padding:16px 0 4px 0}
.sr-g ul{grid-template-columns:minmax(0,1fr)}
.sr-g li{min-width:0}
}
"""
B.page('CR-SEARCH-002', '', main_sr, "    return { navCls: S.nav ? 'ds-open' : '', toggleNav: () => this.setState({ nav: !S.nav }) };", css_sr, 'Credalio · Search · SQL')
s = rd('CR-SEARCH-002.dc.html')
s = s.replace('<input placeholder="Search your learning experiences, learners, discussions…">', '<input placeholder="Search your learning experiences, learners, discussions…" value="SQL">', 1)
wr('CR-SEARCH-002.dc.html', s); OUT.append('CR-SEARCH-002.dc.html')
mobw('CR-SEARCH-002', '<dc-import name="CR-SEARCH-002"', 1060)

# ======================= CR-HELP · variants home / article =======================
HC = [('path', 'Getting started', 8), ('doc', 'Creating', 14), ('col', 'Collaboration', 6), ('val', 'Validation', 11), ('card', 'Payments & Credit Wallet', 7),
      ('coin', 'Earnings & payouts', 6), ('user', 'Learners', 5), ('ai', 'Nova, your Copilot', 5), ('lock', 'Account & security', 7), ('book', 'Policies', 9)]
POP = ['How Credalio validates technical courses', 'Funding your Credit Wallet', 'Inviting a co-creator', 'Setting up payouts', 'What Nova can and can’t do']
cats = ''.join(f'<a href="#" class="hc-c"><span class="hp-ic">{ic(I[i], 20)}</span><span><b>{t.replace("&", "&amp;")}</b><span>{n} articles</span></span></a>' for i, t, n in HC)
pop = ''.join(f'<li><a href="CR-HELP-002.dc.html" class="hc-a"><span>{t}</span>{CHEVR}</a></li>' for t in POP)
home = ('<div class="hc-hero ob-in"><h1 class="ds-h1">How can we help?</h1>'
        '<label class="hc-s">' + SRCH + '<span class="sr-only">Search Help</span><input placeholder="Search Help, for example “payouts”"></label></div>'
        '<div class="hc-g ob-in2"><section aria-labelledby="hc-t"><h2 id="hc-t" class="hc-h2">Browse by topic</h2><div class="hc-cs">' + cats + '</div></section>'
        '<aside class="hc-side"><section class="ds-card hc-pc" aria-labelledby="hc-p"><h2 id="hc-p" class="hc-h2">Popular</h2><ul class="hc-al">' + pop + '</ul></section>'
        '<section class="ds-card hc-sup" aria-label="Contact support"><b>Can’t find an answer?</b><span>Our team replies in your support requests, usually within a day.</span>'
        f'<a href="#" class="ds-btn hp-btn hc-go"><span>Contact support</span><span class="ob-arrow">{ARR}</span></a>'
        '<a href="#" class="ds-link hc-my">My support requests <em>1 open</em></a></section></aside></div>')
BODY = ['Every technical course is reviewed by an Educational Validator and a Subject Matter Validator. When a course has substantial assessments, an Assessment Validator joins too.',
        'Subject Matter Validators check that code, commands and examples run as described, are current, and match the tool versions you state.',
        'If a validator needs something, the request goes to whoever created that part of the course. Everything stays in the case’s Validation Workspace, so nothing gets lost in email.',
        'Most technical cases usually reach a decision within two to three weeks.']
REL = ['Responding to a validator request', 'Validation tiers explained', 'When revalidation is needed']
art = ('<a href="CR-HELP-001.dc.html" class="pg-back ob-in">' + BACK + 'Help</a>'
       '<div class="ha-g"><article class="ha ob-in2"><span class="hp-lab">Validation guide</span><h1 class="ds-h1 ha-h1">How Credalio validates technical courses</h1>'
       '<span class="ha-d">Updated 18 Sep 2026 · 3 min read</span>' + ''.join(f'<p>{p}</p>' for p in BODY) +
       '<div class="ha-fb"><span>Was this helpful?</span><button type="button" class="ha-y">' + UP + 'Yes</button><button type="button" class="ha-y">' + DOWN + 'No</button></div></article>'
       '<aside class="ha-side ob-in3"><section class="ha-rel" aria-labelledby="ha-r"><h2 id="ha-r" class="hp-lab">Related</h2><ul class="hc-al">' + ''.join(f'<li><a href="#" class="hc-a"><span>{t}</span>{CHEVR}</a></li>' for t in REL) + '</ul></section>'
       '<section class="ds-card hc-sup ha-sup" aria-label="Contact support"><b>Still need help?</b><span>Our team usually replies within a day.</span><a href="#" class="hp-rb">Contact support</a></section></aside></div>')
main_h = ('<main class="ds-main hp">\n<sc-if value="{{isHome}}" hint-placeholder-val="{{true}}">' + home + '</sc-if>'
          '<sc-if value="{{isArt}}" hint-placeholder-val="{{false}}">' + art + '</sc-if>\n</main>')
js_h = """    const v = props.variant || 'home';
    return { navCls: S.nav ? 'ds-open' : '', toggleNav: () => this.setState({ nav: !S.nav }), isHome: v === 'home', isArt: v === 'article' };"""
css_h = """
.hc-hero{padding:40px 0 30px 0;display:flex;flex-direction:column;align-items:flex-start;gap:20px}
.hc-s{width:100%;max-width:640px;height:56px;box-sizing:border-box;display:flex;align-items:center;gap:12px;padding:0 20px;border-radius:999px;border:1.5px solid #D6DDEE;background:#FFFFFF;color:#5B6582;box-shadow:0 10px 30px rgba(11,20,51,.05)}
.hc-s:focus-within{border-color:#1652F0;box-shadow:0 0 0 4px rgba(22,82,240,.12)}
.hc-s input{flex-grow:1;min-width:0;border:0;outline:none;font-family:inherit;font-size:16px;color:#0B1433;background:transparent}
.hc-g{display:grid;grid-template-columns:minmax(0,1fr) 360px;gap:28px;align-items:start}
.hc-h2{margin:0 0 14px 2px;font-size:17px;font-weight:600}
.hc-cs{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.hc-c{display:flex;align-items:center;gap:14px;padding:16px;border-radius:18px;border:1.5px solid #E6EAF3;background:#FFFFFF;color:#0B1433;text-decoration:none;transition:border-color .2s ease,box-shadow .2s ease}
.hc-c:hover{border-color:#1652F0;box-shadow:0 10px 24px rgba(22,82,240,.08)}
.hc-c > span:last-child{display:flex;flex-direction:column;gap:2px}.hc-c b{font-size:15px;font-weight:600}.hc-c > span:last-child > span{font-size:13px;color:#5B6582}
.hc-side{display:flex;flex-direction:column;gap:16px}
.hc-pc{padding:22px 22px 12px 22px}
.hc-al{list-style:none;margin:0;padding:0}
.hc-a{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:12px 0;border-top:1.5px solid #F0F2F8;font-size:14.5px;font-weight:500;color:#0B1433;text-decoration:none}
.hc-al li:first-child .hc-a{border-top:0}
.hc-a svg{color:#CBD3E6;flex-shrink:0}.hc-a:hover{color:#1652F0}
.hc-sup{padding:22px;display:flex;flex-direction:column;align-items:flex-start;gap:4px;background:#FFFFFF url(/_blob/d268046654a4206d2a726e62005bcc59) center / cover no-repeat}
.hc-sup b{font-size:16px;font-weight:600}.hc-sup > span{font-size:14px;line-height:1.5;color:#3A4566}
.hc-go{margin-top:14px}
.hc-my{margin-top:12px;font-size:14px;display:inline-flex;align-items:center;gap:8px}
.hc-my em{font-style:normal;height:22px;padding:0 8px;border-radius:999px;background:#EAF0FF;color:#0E3BB8;font-size:12px;font-weight:500;display:inline-flex;align-items:center}
.pg-back{display:inline-flex;align-items:center;gap:8px;margin-top:22px;font-size:14px;font-weight:500;color:#4A5578;text-decoration:none}.pg-back:hover{color:#0B1433}
.ha-g{margin-top:18px;display:grid;grid-template-columns:minmax(0,720px) 320px;gap:48px;align-items:start}
.ha{padding-bottom:20px}
.ha-h1{margin-top:8px !important;font-size:clamp(28px,2.4vw,34px) !important}
.ha-d{display:block;margin-top:10px;font-size:13.5px;color:#5B6582}
.ha p{margin:22px 0 0 0;font-size:16.5px;line-height:1.75;color:#1F2A4A}
.ha-fb{margin-top:34px;padding-top:22px;border-top:1.5px solid #E6EAF3;display:flex;align-items:center;gap:10px;font-size:14.5px;font-weight:500;color:#3A4566}
.ha-fb > span{margin-right:6px}
.ha-y{display:inline-flex;align-items:center;gap:8px;height:40px;padding:0 16px;border-radius:999px;border:1.5px solid #D6DDEE;background:#FFFFFF;font-family:inherit;font-size:14px;font-weight:500;color:#0B1433;cursor:pointer}
.ha-y:hover{border-color:#1652F0}
.ha-side{position:sticky;top:96px;display:flex;flex-direction:column;gap:20px;padding-top:6px}
.ha-rel .hp-lab{margin:0 0 6px 0}
.ha-sup .hp-rb{margin-top:12px}
@media (max-width: 1080px){.hc-g{grid-template-columns:minmax(0,1fr)}.ha-g{grid-template-columns:minmax(0,1fr);gap:24px}.ha-side{position:static}}
@media (max-width: 960px){
.hc-hero{padding:24px 0 22px 0;gap:16px}
.hc-s{height:52px;padding:0 16px}.hc-s input{font-size:15px}
.hc-cs{display:flex;gap:8px;overflow-x:auto;margin:0 -16px;padding:0 16px 4px 16px;scrollbar-width:none}.hc-cs::-webkit-scrollbar{display:none}
.hc-c{flex-shrink:0;padding:10px 16px 10px 10px;gap:10px;border-radius:999px}
.hc-c .hp-ic{width:34px;height:34px;border-radius:50%}
.hc-c > span:last-child > span{display:none}.hc-c b{font-size:14px;white-space:nowrap}
.hc-g{gap:28px}
.hc-pc{padding:18px 18px 8px 18px}
.hc-sup{padding:20px 18px}
.hc-go{width:100%;justify-content:space-between}
.pg-back{margin-top:12px}
.ha-g{margin-top:22px}
.ha p{font-size:15.5px;line-height:1.7;margin-top:18px}
.ha-fb{flex-wrap:wrap}
}
"""
B.page('CR-HELP', '', main_h, js_h, css_h, 'Credalio · Help', "{ nav: false }")
s = rd('CR-HELP.dc.html').replace('constructor(props) { super(props);', 'constructor(props) { super(props); this.props0 = props;', 1)
s = s.replace('    const S = this.state;\n', '    const S = this.state, props = this.props0 || {};\n', 1)
wr('CR-HELP.dc.html', s); OUT.append('CR-HELP.dc.html')
wd = rd('CR-SET-001.dc.html')
for n, var, hm in [('CR-HELP-001', 'home', 900), ('CR-HELP-002', 'article', 1240)]:
    t = wd.replace('<dc-import name="CR-SET" variant="account"', f'<dc-import name="CR-HELP" variant="{var}"').replace('CR-SET-001', n)
    wr(n + '.dc.html', t); OUT.append(n + '.dc.html')
    mobw(n, f'<dc-import name="CR-HELP" variant="{var}"', hm)
print('build34 ok'); print(' '.join(OUT))
