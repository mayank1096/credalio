# build26: payout status (CR-PAYST, variants proc / action = PAYO-005 / 005a), payout history (CR-PAYO-006),
# course overview (CR-COURSE-OV-001) and discussions (CR-DISC, variant all = DISC-001). Studio pages via build17 page().
# Minimal: one job per page, explanations in tooltips. usage: python3 build26.py <canvas project dir>
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build17 as B
from tipx import tip, TIP_CSS
P, rd, wr, ic, I, ARR = B.P, B.rd, B.wr, B.ic, B.I, B.ARR
CHK = ic('<path d="m5 12.5 4.5 4.5L19 7.5"></path>', 12, 3)
CHEV = ic('<path d="m9 6 6 6-6 6"></path>', 16, 2.2)
BACK = ic('<path d="M19 12H5"></path><path d="m11 6-6 6 6 6"></path>', 16, 2.2)
WARN = ic('<path d="M12 8v5M12 16.5v.01"></path><circle cx="12" cy="12" r="9"></circle>', 20, 2.2)
REPLY = ic('<path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.4A8 8 0 1 1 21 12z"></path>', 15, 2)
PPL = '/_blob/27435c5526a86beb998393f8bb53a00c'
wd, wm = rd('CR-DASH-S03.dc.html'), rd('CR-CRED-002c-Mobile.dc.html')
def mob(t, h):
    t = re.sub(r'hint-size="[^"]*"', f'hint-size="390px,{h}px"', t)
    t = re.sub(r'width: \d+px; height: \d+px;', f'width: 390px; height: {h}px;', t, count=1)
    return re.sub(r'"\$preview":\{"width":\d+,"height":\d+\}', f'"$preview":{{"width":390,"height":{h}}}', t)
def wrap(src, items):
    for n, var, hm in items:
        imp = f'<dc-import name="{src}"' + (f' variant="{var}"' if var else '')
        t = wd.replace('<dc-import name="CR-DASH-ST" variant="s03"', imp)
        wr(n + '.dc.html', re.sub(r'<title>.*?</title>', f'<title>{n} preview</title>', t))
        t = mob(wm.replace('<dc-import name="CR-CRED-002" variant="badge"', imp), hm)
        wr(n + '-Mobile.dc.html', re.sub(r'<title>.*?</title>', f'<title>{n} mobile preview</title>', t))
def props_patch(name):
    s = rd(name + '.dc.html').replace('constructor(props) { super(props);', 'constructor(props) { super(props); this.props0 = props;', 1)
    s = s.replace('    const S = this.state;\n', '    const S = this.state, props = this.props0 || {};\n', 1)
    wr(name + '.dc.html', s)
COMMON = TIP_CSS + '''
.pg-back{display:inline-flex;align-items:center;gap:8px;margin-top:22px;font-size:14px;font-weight:500;color:#4A5578;text-decoration:none}
.pg-back:hover{color:#0B1433}
.pg-back + .hp-head{padding-top:10px}
.st{display:inline-flex;align-items:center;height:28px;padding:0 12px;border-radius:999px;font-size:13px;font-weight:500;white-space:nowrap}
.st.cb{background:#EAF0FF;color:#0E3BB8}.st.am{background:#FFF3E0;color:#9A5B00}.st.gr{background:#E7F5EE;color:#0F6B45}.st.gy{background:#F1F3F8;color:#5B6582}
.av{width:36px;height:36px;border-radius:50%;background:#EAF0FF;color:#0E3BB8;display:inline-flex;align-items:center;justify-content:center;font-size:12.5px;font-weight:600;flex-shrink:0}
@media (max-width: 960px){.pg-back{margin-top:12px}}
'''

# ======================= CR-PAYST · payout status =======================
main = ('<main class="ds-main hp">\n<a href="CR-EARN-001.dc.html" class="pg-back">' + BACK + 'Earnings</a>'
        '<div class="hp-head ob-in"><div><h1 class="ds-h1">November payout</h1></div><span class="st {{stCls}}">{{stTxt}}</span></div>'
        '<section class="ds-card ps-card ob-in2" aria-label="Payout status">'
        '<div class="ps-top"><div><span class="hp-lab">Amount</span><b class="ps-big">$2,850.00</b></div>'
        '<div class="ps-to"><img src="' + PPL + '" alt="" width="40" height="40"><span><b>PayPal</b><span>ada.ononuju@example.com</span></span></div></div>'
        '<ol class="ps-trk {{trkCls}}" aria-label="Progress"><li class="dn"><i>' + CHK + '</i><b>Scheduled</b><span>1 Nov</span></li>'
        '<li class="now"><i></i><b>{{midT}}</b><span>{{midS}}</span></li><li><i></i><b>Paid</b><span>Usually by 5 Nov</span></li></ol>'
        '<sc-if value="{{isAction}}" hint-placeholder-val="{{false}}"><div class="ps-act"><span class="ps-ai">' + WARN + '</span>'
        '<span class="ps-at"><b>PayPal needs you to confirm your account</b><span>Your payout continues as soon as it’s confirmed.</span></span>'
        '<a href="CR-PAYO-001.dc.html" class="ds-btn hp-btn"><span>Fix payout details</span><span class="ob-arrow">' + ARR + '</span></a></div></sc-if>'
        '<div class="ps-meta"><span>Covers October earnings' + tip('Earnings that cleared in October. Anything still pending moves to December.') + '</span><span>Reference PO-20488</span></div>'
        '</section>\n</main>')
js = '''    const a = props.variant === 'action';
    return { navCls: S.nav ? 'ds-open' : '', toggleNav: () => this.setState({ nav: !S.nav }), isAction: a,
      stCls: a ? 'am' : 'cb', stTxt: a ? 'Action required' : 'Processing', trkCls: a ? 'am' : '',
      midT: a ? 'Paused' : 'Processing', midS: a ? 'Waiting for you' : 'With PayPal now' };'''
css = COMMON + '''
.ps-card{padding:32px 36px 22px 36px}
.ps-top{display:flex;align-items:flex-end;justify-content:space-between;gap:24px}
.ps-big{display:block;margin-top:10px;font-size:48px;font-weight:600;letter-spacing:-0.03em;line-height:1.05}
.ps-to{display:flex;align-items:center;gap:12px}
.ps-to img{width:40px;height:40px;padding:7px;box-sizing:border-box;border-radius:12px;border:1.5px solid #E6EAF3;background:#FFFFFF}
.ps-to > span{display:flex;flex-direction:column;gap:2px}.ps-to b{font-size:15.5px;font-weight:600}.ps-to > span > span{font-size:14px;color:#5B6582}
.ps-trk{list-style:none;margin:40px 0 0 0;padding:0;display:grid;grid-template-columns:repeat(3,1fr)}
.ps-trk li{position:relative;display:flex;flex-direction:column;gap:4px;padding-top:30px}
.ps-trk li::before{content:"";position:absolute;top:10px;left:0;right:0;height:3px;border-radius:3px;background:#E6EAF3}
.ps-trk li.dn::before{background:#1652F0}
.ps-trk li.now::before{background:linear-gradient(90deg,#1652F0 0 40%,#E6EAF3 40%)}
.ps-trk i{position:absolute;top:0;left:0;width:23px;height:23px;border-radius:50%;background:#FFFFFF;border:2px solid #CBD3E6;box-sizing:border-box;display:flex;align-items:center;justify-content:center;color:#FFFFFF}
.ps-trk li.dn i{background:#1652F0;border-color:#1652F0}
.ps-trk li.now i{border-color:#1652F0;box-shadow:0 0 0 5px rgba(22,82,240,.14)}
.ps-trk li.now i::after{content:"";width:9px;height:9px;border-radius:50%;background:#1652F0}
.ps-trk.am li.now::before{background:linear-gradient(90deg,#D98A00 0 40%,#E6EAF3 40%)}
.ps-trk.am li.now i{border-color:#D98A00;box-shadow:0 0 0 5px rgba(217,138,0,.16)}.ps-trk.am li.now i::after{background:#D98A00}
.ps-trk b{font-size:15px;font-weight:600}.ps-trk li:not(.dn):not(.now) b{color:#5B6582;font-weight:500}
.ps-trk span{font-size:13.5px;color:#5B6582}
.ps-act{margin-top:32px;display:flex;align-items:center;gap:16px;padding:18px 18px 18px 20px;border-radius:16px;background:#FFF8EC;border:1.5px solid #F6DFB5}
.ps-ai{color:#B76E00;flex-shrink:0;display:flex}
.ps-at{flex:1;display:flex;flex-direction:column;gap:3px}.ps-at b{font-size:15px;font-weight:600}.ps-at span{font-size:14px;color:#4A5578}
.ps-meta{margin-top:32px;padding-top:18px;border-top:1.5px solid #F0F2F8;display:flex;justify-content:space-between;gap:16px;font-size:13.5px;color:#5B6582}
.ps-meta > span{display:inline-flex;align-items:center}
@media (max-width: 960px){
.hp-head{flex-direction:row;align-items:center}
.ps-card{padding:22px 20px 16px 20px}
.ps-top{flex-direction:column;align-items:stretch;gap:24px}
.ps-to{padding-top:24px;border-top:1.5px solid #F0F2F8}
.ps-big{font-size:36px}
.ps-trk{margin-top:24px;padding-top:24px;border-top:1.5px solid #F0F2F8;grid-template-columns:1fr;gap:0}
.ps-trk li{padding:0 0 22px 38px;min-height:24px}
.ps-trk li::before{top:24px;bottom:0;left:10px;right:auto;width:3px;height:auto}
.ps-trk li:last-child::before{display:none}
.ps-trk li.now::before{background:#E6EAF3}.ps-trk.am li.now::before{background:#E6EAF3}
.ps-act{flex-wrap:wrap;margin-top:8px}.ps-act .hp-btn{width:100%;justify-content:space-between}
.ps-meta{flex-direction:column;gap:6px;margin-top:20px}
}
'''
B.page('CR-PAYST', 'Earnings & payouts', main, js, css, 'Credalio · Payout', "{ nav: false }")
props_patch('CR-PAYST')
wrap('CR-PAYST', [('CR-PAYO-005', 'proc', 900), ('CR-PAYO-005a', 'action', 1000)])

# ======================= CR-PAYO-006 · payout history =======================
H = [('November 2026', 'Started 1 Nov · PayPal', '$2,850.00', 'Processing'), ('October 2026', 'Paid 1 Oct · PayPal', '$3,400.00', ''),
     ('September 2026', 'Paid 2 Sep · PayPal', '$2,960.00', ''), ('August 2026', 'Paid 1 Aug · PayPal', '$2,410.00', ''),
     ('July 2026', 'Paid 1 Jul · PayPal', '$1,980.00', ''), ('June 2026', 'Paid 2 Jun · PayPal', '$1,820.00', ''),
     ('May 2026', 'Paid 1 May · PayPal', '$1,640.00', ''), ('April 2026', 'Paid 1 Apr · PayPal', '$1,520.00', ''),
     ('March 2026', 'Paid 2 Mar · PayPal', '$1,390.00', ''), ('February 2026', 'Paid 2 Feb · PayPal', '$1,280.00', '')]
rows = ''.join(f'<li><a href="{"CR-PAYO-005.dc.html" if st else "#"}" class="ph-r"><span class="ph-t"><b>{m}</b><span>{d}</span></span>'
               + (f'<span class="st cb">{st}</span>' if st else '') + f'<b class="ph-v">{v}</b>{CHEV}</a></li>' for m, d, v, st in H)
main = ('<main class="ds-main hp">\n<a href="CR-EARN-001.dc.html" class="pg-back">' + BACK + 'Earnings</a>'
        '<div class="hp-head ob-in"><div><h1 class="ds-h1">Payout history</h1></div><div class="ph-sum"><span class="hp-lab">Paid so far</span><b>$18,400.00</b></div></div>'
        '<section class="ds-card ph-card ob-in2" aria-label="Payouts"><ul class="ph-l">' + rows + '</ul></section>\n</main>')
js = '''    return { navCls: S.nav ? 'ds-open' : '', toggleNav: () => this.setState({ nav: !S.nav }) };'''
css = COMMON + '''
.ph-sum{display:flex;flex-direction:column;align-items:flex-end;gap:4px}.ph-sum b{font-size:22px;font-weight:600;letter-spacing:-0.01em;font-variant-numeric:tabular-nums}
.ph-card{padding:6px 12px}
.ph-l{list-style:none;margin:0;padding:0}
.ph-l li + li{border-top:1.5px solid #F0F2F8}
.ph-r{display:flex;align-items:center;gap:20px;padding:18px 16px;border-radius:14px;color:#0B1433;text-decoration:none}
.ph-r:hover{background:#F7F9FD}
.ph-t{flex:1;display:flex;flex-direction:column;gap:3px;min-width:0}.ph-t b{font-size:15.5px;font-weight:600}.ph-t span{font-size:13.5px;color:#5B6582}
.ph-v{font-size:16px;font-weight:600;font-variant-numeric:tabular-nums;min-width:96px;text-align:right}
.ph-r > svg{color:#8A93AD;flex-shrink:0}
@media (max-width: 960px){
.hp-head{flex-direction:row;align-items:flex-end}
.ph-sum b{font-size:17px}
.ph-card{padding:2px 4px}
.ph-r{gap:12px;padding:15px 12px}
.ph-r .st{height:24px;padding:0 9px;font-size:12px}
.ph-v{min-width:0;font-size:15px}
.ph-r > svg{display:none}
}
'''
B.page('CR-PAYO-006', 'Earnings & payouts', main, js, css, 'Credalio · Payout history', "{ nav: false }")
wd2, wm2 = wd, wm
t = mob(wm.replace('<dc-import name="CR-CRED-002" variant="badge"', '<dc-import name="CR-PAYO-006"'), 1000)
wr('CR-PAYO-006-Mobile.dc.html', re.sub(r'<title>.*?</title>', '<title>CR-PAYO-006 mobile preview</title>', t))
# desktop preview board for a page source = the source itself (no wrapper needed)

# ======================= CR-COURSE-OV-001 · course overview =======================
NEED = [('chat', '3 unanswered questions', 'Oldest from 5 days ago', 'Answer', 'CR-DISC-001.dc.html'),
        ('val', 'Revalidation quote is ready', 'Chapter 4 and the final assessment changed', 'Review', 'CR-REVAL-002.dc.html'),
        ('doc', 'John sent Quiz 2 edits', 'Waiting for your review', 'Review', '#')]
need = ''.join(f'<li><span class="hp-ic">{ic(I[k], 19)}</span><span class="co-t"><b>{t}</b><span>{d}</span></span><a href="{h}" class="hp-rb">{c}</a></li>' for k, t, d, c, h in NEED)
KPI = [('Learners', '1,284', ''), ('Completion', '68%', tip('Learners who finished every chapter.')), ('Rating', '4.8', ''), ('Earned in October', '$1,410.00', '')]
kpi = ''.join(f'<div><span class="hp-lab">{l}{t}</span><b>{v}</b></div>' for l, v, t in KPI)
main = ('<main class="ds-main hp">\n<a href="CR-HOME-EXP.dc.html" class="pg-back">' + BACK + 'My learning experiences</a>'
        '<div class="hp-head co-head ob-in"><div class="co-id"><span class="co-th">' + ic(I['book'], 26, 1.8) + '</span><div><h1 class="ds-h1">Data Analysis with SQL</h1>'
        '<div class="co-pills"><span class="st gr">Published</span><span class="st cb">Gold validated</span></div></div></div>'
        '<div class="co-acts"><a href="#" class="hp-rb">View as learner</a><a href="#" class="ds-btn hp-btn"><span>Edit course</span><span class="ob-arrow">' + ARR + '</span></a></div></div>'
        '<section class="ds-card co-k ob-in2" aria-label="At a glance">' + kpi + '</section>'
        '<div class="co-g">'
        '<section class="ds-card co-need ob-in3" aria-labelledby="co-h1"><h2 id="co-h1" class="co-h">Needs you</h2><ul>' + need + '</ul></section>'
        '<section class="ds-card co-ver ob-in3" aria-labelledby="co-h2"><h2 id="co-h2" class="co-h">Live version</h2><dl>'
        '<div><dt>Version</dt><dd>v2 · since 12 Sep</dd></div>'
        '<div><dt>Validated by</dt><dd><span class="co-avs"><span class="av">BO</span><span class="av">KA</span><span class="av">FN</span></span></dd></div>'
        '<div><dt>Team</dt><dd><span class="co-avs"><span class="av">AO</span><span class="av">JA</span><span class="av">MO</span></span></dd></div></dl>'
        '<a href="CR-VAL-MC-001.dc.html" class="ds-link">Validation history</a></section>'
        '</div>\n</main>')
js = '''    return { navCls: S.nav ? 'ds-open' : '', toggleNav: () => this.setState({ nav: !S.nav }) };'''
css = COMMON + '''
.co-head{align-items:center}
.co-id{display:flex;align-items:center;gap:18px;min-width:0}
.co-th{width:64px;height:64px;border-radius:18px;background:linear-gradient(135deg,#1652F0,#5B85F5);color:#FFFFFF;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.co-pills{margin-top:10px;display:flex;gap:8px}
.co-acts{display:flex;align-items:center;gap:10px}
.co-k{display:grid;grid-template-columns:repeat(4,1fr);padding:24px 0}
.co-k > div{display:flex;flex-direction:column;gap:8px;padding:0 32px}
.co-k > div + div{border-left:1.5px solid #F0F2F8}
.co-k .hp-lab{display:flex;align-items:center}
.co-k b{font-size:26px;font-weight:600;letter-spacing:-0.02em;font-variant-numeric:tabular-nums}
.co-g{margin-top:20px;display:grid;grid-template-columns:minmax(0,1fr) 360px;gap:20px;align-items:start}
.co-h{margin:0;font-size:17px;font-weight:600}
.co-need{padding:24px 28px 8px 28px}
.co-need ul{list-style:none;margin:10px 0 0 0;padding:0}
.co-need li{display:flex;align-items:center;gap:16px;padding:16px 0;border-top:1.5px solid #F0F2F8}
.co-need li:first-child{border-top:0}
.co-t{flex:1;display:flex;flex-direction:column;gap:3px;min-width:0}.co-t b{font-size:15px;font-weight:600}.co-t span{font-size:13.5px;color:#5B6582}
.co-ver{padding:24px 26px}
.co-ver dl{margin:10px 0 0 0}
.co-ver dl > div{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:13px 0;border-top:1.5px solid #F0F2F8}
.co-ver dl > div:first-child{border-top:0}
.co-ver dt{font-size:14px;color:#5B6582}.co-ver dd{margin:0;font-size:14.5px;font-weight:600}
.co-avs{display:flex}.co-avs .av{width:30px;height:30px;font-size:11px;border:2px solid #FFFFFF;margin-left:-8px}.co-avs .av:first-child{margin-left:0}
.co-ver .ds-link{display:inline-block;margin-top:14px;font-size:14px;font-weight:600}
@media (max-width: 1080px){.co-g{grid-template-columns:minmax(0,1fr)}}
@media (max-width: 960px){
.co-head{flex-direction:column;align-items:stretch}
.co-id{gap:14px}.co-th{width:52px;height:52px;border-radius:15px}
.co-acts .hp-rb{display:none}
.co-k{grid-template-columns:1fr 1fr;padding:6px 0}
.co-k > div{padding:14px 18px}
.co-k > div + div{border-left:0}
.co-k > div:nth-child(even){border-left:1.5px solid #F0F2F8}.co-k > div:nth-child(n+3){border-top:1.5px solid #F0F2F8}
.co-k b{font-size:20px}
.co-g{margin-top:14px;gap:14px}
.co-need{padding:18px 18px 4px 18px}.co-need li{gap:12px}.co-need .hp-ic{width:36px;height:36px}
.co-ver{padding:18px}
}
'''
B.page('CR-COURSE-OV-001', 'My learning experiences', main, js, css, 'Credalio · Data Analysis with SQL', "{ nav: false }")
t = mob(wm.replace('<dc-import name="CR-CRED-002" variant="badge"', '<dc-import name="CR-COURSE-OV-001"'), 1260)
wr('CR-COURSE-OV-001-Mobile.dc.html', re.sub(r'<title>.*?</title>', '<title>CR-COURSE-OV-001 mobile preview</title>', t))

# ======================= CR-DISC · discussions =======================
D = [('TA', 'Why does my GROUP BY return duplicates?', 'Data Analysis with SQL · Lesson 4.2', 'Tunde A.', 4, '3 h ago', False),
     ('CO', 'LEFT JOIN vs INNER JOIN with missing customers', 'Data Analysis with SQL · Lesson 3.1', 'Chioma O.', 7, 'Yesterday', True),
     ('KB', 'Window functions: when to use PARTITION BY', 'Advanced SQL for Analysts · Lesson 4.3', 'Kwame B.', 0, '2 days ago', False),
     ('AO', 'Share your Chapter 2 practice query', 'Data Analysis with SQL · Chapter 2', 'You', 23, '3 days ago', True),
     ('SE', 'Capstone teams: finding a process to automate', 'Applied AI Program · Week 5', 'Samuel E.', 12, '4 days ago', True),
     ('GM', 'Is the exam open-book?', 'Certified Data Analyst · General', 'Grace M.', 0, '5 days ago', False)]
js_rows = ', '.join("{av:'%s',t:'%s',c:'%s',by:'%s',n:%d,tm:'%s',ok:%s}" % (a, t.replace("'", "\\'"), c, b, n, tm, 'true' if ok else 'false') for a, t, c, b, n, tm, ok in D)
main = ('<main class="ds-main hp">\n<div class="hp-head ob-in"><div><h1 class="ds-h1">Discussions</h1></div><button type="button" class="hp-rb ds-crs">All learning experiences' + ic('<path d="m6 9 6 6 6-6"></path>', 15, 2.2) + '</button></div>'
        '<div class="hp-tabs ds-tb ob-in2" role="tablist"><sc-for list="{{tabs}}" as="t" hint-placeholder-count="3"><button type="button" role="tab" class="hp-tab {{t.cls}}" onClick="{{t.pick}}">{{t.l}}<sc-if value="{{t.hasN}}" hint-placeholder-val="{{true}}"><em class="ds-n">{{t.n}}</em></sc-if></button></sc-for></div>'
        '<section class="ds-card dl-card ob-in3" aria-label="Threads"><ul class="dl-l"><sc-for list="{{rows}}" as="r" hint-placeholder-count="6"><li><a href="CR-DISC-002.dc.html" class="dl-r {{r.unCls}}">'
        '<span class="av">{{r.av}}</span><span class="dl-t"><b>{{r.t}}</b><span>{{r.c}} · {{r.by}} · {{r.tm}}</span></span>'
        '<sc-if value="{{r.un}}" hint-placeholder-val="{{false}}"><span class="st am">Unanswered</span></sc-if>'
        '<span class="dl-n">' + REPLY + '{{r.n}}</span></a></li></sc-for></ul></section>\n</main>')
js = '''    const D = [''' + js_rows + '''];
    const f = S.f || props.variant || 'all';
    const list = D.filter((d) => f === 'all' || (f === 'unanswered' ? !d.ok : d.ok));
    const T = [['all', 'All', ''], ['unanswered', 'Unanswered', String(D.filter((d) => !d.ok).length)], ['answered', 'Answered', '']];
    return { navCls: S.nav ? 'ds-open' : '', toggleNav: () => this.setState({ nav: !S.nav }),
      tabs: T.map((t) => ({ l: t[1], n: t[2], hasN: !!t[2], cls: f === t[0] ? 'on' : '', pick: () => this.setState({ f: t[0] }) })),
      rows: list.map((d) => Object.assign({}, d, { un: !d.ok, unCls: d.ok ? '' : 'un' })) };'''
css = COMMON + '''
.ds-crs{gap:8px}.ds-crs svg{color:#5B6582}
.ds-tb{margin-bottom:18px}
.ds-n{font-style:normal;min-width:20px;height:20px;padding:0 6px;border-radius:999px;background:#FFF3E0;color:#9A5B00;font-size:12px;font-weight:600;display:inline-flex;align-items:center;justify-content:center;box-sizing:border-box}
.dl-card{padding:6px 12px}
.dl-l{list-style:none;margin:0;padding:0}
.dl-l li + li{border-top:1.5px solid #F0F2F8}
.dl-r{display:flex;align-items:center;gap:16px;padding:18px 16px;border-radius:14px;color:#0B1433;text-decoration:none}
.dl-r:hover{background:#F7F9FD}
.dl-t{flex:1;min-width:0;display:flex;flex-direction:column;gap:4px}
.dl-t b{font-size:15.5px;font-weight:600;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.dl-t > span{font-size:13.5px;color:#5B6582;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.dl-n{display:inline-flex;align-items:center;gap:6px;min-width:44px;justify-content:flex-end;font-size:14px;font-weight:500;color:#5B6582;font-variant-numeric:tabular-nums}
.dl-n svg{color:#8A93AD}
@media (max-width: 960px){
.hp-head{flex-direction:row;align-items:center}
.ds-crs{display:inline-flex !important;height:34px;padding:0 12px;font-size:13px}
.ds-tb{margin-bottom:12px}
.dl-card{padding:2px 4px}
.dl-r{align-items:flex-start;gap:12px;padding:15px 10px;flex-wrap:wrap}
.dl-r .av{width:32px;height:32px;font-size:11.5px}
.dl-t{flex-basis:calc(100% - 44px)}
.dl-t b{white-space:normal;font-size:15px}
.dl-t > span{white-space:normal}
.dl-r .st{display:none}
.dl-r.un .dl-t b::before{content:"";display:inline-block;width:8px;height:8px;margin:0 8px 2px 0;border-radius:50%;background:#D98A00;vertical-align:middle}
.dl-n{display:none}
}
'''
B.page('CR-DISC', 'Discussions', main, js, css, 'Credalio · Discussions', "{ nav: false, f: '' }")
props_patch('CR-DISC')
wrap('CR-DISC', [('CR-DISC-001', '', 1000)])
print('build26 ok')
