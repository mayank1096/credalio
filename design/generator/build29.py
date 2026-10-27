# build29: CR-CAL-004 availability exceptions, CR-CAL-005 presence & visibility, CR-SUP learner support
# (variants inbox / conv = SUP-001 / SUP-002), CR-LRN-001 learners. Studio pages via build17 page().
# usage: python3 build29.py <canvas project dir>
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build17 as B
from tipx import tip, TIP_CSS
P, rd, wr, ic, I, ARR = B.P, B.rd, B.wr, B.ic, B.I, B.ARR
CHK = ic('<path d="m5 12.5 4.5 4.5L19 7.5"></path>', 12, 3)
BACK = ic('<path d="M19 12H5"></path><path d="m11 6-6 6 6 6"></path>', 16, 2.2)
CHEVD = ic('<path d="m6 9 6 6 6-6"></path>', 15, 2.2)
SRCH = ic('<circle cx="11" cy="11" r="7"></circle><path d="m20 20-3.5-3.5"></path>', 17, 2)
SEND = ic('<path d="M5 12h14"></path><path d="m13 6 6 6-6 6"></path>', 18, 2.4)
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
.st{display:inline-flex;align-items:center;height:28px;padding:0 12px;border-radius:999px;font-size:13px;font-weight:500;white-space:nowrap}
.st.cb{background:#EAF0FF;color:#0E3BB8}.st.am{background:#FFF3E0;color:#9A5B00}.st.gr{background:#E7F5EE;color:#0F6B45}.st.gy{background:#F1F3F8;color:#5B6582}
.av{width:36px;height:36px;border-radius:50%;background:#EAF0FF;color:#0E3BB8;display:inline-flex;align-items:center;justify-content:center;font-size:12.5px;font-weight:600;flex-shrink:0}
.seg{display:inline-flex;padding:4px;border-radius:14px;background:#EEF1F7}
.seg > *{display:inline-flex;align-items:center;justify-content:center;height:38px;padding:0 16px;border-radius:11px;font-size:14px;font-weight:500;color:#5B6582}
.seg > .on{background:#FFFFFF;color:#0B1433;box-shadow:0 1px 4px rgba(11,20,51,.08)}
.fld{display:flex;flex-direction:column;gap:7px}
.fld > span:first-child{font-size:13.5px;font-weight:500;color:#4A5578}
.inp{display:flex;align-items:center;justify-content:space-between;gap:10px;height:48px;padding:0 16px;border-radius:12px;border:1.5px solid #D6DDEE;background:#FFFFFF;font-size:15px;color:#0B1433}
.inp.ph{color:#8A93AD}.inp svg{color:#8A93AD;flex-shrink:0}
@media (max-width: 960px){.pg-back{margin-top:12px}}
'''

# ======================= CR-CAL-004 · exceptions =======================
EXC = [('24 Dec – 1 Jan', 'Away', 'Holiday break', 'gy'), ('Fri 23 Oct', '12:00 – 15:00', 'Custom hours', 'cb'), ('Mon 2 Nov', 'Unavailable', 'Conference', 'gy')]
rows = ''.join(f'<li><span class="ex-d"><b>{d}</b><span>{n}</span></span><span class="st {c}">{s}</span><button type="button" class="ex-x" aria-label="Remove">' + ic('<path d="M7 7l10 10M17 7 7 17"></path>', 15, 2.2) + '</button></li>' for d, s, n, c in EXC)
main = ('<main class="ds-main hp">\n<a href="CR-CAL-003.dc.html" class="pg-back">' + BACK + 'Weekly availability</a>'
        '<div class="hp-head ob-in"><div><h1 class="ds-h1">Days off &amp; exceptions' + tip('These override your weekly hours for the dates you pick. Bookings already made stay; we’ll tell you about any clash.') + '</h1></div></div>'
        '<div class="ex-g">'
        '<section class="ds-card ex-new ob-in2" aria-labelledby="ex-h1"><h2 id="ex-h1" class="ex-h">New exception</h2>'
        '<div class="ex-f"><label class="fld"><span>From</span><span class="inp">Fri 23 Oct 2026' + ic(I['cal'], 17, 2) + '</span></label><label class="fld"><span>To</span><span class="inp">Fri 23 Oct 2026' + ic(I['cal'], 17, 2) + '</span></label></div>'
        '<div class="fld ex-row"><span>On these days</span><span class="seg"><span>Unavailable</span><span class="on">Custom hours</span></span></div>'
        '<div class="ex-f"><label class="fld"><span>Start</span><span class="inp">12:00' + CHEVD + '</span></label><label class="fld"><span>End</span><span class="inp">15:00' + CHEVD + '</span></label></div>'
        '<label class="fld ex-row"><span>Note <em>(only you see this)</em></span><span class="inp">Dentist in the morning</span></label>'
        '<div class="ex-foot"><a href="#" class="ds-btn hp-btn"><span>Add exception</span><span class="ob-arrow">' + ARR + '</span></a></div></section>'
        '<section class="ex-up ob-in3" aria-labelledby="ex-h2"><h2 id="ex-h2" class="hp-lab">Upcoming</h2><ul class="ds-card ex-l">' + rows + '</ul></section>'
        '</div>\n</main>')
css = COMMON + '''
.ex-g{display:grid;grid-template-columns:minmax(0,1fr) 380px;gap:24px;align-items:start;max-width:1100px}
.ex-new{padding:26px 28px}
.ex-h{margin:0;font-size:17px;font-weight:600}
.ex-f{margin-top:20px;display:grid;grid-template-columns:1fr 1fr;gap:14px}
.ex-row{margin-top:20px}
.fld em{font-style:normal;color:#8A93AD;font-weight:400}
.ex-row .seg{align-self:flex-start}
.ex-foot{margin-top:28px;padding-top:20px;border-top:1.5px solid #F0F2F8;display:flex;justify-content:flex-end}
.ex-up .hp-lab{margin:0 0 10px 4px}
.ex-l{list-style:none;margin:0;padding:4px 20px}
.ex-l li{display:flex;align-items:center;gap:12px;padding:16px 0}
.ex-l li + li{border-top:1.5px solid #F0F2F8}
.ex-d{flex:1;display:flex;flex-direction:column;gap:3px;min-width:0}.ex-d b{font-size:15px;font-weight:600}.ex-d span{font-size:13.5px;color:#5B6582}
.ex-x{width:30px;height:30px;border:0;border-radius:50%;background:transparent;color:#8A93AD;display:inline-flex;align-items:center;justify-content:center;cursor:pointer}
@media (max-width: 1080px){.ex-g{grid-template-columns:minmax(0,1fr)}}
@media (max-width: 960px){
.ex-new{padding:20px 18px}
.ex-f{gap:10px}
.ex-row .seg{align-self:stretch}.ex-row .seg > *{flex:1}
.ex-foot .hp-btn{width:100%;justify-content:space-between}
.ex-g{gap:28px}
.ex-l{padding:2px 16px}
}
'''
B.page('CR-CAL-004', 'Calendar', main, NAVJS, css, 'Credalio · Days off', "{ nav: false }")
wrap('CR-CAL-004', [('CR-CAL-004', '', 1100)])

# ======================= CR-CAL-005 · presence =======================
PR = [('Online', 'gr', 'Learners and your team see you’re around', True), ('Away', 'am', 'You’ll get messages later, nothing pops up', False), ('Appear offline', 'gy', 'Nobody sees your status', False)]
opts = ''.join(f'<button type="button" role="radio" aria-checked="{"true" if on else "false"}" class="pr-o {"on" if on else ""}"><i class="pr-dot {c}"></i><span><b>{t}</b><span>{d}</span></span>' + (f'<i class="pr-ck">{CHK}</i>' if on else '') + '</button>' for t, c, d, on in PR)
SW = [('Show my status to learners', '', True), ('Show my weekly hours to teammates', 'They can only book you inside them.', True), ('Message pop-ups', 'Learner Support and Team Chat only. Paused when you’re Away or appear offline.', True)]
sws = ''.join(f'<li><span class="pr-l">{t}' + (tip(h, 'r') if h else '') + f'</span><button type="button" class="hp-sw {"on" if on else ""}" aria-pressed="{"true" if on else "false"}" aria-label="{t}"></button></li>' for t, h, on in SW)
main = ('<main class="ds-main hp">\n<a href="CR-CAL-001.dc.html" class="pg-back">' + BACK + 'Calendar</a>'
        '<div class="hp-head ob-in"><div><h1 class="ds-h1">Presence &amp; visibility' + tip('Whether you’re online right now is separate from your weekly hours.') + '</h1></div></div>'
        '<div class="pr-g">'
        '<section class="ob-in2" aria-labelledby="pr-h1"><h2 id="pr-h1" class="hp-lab pr-lab">Right now</h2><div class="pr-os" role="radiogroup" aria-labelledby="pr-h1">' + opts + '</div></section>'
        '<section class="ob-in3" aria-labelledby="pr-h2"><h2 id="pr-h2" class="hp-lab pr-lab">Who sees what</h2><ul class="ds-card pr-sw">' + sws + '</ul></section>'
        '</div>\n</main>')
css = COMMON + '''
.pr-g{display:flex;flex-direction:column;gap:32px;max-width:760px}
.pr-lab{margin:0 0 10px 4px}
.pr-os{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.pr-o{position:relative;display:flex;flex-direction:column;align-items:flex-start;gap:14px;padding:18px 18px 20px 18px;border-radius:18px;border:1.5px solid #E6EAF3;background:#FFFFFF;font-family:inherit;text-align:left;color:#0B1433;cursor:pointer}
.pr-o > span{display:flex;flex-direction:column;gap:4px}.pr-o b{font-size:15.5px;font-weight:600}.pr-o > span > span{font-size:13.5px;line-height:1.45;color:#5B6582}
.pr-o.on{border-color:#1652F0;background:#F5F8FF;box-shadow:0 0 0 4px rgba(22,82,240,.10)}
.pr-dot{width:12px;height:12px;border-radius:50%}.pr-dot.gr{background:#0F6B45}.pr-dot.am{background:#D98A00}.pr-dot.gy{background:#B6BED3}
.pr-ck{position:absolute;top:16px;right:16px;width:20px;height:20px;border-radius:50%;background:#1652F0;color:#FFFFFF;display:inline-flex;align-items:center;justify-content:center}
.pr-sw{list-style:none;margin:0;padding:4px 24px}
.pr-sw li{display:flex;align-items:center;justify-content:space-between;gap:16px;padding:18px 0}
.pr-sw li + li{border-top:1.5px solid #F0F2F8}
.pr-l{display:inline-flex;align-items:center;font-size:15px;font-weight:500}
@media (max-width: 960px){
.pr-g{gap:28px}
.pr-os{grid-template-columns:1fr;gap:10px}
.pr-o{flex-direction:row;align-items:center;gap:14px;padding:16px 48px 16px 16px}
.pr-ck{top:50%;margin-top:-10px}
.pr-sw{padding:2px 16px}
.pr-l{font-size:14.5px}
}
'''
B.page('CR-CAL-005', 'Calendar', main, NAVJS, css, 'Credalio · Presence', "{ nav: false }")
wrap('CR-CAL-005', [('CR-CAL-005', '', 780)])

# ======================= CR-SUP · learner support =======================
TH = [('ME', 'Mary E.', 'Data Analysis with SQL · Lesson 4.2', 'I added city to the GROUP BY like the coach said, but some customers still show twice.', '12 min', 'w', True),
      ('TA', 'Tunde A.', 'Data Analysis with SQL · Lesson 3.1', 'Could I get two more days for the Chapter 3 quiz? I was ill this week.', '2 h', 'w', False),
      ('IN', 'Ifeoma N.', 'Advanced SQL for Analysts · Lesson 2.4', 'Thanks, that fixed it!', 'Yesterday', 'r', True),
      ('KB', 'Kwame B.', 'Certified Data Analyst · Exam prep', 'Is the final exam proctored?', '2 days', 'r', False)]
js_rows = ', '.join("{av:'%s',n:'%s',c:'%s',m:'%s',t:'%s',w:%s,ai:%s}" % (a, n, c, m.replace("'", "\\'"), t, 'true' if s == 'w' else 'false', 'true' if ai else 'false') for a, n, c, m, t, s, ai in TH)
AIIC = ic(I['ai'], 13, 2.2)
inbox = ('<sc-if value="{{vInbox}}" hint-placeholder-val="{{true}}">'
         '<div class="hp-head ob-in"><div><h1 class="ds-h1">Learner Support' + tip('Private help for learners enrolled in your learning experiences, after the AI Coach has tried to help.') + '</h1></div></div>'
         '<div class="hp-tabs su-tb ob-in2" role="tablist"><sc-for list="{{tabs}}" as="t" hint-placeholder-count="3"><button type="button" role="tab" class="hp-tab {{t.cls}}" onClick="{{t.pick}}">{{t.l}}<sc-if value="{{t.hasN}}" hint-placeholder-val="{{true}}"><em class="su-n">{{t.n}}</em></sc-if></button></sc-for></div>'
         '<section class="ds-card su-card ob-in3" aria-label="Conversations"><ul class="su-l"><sc-for list="{{rows}}" as="r" hint-placeholder-count="4"><li><a href="CR-SUP-002.dc.html" class="su-r {{r.cls}}">'
         '<span class="av">{{r.av}}</span><span class="su-t"><span class="su-top"><b>{{r.n}}</b><span>{{r.c}}</span></span><span class="su-m">{{r.m}}</span></span>'
         '<span class="su-meta"><span class="su-tm">{{r.t}}</span><sc-if value="{{r.ai}}" hint-placeholder-val="{{false}}"><span class="su-ai">' + AIIC + 'From AI Coach</span></sc-if></span></a></li></sc-for></ul></section></sc-if>')
conv = ('<sc-if value="{{vConv}}" hint-placeholder-val="{{false}}"><a href="CR-SUP-001.dc.html" class="pg-back">' + BACK + 'Learner Support</a>'
        '<div class="sc-g">'
        '<section class="ds-card sc-chat ob-in2" aria-label="Conversation with Mary E.">'
        '<header class="sc-hd"><span class="av">ME</span><span><b>Mary E.</b><span>Data Analysis with SQL · Lesson 4.2</span></span><a href="#" class="hp-rb">Mark resolved</a></header>'
        '<div class="sc-body"><div class="sc-sum"><span class="sc-sl">' + AIIC + 'Summary from the AI Coach' + tip('Mary chose to share this summary. Her private AI Coach conversation is never shared.') + '</span>'
        '<p>Mary asked why her GROUP BY returns duplicate customers. The coach explained grouping by every non-aggregated column; she still sees repeats and asked for a tutor.</p></div>'
        '<span class="sc-day">Today</span>'
        '<div class="sc-msg"><span class="av">ME</span><div><p>I added city to the GROUP BY like the coach said, but some customers still show twice. Here’s my query:</p>'
        '<pre>SELECT customer_id, city, SUM(amount)\nFROM orders\nGROUP BY customer_id, city;</pre><span class="sc-tm">12 min ago</span></div></div></div>'
        '<div class="sc-cmp"><span class="sc-in">Reply to Mary…</span><button type="button" class="sc-send" aria-label="Send">' + SEND + '</button></div></section>'
        '<aside class="ds-card sc-side ob-in3" aria-label="About Mary"><span class="hp-lab">Learner</span><b>Mary E.</b><span>Enrolled 2 Sep 2026</span>'
        '<div class="sc-pr"><span><span>Progress</span><b>62%</b></span><i><em style="width:62%"></em></i></div>'
        '<a href="CR-LRN-001.dc.html" class="ds-link">View learner</a></aside>'
        '</div></sc-if>')
main = '<main class="ds-main hp">\n' + inbox + conv + '\n</main>'
js = '''    const v = props.variant || 'inbox';
    const D = [''' + js_rows + '''];
    const f = S.f || 'waiting';
    const list = D.filter((d) => f === 'all' || (f === 'waiting' ? d.w : !d.w));
    const T = [['waiting', 'Waiting for you', String(D.filter((d) => d.w).length)], ['all', 'All', ''], ['resolved', 'Resolved', '']];
    return { navCls: S.nav ? 'ds-open' : '', toggleNav: () => this.setState({ nav: !S.nav }), vInbox: v === 'inbox', vConv: v === 'conv',
      tabs: T.map((t) => ({ l: t[1], n: t[2], hasN: !!t[2], cls: f === t[0] ? 'on' : '', pick: () => this.setState({ f: t[0] }) })),
      rows: list.map((d) => Object.assign({}, d, { cls: d.w ? 'w' : 'r' })) };'''
css = COMMON + '''
.su-tb{margin-bottom:18px}
.su-n{font-style:normal;min-width:20px;height:20px;padding:0 6px;border-radius:999px;background:#FFF3E0;color:#9A5B00;font-size:12px;font-weight:600;display:inline-flex;align-items:center;justify-content:center;box-sizing:border-box}
.su-card{padding:6px 12px}
.su-l{list-style:none;margin:0;padding:0}
.su-l li + li{border-top:1.5px solid #F0F2F8}
.su-r{display:flex;align-items:center;gap:16px;padding:18px 16px;border-radius:14px;color:#0B1433;text-decoration:none}
.su-r:hover{background:#F7F9FD}
.su-r.w .av{box-shadow:0 0 0 2px #FFFFFF,0 0 0 4px #D98A00}
.su-t{flex:1;min-width:0;display:flex;flex-direction:column;gap:4px}
.su-top{display:flex;align-items:baseline;gap:10px;min-width:0}.su-top b{font-size:15.5px;font-weight:600;white-space:nowrap}.su-top > span{font-size:13px;color:#8A93AD;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.su-m{font-size:14px;color:#4A5578;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.su-r.r .su-m{color:#8A93AD}
.su-meta{display:flex;flex-direction:column;align-items:flex-end;gap:6px;flex-shrink:0}
.su-tm{font-size:13px;color:#8A93AD}
.su-ai{display:inline-flex;align-items:center;gap:5px;height:24px;padding:0 9px;border-radius:999px;background:#EAF0FF;color:#0E3BB8;font-size:12px;font-weight:500}
/* conversation */
.sc-g{margin-top:16px;display:grid;grid-template-columns:minmax(0,1fr) 300px;gap:20px;align-items:start}
.sc-chat{padding:0;display:flex;flex-direction:column;height:calc(100vh - 170px);min-height:560px;overflow:hidden}
.sc-hd{display:flex;align-items:center;gap:12px;padding:16px 20px;border-bottom:1.5px solid #F0F2F8}
.sc-hd > span:nth-child(2){flex:1;display:flex;flex-direction:column;gap:2px}.sc-hd b{font-size:15.5px;font-weight:600}.sc-hd > span > span{font-size:13px;color:#5B6582}
.sc-body{flex:1;display:flex;flex-direction:column;justify-content:flex-end;gap:16px;padding:20px 24px;overflow:auto}
.sc-sum{padding:16px 18px;border-radius:16px;background:#F5F8FF;border:1.5px solid #E2E9FB}
.sc-sl{display:flex;align-items:center;gap:6px;font-size:12.5px;font-weight:500;color:#0E3BB8}
.sc-sum p{margin:8px 0 0 0;font-size:14px;line-height:1.55;color:#3A4566}
.sc-day{align-self:center;font-size:12px;font-weight:500;color:#8A93AD}
.sc-msg{display:flex;gap:12px;max-width:620px}
.sc-msg .av{width:32px;height:32px;font-size:11.5px}
.sc-msg > div{padding:14px 16px;border-radius:4px 18px 18px 18px;background:#F1F3F8}
.sc-msg p{margin:0;font-size:14.5px;line-height:1.55}
.sc-msg pre{margin:10px 0 0 0;padding:12px 14px;border-radius:12px;background:#0B1433;color:#DCE4FF;font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:13px;line-height:1.55;white-space:pre-wrap}
.sc-tm{display:block;margin-top:8px;font-size:12px;color:#8A93AD}
.sc-cmp{display:flex;align-items:center;gap:10px;margin:0 16px 16px 16px;padding:8px 8px 8px 18px;border-radius:999px;border:1.5px solid #D6DDEE;background:#FFFFFF}
.sc-in{flex:1;font-size:15px;color:#8A93AD}
.sc-send{width:40px;height:40px;border:0;border-radius:50%;background:#1652F0;color:#FFFFFF;display:inline-flex;align-items:center;justify-content:center;cursor:pointer}
.sc-side{padding:22px 24px;display:flex;flex-direction:column;gap:4px}
.sc-side b{margin-top:8px;font-size:15.5px;font-weight:600}.sc-side > span:not(.hp-lab){font-size:13.5px;color:#5B6582}
.sc-pr{margin-top:18px;display:flex;flex-direction:column;gap:8px}
.sc-pr > span{display:flex;justify-content:space-between;font-size:13.5px;color:#5B6582}.sc-pr b{color:#0B1433;font-weight:600}
.sc-pr i{display:block;height:6px;border-radius:6px;background:#E6EAF3;overflow:hidden}.sc-pr em{display:block;height:100%;background:#1652F0;border-radius:6px}
.sc-side .ds-link{margin-top:18px;font-size:14px;font-weight:600}
@media (max-width: 1080px){.sc-g{grid-template-columns:minmax(0,1fr)}.sc-side{display:none}}
@media (max-width: 960px){
.su-tb{margin-bottom:12px}
.su-card{padding:2px 4px}
.su-r{align-items:flex-start;gap:12px;padding:15px 10px}
.su-r .av{width:32px;height:32px;font-size:11.5px}
.su-top{flex-direction:column;gap:2px}
.su-m{white-space:normal;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical}
.su-ai{display:none}
.sc-chat{height:auto;min-height:0;border-radius:18px}
.sc-hd{padding:14px 14px}.sc-hd .hp-rb{display:inline-flex !important;height:34px;padding:0 12px;font-size:13px}
.sc-body{padding:16px 14px}
.sc-cmp{margin:0 12px 12px 12px}
}
'''
B.page('CR-SUP', 'Learner support', main, js, css, 'Credalio · Learner Support', "{ nav: false, f: '' }")
props_patch('CR-SUP')
wrap('CR-SUP', [('CR-SUP-001', 'inbox', 844), ('CR-SUP-002', 'conv', 844)])

# ======================= CR-LRN-001 · learners =======================
L = [('ME', 'Mary E.', 'Data Analysis with SQL', 62, '12 min ago', ''), ('TA', 'Tunde A.', 'Data Analysis with SQL', 41, '2 h ago', ''),
     ('IN', 'Ifeoma N.', 'Advanced SQL for Analysts', 100, 'Yesterday', 'Completed'), ('CO', 'Chioma O.', 'Data Analysis with SQL', 78, 'Yesterday', ''),
     ('KB', 'Kwame B.', 'Certified Data Analyst', 23, '16 days ago', 'Inactive'), ('GM', 'Grace M.', 'Certified Data Analyst', 55, '3 days ago', ''),
     ('SE', 'Samuel E.', 'Applied AI Program', 88, 'Today', '')]
def lrow(a, n, c, p, t, s):
    st = {'Completed': 'gr', 'Inactive': 'am'}.get(s, '')
    return (f'<li><a href="#" class="ln-r"><span class="av">{a}</span><span class="ln-n"><b>{n}</b><span>{c}</span></span>'
            f'<span class="ln-p"><i><em style="width:{p}%"></em></i><b>{p}%</b></span><span class="ln-t">{t}</span>'
            f'<span class="ln-s">' + (f'<span class="st {st}">{s}</span>' if s else '') + '</span></a></li>')
main = ('<main class="ds-main hp">\n<div class="hp-head ob-in"><div><h1 class="ds-h1">Learners <span class="ln-cnt">1,284</span></h1></div></div>'
        '<div class="ln-bar ob-in2"><span class="ln-q">' + SRCH + '<span>Search learners</span></span>'
        '<button type="button" class="hp-rb ln-f">All learning experiences' + CHEVD + '</button><button type="button" class="hp-rb ln-f">Any progress' + CHEVD + '</button></div>'
        '<section class="ds-card ln-card ob-in3" aria-label="Learners"><div class="ln-hd"><span>Learner</span><span>Progress</span><span>Last active</span><span></span></div>'
        '<ul class="ln-l">' + ''.join(lrow(*r) for r in L) + '</ul></section>\n</main>')
css = COMMON + '''
.ln-cnt{font-size:18px;font-weight:500;color:#8A93AD;letter-spacing:0;margin-left:6px;vertical-align:4px}
.ln-bar{display:flex;align-items:center;gap:10px;margin-bottom:16px}
.ln-q{flex:1;max-width:420px;display:flex;align-items:center;gap:10px;height:42px;padding:0 16px;border-radius:999px;border:1.5px solid #D6DDEE;background:#FFFFFF;font-size:14.5px;color:#8A93AD}
.ln-f{gap:8px}.ln-f svg{color:#5B6582}
.ln-card{padding:4px 12px 8px 12px}
.ln-hd,.ln-r{display:grid;grid-template-columns:minmax(0,1.6fr) minmax(0,1fr) 140px 120px;align-items:center;gap:20px}
.ln-hd{padding:14px 16px 10px 16px;font-size:12.5px;font-weight:500;color:#8A93AD}
.ln-l{list-style:none;margin:0;padding:0}
.ln-l li{border-top:1.5px solid #F0F2F8}
.ln-r{padding:14px 16px;border-radius:14px;color:#0B1433;text-decoration:none}
.ln-r:hover{background:#F7F9FD}
.ln-r .av{position:absolute}
.ln-n{display:flex;flex-direction:column;gap:2px;padding-left:50px;position:relative;min-height:36px;justify-content:center}
.ln-r{position:relative}
.ln-n b{font-size:15px;font-weight:600}.ln-n span{font-size:13px;color:#5B6582;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.ln-p{display:flex;align-items:center;gap:12px}.ln-p i{flex:1;max-width:160px;height:6px;border-radius:6px;background:#E6EAF3;overflow:hidden}.ln-p em{display:block;height:100%;border-radius:6px;background:#1652F0}
.ln-p b{font-size:14px;font-weight:600;font-variant-numeric:tabular-nums;min-width:38px}
.ln-t{font-size:14px;color:#5B6582}
.ln-s{display:flex;justify-content:flex-end}
@media (max-width: 960px){
.ln-cnt{font-size:15px;vertical-align:2px}
.ln-bar{flex-wrap:wrap;gap:8px;margin-bottom:12px}
.ln-q{flex-basis:100%;max-width:none}
.ln-f{display:inline-flex !important;height:36px;font-size:13px;padding:0 12px}
.ln-card{padding:2px 4px}
.ln-hd{display:none}
.ln-r{grid-template-columns:minmax(0,1fr) auto;gap:8px 12px;padding:14px 10px}
.ln-p{grid-column:1 / -1;padding-left:50px}
.ln-t{display:none}
.ln-s{grid-row:1;grid-column:2}
.ln-s .st{height:24px;padding:0 9px;font-size:12px}
}
'''
B.page('CR-LRN-001', 'Learners', main, NAVJS, css, 'Credalio · Learners', "{ nav: false }")
wrap('CR-LRN-001', [('CR-LRN-001', '', 940)])
print('build29 ok')
