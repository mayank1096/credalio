# build20: validation — CR-VAL-MC-001 (Validation Centre, Studio page) + Validation Workspace inside the Course Studio:
# CR-VAL-WS one source, variants lead / mary / req / resp / leadreq (= VAL-WS-lead / VAL-WS-mary / VAL-MC-002 / VAL-MC-003 / VAL-MC-002L).
# Course Studio shell = focus top bar (close, course, Content / Validation / Team / Settings tabs) on the LIVE CR-COL-002 head.
# Imports build17 for page(). Only writes its own files. usage: python3 build20.py <canvas project dir>
import re, sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build17 as B
P, rd, wr, ic, I, ARR = B.P, B.rd, B.wr, B.ic, B.I, B.ARR
CHK = ic('<path d="m5 12.5 4.5 4.5L19 7.5"></path>', 13, 2.8)
CLIP = ic('<path d="m21 11-8.5 8.5a5 5 0 0 1-7-7L14 4a3.5 3.5 0 0 1 5 5l-8.5 8.5a2 2 0 0 1-3-3L15 7"></path>', 16)
LINK = ic('<path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1"></path><path d="M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"></path>', 16)
CAL = ic(I['cal'], 16)
SEND = ic('<path d="M5 12h14"></path><path d="m13 6 6 6-6 6"></path>', 16, 2.4)
EYE = ic(I['eye'], 15)

VALS = [('AB', 'v1', 'Dr. Amina Bello', 'Educational'), ('KA', 'v2', 'Prof. Kunle Ade', 'Subject matter'), ('SO', 'v3', 'Dr. Sarah Okoye', 'Assessment')]
AV_CSS = '''
.va{width:34px;height:34px;flex-shrink:0;border-radius:50%;color:#FFFFFF;font-size:12px;font-weight:600;display:flex;align-items:center;justify-content:center;background:#0B1433}
.va.v1{background:#3A4566}.va.v2{background:#0F6B45}.va.v3{background:#5B6582}.va.me{background:#1652F0}.va.mo{background:#5B6582}.va.ja{background:#1652F0}
.vp{display:inline-flex;align-items:center;height:28px;padding:0 11px;border-radius:999px;font-size:12.5px;font-weight:500;white-space:nowrap;flex-shrink:0}
.vp.am{background:#FFF3DC;color:#8A5300}.vp.cb{background:#EAF0FF;color:#0E3BB8}.vp.gr{background:#E7F5EE;color:#0F6B45}.vp.gy{background:#F1F3F8;color:#4A5578}
'''

# ======================= CR-VAL-MC-001 · Validation Centre =======================
track = lambda n: '<ol class="vc-tr">' + ''.join(f'<li class="{"dn" if i < n else ("on" if i == n else "")}"><i></i><span>{t}</span></li>' for i, t in enumerate(['Submitted', 'Validators assigned', 'Review', 'Decision'])) + '</ol>'
vals = ''.join(f'<span class="vc-v"><span class="va {c}">{a}</span><span><b>{n}</b><span>{r} validator</span></span></span>' for a, c, n, r in VALS)
main_vc = ('<main class="ds-main hp">\n<div class="hp-head ob-in"><div><h1 class="ds-h1">Validation Centre</h1><p class="hp-sub">2 cases · each workspace opens inside its course Studio</p></div></div>'
           '<section class="ds-card vc ob-in2" aria-label="Data Analysis with SQL"><div class="vc-h"><span class="vc-cv">' + ic(I['book'], 22) + '</span>'
           '<span class="vc-t"><b>Data Analysis with SQL</b><span>Case VAL-00928 · you’re the Lead Creator</span></span><span class="vp cb">Review in progress</span></div>'
           + track(2) +
           '<div class="vc-g"><div class="vc-c"><span class="hp-lab">Validators</span><div class="vc-vv"><span class="vc-st">' + ''.join(f'<span class="va {c}">{a}</span>' for a, c, n, r in VALS) + '</span><b>3 assigned</b></div><span class="vc-s">Educational · Subject matter · Assessment</span></div>'
           '<div class="vc-c"><span class="hp-lab">Open requests</span><b class="vc-big">3</b><span class="vc-s vc-am"><i></i>1 needs you</span></div>'
           '<div class="vc-c"><span class="hp-lab">Next</span><b>Meeting with Dr. Amina Bello</b><span class="vc-s">Pick a time by Thu 8 Oct</span></div></div>'
           '<div class="vc-f"><span class="vc-note">' + EYE + 'Requests go to whoever made the affected content. You see all of them.</span>'
           '<a href="CR-VAL-WS-lead.dc.html" class="ds-btn hp-btn"><span>Open workspace</span><span class="ob-arrow">' + ARR + '</span></a></div></section>'
           '<section class="ds-card vc vc-sm ob-in3" aria-label="Data Analyst Career Path"><div class="vc-h"><span class="vc-cv">' + ic(I['path'], 22) + '</span>'
           '<span class="vc-t"><b>Data Analyst Career Path</b><span>Case VAL-01102 · you’re the Lead Creator</span></span><span class="vp cb">Validators assigned</span>'
           '<span class="vc-mt">No open requests</span><a href="#" class="hp-rb">Open</a></div></section>\n</main>')
css_vc = AV_CSS + '''
.vc{padding:22px 24px;margin-top:4px}
.vc + .vc{margin-top:14px}
.vc-h{display:flex;align-items:center;gap:14px}
.vc-cv{width:48px;height:48px;flex-shrink:0;border-radius:14px;background:linear-gradient(135deg,#1652F0,#6E96FF);color:#FFFFFF;display:flex;align-items:center;justify-content:center}
.vc-t{flex-grow:1;display:flex;flex-direction:column;gap:3px;min-width:0}
.vc-t b{font-size:18px;font-weight:600;letter-spacing:-0.01em}.vc-t span{font-size:13.5px;color:#5B6582}
.vc-tr{list-style:none;margin:22px 0 0 0;padding:0;display:grid;grid-template-columns:repeat(4,1fr);gap:6px}
.vc-tr li{display:flex;flex-direction:column;gap:8px;font-size:13px;font-weight:500;color:#8A93AD}
.vc-tr i{height:4px;border-radius:4px;background:#E6EAF3}
.vc-tr .dn{color:#3A4566}.vc-tr .dn i{background:#1652F0}
.vc-tr .on{color:#0B1433}.vc-tr .on i{background:linear-gradient(90deg,#1652F0 50%,#E6EAF3 50%)}
.vc-g{margin-top:22px;display:grid;grid-template-columns:1.3fr 1fr 1.2fr}
.vc-c{display:flex;flex-direction:column;gap:6px;padding:2px 24px;border-left:1.5px solid #F0F2F8;min-width:0}
.vc-c:first-child{padding-left:0;border-left:0}
.vc-c b{font-size:15.5px;font-weight:600}
.vc-big{font-size:24px !important;line-height:1}
.vc-vv{display:flex;align-items:center;gap:10px}
.vc-st{display:flex}.vc-st .va{width:30px;height:30px;font-size:11px;border:2px solid #FFFFFF}.vc-st .va + .va{margin-left:-8px}
.vc-s{font-size:13px;color:#5B6582}
.vc-am{display:inline-flex;align-items:center;gap:7px;color:#8A5300;font-weight:500}.vc-am i{width:7px;height:7px;border-radius:50%;background:#D68C14}
.vc-f{margin-top:20px;padding-top:18px;border-top:1.5px solid #F0F2F8;display:flex;align-items:center;justify-content:space-between;gap:16px}
.vc-note{display:flex;align-items:center;gap:8px;font-size:13.5px;color:#5B6582}
.vc-sm{padding:16px 20px}
.vc-sm .vc-cv{width:44px;height:44px;border-radius:13px}
.vc-sm .vc-t b{font-size:16px}
.vc-mt{font-size:13.5px;color:#5B6582;margin:0 8px}
@media (max-width: 960px){
.vc{padding:16px}
.vc-h{flex-wrap:wrap;gap:12px}
.vc-cv{width:42px;height:42px;border-radius:12px}
.vc-t{flex-basis:calc(100% - 56px)}
.vc-t b{font-size:16px}
.vc-h > .vp{margin-left:54px}
.vc-tr{margin-top:18px}
.vc-tr span{font-size:11.5px}
.vc-g{grid-template-columns:minmax(0,1fr) minmax(0,1.3fr);margin-top:16px}
.vc-c{padding:12px 0 0 16px;border-top:1.5px solid #F0F2F8;margin-top:12px}
.vc-c:first-child{grid-column:1 / -1;border-top:0;padding:0;margin-top:0}
.vc-c:nth-child(2){padding-left:0;border-left:0}
.vc-big{font-size:20px !important}
.vc-c b{font-size:14.5px}
.vc-f{flex-direction:column;align-items:stretch}
.vc-f .hp-btn{width:100%;justify-content:space-between}
.vc-sm .vc-mt{display:none}
.vc-sm .hp-rb{margin-left:auto}
}
'''
B.page('CR-VAL-MC-001', 'Validation Centre', main_vc, B.js_new, css_vc, 'Credalio · Validation Centre')

# ======================= CR-VAL-WS · Validation Workspace inside the Course Studio =======================
col = rd('CR-COL-002.dc.html')
head = col[:col.index('<div class="tk-root')]
X = col[col.index('class="lp-x"'):]
X = X[X.index('<svg'):X.index('</a>')]

# (n, type, affected, who, whoName, av, due, title, finding, raisedBy, status, tone)
REQ = [(16, 'Meeting request', 'Whole course', 'ada', 'You', 'me', 'Thu 8 Oct', 'Sequencing of Chapters 3–5', '', 'AB', 'Needs you', 'am'),
       (14, 'Clarification', 'Chapter 4 · Lesson 3', 'mary', 'Mary Okafor', 'mo', 'Sun 4 Oct', 'ROW_NUMBER vs RANK with ties', '', 'KA', 'Waiting on Mary', 'gy'),
       (15, 'Evidence', 'Chapter 2 · Lesson 2', 'john', 'John Adeyemi', 'ja', 'Tue 6 Oct', 'Source for an indexing claim', '', 'KA', 'Waiting on John', 'gy'),
       (12, 'Clarification', 'Chapter 1 · Lesson 1', 'ada', 'You', 'me', 'Done', 'Course prerequisites', '', 'AB', 'Ready for review', 'cb')]
def rows(mary):
    o = ''
    for n, ty, aff, who, wn, av, due, t, _, _, st, tone in REQ:
        if mary and who != 'mary': continue
        ini = {'me': 'AO', 'mo': 'MO', 'ja': 'JA'}[av]
        if mary: wn, st, tone, av = 'You', 'Needs you', 'am', 'me'
        mine = (who == 'ada') if not mary else True
        href = 'CR-VAL-MC-002.dc.html' if mary else ('CR-VAL-MC-002L.dc.html' if n == 14 else '#')
        o += (f'<a href="{href}" class="ws-r{" mine" if mine and st == "Needs you" else ""}"><span class="ws-n">#{n}</span><span class="ws-t"><b>{t}</b><span>{ty} · {aff}</span></span>'
              f'<span class="ws-w"><span class="va sm {av}">{ini if not (mary) else "MO"}</span><span>{wn}</span></span><span class="ws-d">{due}</span><span class="vp {tone}">{st}</span></a>')
    return o
ws_list = lambda mary: ('<div class="ws-hd"><span>Request</span><span>Assigned to</span><span>Due</span><span>Status</span></div><div class="ws-l">' + rows(mary) + '</div>')
WTABS = '<div class="ws-tabs" role="tablist"><span class="on">Requests <em>{{nReq}}</em></span><span>Findings</span><span>Meetings</span><span>Decision</span></div>'

lead_v = ('<sc-if value="{{vLead}}" hint-placeholder-val="{{true}}"><div class="ws-head ob-in"><div><span class="ws-eb">Validation · Case VAL-00928</span><h1 class="ws-h1">Requests</h1>'
          '<p class="ws-sub">You see every request. Each one goes to whoever made the affected content.</p></div><span class="ws-as">' + EYE + 'Viewing as Lead Creator</span></div>'
          + WTABS + '<section class="ws-card ob-in2" aria-label="Requests">' + ws_list(False) + '</section></sc-if>')
mary_v = ('<sc-if value="{{vMary}}" hint-placeholder-val="{{false}}"><div class="ws-head ob-in"><div><span class="ws-eb">Validation · Case VAL-00928</span><h1 class="ws-h1">Requests</h1>'
          '<p class="ws-sub">Requests about your part of the course: Chapter 4 and the Final assessment.</p></div><span class="ws-as">' + EYE + 'Viewing as Contributor</span></div>'
          + WTABS + '<section class="ws-card ob-in2" aria-label="Requests">' + ws_list(True) + '<div class="ws-hid">3 other requests on this case are with other creators. Ada, the Lead Creator, sees all of them.</div></section></sc-if>')

# request detail (Mary: req / resp; Lead read-only: leadreq)
KA_MSG = 'Lesson 4.3 says ROW_NUMBER and RANK return the same result when values tie. Please clarify or correct this, and confirm how the practice task handles ties.'
MARY_MSG = 'Corrected: ROW_NUMBER gives unique numbers; RANK gives tied rows the same rank and skips the next. The practice task now includes a tie.'
meta = lambda who_txt: ('<aside class="rq-side ob-in3"><section class="ws-card rq-meta"><dl>'
                        '<div><dt>Affected</dt><dd>Chapter 4 · Lesson 3</dd></div>'
                        f'<div><dt>Assigned to</dt><dd>{who_txt}</dd></div>'
                        '<div><dt>Raised by</dt><dd>Prof. Kunle Ade · Subject matter</dd></div>'
                        '<div><dt>Due</dt><dd class="rq-due">Sun 4 Oct</dd></div>'
                        '<div><dt>Visible to</dt><dd>You, Ada (Lead Creator) and the validators</dd></div></dl></section>')
detail = ('<sc-if value="{{vDetail}}" hint-placeholder-val="{{false}}"><a href="{{backHref}}" class="rq-back">' + ic('<path d="M19 12H5"></path><path d="m11 6-6 6 6 6"></path>', 16, 2.2) + '<span>All requests</span></a>'
          '<div class="rq ob-in"><div class="rq-main">'
          '<section class="ws-card rq-top"><div class="rq-tl"><span class="vp gy">Clarification #14</span><span class="vp {{stTone}}">{{stTxt}}</span></div>'
          '<h1 class="ws-h1 rq-h">ROW_NUMBER vs RANK with ties</h1>'
          '<div class="rq-thread">'
          f'<div class="rq-m"><span class="va v2">KA</span><div><span class="rq-who"><b>Prof. Kunle Ade</b> · Subject matter validator · 2 days ago</span><p>{KA_MSG}</p></div></div>'
          '<sc-if value="{{posted}}" hint-placeholder-val="{{false}}">'
          f'<div class="rq-m me"><span class="va mo">MO</span><div><span class="rq-who"><b>Mary Okafor</b> · Contributor · just now</span><p>{MARY_MSG}</p><span class="rq-att">{CLIP}Lesson 4.3 (revised).pdf</span></div></div></sc-if>'
          '</div>'
          '<sc-if value="{{canRespond}}" hint-placeholder-val="{{true}}"><div class="rq-comp"><label for="rq-r" class="sr-only">Your response</label>'
          '<textarea id="rq-r" rows="3" placeholder="Reply, clarify or explain your fix…" value="{{draft}}" onChange="{{onDraft}}"></textarea>'
          '<sc-if value="{{hasAtt}}" hint-placeholder-val="{{false}}"><span class="rq-att rq-pend">' + CLIP + 'Lesson 4.3 (revised).pdf<i>2.1 MB</i></span></sc-if>'
          '<div class="rq-tools"><button type="button" class="rq-tb">' + CLIP + '<span>Upload evidence</span></button><button type="button" class="rq-tb">' + LINK + '<span>Add source</span></button>'
          '<button type="button" class="rq-tb">' + CAL + '<span>Request meeting</span></button><span style="flex-grow: 1"></span>'
          '<button type="button" class="ds-btn rq-send {{sendOff}}" onClick="{{send}}"><span>Send</span><span class="ob-arrow">' + SEND + '</span></button></div></div></sc-if>'
          '<sc-if value="{{readOnly}}" hint-placeholder-val="{{false}}"><div class="rq-ro">' + EYE + '<span>Assigned to Mary. You can follow along here; Mary responds.</span><a href="#" class="hp-rb">Message Mary</a></div></sc-if>'
          '</section></div>'
          + meta('{{whoTxt}}') +
          '<sc-if value="{{canRespond}}" hint-placeholder-val="{{true}}"><section class="ws-card rq-ready"><b>Done responding?</b><span>Mark it ready and the validator is told your response is complete.</span>'
          '<button type="button" class="ds-ghost rq-rb {{readyOff}}">' + CHK + '<span>Mark ready for review</span></button></section></sc-if></aside></div></sc-if>')

body = ('<div class="tk-root ws-root">\n'
        '<header class="tk-top ws-top">\n<a href="CR-VAL-MC-001.dc.html" class="lp-x" aria-label="Close and go back to Validation Centre">' + X + '</a>\n'
        '<div class="lp-title"><span class="lp-t1" style="display: block">Data Analysis with SQL</span></div>\n'
        '<nav class="ws-nav" aria-label="Course Studio"><a href="#">Content</a><a href="#" class="on" aria-current="page">Validation<i>{{navBadge}}</i></a><a href="#">Team</a><a href="#">Settings</a></nav>\n'
        '<span style="flex-grow: 1"></span><span class="va sm {{meCls}} ws-me">{{meIni}}</span>\n</header>\n'
        '<main class="ws">\n' + lead_v + mary_v + detail + '\n</main>\n</div>\n</x-dc>\n')

CSS = AV_CSS + '''
/* build20 workspace */
.hp-rb{display:inline-flex;align-items:center;gap:6px;height:38px;padding:0 15px;border-radius:999px;border:1.5px solid #D6DDEE;background:#FFFFFF;color:#0B1433;font-size:13.5px;font-weight:600;text-decoration:none;flex-shrink:0;font-family:inherit;cursor:pointer;white-space:nowrap}
.ws-root{background:#F7F9FD}
.ws-nav{position:absolute;left:50%;transform:translateX(-50%);display:flex;gap:4px;height:100%}
.ws-nav a{display:flex;align-items:center;gap:6px;padding:0 14px;font-size:14.5px;font-weight:500;color:#5B6582;text-decoration:none;border-bottom:2.5px solid transparent;margin-bottom:-1.5px}
.ws-nav a.on{color:#0B1433;font-weight:600;border-bottom-color:#1652F0}
.ws-nav i{font-style:normal;min-width:20px;height:20px;padding:0 6px;box-sizing:border-box;border-radius:999px;background:#FFF3DC;color:#8A5300;font-size:12px;font-weight:600;display:flex;align-items:center;justify-content:center}
.va.sm{width:30px;height:30px;font-size:11px}
.ws{flex-grow:1;width:min(1180px,100%);box-sizing:border-box;margin:0 auto;padding:clamp(24px,4vh,40px) 32px 56px 32px}
.ws-head{display:flex;align-items:flex-end;justify-content:space-between;gap:20px}
.ws-eb{font-size:13px;font-weight:500;color:#8A93AD}
.ws-h1{margin:6px 0 0 0;font-size:clamp(26px,3.6vh,32px);line-height:1.15;font-weight:600;letter-spacing:-0.02em}
.ws-sub{margin:8px 0 0 0;font-size:15px;line-height:1.55;color:#4A5578}
.ws-as{display:inline-flex;align-items:center;gap:7px;height:34px;padding:0 13px;border-radius:999px;background:#EAF0FF;color:#0E3BB8;font-size:13px;font-weight:500;white-space:nowrap}
.ws-tabs{margin-top:22px;display:flex;gap:6px;border-bottom:1.5px solid #E6EAF3}
.ws-tabs span{display:flex;align-items:center;gap:6px;padding:10px 14px;font-size:14.5px;font-weight:500;color:#5B6582;border-bottom:2.5px solid transparent;margin-bottom:-1.5px}
.ws-tabs .on{color:#0B1433;font-weight:600;border-bottom-color:#1652F0}
.ws-tabs em{font-style:normal;color:#8A93AD;font-weight:500}
.ws-card{background:#FFFFFF;border:1.5px solid #E6EAF3;border-radius:20px}
.ws-tabs + .ws-card{margin-top:18px}
.ws-hd,.ws-r{display:grid;grid-template-columns:56px minmax(0,1fr) 180px 110px 150px;align-items:center;column-gap:16px;padding:0 22px}
.ws-hd{padding-top:12px;padding-bottom:10px;font-size:12.5px;color:#8A93AD;border-bottom:1.5px solid #F0F2F8}
.ws-hd span:first-child{grid-column:1 / 3}
.ws-r{padding-top:15px;padding-bottom:15px;border-top:1.5px solid #F0F2F8;text-decoration:none;color:#0B1433;transition:background .2s ease}
.ws-r:first-child{border-top:0}
.ws-r:hover{background:#F7F9FD}
.ws-r.mine{background:#FFFBF3}
.ws-n{font-size:14px;font-weight:600;color:#5B6582}
.ws-t{display:flex;flex-direction:column;gap:3px;min-width:0}
.ws-t b{font-size:15px;font-weight:600}.ws-t span{font-size:13px;color:#5B6582}
.ws-w{display:flex;align-items:center;gap:9px;font-size:14px}
.ws-d{font-size:14px;color:#3A4566}
.ws-r .vp{justify-self:start}
.ws-l:last-child .ws-r:last-child{border-radius:0 0 20px 20px}
.ws-hid{display:flex;align-items:center;gap:8px;padding:14px 22px;border-top:1.5px solid #F0F2F8;font-size:13.5px;color:#5B6582;background:#F7F9FD;border-radius:0 0 20px 20px}
.rq-back{display:inline-flex;align-items:center;gap:6px;font-size:14px;font-weight:600;color:#3A4566;text-decoration:none}
.rq{margin-top:16px;display:grid;grid-template-columns:minmax(0,1fr) 320px;gap:20px;align-items:start}
.rq-top{padding:24px 26px}
.rq-tl{display:flex;gap:8px}
.rq-h{margin-top:12px}
.rq-thread{margin-top:20px;display:flex;flex-direction:column;gap:14px}
.rq-m{display:flex;gap:12px;align-items:flex-start}
.rq-m > div{flex-grow:1;padding:14px 16px;border-radius:16px;background:#F7F9FD}
.rq-m.me > div{background:#F5F8FF;border:1.5px solid #E1E9FF}
.rq-who{font-size:12.5px;color:#5B6582}.rq-who b{color:#0B1433;font-weight:600}
.rq-m p{margin:6px 0 0 0;font-size:15px;line-height:1.6;color:#0B1433}
.rq-att{margin-top:10px;display:inline-flex;align-items:center;gap:7px;height:34px;padding:0 12px;border-radius:10px;background:#FFFFFF;border:1.5px solid #E6EAF3;font-size:13.5px;font-weight:500;color:#0E3BB8}
.rq-att i{font-style:normal;color:#8A93AD;font-weight:400;margin-left:4px}
.rq-comp{margin-top:20px;border:1.5px solid #D6DDEE;border-radius:18px;padding:12px 12px 10px 16px;background:#FFFFFF}
.rq-comp:focus-within{border-color:#1652F0;box-shadow:0 0 0 4px rgba(22,82,240,.10)}
.rq-comp textarea{width:100%;box-sizing:border-box;border:0;outline:none;resize:none;font-family:inherit;font-size:15px;line-height:1.55;color:#0B1433;background:none}
.rq-pend{margin:4px 0 6px 0}
.rq-tools{display:flex;align-items:center;gap:6px;margin-top:4px}
.rq-tb{display:inline-flex;align-items:center;gap:6px;height:36px;padding:0 12px;border-radius:999px;border:0;background:#F5F8FF;color:#3A4566;font-family:inherit;font-size:13.5px;font-weight:500;cursor:pointer}
.rq-tb svg{color:#1652F0}
.rq-send{height:44px;padding:0 4px 0 18px;font-size:14.5px;gap:10px}.rq-send .ob-arrow{width:36px;height:36px}
.rq-send.lp-off,.rq-rb.lp-off{background:#C9D3EC;box-shadow:none;pointer-events:none;color:#FFFFFF}
.rq-send.lp-off .ob-arrow{color:#9AA8CC}
.rq-ro{margin-top:20px;display:flex;align-items:center;gap:10px;padding:12px 12px 12px 16px;border-radius:14px;background:#F5F8FF;font-size:14px;color:#3A4566}
.rq-ro span{flex-grow:1}
.rq-side{display:flex;flex-direction:column;gap:12px;position:sticky;top:88px}
.rq-meta{padding:6px 20px}
.rq-meta dl{margin:0}
.rq-meta dl > div{padding:12px 0;border-top:1.5px solid #F0F2F8}
.rq-meta dl > div:first-child{border-top:0}
.rq-meta dt{font-size:12.5px;color:#8A93AD}
.rq-meta dd{margin:3px 0 0 0;font-size:14.5px;font-weight:500;color:#0B1433;line-height:1.45}
.rq-due{color:#8A5300 !important}
.rq-ready{padding:18px 20px;display:flex;flex-direction:column;gap:6px}
.rq-ready b{font-size:15px;font-weight:600}.rq-ready > span{font-size:13.5px;line-height:1.5;color:#5B6582}
.rq-rb{margin-top:8px;width:100%;gap:8px}
.rq-rb.lp-off{background:#F1F3F8;color:#8A93AD;border-color:#E6EAF3}
.rq-rb svg{color:currentColor}
@media (max-width: 960px){
.ws-top .lp-title{max-width:calc(100% - 100px)}
.ws-nav{display:none}
.ws{padding:32px 16px 40px 16px}
.ws-head{flex-direction:column;align-items:flex-start;gap:12px}
.ws-h1{font-size:24px}
.ws-sub{font-size:14.5px}
.ws-tabs{margin:20px -16px 0 -16px;padding:0 16px;overflow-x:auto;scrollbar-width:none}
.ws-tabs span{white-space:nowrap}
.ws-hd{display:none}
.ws-r{grid-template-columns:minmax(0,1fr) auto;row-gap:8px;padding:14px 16px}
.ws-n{display:none}
.ws-t{grid-column:1 / -1}
.ws-w{font-size:13px}.ws-w .va{width:24px;height:24px;font-size:10px}
.ws-d{display:none}
.ws-r .vp{justify-self:end}
.ws-hid{padding:14px 16px}
.rq{grid-template-columns:minmax(0,1fr);gap:14px}
.rq-top{padding:18px 16px}
.rq-h{font-size:21px}
.rq-m .va{display:none}
.rq-tools{flex-wrap:wrap}
.rq-tb span{display:none}.rq-tb{width:36px;padding:0;justify-content:center}
.rq-side{position:static}
.rq-meta dl{display:grid;grid-template-columns:1fr 1fr;column-gap:16px}
.rq-meta dl > div:nth-child(2){border-top:0}
.rq-meta dl > div:last-child{grid-column:1 / -1}
.rq-ro{display:grid;grid-template-columns:auto minmax(0,1fr);gap:10px}
.rq-ro .hp-rb{grid-column:1 / -1;justify-content:center}
}
'''

SCRIPT = '''<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":1440,"height":820}}'>
class Component extends DCLogic {
  constructor(props) { super(props); const v = (props && props.variant) || 'lead'; this.state = { v, draft: v === 'resp' ? ''' + json.dumps(MARY_MSG) + ''' : '', posted: false }; }
  renderVals() {
    const S = this.state, v = S.v, mary = v !== 'lead' && v !== 'leadreq';
    const respond = v === 'req' || v === 'resp';
    return {
      vLead: v === 'lead', vMary: v === 'mary', vDetail: v === 'req' || v === 'resp' || v === 'leadreq',
      meIni: mary ? 'MO' : 'AO', meCls: mary ? 'mo' : 'me', nReq: mary ? 1 : 4, navBadge: mary ? 1 : 1,
      backHref: mary ? 'CR-VAL-WS-mary.dc.html' : 'CR-VAL-WS-lead.dc.html',
      canRespond: respond && !S.posted, readOnly: v === 'leadreq', posted: S.posted,
      whoTxt: v === 'leadreq' ? 'Mary Okafor · Contributor' : 'You (Mary Okafor)',
      stTxt: S.posted ? 'Responded' : (v === 'leadreq' ? 'Waiting on Mary' : 'Needs your response'), stTone: S.posted ? 'cb' : (v === 'leadreq' ? 'gy' : 'am'),
      draft: S.draft, onDraft: (e) => this.setState({ draft: e.target.value }), hasAtt: v === 'resp',
      sendOff: S.draft.trim() ? '' : 'lp-off', send: () => this.setState({ posted: true }),
      readyOff: S.posted ? '' : 'lp-off'
    };
  }
}
</script>
</body>
</html>
'''
s = head.replace('</style>', CSS + '</style>', 1)
s = re.sub(r'<title>.*?</title>', '<title>Credalio · Validation Workspace</title>', s)
wr('CR-VAL-WS.dc.html', s + body + SCRIPT)

wd, wm = rd('CR-DASH-S03.dc.html'), rd('CR-CRED-002c-Mobile.dc.html')
def mob(t, h):
    t = re.sub(r'hint-size="[^"]*"', f'hint-size="390px,{h}px"', t)
    t = re.sub(r'width: \d+px; height: \d+px;', f'width: 390px; height: {h}px;', t, count=1)
    return re.sub(r'"\$preview":\{"width":\d+,"height":\d+\}', f'"$preview":{{"width":390,"height":{h}}}', t)
for n, var, hm in [('CR-VAL-WS-lead', 'lead', 844), ('CR-VAL-WS-mary', 'mary', 844), ('CR-VAL-MC-002', 'req', 1100), ('CR-VAL-MC-003', 'resp', 1100), ('CR-VAL-MC-002L', 'leadreq', 1000)]:
    imp = f'<dc-import name="CR-VAL-WS" variant="{var}"'
    t = wd.replace('<dc-import name="CR-DASH-ST" variant="s03"', imp)
    wr(n + '.dc.html', re.sub(r'<title>.*?</title>', f'<title>{n} preview</title>', t))
    t = mob(wm.replace('<dc-import name="CR-CRED-002" variant="badge"', imp), hm)
    wr(n + '-Mobile.dc.html', re.sub(r'<title>.*?</title>', f'<title>{n} mobile preview</title>', t))
t = wm.replace('<dc-import name="CR-CRED-002" variant="badge"', '<dc-import name="CR-VAL-MC-001"')
wr('CR-VAL-MC-001-Mobile.dc.html', re.sub(r'<title>.*?</title>', '<title>CR-VAL-MC-001 mobile preview</title>', mob(t, 1000)))
print('build20 ok')
