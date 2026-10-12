# build31: CR-ANA-002p program analytics, CR-ANA-003 compare, CR-PROF (variants profile / creds = PROF-001 / 001c),
# CR-PUB (variant preview = PROF-001v; public = PROF-002 later). Studio pages via build17 page(). usage: python3 build31.py <dir>
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build17 as B
from tipx import tip, TIP_CSS
P, rd, wr, ic, I, ARR = B.P, B.rd, B.wr, B.ic, B.I, B.ARR
CHK = ic('<path d="m5 12.5 4.5 4.5L19 7.5"></path>', 12, 3)
BACK = ic('<path d="M19 12H5"></path><path d="m11 6-6 6 6 6"></path>', 16, 2.2)
CHEVD = ic('<path d="m6 9 6 6 6-6"></path>', 15, 2.2)
X = ic('<path d="M7 7l10 10M17 7 7 17"></path>', 13, 2.2)
PLUS = ic('<path d="M12 5v14M5 12h14"></path>', 15, 2.2)
EYE = ic('<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"></path><circle cx="12" cy="12" r="3"></circle>', 16, 2)
PIN = ic('<path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21z"></path><circle cx="12" cy="9.5" r="2.5"></circle>', 15, 2)
SHIELD = ic('<path d="M12 3l8 3v6c0 4.5-3.4 8.3-8 9-4.6-.7-8-4.5-8-9V6z"></path><path d="m8.5 12 2.5 2.5 4.5-5"></path>', 15, 2)
PBG = '/_blob/d268046654a4206d2a726e62005bcc59'
wd, wm = rd('CR-DASH-S03.dc.html'), rd('CR-CRED-002c-Mobile.dc.html')
def mob(t, h):
    t = re.sub(r'hint-size="[^"]*"', f'hint-size="390px,{h}px"', t)
    t = re.sub(r'width: \d+px; height: \d+px;', f'width: 390px; height: {h}px;', t, count=1)
    return re.sub(r'"\$preview":\{"width":\d+,"height":\d+\}', f'"$preview":{{"width":390,"height":{h}}}', t)
def wrap(src, items):
    for n, var, hm in items:
        imp = f'<dc-import name="{src}"' + (f' variant="{var}"' if var else '')
        if n != src:
            t = wd.replace('<dc-import name="CR-DASH-ST" variant="s03"', imp)
            wr(n + '.dc.html', re.sub(r'<title>.*?</title>', f'<title>{n} preview</title>', t))
        t = mob(wm.replace('<dc-import name="CR-CRED-002" variant="badge"', imp), hm)
        wr(n + '-Mobile.dc.html', re.sub(r'<title>.*?</title>', f'<title>{n} mobile preview</title>', t))
def props_patch(name):
    s = rd(name + '.dc.html').replace('constructor(props) { super(props);', 'constructor(props) { super(props); this.props0 = props;', 1)
    s = s.replace('    const S = this.state;\n', '    const S = this.state, props = this.props0 || {};\n', 1)
    wr(name + '.dc.html', s)
NAVJS = '''    return { navCls: S.nav ? 'ds-open' : '', toggleNav: () => this.setState({ nav: !S.nav }) };'''
COMMON = TIP_CSS + '''
.pg-back{display:inline-flex;align-items:center;gap:8px;margin-top:22px;font-size:14px;font-weight:500;color:#4A5578;text-decoration:none}
.pg-back:hover{color:#0B1433}
.pg-back + .hp-head{padding-top:10px}
.ds-h1 .tip{margin-left:10px;vertical-align:4px}
.st{display:inline-flex;align-items:center;gap:6px;height:28px;padding:0 12px;border-radius:999px;font-size:13px;font-weight:500;white-space:nowrap}
.st.cb{background:#EAF0FF;color:#0E3BB8}.st.am{background:#FFF3E0;color:#9A5B00}.st.gr{background:#E7F5EE;color:#0F6B45}.st.gy{background:#F1F3F8;color:#5B6582}
.h2c{display:flex;align-items:center;margin:0;font-size:17px;font-weight:600}
.kpi{display:grid;grid-template-columns:repeat(4,1fr);padding:22px 0}
.kpi > div{display:flex;flex-direction:column;gap:8px;padding:0 28px}
.kpi > div + div{border-left:1.5px solid #F0F2F8}
.kpi .hp-lab{display:flex;align-items:center}
.kpi b{font-size:26px;font-weight:600;letter-spacing:-0.02em;font-variant-numeric:tabular-nums}
.rb-ic{gap:8px}.rb-ic svg{color:#5B6582}
.chip{display:inline-flex;align-items:center;gap:6px;height:34px;padding:0 8px 0 14px;border-radius:999px;background:#F5F8FF;border:1.5px solid #D6DDEE;font-size:14px;font-weight:500;color:#0B1433}
.chip button{width:22px;height:22px;border:0;border-radius:50%;background:transparent;color:#8A93AD;display:inline-flex;align-items:center;justify-content:center;cursor:pointer}
.chip.add{padding:0 14px;border-style:dashed;background:#FFFFFF;color:#1652F0;gap:6px}
@media (max-width: 960px){
.pg-back{margin-top:12px}
.kpi{grid-template-columns:1fr 1fr;padding:6px 0}
.kpi > div{padding:14px 18px}
.kpi > div + div{border-left:0}
.kpi > div:nth-child(even){border-left:1.5px solid #F0F2F8}.kpi > div:nth-child(n+3){border-top:1.5px solid #F0F2F8}
.kpi b{font-size:20px}
}
'''
RANGE = '<button type="button" class="hp-rb rb-ic">' + ic(I['cal'], 15, 2) + 'Last 30 days' + CHEVD + '</button>'

# ======================= CR-ANA-002p · learning program =======================
WK = [(1, 96), (2, 91), (3, 84), (4, 76), (5, 52), (6, 0), (7, 0), (8, 0)]
weeks = ''.join(f'<div class="wk {"now" if w == 5 else ("fut" if p == 0 else "")}"><i style="height:{max(p, 0)}%"><span class="wk-tt">Week {w}: <b>{p}%</b> done</span></i><em>W{w}</em></div>' for w, p in WK)
TEAMS = [('Ledger', 'Automating invoice matching', 'On track', 'gr'), ('Pulse', 'Support ticket triage', 'On track', 'gr'), ('Atlas', 'Stock forecasting', 'Needs help', 'am'), ('Signal', 'Churn early warning', 'On track', 'gr')]
teams = ''.join(f'<li><span><b>{n}</b><span>{d}</span></span><span class="st {c}">{s}</span></li>' for n, d, s, c in TEAMS)
main = ('<main class="ds-main hp">\n<a href="CR-ANA-001.dc.html" class="pg-back">' + BACK + 'Analytics</a>'
        '<div class="hp-head ob-in"><div><h1 class="ds-h1">Applied AI Program</h1></div><div class="an-acts">' + RANGE + '</div></div>'
        '<section class="ds-card kpi ob-in2"><div><span class="hp-lab">Learners</span><b>186</b></div><div><span class="hp-lab">Cohort</span><b>Week 5 of 8</b></div>'
        '<div><span class="hp-lab">On pace' + tip('Learners who finished every module released so far.') + '</span><b>71%</b></div><div><span class="hp-lab">Rating</span><b>4.5</b></div></section>'
        '<div class="ax-g"><section class="ds-card ax-c ob-in3" aria-labelledby="pg-h1"><h2 id="pg-h1" class="h2c">Weekly modules done</h2><div class="wks">' + weeks + '</div></section>'
        '<section class="ds-card ax-c ob-in3" aria-labelledby="pg-h2"><h2 id="pg-h2" class="h2c">Capstone teams</h2><ul class="tm">' + teams + '</ul></section></div>\n</main>')
css = COMMON + '''
.an-acts{display:flex;gap:10px}
.ax-g{margin-top:20px;display:grid;grid-template-columns:minmax(0,1.5fr) minmax(0,1fr);gap:20px;align-items:start}
.ax-c{padding:24px 26px}
.wks{margin-top:26px;height:220px;display:grid;grid-template-columns:repeat(8,1fr);gap:10px;align-items:end;padding-bottom:26px;border-bottom:1.5px solid #E6EAF3}
.wk{position:relative;height:100%;display:flex;align-items:flex-end}
.wk i{position:relative;display:block;width:100%;border-radius:4px 4px 0 0;background:#1652F0;cursor:crosshair}
.wk.now i{background:#7FA0F7}
.wk.fut i{height:100% !important;background:repeating-linear-gradient(135deg,#F5F7FB 0 6px,#EEF1F7 6px 12px);border-radius:4px;cursor:default}
.wk.fut .wk-tt{display:none}
.wk em{position:absolute;bottom:-24px;left:0;right:0;text-align:center;font-style:normal;font-size:12px;color:#8A93AD}
.wk.now em{color:#0B1433;font-weight:600}
.wk-tt{position:absolute;left:50%;bottom:calc(100% + 8px);transform:translateX(-50%);padding:5px 9px;border-radius:9px;background:#0B1433;color:#FFFFFF;font-size:12px;white-space:nowrap;opacity:0;pointer-events:none;z-index:3}
.wk i:hover .wk-tt{opacity:1}
.tm{list-style:none;margin:12px 0 0 0;padding:0}
.tm li{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:14px 0;border-top:1.5px solid #F0F2F8}
.tm li:first-child{border-top:0}
.tm li > span:first-child{display:flex;flex-direction:column;gap:2px;min-width:0}.tm b{font-size:15px;font-weight:600}.tm li > span > span{font-size:13.5px;color:#5B6582}
@media (max-width: 1080px){.ax-g{grid-template-columns:minmax(0,1fr)}}
@media (max-width: 960px){
.hp-head{flex-direction:column;align-items:stretch;gap:12px}
.an-acts .rb-ic{display:inline-flex !important;height:36px;padding:0 12px;font-size:13px;align-self:flex-start}
.ax-g{gap:14px;margin-top:14px}.ax-c{padding:18px 16px}
.wks{height:170px;gap:6px}
}
'''
B.page('CR-ANA-002p', 'Analytics', main, NAVJS, css, 'Credalio · Applied AI Program', "{ nav: false }")
wrap('CR-ANA-002p', [('CR-ANA-002p', '', 1000)])

# ======================= CR-ANA-003 · compare =======================
CO = ['Data Analysis with SQL', 'Advanced SQL for Analysts']
ROWS = [('Learners', ['1,284', '428'], 0, ''), ('Completion', ['68%', '59%'], 0, ''), ('Average quiz score', ['81%', '84%'], 1, ''),
        ('Rating', ['4.8', '4.7'], 0, ''), ('Earned · 30 days', ['$1,410', '$430'], 0, ''), ('Biggest drop', ['Chapter 4', 'Chapter 2'], -1, 'Where the most learners stop.')]
def crow(lab, vals, best, t):
    cells = ''.join(f'<span class="cp-v {"best" if i == best else ""}">{v}' + ('<em>Best</em>' if i == best else '') + '</span>' for i, v in enumerate(vals))
    return f'<li><span class="cp-l">{lab}' + (tip(t) if t else '') + f'</span>{cells}<span class="cp-v cp-e"></span></li>'
main = ('<main class="ds-main hp">\n<a href="CR-ANA-001.dc.html" class="pg-back">' + BACK + 'Analytics</a>'
        '<div class="hp-head ob-in"><div><h1 class="ds-h1">Compare</h1></div><div class="an-acts">' + RANGE + '</div></div>'
        '<section class="ds-card cp ob-in2" aria-label="Comparison"><div class="cp-hd"><span></span>'
        + ''.join(f'<span class="chip">{c}<button type="button" aria-label="Remove">{X}</button></span>' for c in CO) +
        '<span><button type="button" class="chip add">' + PLUS + 'Add</button></span></div>'
        '<ul class="cp-l">' + ''.join(crow(*r) for r in ROWS) + '</ul></section>\n</main>')
css = COMMON + '''
.an-acts{display:flex;gap:10px}
.cp{padding:14px 26px 10px 26px}
.cp-hd,.cp-l li{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.2fr) minmax(0,1.2fr) minmax(0,1fr);gap:20px;align-items:center}
.cp-hd{padding:12px 0 16px 0;border-bottom:1.5px solid #F0F2F8}
.cp-hd .chip{justify-self:start;max-width:100%}
.cp-l{list-style:none;margin:0;padding:0}
.cp-l li{padding:18px 0;border-top:1.5px solid #F0F2F8}
.cp-l li:first-child{border-top:0}
.cp-l-dummy{}
.cp-l{list-style:none}
.cp-l .cp-l{display:none}
.cp-l li > .cp-l{}
.cp-l li .cp-l{}
.cp-l .cp-v{font-size:18px;font-weight:600;font-variant-numeric:tabular-nums;display:inline-flex;align-items:center;gap:10px}
.cp-l .cp-v em{font-style:normal;height:22px;padding:0 8px;border-radius:999px;background:#EAF0FF;color:#0E3BB8;font-size:12px;font-weight:500;display:inline-flex;align-items:center}
.cp-l li > span:first-child{display:inline-flex;align-items:center;font-size:14.5px;color:#4A5578}
@media (max-width: 960px){
.hp-head{flex-direction:column;align-items:stretch;gap:12px}
.an-acts .rb-ic{display:inline-flex !important;height:36px;padding:0 12px;font-size:13px;align-self:flex-start}
.cp{padding:6px 14px}
.cp-hd{grid-template-columns:1fr 1fr;gap:8px}.cp-hd > span:first-child,.cp-hd > span:last-child{display:none}
.cp-hd .chip{font-size:12.5px;height:auto;min-height:34px;padding:6px 6px 6px 12px;line-height:1.3}
.cp-l li{grid-template-columns:1fr 1fr;gap:6px 8px;padding:14px 0}
.cp-l li > span:first-child{grid-column:1 / -1;font-size:13px}
.cp-e{display:none !important}
.cp-l .cp-v{font-size:16px}
}
'''
B.page('CR-ANA-003', 'Analytics', main, NAVJS, css, 'Credalio · Compare', "{ nav: false }")
wrap('CR-ANA-003', [('CR-ANA-003', '', 800)])

# ======================= CR-PROF · profile management =======================
TOP = ['Data Analysis', 'SQL', 'Business Intelligence']
CRED = [('MSc Data Science', 'University of Lagos · 2017', 'Verified', 'gr', True), ('AWS Certified Data Analytics', 'Amazon Web Services · 2023', 'Verified', 'gr', True),
        ('Google Data Analytics Certificate', 'Google · 2024', 'Couldn’t read', 'am', False), ('Senior Data Analyst', 'Flutterwave · 2019 – now', 'In review', 'cb', False)]
creds = ''.join(f'<li><span class="pc-t"><b>{t}</b><span>{d}</span></span><span class="st {c}">' + (CHK if c == 'gr' else '') + f'{s}' + (tip('Upload a clearer copy and we’ll verify it again.', 'r') if c == 'am' else '') + '</span>'
                + f'<button type="button" class="hp-sw {"on" if on else ""}" aria-pressed="{"true" if on else "false"}" aria-label="Show {t} on profile" ' + ('' if c == 'gr' else 'disabled') + '></button></li>' for t, d, s, c, on in CRED)
tabs = '<div class="hp-tabs pf-tb ob-in2" role="tablist"><a href="CR-PROF-001.dc.html" class="hp-tab {{tP}}">Profile</a><a href="CR-PROF-001c.dc.html" class="hp-tab {{tC}}">Credentials</a></div>'
prof = ('<sc-if value="{{vProf}}" hint-placeholder-val="{{true}}"><div class="pf-g">'
        '<section class="ds-card pf-form ob-in3" aria-label="Edit profile">'
        '<div class="pf-me"><span class="pf-av">AO</span><span><b>Ada Ononuju</b><a href="#" class="ds-link">Change photo</a></span></div>'
        '<label class="fld"><span>Headline</span><span class="inp">I help professionals turn messy data into decisions.</span></label>'
        '<label class="fld"><span>Field and experience</span><span class="inp">Data &amp; Analytics · 8+ years' + CHEVD + '</span></label>'
        '<div class="fld"><span>Topics</span><span class="pf-ch">' + ''.join(f'<span class="chip">{t}<button type="button" aria-label="Remove">{X}</button></span>' for t in TOP) + '<button type="button" class="chip add">' + PLUS + 'Add</button></span></div>'
        '<div class="pf-sw"><span>Show “Lagos, Nigeria” on my profile</span><button type="button" class="hp-sw on" aria-pressed="true" aria-label="Show location"></button></div>'
        '<div class="pf-ft"><a href="#" class="ds-btn hp-btn"><span>Save changes</span><span class="ob-arrow">' + ARR + '</span></a></div></section>'
        '<aside class="pf-prev ob-in3" aria-label="How learners see you"><span class="hp-lab">How learners see you</span><div class="pv-card"><div class="pv-ban"></div><span class="pf-av pv-av">AO</span>'
        '<b class="pv-n">Ada Ononuju<span class="pv-badge" title="Identity verified">' + SHIELD + '</span></b><span class="pv-f">Data &amp; Analytics · 8+ years</span>'
        '<p>I help professionals turn messy data into decisions.</p><span class="pv-tp">' + ''.join(f'<i>{t}</i>' for t in TOP) + '</span></div></aside></div></sc-if>')
cred = ('<sc-if value="{{vCred}}" hint-placeholder-val="{{false}}"><section class="ds-card pc ob-in3" aria-label="Credentials"><div class="pc-hd"><span class="hp-lab">Show on profile' + tip('Only verified credentials can appear on your public profile.', 'r') + '</span></div><ul class="pc-l">' + creds + '</ul>'
        '<div class="pc-ft"><a href="CR-CRED-002.dc.html" class="hp-rb rb-ic">' + PLUS + 'Add credential</a></div></section></sc-if>')
main = ('<main class="ds-main hp">\n<div class="hp-head ob-in"><div><h1 class="ds-h1">Creator profile</h1></div><a href="CR-PROF-001v.dc.html" class="hp-rb rb-ic">' + EYE + 'View public profile</a></div>'
        + tabs + prof + cred + '\n</main>')
js = '''    const v = props.variant || 'profile';
    return { navCls: S.nav ? 'ds-open' : '', toggleNav: () => this.setState({ nav: !S.nav }), vProf: v === 'profile', vCred: v === 'creds',
      tP: v === 'profile' ? 'on' : '', tC: v === 'creds' ? 'on' : '' };'''
css = COMMON + '''
.pf-tb{margin-bottom:18px}
.pf-tb .hp-tab{text-decoration:none}
.pf-g{display:grid;grid-template-columns:minmax(0,1fr) 360px;gap:24px;align-items:start}
.pf-form{padding:26px 28px;display:flex;flex-direction:column;gap:22px}
.pf-me{display:flex;align-items:center;gap:16px}
.pf-me > span:last-child{display:flex;flex-direction:column;gap:4px}.pf-me b{font-size:16px;font-weight:600}.pf-me .ds-link{font-size:13.5px;font-weight:600}
.pf-av{width:64px;height:64px;border-radius:50%;background:#0B1433;color:#FFFFFF;display:inline-flex;align-items:center;justify-content:center;font-size:20px;font-weight:600;flex-shrink:0}
.fld{display:flex;flex-direction:column;gap:7px}
.fld > span:first-child{font-size:13.5px;font-weight:500;color:#4A5578}
.inp{display:flex;align-items:center;justify-content:space-between;gap:10px;min-height:48px;padding:0 16px;border-radius:12px;border:1.5px solid #D6DDEE;background:#FFFFFF;font-size:15px;color:#0B1433}.inp svg{color:#8A93AD}
.pf-ch{display:flex;flex-wrap:wrap;gap:8px}
.pf-sw{display:flex;align-items:center;justify-content:space-between;gap:16px;padding-top:18px;border-top:1.5px solid #F0F2F8;font-size:15px;font-weight:500}
.pf-ft{display:flex;justify-content:flex-end}
.pf-prev .hp-lab{margin:0 0 10px 4px}
.pv-card{position:relative;padding:0 22px 24px 22px;border-radius:20px;background:#FFFFFF;border:1.5px solid #E6EAF3;overflow:hidden;display:flex;flex-direction:column;align-items:flex-start}
.pv-ban{margin:0 -22px;width:calc(100% + 44px);height:96px;background:#EAF0FF url(''' + PBG + ''') center/cover no-repeat}
.pv-av{margin-top:-32px;border:4px solid #FFFFFF;width:68px;height:68px}
.pv-n{margin-top:12px;display:inline-flex;align-items:center;gap:6px;font-size:18px;font-weight:600}
.pv-badge{color:#0F6B45;display:inline-flex}
.pv-f{margin-top:2px;font-size:13.5px;color:#5B6582}
.pv-card p{margin:12px 0 0 0;font-size:14.5px;line-height:1.5;color:#1E2742}
.pv-tp{margin-top:14px;display:flex;flex-wrap:wrap;gap:6px}.pv-tp i{font-style:normal;height:28px;padding:0 11px;border-radius:999px;background:#F1F3F8;font-size:12.5px;font-weight:500;display:inline-flex;align-items:center;color:#3A4566}
.pc{padding:8px 28px 22px 28px;max-width:920px}
.pc-hd{display:flex;justify-content:flex-end;padding:14px 0 6px 0}
.pc-hd .hp-lab{display:inline-flex;align-items:center}
.pc-l{list-style:none;margin:0;padding:0}
.pc-l li{display:grid;grid-template-columns:minmax(0,1fr) auto 44px;align-items:center;gap:18px;padding:16px 0;border-top:1.5px solid #F0F2F8}
.pc-l li:first-child{border-top:0}
.pc-t{display:flex;flex-direction:column;gap:3px;min-width:0}.pc-t b{font-size:15px;font-weight:600}.pc-t span{font-size:13.5px;color:#5B6582}
.pc-l .st svg{color:#0F6B45}
.hp-sw[disabled]{opacity:.4;cursor:not-allowed}
.pc-ft{margin-top:10px;padding-top:18px;border-top:1.5px solid #F0F2F8}
@media (max-width: 1080px){.pf-g{grid-template-columns:minmax(0,1fr)}.pf-prev{display:none}}
@media (max-width: 960px){
.hp-head{flex-direction:row;align-items:center}
.hp-head .rb-ic{display:inline-flex !important;height:36px;padding:0 12px;font-size:13px}
.pf-tb{margin-bottom:12px}
.pf-form{padding:20px 18px;gap:18px}
.pf-av{width:52px;height:52px;font-size:17px}
.pf-sw{font-size:14px}
.pf-ft .hp-btn{width:100%;justify-content:space-between}
.pc{padding:4px 16px 16px 16px}
.pc-l li{grid-template-columns:minmax(0,1fr) 44px;gap:8px 12px}
.pc-l .st{grid-row:2;grid-column:1;justify-self:start;height:24px;font-size:12px;padding:0 9px}
.pc-l .hp-sw{grid-row:1 / span 2;grid-column:2}
}
'''
B.page('CR-PROF', 'Creator profile', main, js, css, 'Credalio · Creator profile', "{ nav: false }")
props_patch('CR-PROF')
wrap('CR-PROF', [('CR-PROF-001', 'profile', 820), ('CR-PROF-001c', 'creds', 844)])

# ======================= CR-PUB · public profile (preview) =======================
EXPS = [('Data Analysis with SQL', 'Course', 'Gold validated', '4.8', '1,284', 'c1'), ('Certified Data Analyst', 'Certification', '', '4.6', '312', 'c2'),
        ('Advanced SQL for Analysts', 'Course', '', '4.7', '428', 'c3'), ('Applied AI Program', 'Learning Program', 'with Samuel E.', '4.5', '186', 'c4')]
def ecard(t, k, x, r, l, c):
    return (f'<a href="#" class="pe {c}"><span class="pe-cv"><span class="pe-k">{k}</span>{ic(I["book"], 26, 1.7)}</span><span class="pe-b"><b>{t}</b>'
            + (f'<span class="pe-x">{x}</span>' if x else '') + f'<span class="pe-m">{ic(I["star"], 14, 2)}<b>{r}</b><em>{l} learners</em></span></span></a>')
CRS = [('MSc Data Science', 'University of Lagos'), ('AWS Certified Data Analytics', 'Amazon Web Services'), ('Senior Data Analyst', 'Flutterwave')]
main = ('<main class="ds-main hp">\n<sc-if value="{{isPrev}}" hint-placeholder-val="{{true}}"><div class="pb-bar ob-in">' + EYE + '<span>Preview · this is what learners see</span><a href="CR-PROF-001.dc.html" class="hp-rb">Edit profile</a></div></sc-if>'
        '<div class="pp-g">'
        '<aside class="pp-id ob-in2" aria-label="About Ada"><div class="pp-top"><span class="pp-av">AO</span><span class="pb-badge">' + SHIELD + 'Identity verified</span></div>'
        '<h1 class="pp-n">Ada Ononuju</h1><span class="pp-f">Data &amp; Analytics · 8+ years</span><span class="pp-loc">' + PIN + 'Lagos, Nigeria</span>'
        '<p class="pp-hl">I help professionals turn messy data into decisions.</p>'
        '<div class="pp-tp"><i>Data Analysis</i><i>SQL</i><i>Business Intelligence</i></div>'
        '<div class="pp-st"><div><b>2,210</b><span>learners</span></div><div><b>4.7</b><span>rating</span></div></div>'
        '<span class="hp-lab pp-lab">Verified credentials</span><ul class="pp-cr">' + ''.join(f'<li>{SHIELD}<span><b>{t}</b><span>{o}</span></span></li>' for t, o in CRS) + '</ul></aside>'
        '<section class="pp-ex ob-in3" aria-labelledby="pp-h"><h2 id="pp-h" class="pp-h">Learning experiences <em>4</em></h2><div class="pp-cards">' + ''.join(ecard(*e) for e in EXPS) + '</div></section>'
        '</div>\n</main>')
js = """    const v = props.variant || 'preview';
    return { navCls: S.nav ? 'ds-open' : '', toggleNav: () => this.setState({ nav: !S.nav }), isPrev: v === 'preview' };"""
css = COMMON + """
.pb-bar{margin-top:18px;display:flex;align-items:center;gap:8px;padding:0 4px;font-size:13.5px;font-weight:500;color:#5B6582}
.pb-bar svg{color:#8A93AD}.pb-bar span{flex:1}.pb-bar .hp-rb{height:auto;padding:0;border:0;background:transparent;color:#1652F0;font-size:13.5px;font-weight:600}
.pp-g{margin-top:24px;display:grid;grid-template-columns:360px minmax(0,1fr);gap:28px;align-items:start}
.pp-id{position:relative;padding:28px 28px 26px 28px;border-radius:24px;background:#FFFFFF url(""" + "'" + PBG + "'" + """) top center/100% 180px no-repeat;border:1.5px solid #E6EAF3;display:flex;flex-direction:column;align-items:flex-start}
.pp-top{width:100%;display:flex;align-items:flex-start;justify-content:space-between}
.pp-av{width:88px;height:88px;border-radius:50%;border:4px solid #FFFFFF;background:#0B1433;color:#FFFFFF;display:inline-flex;align-items:center;justify-content:center;font-size:26px;font-weight:600;box-shadow:0 10px 24px rgba(11,20,51,.12)}
.pb-badge{display:inline-flex;align-items:center;gap:6px;height:28px;padding:0 11px;border-radius:999px;background:#FFFFFF;color:#0F6B45;font-size:12.5px;font-weight:500}
.pp-n{margin:16px 0 0 0;font-size:28px;font-weight:600;letter-spacing:-0.02em;line-height:1.15}
.pp-f{margin-top:6px;font-size:14.5px;color:#3A4566}
.pp-loc{margin-top:4px;display:inline-flex;align-items:center;gap:6px;font-size:13.5px;color:#5B6582}.pp-loc svg{color:#8A93AD}
.pp-hl{margin:18px 0 0 0;font-size:16.5px;line-height:1.5;font-weight:500;color:#0B1433}
.pp-tp{margin-top:14px;width:100%;display:flex;flex-wrap:nowrap;gap:6px;overflow-x:auto;scrollbar-width:none;-webkit-mask-image:linear-gradient(90deg,#000 85%,transparent);mask-image:linear-gradient(90deg,#000 85%,transparent)}.pp-tp::-webkit-scrollbar{display:none}.pp-tp i{flex-shrink:0;white-space:nowrap}.pp-tp i{font-style:normal;height:30px;padding:0 12px;border-radius:999px;background:#F1F3F8;font-size:13px;font-weight:500;display:inline-flex;align-items:center;color:#3A4566}
.pp-st{margin-top:18px;width:100%;display:flex;gap:32px;padding:14px 0;border-top:1.5px solid #F0F2F8;border-bottom:1.5px solid #F0F2F8}
.pp-st div{display:flex;align-items:baseline;gap:8px}.pp-st b{font-size:22px;font-weight:600;letter-spacing:-0.01em}.pp-st span{font-size:13.5px;color:#5B6582}
.pp-lab{margin-top:16px}
.pp-cr{list-style:none;margin:10px 0 0 0;padding:0;display:flex;flex-direction:column;gap:12px;width:100%}
.pp-cr li{display:flex;align-items:flex-start;gap:10px}.pp-cr svg{color:#0F6B45;flex-shrink:0;margin-top:2px}
.pp-cr li > span{display:flex;flex-direction:column;gap:1px}.pp-cr b{font-size:14px;font-weight:600}.pp-cr li > span > span{font-size:12.5px;color:#5B6582}
.pp-h{margin:4px 0 16px 2px;display:flex;align-items:center;gap:10px;font-size:20px;font-weight:600;letter-spacing:-0.01em}
.pp-h em{font-style:normal;height:24px;min-width:24px;padding:0 8px;border-radius:999px;background:#EAF0FF;color:#0E3BB8;font-size:13px;font-weight:500;display:inline-flex;align-items:center;justify-content:center;box-sizing:border-box}
.pp-cards{display:grid;grid-template-columns:1fr 1fr;gap:18px}
.pe{display:flex;flex-direction:column;border-radius:20px;background:#FFFFFF;border:1.5px solid #E6EAF3;overflow:hidden;color:#0B1433;text-decoration:none;transition:box-shadow .2s ease,transform .2s ease}
.pe:hover{box-shadow:0 14px 34px rgba(11,20,51,.10);transform:translateY(-2px)}
.pe-cv{position:relative;height:112px;display:flex;align-items:flex-end;justify-content:flex-end;padding:16px 18px;color:rgba(255,255,255,.85)}
.pe.c1 .pe-cv{background:linear-gradient(135deg,#0E3BB8,#1652F0 60%,#5B85F5)}
.pe.c2 .pe-cv{background:linear-gradient(135deg,#0B1433,#1E3A8A)}
.pe.c3 .pe-cv{background:linear-gradient(135deg,#1652F0,#7FA0F7)}
.pe.c4 .pe-cv{background:linear-gradient(135deg,#1E3A8A,#4C6FE0)}
.pe-k{position:absolute;top:14px;left:16px;height:26px;padding:0 10px;border-radius:999px;background:rgba(255,255,255,.18);color:#FFFFFF;font-size:12px;font-weight:500;display:inline-flex;align-items:center;backdrop-filter:blur(4px)}
.pe-b{padding:16px 18px 18px 18px;display:flex;flex-direction:column;gap:4px}
.pe-b > b{font-size:16px;font-weight:600;line-height:1.3}
.pe-x{font-size:13px;color:#5B6582}
.pe-m{margin-top:10px;display:inline-flex;align-items:center;gap:6px;font-size:13.5px}.pe-m b{font-weight:600}.pe-m em{font-style:normal;color:#5B6582;margin-left:4px}
@media (max-width: 1180px){.pp-g{grid-template-columns:320px minmax(0,1fr)}}
@media (max-width: 1080px){.pp-g{grid-template-columns:minmax(0,1fr)}}
@media (max-width: 960px){
.pb-bar{margin-top:12px;font-size:13px}.pb-bar .hp-rb{display:inline-flex !important;font-size:13px}
.pp-g{margin-top:16px;gap:28px}
.pp-id{padding:26px 20px 28px 20px;border-radius:20px;background-size:100% 150px}
.pp-n{margin-top:22px !important}.pp-f{margin-top:8px}.pp-loc{margin-top:6px}
.pp-hl{margin-top:22px !important}.pp-tp{margin-top:18px}
.pp-st{margin-top:26px;padding:20px 0}
.pp-lab{margin-top:26px}.pp-cr{margin-top:14px;gap:18px}
.pp-av{width:76px;height:76px;font-size:22px}
.pp-n{font-size:24px;margin-top:18px}
.pp-hl{font-size:15.5px}
.pp-cards{grid-template-columns:1fr;gap:12px}
.pe{flex-direction:row}
.pe-cv{width:92px;height:auto;flex-shrink:0;padding:12px;justify-content:center;align-items:center}
.pe-k{display:none}
.pe-b{padding:14px 16px}
.pe-b > b{font-size:15px}
.pe-m{margin-top:6px}
}
"""
B.page('CR-PUB', 'Creator profile', main, js, css, 'Credalio · Ada Ononuju', "{ nav: false }")
props_patch('CR-PUB')
wrap('CR-PUB', [('CR-PROF-001v', 'preview', 1320)])
print('build31 ok')
