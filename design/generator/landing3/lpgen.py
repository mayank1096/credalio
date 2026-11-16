"""Landing batch 3 (client review): COURSES-003 free lesson preview, opened from "Preview lesson 1" and the
free-preview lessons in the curriculum. One responsive source, prop kind = video | reading.
Focus mode: slim bar (back to the course, title, start), the lesson, the course content beside it (free lessons
open, the rest locked), and a clear way out. Usage: python3 lpgen.py <canvas3/project>"""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kit
from kit import tip, ck, nova_av, ARROW
D = sys.argv[1]

def svg(d, w=18, sw=2):
    return '<svg width="%d" height="%d" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="%s" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>' % (w, w, sw, d)
BACK = svg('<path d="M19 12H5"></path><path d="m11 18-6-6 6-6"></path>', 18, 2.2)
PLAY = '<svg width="26" height="26" viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5.5v13l11-6.5z" fill="currentColor"></path></svg>'
LOCK = svg('<rect x="5" y="11" width="14" height="9" rx="2.2"></rect><path d="M8 11V8a4 4 0 0 1 8 0v3"></path>', 15, 2)
VID = svg('<rect x="3" y="5" width="18" height="14" rx="3"></rect><path d="m10 9 5 3-5 3z"></path>', 15, 2)
DOC = svg('<path d="M5 4h10l4 4v12H5z"></path><path d="M9 12h6M9 16h6"></path>', 15, 2)
CODE = svg('<path d="m8 9-4 3 4 3M16 9l4 3-4 3"></path>', 15, 2)
QZ = svg('<circle cx="12" cy="12" r="9"></circle><path d="M12 17h.01M9.5 9.5a2.5 2.5 0 1 1 3.5 2.3c-.6.3-1 .8-1 1.5"></path>', 15, 2)
CHEV = svg('<path d="m6 9 6 6 6-6"></path>', 16, 2.2)
FULL = svg('<path d="M4 9V4h5M20 9V4h-5M4 15v5h5M20 15v5h-5"></path>', 16, 2)
VOL = svg('<path d="M4 9h4l5-4v14l-5-4H4z"></path><path d="M17 9a4 4 0 0 1 0 6"></path>', 16, 2)

MODS = [('Working with spreadsheet data', [('Why data skills matter', 'Video · 6 min', VID, 'video'), ('Structuring a clean table', 'Reading · 8 min', DOC, 'reading'),
                                           ('Sorting and filtering', 'Practice · 15 min', CODE, ''), ('Module check', 'Quiz · 5 min', QZ, '')]),
        ('Cleaning messy data', 4), ('Your first SQL queries', 4), ('Joining tables with SQL', 4), ('Summarising with aggregation', 4), ('Project and final assessment', 4)]
def rail():
    m1, ls = MODS[0]
    rows = ''
    for t, meta, icon, kind in ls:
        if kind:
            rows += ('<a class="lp-l {{cur_%s}}" href="%s"><span class="lp-li">%s</span><span class="lp-lt"><b>%s</b><em>%s</em></span><span class="lp-free">{{tag_%s}}</span></a>') % (
                kind, 'LessonPreview.dc.html' if kind == 'video' else 'LessonPreview-Reading.dc.html', icon, t, meta, kind)
        else:
            rows += '<div class="lp-l lp-lock"><span class="lp-li">%s</span><span class="lp-lt"><b>%s</b><em>%s</em></span><span class="lp-lk" aria-label="Locked">%s</span></div>' % (icon, t, meta, LOCK)
    more = ''.join('<div class="lp-m lp-lock"><span class="lp-mn">%d</span><span class="lp-lt"><b>%s</b><em>%d lessons</em></span><span class="lp-lk" aria-label="Locked">%s</span></div>' % (i + 2, t, n, LOCK) for i, (t, n) in enumerate(MODS[1:]))
    return ('<aside class="lp-rail" aria-label="Course content"><div class="lp-rh"><b>Course content</b><span>6 modules · 24 lessons · 12 hrs</span></div>'
            '<div class="lp-m on"><span class="lp-mn">1</span><span class="lp-lt"><b>%s</b><em>2 free lessons to try</em></span>%s</div><div class="lp-ls">%s</div>%s</aside>') % (m1, CHEV, rows, more)

TRANS = [('0:00', 'Most of us already work with data every day, in spreadsheets.'), ('0:18', 'The trouble starts when the sheet gets big, or when three people edit it at once.'),
         ('0:41', 'In this course, we’ll keep everything you already know, and add the one skill that scales: SQL.'), ('1:05', 'By the end, you’ll answer a real business question from a sales database.'),
         ('1:32', 'First, let’s look at why clean, well-structured data matters so much.')]
VIDEO = ('<div class="lp-player aur" role="region" aria-label="Video player">'
         '<span class="lp-cap" aria-hidden="true">{{capLine}}</span>'
         '<button class="lp-play" type="button" aria-label="Play video">%s</button>'
         '<div class="lp-ctl"><button class="lp-cb" type="button" aria-label="Play">%s</button><span class="lp-time">1:05 / 6:00</span>'
         '<span class="lp-bar" aria-hidden="true"><i></i></span><button class="lp-cb" type="button" aria-label="Volume">%s</button>'
         '<button class="lp-cc {{ccCls}}" type="button" aria-pressed="{{ccOn}}" onClick="{{toggleCc}}">CC</button><button class="lp-cb" type="button" aria-label="Full screen">%s</button></div></div>'
         '<div class="lp-hd"><span class="lp-k">Module 1 · Video · 6 min</span><h1 class="lp-h1">Why data skills matter</h1>'
         '<p class="lp-d">Why spreadsheets stop scaling, and what you’ll be able to do by the end of the course.</p></div>'
         '<section class="lp-tr" aria-label="Transcript"><div class="lp-trh"><b>Transcript</b><span>Captions and transcript in English</span>'
         '<button class="ds-link" type="button" onClick="{{toggleTr}}">{{trLabel}}</button></div>'
         '<sc-if value="{{trOpen}}" hint-placeholder-val="{{ true }}"><ol class="lp-tl">%s</ol></sc-if></section>') % (
    PLAY, svg('<path d="M8 5.5v13l11-6.5z" fill="currentColor" stroke="none"></path>', 16, 2), VOL, FULL, ''.join('<li class="%s"><time>%s</time><span>%s</span></li>' % ('on' if i == 3 else '', a, b) for i, (a, b) in enumerate(TRANS)))

TABLE = [['order_id', 'date', 'region', 'product', 'amount'], ['1042', '2026-03-02', 'North', 'Desk lamp', '38.00'], ['1043', '2026-03-02', 'South', 'Office chair', '149.00'], ['1044', '2026-03-03', 'North', 'Notebook', '4.50']]
READING = ('<div class="lp-hd"><span class="lp-k">Module 1 · Reading · 8 min</span><h1 class="lp-h1">Structuring a clean table</h1>'
           '<p class="lp-d">One idea per column, one record per row. It sounds simple, and it’s what makes everything after it work.</p></div>'
           '<article class="lp-art"><p>Before you write a single query, look at how your data is laid out. A clean table has a header row, one kind of information in each column, and one record in each row. '
           'No merged cells, no totals hiding in the middle, no notes typed next to the numbers.</p>'
           '<figure class="lp-fig"><figcaption>A clean sales table</figcaption><div class="lp-tbl" role="table" aria-label="A clean sales table">%s</div></figure>'
           '<p>Every column here answers one question: when, where, what, how much. That’s exactly how a database stores data, which is why moving from this sheet to SQL feels natural.</p>'
           '<div class="lp-try"><span class="lp-li">%s</span><div><b>Try it next: Sorting and filtering</b><span>A 15-minute practice task in the SQL editor. Unlocks when you start the course.</span></div><span class="lp-lk">%s</span></div>'
           '<div class="lp-nv nova-card">%s<p><b>Nova, your AI Coach</b> is in every lesson. Ask “why can’t I merge cells?” and get an answer that fits what you’re reading.</p></div>'
           '</article>') % (''.join('<div class="lp-tr2%s" role="row">%s</div>' % (' lp-th' if i == 0 else '', ''.join('<span role="%s">%s</span>' % ('columnheader' if i == 0 else 'cell', c) for c in r)) for i, r in enumerate(TABLE)),
                            CODE, LOCK, nova_av('sm'))

END = ('<div class="lp-end"><div><b>Like what you’ve seen?</b><span>Start the course to open all 24 lessons, the project and your certificate.</span>'
       '<span class="lp-pr"><span class="dlp-c" aria-hidden="true"></span>200 DLP<em>or own it for 400 Credits</em></span></div>'
       '<div class="lp-ea"><a class="ds-btn" href="CourseDetail.dc.html"><span>Start the course</span><span class="ob-arrow">%s</span></a><a class="ds-link" href="CourseDetail.dc.html">Back to the course page</a></div></div>') % ARROW

BODY = '''<div class="lp-root">
<header class="lp-top">
<a class="lp-back" href="CourseDetail.dc.html" aria-label="Back to the course page">%s<span>Back to course</span></a>
<div class="lp-tt"><b>Data Foundations: Spreadsheets to SQL</b><span class="ds-tag blue">Free preview</span></div>
<a class="ds-ghost sm lp-start" href="CourseDetail.dc.html">Start the course</a>
</header>
<div class="lp-grid">
<main class="lp-main">
<sc-if value="{{isVideo}}" hint-placeholder-val="{{ true }}">%s</sc-if>
<sc-if value="{{isReading}}" hint-placeholder-val="{{ false }}">%s</sc-if>
%s
</main>
%s
</div>
<div class="ds-mbar lp-mbar"><a class="ds-btn" href="CourseDetail.dc.html"><span>Start the course</span><span class="ob-arrow">%s</span></a></div>
</div>''' % (BACK, VIDEO, READING, END, rail(), ARROW)

CSS = kit.KIT_CSS + '\n' + kit.AUR_CSS + r'''
body{margin:0}
.lp-root{min-height:100vh;background:#FFFFFF;font-family:'Google Sans',system-ui,sans-serif;color:#0B1433}
.lp-top{position:sticky;top:0;z-index:10;display:flex;align-items:center;gap:20px;height:68px;padding:0 32px;background:rgba(255,255,255,.94);-webkit-backdrop-filter:blur(10px);backdrop-filter:blur(10px);border-bottom:1.5px solid #EEF1F7}
.lp-back{display:inline-flex;align-items:center;gap:8px;height:40px;padding:0 14px 0 10px;margin-left:-10px;border-radius:999px;color:#3A4566;font-size:14.5px;font-weight:500;text-decoration:none}
.lp-back:hover{background:#F5F8FF;color:#0B1433}
.lp-tt{flex:1;min-width:0;display:flex;align-items:center;justify-content:center;gap:10px}
.lp-tt b{font-size:15px;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.lp-start{height:40px;font-size:14px}
.lp-grid{max-width:1360px;margin:0 auto;padding:32px 32px 72px;box-sizing:border-box;display:grid;grid-template-columns:minmax(0,1fr) 360px;gap:40px;align-items:start}
.lp-main{min-width:0;display:flex;flex-direction:column;gap:24px}
.lp-player{position:relative;aspect-ratio:16 / 9;border-radius:22px;display:flex;align-items:center;justify-content:center;color:#FFFFFF}
.lp-play{width:84px;height:84px;border-radius:50%;border:none;background:rgba(255,255,255,.95);color:#1652F0;display:flex;align-items:center;justify-content:center;cursor:pointer;box-shadow:0 18px 40px -12px rgba(0,0,0,.5);transition:transform .2s ease}
.lp-play:hover{transform:scale(1.05)}
.lp-play svg{margin-left:4px}
.lp-cap{position:absolute;left:50%;bottom:76px;transform:translateX(-50%);max-width:78%;padding:6px 12px;border-radius:8px;background:rgba(11,20,51,.72);font-size:15px;line-height:1.4;text-align:center}
.lp-cap:empty{display:none}
.lp-ctl{position:absolute;left:16px;right:16px;bottom:16px;display:flex;align-items:center;gap:12px;padding:8px 12px;border-radius:14px;background:rgba(11,20,51,.55);-webkit-backdrop-filter:blur(8px);backdrop-filter:blur(8px)}
.lp-cb{width:32px;height:32px;border:none;border-radius:8px;background:transparent;color:#FFFFFF;display:flex;align-items:center;justify-content:center;cursor:pointer}
.lp-time{font-size:13px;font-variant-numeric:tabular-nums;color:rgba(255,255,255,.85);white-space:nowrap}
.lp-bar{flex:1;height:4px;border-radius:2px;background:rgba(255,255,255,.25);overflow:hidden}
.lp-bar i{display:block;width:18%;height:100%;background:#FFFFFF}
.lp-cc{height:26px;padding:0 8px;border-radius:6px;border:1.5px solid rgba(255,255,255,.5);background:transparent;color:#FFFFFF;font-family:inherit;font-size:12px;font-weight:600;cursor:pointer}
.lp-cc.on{background:#FFFFFF;color:#0B1433;border-color:#FFFFFF}
.lp-hd{display:flex;flex-direction:column;gap:8px}
.lp-k{font-size:13px;font-weight:500;color:#1652F0}
.lp-h1{margin:0;font-size:32px;line-height:1.15;font-weight:600;letter-spacing:-.8px}
.lp-d{margin:0;font-size:16px;line-height:1.6;color:#4A5578;max-width:720px}
.lp-tr{border:1.5px solid #E6EAF3;border-radius:20px;padding:18px 20px}
.lp-trh{display:flex;align-items:center;gap:12px;flex-wrap:wrap}
.lp-trh b{font-size:16px;font-weight:600}
.lp-trh span{font-size:13px;color:#8A93AD}
.lp-trh .ds-link{margin-left:auto}
.lp-tl{margin:14px 0 0;padding:0;list-style:none;display:flex;flex-direction:column;gap:2px}
.lp-tl li{display:grid;grid-template-columns:52px minmax(0,1fr);gap:12px;padding:8px 10px;border-radius:10px;font-size:14.5px;line-height:1.5;color:#3A4566}
.lp-tl li.on{background:#EAF0FF;color:#0B1433}
.lp-tl time{font-size:13px;font-weight:500;color:#1652F0;font-variant-numeric:tabular-nums}
.lp-art{display:flex;flex-direction:column;gap:20px;max-width:760px}
.lp-art > p{margin:0;font-size:16.5px;line-height:1.75;color:#3A4566}
.lp-fig{margin:0;display:flex;flex-direction:column;gap:10px}
.lp-fig figcaption{font-size:13px;font-weight:500;color:#8A93AD}
.lp-tbl{border:1.5px solid #E6EAF3;border-radius:14px;overflow:hidden;font-size:14px}
.lp-tr2{display:grid;grid-template-columns:.8fr 1.1fr .8fr 1.2fr .8fr}
.lp-tr2 span{padding:10px 14px;border-top:1px solid #EEF1F7;color:#0B1433;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.lp-th span{border-top:none;background:#F5F8FF;font-weight:600;color:#0E3BB8;font-family:ui-monospace,Menlo,monospace;font-size:13px}
.lp-try{display:flex;align-items:center;gap:14px;padding:16px 18px;border-radius:18px;border:1.5px dashed #CBD7F5;background:#FAFBFF}
.lp-try > div{flex:1;display:flex;flex-direction:column;gap:3px}
.lp-try b{font-size:15px;font-weight:600}
.lp-try span{font-size:13.5px;color:#5B6582}
.lp-nv{display:flex;align-items:center;gap:12px;padding:14px 18px;border-radius:18px;border:1.5px solid #DCE5FB}
.lp-nv p{margin:0;font-size:14px;line-height:1.5;color:#3A4566}
.lp-nv b{font-weight:600;color:#0B1433}
.nova-card{background:#FFFFFF url(''' + kit.NOVA_BG + r''') center / cover no-repeat}
.lp-end{display:flex;align-items:center;justify-content:space-between;gap:24px;padding:24px 28px;border-radius:22px;background:linear-gradient(160deg,#F5F8FF,#EAF0FF);border:1.5px solid #DCE5FB}
.lp-end > div:first-child{display:flex;flex-direction:column;gap:6px}
.lp-end b{font-size:20px;font-weight:600;letter-spacing:-.3px}
.lp-end > div > span{font-size:14.5px;color:#4A5578}
.lp-pr{display:inline-flex !important;align-items:center;gap:8px;margin-top:4px;font-size:15px !important;font-weight:600;color:#0B1433 !important}
.lp-pr em{font-style:normal;font-weight:400;color:#5B6582}
.lp-ea{display:flex;flex-direction:column;align-items:center;gap:10px;flex-shrink:0}
.lp-rail{position:sticky;top:92px;border:1.5px solid #E6EAF3;border-radius:22px;overflow:hidden;background:#FFFFFF}
.lp-rh{display:flex;flex-direction:column;gap:2px;padding:18px 20px;border-bottom:1px solid #EEF1F7}
.lp-rh b{font-size:16px;font-weight:600}
.lp-rh span{font-size:13px;color:#8A93AD}
.lp-m{display:flex;align-items:center;gap:12px;padding:14px 20px;border-top:1px solid #EEF1F7}
.lp-m:first-of-type{border-top:none}
.lp-m.on{background:#FAFBFF}
.lp-m.on svg{color:#5B6582;transform:rotate(180deg)}
.lp-mn{width:28px;height:28px;border-radius:9px;background:#F5F8FF;color:#5B6582;font-size:13px;font-weight:600;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.lp-m.on .lp-mn{background:#1652F0;color:#FFFFFF}
.lp-lt{flex:1;min-width:0;display:flex;flex-direction:column;gap:1px}
.lp-lt b{font-size:14px;font-weight:500;color:#0B1433;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.lp-lt em{font-style:normal;font-size:12.5px;color:#8A93AD}
.lp-ls{padding:4px 12px 10px 28px;background:#FAFBFF;display:flex;flex-direction:column;gap:2px}
.lp-l{display:flex;align-items:center;gap:12px;padding:10px 12px;border-radius:12px;text-decoration:none}
a.lp-l:hover{background:#F0F4FF}
.lp-l.cur{background:#EAF0FF}
.lp-l.cur .lp-lt b{color:#0E3BB8;font-weight:600}
.lp-li{width:30px;height:30px;border-radius:9px;background:#FFFFFF;border:1px solid #E6EAF3;color:#1652F0;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.lp-free{font-size:11.5px;font-weight:500;color:#0F6B45;background:#E7F5EE;border-radius:999px;padding:2px 8px;white-space:nowrap}
.lp-lock .lp-li,.lp-lock .lp-mn{color:#8A93AD}
.lp-lock .lp-lt b{color:#5B6582}
.lp-lk{color:#8A93AD;display:flex}
.lp-mbar{display:none}
@media (max-width: 1080px){.lp-grid{grid-template-columns:minmax(0,1fr) 320px;gap:28px}}
@media (max-width: 960px){.lp-grid{grid-template-columns:minmax(0,1fr)}.lp-rail{position:static}}
@media (max-width: 760px){
.lp-top{height:60px;padding:0 12px 0 16px;gap:10px}
.lp-back span,.lp-tt .ds-tag,.lp-start{display:none}
.lp-back{width:44px;height:44px;padding:0;justify-content:center;margin-left:-8px}
.lp-tt{justify-content:flex-start}
.lp-tt b{font-size:14.5px}
.lp-grid{padding:0 0 0;gap:20px}
.lp-main{gap:18px}
.lp-player{border-radius:0}
.lp-play{display:none}
.lp-cap{bottom:58px;font-size:13px}
.lp-ctl{left:8px;right:8px;bottom:8px;gap:6px;padding:4px 6px}
.lp-ctl .lp-cb:nth-of-type(2),.lp-ctl .lp-cb:last-child{display:none}
.lp-hd,.lp-tr,.lp-art,.lp-end{margin:0 16px}
.lp-hd:first-child{margin-top:20px}
.lp-h1{font-size:24px;letter-spacing:-.5px}
.lp-d{font-size:15px}
.lp-tr{padding:14px 14px}
.lp-tl li{grid-template-columns:44px minmax(0,1fr);padding:8px 6px;font-size:14px}
.lp-art > p{font-size:15.5px;line-height:1.7}
.lp-tbl{overflow-x:auto}
.lp-tr2{min-width:520px}
.lp-end{flex-direction:column;align-items:stretch;padding:20px}
.lp-ea{display:none}
.lp-rail{margin:0 16px 8px;border-radius:20px}
.lp-mbar{display:flex;position:sticky;bottom:0;z-index:20;padding:12px 16px;background:#FFFFFF;border-top:1.5px solid #EEF1F7}
.lp-mbar .ds-btn{width:100%;justify-content:space-between}
}
'''
JS = '''class Component extends DCLogic {
''' + kit.AURORA_JS + '''
  componentWillUnmount() { if (this._aurMo) this._aurMo.disconnect(); }
  componentDidMount() { this.aurScan(); }
  constructor(props) { super(props); this.state = { cc: true, tr: true }; }
  renderVals() {
    var self = this, S = this.state, k = this.props.kind === 'reading' ? 'reading' : 'video';
    return {
      isVideo: k === 'video', isReading: k === 'reading',
      cur_video: k === 'video' ? 'cur' : '', cur_reading: k === 'reading' ? 'cur' : '',
      tag_video: k === 'video' ? 'Playing' : 'Free', tag_reading: k === 'reading' ? 'Reading' : 'Free',
      ccOn: S.cc ? 'true' : 'false', ccCls: S.cc ? 'on' : '', toggleCc: function () { self.setState({ cc: !S.cc }); },
      capLine: S.cc ? 'By the end, you’ll answer a real business question from a sales database.' : '',
      trOpen: S.tr, trLabel: S.tr ? 'Hide' : 'Show', toggleTr: function () { self.setState({ tr: !S.tr }); }
    };
  }
}'''
DOC_ = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>COURSES-003 Lesson preview</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500;600;700&amp;display=swap">
<style>
%s
</style>
</helmet>
%s
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{"kind":{"editor":"enum","options":["video","reading"],"default":"video"},"$preview":{"width":1440,"height":1100}}'>
%s
</script>
</body>
</html>
''' % (CSS, BODY, JS)
open(os.path.join(D, 'LessonPreview.dc.html'), 'w').write(DOC_)
print('LessonPreview written')
