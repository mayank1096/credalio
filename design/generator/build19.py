# build19: CR-ASG-001 (Assigned to me, Studio page) + contributor declarations flow.
# CR-DEC-001 one source, variants request / declare / status / lead (= DEC-001 / 002 / 003 / 004), focus-mode shell
# reusing the LIVE CR-COL-002 head + styles (cl-*). Imports build17 for the Studio page() helper (build17 rewrites its own
# files identically). Only writes its own files. usage: python3 build19.py <canvas project dir>
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build17 as B
P, rd, wr, ic, I, ARR = B.P, B.rd, B.wr, B.ic, B.I, B.ARR
CHK = ic('<path d="m5 12.5 4.5 4.5L19 7.5"></path>', 14, 2.6)
BACK = ic('<path d="M19 12H5"></path><path d="m11 6-6 6 6 6"></path>', 18, 2.2)
PEN = ic('<path d="M4 20h4L19 9l-4-4L4 16z"></path><path d="m13.5 6.5 4 4"></path>', 18)
BELL = ic(I['bell'], 16)

# ======================= CR-ASG-001 · Assigned to me =======================
# (title, experience, type, icon, due, status, tone, group)
ASG = [
 ('Review Mary’s Chapter 4 changes', 'Data Analysis with SQL', 'Review', 'eye', 'Due Sat 3 Oct', 'Needs review', 'am', 'This week', 'Review'),
 ('Lesson 3.2 · Building a revenue model', 'Financial Modelling Basics', 'Lesson', 'book', 'Due Fri 2 Oct', 'In progress', 'cb', 'This week', 'Resume'),
 ('Validation request #16 · meeting', 'Data Analysis with SQL', 'Validation', 'val', 'Due Thu 8 Oct', 'Needs you', 'am', 'Next week', 'Open'),
 ('Lesson 3.3 · Scenario analysis (video)', 'Financial Modelling Basics', 'Lesson', 'book', 'Due Wed 7 Oct', 'To do', 'gy', 'Next week', 'Start'),
 ('Contributor declaration', 'Financial Modelling Basics', 'Declaration', 'doc', 'Due Mon 12 Oct', 'To do', 'gy', 'Later', 'Start'),
 ('Quiz 3 · Revenue models', 'Financial Modelling Basics', 'Assessment', 'cert', 'Due Mon 19 Oct', 'To do', 'gy', 'Later', 'Start'),
 ('Lesson 3.1 · Model structure', 'Financial Modelling Basics', 'Lesson', 'book', 'Done 28 Sep', 'Done', 'gr', 'Done', 'Open'),
]
F = {'Needs review': 'rv', 'Needs you': 'rv', 'In progress': 'ip', 'To do': 'td', 'Done': 'dn'}
groups = ''
for g in ['This week', 'Next week', 'Later', 'Done']:
    rows = ''
    for t, exp, ty, icn, due, st, tone, gg, act in ASG:
        if gg != g: continue
        soon = ' soon' if g == 'This week' else ''
        rows += (f'<li class="as-r" data-f="{F[st]}"><span class="hp-ic">{ic(I[icn], 20)}</span><span class="as-t"><b>{t}</b><span>{exp} · {ty}</span></span>'
                 f'<span class="as-d{soon}">{due}</span><span class="as-st"><span class="ex-pill {tone}">{st}</span></span><a href="#" class="hp-rb">{act}</a></li>')
    groups += f'<section class="as-g as-{g[:2].lower()}" aria-label="{g}"><span class="hp-lab">{g}</span><ul class="ds-card as-l">{rows}</ul></section>'
TABS = [('All', 7), ('Needs you', 2), ('In progress', 1), ('To do', 3), ('Done', 1)]
main_asg = ('<main class="ds-main hp">\n<div class="hp-head ob-in"><div><h1 class="ds-h1">Assigned to me</h1><p class="hp-sub">2 need you this week · across 2 learning experiences</p></div></div>'
            '<div class="hp-tabs ob-in2" role="tablist" aria-label="Filter"><sc-for list="{{tabs}}" as="c" hint-placeholder-count="5"><button type="button" role="tab" aria-selected="{{c.sel}}" class="hp-tab {{c.cls}}" onClick="{{c.pick}}">{{c.t}} <em>{{c.n}}</em></button></sc-for></div>'
            '<div class="as ob-in3 {{fCls}}">' + groups + '</div>\n</main>')
import json
js_asg = '''    const T = ''' + json.dumps([list(x) for x in TABS]) + ''';
    const key = { 'All': '', 'Needs you': 'f-rv', 'In progress': 'f-ip', 'To do': 'f-td', 'Done': 'f-dn' };
    return { navCls: S.nav ? 'ds-open' : '', toggleNav: () => this.setState({ nav: !S.nav }), fCls: key[S.tab],
      tabs: T.map((x) => ({ t: x[0], n: x[1], cls: S.tab === x[0] ? 'on' : '', sel: S.tab === x[0] ? 'true' : 'false', pick: () => this.setState({ tab: x[0] }) })) };'''
css_asg = '''
.as-g{margin-top:22px}
.as-l{list-style:none;margin:10px 0 0 0;padding:4px 20px}
.as-r{display:grid;grid-template-columns:40px minmax(0,1fr) 150px 130px 92px;align-items:center;column-gap:16px;padding:14px 0;border-top:1.5px solid #F0F2F8}
.as-r:first-child{border-top:0}
.as-t{display:flex;flex-direction:column;gap:3px;min-width:0}
.as-t b{font-size:15px;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.as-t span{font-size:13.5px;color:#5B6582}
.as-d{font-size:13.5px;color:#3A4566}.as-d.soon{color:#8A5300;font-weight:500}
.ex-pill{display:inline-flex;align-items:center;height:28px;padding:0 11px;border-radius:999px;font-size:12.5px;font-weight:500;white-space:nowrap}
.ex-pill.gr{background:#E7F5EE;color:#0F6B45}.ex-pill.cb{background:#EAF0FF;color:#0E3BB8}.ex-pill.gy{background:#F1F3F8;color:#4A5578}.ex-pill.am{background:#FFF3DC;color:#8A5300}
.as-r .hp-rb{justify-self:end}
.as-do .as-r b{color:#5B6582;font-weight:500}
.f-rv .as-r:not([data-f="rv"]),.f-ip .as-r:not([data-f="ip"]),.f-td .as-r:not([data-f="td"]),.f-dn .as-r:not([data-f="dn"]){display:none}
.f-rv .as-g:not(:has(.as-r[data-f="rv"])),.f-ip .as-g:not(:has(.as-r[data-f="ip"])),.f-td .as-g:not(:has(.as-r[data-f="td"])),.f-dn .as-g:not(:has(.as-r[data-f="dn"])){display:none}
@media (max-width: 960px){
.as-g{margin-top:20px}
.as-l{padding:2px 14px}
.as-r{grid-template-columns:36px minmax(0,1fr) auto;row-gap:4px;column-gap:12px;align-items:start;padding:13px 0;position:relative}
.as-r .hp-ic{width:36px;height:36px;border-radius:11px;grid-row:span 2}
.as-t b{white-space:normal;font-size:14.5px}
.as-d{grid-column:2;grid-row:2;font-size:12.5px}
.as-st{grid-column:3;grid-row:1}
.as-st .ex-pill{height:24px;padding:0 9px;font-size:12px}
.as-r .hp-rb{position:absolute;inset:0;height:auto;opacity:0;font-size:0}
}
'''
B.page('CR-ASG-001', 'Assigned to me', main_asg, js_asg, css_asg, 'Credalio · Assigned to me', "{ nav: false, tab: 'All' }")

# ======================= CR-DEC-001 · contributor declarations (focus shell) =======================
col = rd('CR-COL-002.dc.html')
head = col[:col.index('<div class="tk-root')]
X = col[col.index('class="lp-x"'):]
X = X[X.index('<svg'):X.index('</a>')]
DECL = ['The content I contributed is accurate to the best of my knowledge.', 'I have the rights and permissions to use it.', 'I’ve provided the required sources and disclosures.',
        'AI-assisted content I contributed has been reviewed.', 'My contribution follows Credalio policies.']

def steps(labels):
    return '<ol class="cl-steps" aria-label="Steps">' + ''.join(f'<li class="{{{{s{i}}}}}"><i></i><span>{t}</span></li>' for i, t in enumerate(labels)) + '</ol>'

side_m = ('<sc-if value="{{asMary}}" hint-placeholder-val="{{true}}"><aside class="cl-side ob-in">'
          '<div class="cl-from"><span class="cl-av">AO</span><span><b>Ada Ononuju</b><span>Lead Creator · course owner</span></span></div>'
          '<span class="cl-eb">Asks for your declaration</span><h1 class="cl-h1">Data Analysis with SQL</h1>'
          '<p class="cl-sub">Ada is preparing the course for validation. It can be submitted once every contributor has declared their own work.</p>'
          '<div class="cl-meta"><span>Course</span><span>Due Mon 5 Oct</span></div>'
          + steps(['Review', 'Declare', 'Done']) + '</aside></sc-if>')
side_a = ('<sc-if value="{{asAda}}" hint-placeholder-val="{{false}}"><aside class="cl-side ob-in">'
          '<h1 class="cl-h1 dc-h0">Data Analysis with SQL</h1>'
          '<p class="cl-sub">Before validation, every contributor declares their own work, and you sign last for the whole course.</p>'
          '<div class="cl-meta"><span>Course</span><span>Draft · ready to submit</span></div>'
          '<div class="cl-team"><span class="cl-avs"><span class="cl-av sm">AO</span><span class="cl-av sm t2">JA</span><span class="cl-av sm t3">MO</span></span><span>You, John Adeyemi and Mary Okafor</span></div>'
          + steps(['Declarations', 'Your declaration', 'Quote']) + '</aside></sc-if>')

ROWS = [('book', 'Chapter 4 · Aggregating for business questions', '4 lessons · 1 practice · 2 AI-assisted questions approved'), ('cert', 'Final assessment', '30 questions · exam')]
request = ('<sc-if value="{{vRequest}}" hint-placeholder-val="{{true}}"><section class="cl-panel ob-in2" aria-labelledby="dc-h1">'
           '<h2 id="dc-h1" class="cl-ph">Your contribution</h2><p class="cl-pp">You declare only for what you made. Take a last look before you sign.</p>'
           '<ul class="dc-l">' + ''.join(f'<li><span class="cl-chi">{ic(I[i], 20)}</span><span class="dc-t"><b>{t}</b><span>{d}</span></span><a href="#" class="hp-rb">Review</a></li>' for i, t, d in ROWS) + '</ul>'
           '<div class="cl-foot"><a href="CR-DEC-002.dc.html" class="ds-btn cl-go dc-go"><span>Review and declare</span><span class="ob-arrow">' + ARR + '</span></a></div>'
           '</section></sc-if>')

checks = ''.join(f'<button type="button" role="checkbox" aria-checked="{{{{c{i}.on}}}}" class="cl-ck {{{{c{i}.cls}}}}" onClick="{{{{c{i}.pick}}}}"><span class="tk-box">{CHK}</span><span><b>{t}</b></span></button>' for i, t in enumerate(DECL))
declare = ('<sc-if value="{{vDeclare}}" hint-placeholder-val="{{false}}"><section class="cl-panel ob-in2" aria-labelledby="dc-h2">'
           '<h2 id="dc-h2" class="cl-ph">Your declaration</h2><p class="cl-pp">For Chapter 4 and the Final assessment only.</p>'
           '<div class="cl-ckw"><div class="cl-ckh"><span>Tick each statement</span><b>{{nOn}} of 5 ticked</b></div><div class="cl-cks dc-cks">' + checks + '</div></div>'
           '<label class="dc-sig"><span>Type your full name to sign</span><input value="{{name}}" onChange="{{onName}}" placeholder="Mary Okafor">' + PEN + '</label>'
           '<div class="cl-foot"><a href="CR-DEC-001.dc.html" class="ds-ghost cl-bk" aria-label="Back">' + BACK + '<span>Back</span></a>'
           '<a href="#" class="ds-btn cl-go {{signOff}}"><span>Sign declaration</span><span class="ob-arrow">' + ARR + '</span></a></div>'
           '</section></sc-if>')

PPL = [('AO', '', 'You', 'Lead Creator · Chapters 1, 5, 6 and course design', 'last'), ('JA', 't2', 'John Adeyemi', 'Co-Creator · Chapters 2–3 and Quiz 2', 'ok'), ('MO', 't3', 'Mary Okafor', 'Contributor · Chapter 4 and Final assessment', 'wait')]
ppl = ''
for av, t, n, r, st in PPL:
    pill = {'ok': '<span class="ex-pill gr">' + CHK + 'Declared</span>', 'wait': '<span class="ex-pill am">Waiting</span>', 'last': '<span class="ex-pill gy">Signs last</span>'}[st]
    act = '<button type="button" class="hp-rb dc-rm" onClick="{{remind}}">' + BELL + '<span>{{remLbl}}</span></button>' if st == 'wait' else ''
    ppl += f'<li class="dc-p dc-s-{st}"><span class="cl-av {t}">{av}</span><span class="dc-t"><b>{n}</b><span>{r}</span></span>{pill}{act}</li>'
status = ('<sc-if value="{{vStatus}}" hint-placeholder-val="{{false}}"><section class="cl-panel ob-in2" aria-labelledby="dc-h3">'
          '<h2 id="dc-h3" class="cl-ph">Contributor declarations</h2><p class="cl-pp">1 of 2 contributors have declared.</p>'
          '<ul class="dc-l dc-pl">' + ppl + '</ul>'
          '<div class="cl-note dc-amb">' + ic('<circle cx="12" cy="12" r="9"></circle><path d="M12 7v6M12 16.5v.01"></path>', 18, 2.2) + '<span>Submission is waiting on Mary’s declaration. She was asked on Mon 28 Sep.</span></div>'
          '<div class="cl-foot"><a href="CR-DEC-004.dc.html" class="ds-btn cl-go dc-go lp-off"><span>Continue to your declaration</span><span class="ob-arrow">' + ARR + '</span></a></div>'
          '</section></sc-if>')

lchecks = ''.join(f'<button type="button" role="checkbox" aria-checked="{{{{l{i}.on}}}}" class="cl-ck {{{{l{i}.cls}}}}" onClick="{{{{l{i}.pick}}}}"><span class="tk-box">{CHK}</span><span><b>{t}</b></span></button>'
                  for i, t in enumerate(['I’m authorised to submit this course for validation, and every required contributor declaration is complete.', 'My own contribution is accurate, and AI-assisted content I added has been reviewed.']))
lead = ('<sc-if value="{{vLead}}" hint-placeholder-val="{{false}}"><section class="cl-panel ob-in2" aria-labelledby="dc-h4">'
        '<h2 id="dc-h4" class="cl-ph">Your submission declaration</h2>'
        '<div class="cl-sum dc-sum"><span class="cl-sv"><em>Contributor declarations</em><b class="dc-ok">' + CHK + '2 of 2 complete</b></span><span class="cl-sv"><em>Next</em><b>Quote → payment → case opens</b></span></div>'
        '<div class="cl-ckw"><div class="cl-cks dc-cks">' + lchecks + '</div></div>'
        '<label class="dc-sig"><span>Type your full name to sign</span><input value="{{name}}" onChange="{{onName}}" placeholder="Ada Ononuju">' + PEN + '</label>'
        '<div class="cl-foot"><a href="CR-DEC-003.dc.html" class="ds-ghost cl-bk" aria-label="Back">' + BACK + '<span>Back</span></a>'
        '<a href="#" class="ds-btn cl-go {{leadOff}}"><span>Sign and submit</span><span class="ob-arrow">' + ARR + '</span></a></div>'
        '</section></sc-if>')

body = ('<div class="tk-root cl-root {{rootCls}}">\n<div class="tk-scene" aria-hidden="true"></div><div class="cl-glow" aria-hidden="true"></div>\n'
        '<header class="tk-top">\n<a href="{{closeHref}}" class="lp-x" aria-label="Close">' + X + '</a>\n'
        '<div class="lp-title"><span class="lp-t1" style="display: block">{{title}}</span></div>\n<span style="flex-grow: 1"></span>\n</header>\n'
        '<main class="cl">\n' + side_m + side_a + '\n<div class="cl-main">' + request + declare + status + lead + '</div>\n</main>\n</div>\n</x-dc>\n')

CSS = '''
/* build19 declarations */
.dc-h0{margin-top:0}
.dc-sum{margin-top:16px}
.dc-l{list-style:none;margin:18px 0 0 0;padding:0;border:1.5px solid #E6EAF3;border-radius:18px}
.dc-l li{display:flex;align-items:center;gap:14px;padding:14px 16px;border-top:1.5px solid #F0F2F8}
.dc-l li:first-child{border-top:0}
.dc-t{flex-grow:1;display:flex;flex-direction:column;gap:2px;min-width:0}
.dc-t b{font-size:15px;font-weight:600}.dc-t span{font-size:13px;color:#5B6582}
.hp-rb{display:inline-flex;align-items:center;gap:6px;height:38px;padding:0 15px;border-radius:999px;border:1.5px solid #D6DDEE;background:#FFFFFF;color:#0B1433;font-size:13.5px;font-weight:600;text-decoration:none;flex-shrink:0;font-family:inherit;cursor:pointer;white-space:nowrap}
.dc-n{margin-top:14px}
.dc-go{margin-left:auto}
.dc-sig{margin-top:18px;position:relative;display:flex;flex-direction:column;gap:8px}
.dc-sig > span{font-size:13px;font-weight:500;color:#3A4566}
.dc-sig input{height:52px;box-sizing:border-box;padding:0 44px 0 16px;border-radius:14px;border:1.5px solid #D6DDEE;font-family:inherit;font-size:18px;font-style:italic;color:#0B1433;outline:none;background:#FFFFFF}
.dc-sig input:focus{border-color:#1652F0;box-shadow:0 0 0 4px rgba(22,82,240,.12)}
.dc-sig svg{position:absolute;right:16px;bottom:17px;color:#8A93AD}
.dc-cks{max-height:none}
.cl-av.sm{width:30px;height:30px}
.dc-p .cl-av{width:40px;height:40px;font-size:13px}
.ex-pill{display:inline-flex;align-items:center;gap:5px;height:28px;padding:0 11px;border-radius:999px;font-size:12.5px;font-weight:500;white-space:nowrap;flex-shrink:0}
.ex-pill.gr{background:#E7F5EE;color:#0F6B45}.ex-pill.gy{background:#F1F3F8;color:#4A5578}.ex-pill.am{background:#FFF3DC;color:#8A5300}
.ex-pill svg{width:12px;height:12px}
.dc-rm svg{color:#5B6582}
.dc-amb{margin-top:14px;background:#FFF8EC;color:#6B4A12;font-weight:500;align-items:flex-start}
.dc-amb svg{color:#B26A00;flex-shrink:0;margin-top:1px}
.is-wait .cl-glow{background:radial-gradient(60% 100% at 50% 0,rgba(214,140,20,.10),transparent 70%)}
.dc-sum{grid-template-columns:auto auto;justify-content:start;gap:12px 40px;padding:14px 18px}
.dc-ok{display:inline-flex;align-items:center;gap:6px;color:#0F6B45}
@media (max-width: 960px){
.dc-l li{padding:12px 14px;gap:12px}
.dc-l .hp-rb{height:34px;padding:0 12px;font-size:13px}
.dc-l li.dc-p{display:grid;grid-template-columns:40px minmax(0,1fr) auto;align-items:start;column-gap:12px;row-gap:10px}
.dc-p .dc-rm{grid-column:2 / -1;justify-self:start}
.dc-sum{grid-template-columns:minmax(0,1fr);padding:14px}
.dc-cks{max-height:none}
}
'''

SCRIPT = '''<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":1440,"height":820}}'>
class Component extends DCLogic {
  constructor(props) { super(props); const v = (props && props.variant) || 'request'; this.state = { v, ck: v === 'declare' ? { 0: 1, 1: 1 } : {}, lk: {}, name: '', rem: false }; }
  renderVals() {
    const S = this.state, v = S.v, out = {}, mary = v === 'request' || v === 'declare';
    const tick = (key, n, pre) => { for (let i = 0; i < n; i++) { const on = !!S[key][i]; out[pre + i] = { on: on ? 'true' : 'false', cls: on ? 'tk-on' : '', pick: () => this.setState({ [key]: Object.assign({}, S[key], { [i]: !on }) }) }; } return Object.keys(S[key]).filter((k) => S[key][k]).length; };
    const n = tick('ck', 5, 'c'), nl = tick('lk', 2, 'l');
    const step = (i) => (i === 0 ? (v === 'request' || v === 'status' ? 'on' : 'dn') : (v === 'declare' || v === 'lead' ? 'on' : ''));
    return Object.assign(out, {
      vRequest: v === 'request', vDeclare: v === 'declare', vStatus: v === 'status', vLead: v === 'lead', asMary: mary, asAda: !mary,
      rootCls: v === 'status' ? 'is-wait' : '', title: mary ? 'Contributor declaration' : 'Submit for validation',
      closeHref: mary ? 'CR-ASG-001.dc.html' : 'CR-HOME-EXP.dc.html', s0: step(0), s1: step(1), s2: '',
      nOn: n, name: S.name, onName: (e) => this.setState({ name: e.target.value }),
      signOff: n < 5 || S.name.trim().length < 3 ? 'lp-off' : '', leadOff: nl < 2 || S.name.trim().length < 3 ? 'lp-off' : '',
      remLbl: S.rem ? 'Reminder sent' : 'Send reminder', remind: () => this.setState({ rem: true })
    });
  }
}
</script>
</body>
</html>
'''
s = head.replace('</style>', CSS + '</style>', 1)
s = re.sub(r'<title>.*?</title>', '<title>Credalio · Contributor declarations</title>', s)
wr('CR-DEC-001.dc.html', s + body + SCRIPT)

wd, wm = rd('CR-DASH-S03.dc.html'), rd('CR-CRED-002c-Mobile.dc.html')
for n, var in [('CR-DEC-001', None), ('CR-DEC-002', 'declare'), ('CR-DEC-003', 'status'), ('CR-DEC-004', 'lead')]:
    imp = '<dc-import name="CR-DEC-001"' + (f' variant="{var}"' if var else '')
    if var:
        t = wd.replace('<dc-import name="CR-DASH-ST" variant="s03"', imp)
        wr(n + '.dc.html', re.sub(r'<title>.*?</title>', f'<title>{n} preview</title>', t))
    t = wm.replace('<dc-import name="CR-CRED-002" variant="badge"', imp)
    wr(n + '-Mobile.dc.html', re.sub(r'<title>.*?</title>', f'<title>{n} mobile preview</title>', t))
t = wm.replace('<dc-import name="CR-CRED-002" variant="badge"', '<dc-import name="CR-ASG-001"')
t = re.sub(r'hint-size="[^"]*"', 'hint-size="390px,1100px"', t)
t = re.sub(r'width: \d+px; height: \d+px;', 'width: 390px; height: 1100px;', t, count=1)
t = re.sub(r'"\$preview":\{"width":\d+,"height":\d+\}', '"$preview":{"width":390,"height":1100}', t)
wr('CR-ASG-001-Mobile.dc.html', re.sub(r'<title>.*?</title>', '<title>CR-ASG-001 mobile preview</title>', t))
print('build19 ok')
