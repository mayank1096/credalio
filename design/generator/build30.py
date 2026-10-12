# build30: CR-LRN-002 learner detail, CR-ANA (variants overview / export = ANA-001 / 004), CR-ANX experience analytics
# (variants course / cert = ANA-002 / 002c). Studio pages via build17 page(). Charts: single-series cobalt, hover values.
# usage: python3 build30.py <canvas project dir>
import re, sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build17 as B
from tipx import tip, TIP_CSS
P, rd, wr, ic, I, ARR = B.P, B.rd, B.wr, B.ic, B.I, B.ARR
CHK = ic('<path d="m5 12.5 4.5 4.5L19 7.5"></path>', 12, 3)
BACK = ic('<path d="M19 12H5"></path><path d="m11 6-6 6 6 6"></path>', 16, 2.2)
CHEVD = ic('<path d="m6 9 6 6 6-6"></path>', 15, 2.2)
CHEV = ic('<path d="m9 6 6 6-6 6"></path>', 16, 2.2)
DL = ic('<path d="M12 4v11"></path><path d="m7 10 5 5 5-5"></path><path d="M5 20h14"></path>', 16, 2.1)
X = ic('<path d="M6 6l12 12M18 6 6 18"></path>', 17, 2.2)
NOVA_BG = '/_blob/d268046654a4206d2a726e62005bcc59'
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
.h2c{margin:0;font-size:17px;font-weight:600}
.kpi{display:grid;grid-template-columns:repeat(4,1fr);padding:22px 0}
.kpi > div{display:flex;flex-direction:column;gap:8px;padding:0 28px}
.kpi > div + div{border-left:1.5px solid #F0F2F8}
.kpi .hp-lab{display:flex;align-items:center}
.kpi b{font-size:26px;font-weight:600;letter-spacing:-0.02em;font-variant-numeric:tabular-nums}
.kpi em{font-style:normal;font-size:13px;font-weight:500;color:#0F6B45;margin-left:8px;letter-spacing:0}
.kpi em.dn{color:#9A5B00}
.bar{display:block;height:6px;border-radius:6px;background:#E6EAF3;overflow:hidden}.bar i{display:block;height:100%;border-radius:6px;background:#1652F0}
.rb-ic{gap:8px}.rb-ic svg{color:#5B6582}
@media (max-width: 960px){
.pg-back{margin-top:12px}
.kpi{grid-template-columns:1fr 1fr;padding:6px 0}
.kpi > div{padding:14px 18px}
.kpi > div + div{border-left:0}
.kpi > div:nth-child(even){border-left:1.5px solid #F0F2F8}.kpi > div:nth-child(n+3){border-top:1.5px solid #F0F2F8}
.kpi b{font-size:20px}.kpi em{display:block;margin:4px 0 0 0}
}
'''

# ======================= CR-LRN-002 · learner detail =======================
CH = [('Getting started', 'dn'), ('Selecting data', 'dn'), ('Joining tables', 'dn'), ('Grouping & aggregates', 'now'), ('Window functions', ''), ('Capstone', '')]
chs = ''.join(f'<li class="{c}"><i>' + (CHK if c == 'dn' else '') + f'</i><span>{t}</span></li>' for t, c in CH)
AS = [('Quiz 1 · Selecting data', '92%', 'gr'), ('Quiz 2 · Joins', '78%', 'gr'), ('Final assessment', 'Not started', 'gy')]
ass = ''.join(f'<li><span>{t}</span><span class="st {c}">{s}</span></li>' for t, s, c in AS)
main = ('<main class="ds-main hp">\n<a href="CR-LRN-001.dc.html" class="pg-back">' + BACK + 'Learners</a>'
        '<div class="hp-head ld-head ob-in"><div class="ld-id"><span class="av ld-av">ME</span><div><h1 class="ds-h1">Mary E.' + tip('You only see what helps you support Mary in your learning experiences. Never her payments, other courses or private AI Coach chats.') + '</h1>'
        '<span class="ld-sub">Learning with you since 2 Sep 2026 · last active 12 min ago</span></div></div>'
        '<a href="CR-SUP-002.dc.html" class="ds-btn hp-btn"><span>Message Mary</span><span class="ob-arrow">' + ARR + '</span></a></div>'
        '<div class="ld-g">'
        '<section class="ds-card ld-card ob-in2" aria-labelledby="ld-h1"><div class="ld-ch"><div><h2 id="ld-h1" class="h2c">Data Analysis with SQL</h2><span class="ld-cs">Now on Lesson 4.2 · Grouping</span></div><b class="ld-pc">62%</b></div>'
        '<span class="bar ld-bar"><i style="width:62%"></i></span>'
        '<ol class="ld-path">' + chs + '</ol>'
        '<h3 class="hp-lab ld-lab">Assessments</h3><ul class="ld-as">' + ass + '</ul></section>'
        '<aside class="ld-side ob-in3">'
        '<section class="ds-card ld-mini"><span class="hp-lab">With you</span>'
        '<a href="CR-SUP-002.dc.html" class="ld-row"><span><b>Learner Support</b><span>1 open conversation</span></span><span class="st am">Waiting</span></a>'
        '<a href="CR-DISC-001.dc.html" class="ld-row"><span><b>Discussions</b><span>3 posts · last 2 days ago</span></span>' + CHEV + '</a></section>'
        '</aside></div>\n</main>')
css = COMMON + '''
.ld-head{align-items:center}
.ld-id{display:flex;align-items:center;gap:18px}
.ld-av{width:60px;height:60px;font-size:18px}
.ld-sub{display:block;margin-top:6px;font-size:14px;color:#5B6582}
.ld-g{display:grid;grid-template-columns:minmax(0,1fr) 340px;gap:20px;align-items:start}
.ld-card{padding:26px 28px}
.ld-ch{display:flex;align-items:flex-end;justify-content:space-between;gap:16px}
.ld-cs{display:block;margin-top:6px;font-size:14px;color:#5B6582}
.ld-pc{font-size:28px;font-weight:600;letter-spacing:-0.02em}
.ld-bar{margin-top:14px;height:8px}
.ld-path{list-style:none;margin:26px 0 0 0;padding:0;display:grid;grid-template-columns:repeat(6,1fr);gap:10px}
.ld-path li{display:flex;flex-direction:column;gap:10px;font-size:13px;color:#5B6582;line-height:1.35}
.ld-path i{width:22px;height:22px;border-radius:50%;border:2px solid #CBD3E6;box-sizing:border-box;display:flex;align-items:center;justify-content:center;color:#FFFFFF}
.ld-path li.dn i{background:#1652F0;border-color:#1652F0}.ld-path li.dn span{color:#0B1433}
.ld-path li.now i{border-color:#1652F0;box-shadow:0 0 0 4px rgba(22,82,240,.14)}.ld-path li.now span{color:#0B1433;font-weight:600}
.ld-lab{margin:30px 0 6px 0}
.ld-as{list-style:none;margin:0;padding:0}
.ld-as li{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:14px 0;border-top:1.5px solid #F0F2F8;font-size:14.5px}
.ld-as li:first-child{border-top:0}
.ld-mini{padding:20px 22px 10px 22px}
.ld-row{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:14px 0;border-top:1.5px solid #F0F2F8;color:#0B1433;text-decoration:none}
.ld-mini .hp-lab + .ld-row{border-top:0;margin-top:4px}
.ld-row > span:first-child{display:flex;flex-direction:column;gap:2px}.ld-row b{font-size:14.5px;font-weight:600}.ld-row > span > span{font-size:13px;color:#5B6582}
.ld-row svg{color:#8A93AD}
@media (max-width: 1080px){.ld-g{grid-template-columns:minmax(0,1fr)}}
@media (max-width: 960px){
.ld-head{flex-direction:column;align-items:stretch;gap:18px}
.ld-av{width:48px;height:48px;font-size:15px}
.ld-head .hp-btn{width:100%;justify-content:space-between}
.ld-card{padding:20px 18px}
.ld-pc{font-size:22px}
.ld-path{grid-template-columns:1fr;gap:12px}
.ld-path li{flex-direction:row;align-items:center;gap:12px;font-size:14px}
}
'''
B.page('CR-LRN-002', 'Learners', main, NAVJS, css, 'Credalio · Mary E.', "{ nav: false }")
wrap('CR-LRN-002', [('CR-LRN-002', '', 1060)])

# ======================= CR-ANA · overview (+ export dialog) =======================
VALS = [618, 640, 655, 649, 672, 690, 701, 688, 705, 722, 736, 741, 729, 748, 760, 774, 769, 782, 790, 803, 798, 812, 820, 815, 826, 831, 838, 829, 836, 842]
W, H, PADY = 1000, 220, 14
lo, hi = 560, 880
xs = [i * W / (len(VALS) - 1) for i in range(len(VALS))]
ys = [PADY + (H - 2 * PADY) * (1 - (v - lo) / (hi - lo)) for v in VALS]
line = 'M' + ' L'.join(f'{x:.1f},{y:.1f}' for x, y in zip(xs, ys))
area = line + f' L{W},{H} L0,{H} Z'
days = [f'{d} Sep' if d <= 30 else '' for d in range(14, 14 + 30)]
def lab(i):
    d = 14 + i
    return f'{d} Sep' if d <= 30 else f'{d - 30} Oct'
grid_y = ''.join(f'<line x1="0" x2="{W}" y1="{PADY + (H - 2 * PADY) * (1 - (g - lo) / (hi - lo)):.1f}" y2="{PADY + (H - 2 * PADY) * (1 - (g - lo) / (hi - lo)):.1f}"></line>' for g in (600, 700, 800))
ylab = ''.join(f'<span style="top:{(PADY + (H - 2 * PADY) * (1 - (g - lo) / (hi - lo))) / H * 100:.2f}%">{g}</span>' for g in (600, 700, 800))
pts = ''.join(f'<div class="ch-pt" style="left:{x / W * 100:.3f}%"><i style="top:{y / H * 100:.2f}%"></i><span class="ch-tt" style="top:{y / H * 100:.2f}%"><b>{v}</b> active · {lab(i)}</span></div>' for i, (x, y, v) in enumerate(zip(xs, ys, VALS)))
CHART = ('<div class="ch"><div class="ch-y">' + ylab + '</div><div class="ch-plot"><svg viewBox="0 0 1000 220" preserveAspectRatio="none" aria-hidden="true">'
         '<defs><linearGradient id="chg" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#1652F0" stop-opacity=".16"></stop><stop offset="1" stop-color="#1652F0" stop-opacity="0"></stop></linearGradient></defs>'
         '<g class="ch-grid">' + grid_y + '</g><path d="' + area + '" fill="url(#chg)"></path><path d="' + line + '" class="ch-line" vector-effect="non-scaling-stroke"></path></svg>'
         '<div class="ch-pts">' + pts + '</div></div>'
         '<div class="ch-x"><span>14 Sep</span><span>21 Sep</span><span>28 Sep</span><span>5 Oct</span><span>13 Oct</span></div></div>')
EXP = [('Data Analysis with SQL', '1,284', 68, '4.8', '$1,410'), ('Certified Data Analyst', '312', 71, '4.6', '$780'), ('Advanced SQL for Analysts', '428', 59, '4.7', '$430'), ('Applied AI Program', '186', 44, '4.5', '$230')]
erows = ''.join(f'<li><a href="{"CR-ANA-002c.dc.html" if "Certified" in n else "CR-ANA-002.dc.html"}" class="ae-r"><b class="ae-n">{n}</b><span class="ae-c">{l}</span>'
                f'<span class="ae-p"><span class="bar"><i style="width:{c}%"></i></span><em>{c}%</em></span><span class="ae-c">{r}</span><span class="ae-c ae-e">{e}</span>{CHEV}</a></li>' for n, l, c, r, e in EXP)
RANGE = '<button type="button" class="hp-rb rb-ic">' + ic(I['cal'], 15, 2) + 'Last 30 days' + CHEVD + '</button>'
overview = ('<div class="hp-head ob-in"><div><h1 class="ds-h1">Analytics</h1></div><div class="an-acts">' + RANGE + '<a href="CR-ANA-004.dc.html" class="hp-rb rb-ic an-ex">' + DL + 'Export</a></div></div>'
            '<section class="ds-card kpi ob-in2" aria-label="Last 30 days">'
            '<div><span class="hp-lab">Active learners' + tip('Learners who opened a lesson or assessment in the last 30 days.') + '</span><b>842<em>+6%</em></b></div>'
            '<div><span class="hp-lab">Completion</span><b>64%<em>+2 pts</em></b></div>'
            '<div><span class="hp-lab">Rating</span><b>4.7</b></div>'
            '<div><span class="hp-lab">Earned</span><b>$2,850<em>+19%</em></b></div></section>'
            '<section class="ds-card an-chart ob-in3" aria-labelledby="an-h1"><div class="an-ch"><h2 id="an-h1" class="h2c">Active learners</h2><span class="an-tbl">Table view</span></div>' + CHART + '</section>'
            '<section class="nova-card an-nova ob-in3"><span class="an-nl">' + ic(I['ai'], 15, 2) + 'Nova noticed</span><p><b>Chapter 4 of Data Analysis with SQL loses more learners than any other.</b> A short practice before Lesson 4.2 usually helps.</p><a href="CR-ANA-002.dc.html" class="hp-rb">See where</a></section>'
            '<section class="ds-card ae ob-in3" aria-labelledby="an-h2"><div class="ae-hd"><h2 id="an-h2" class="h2c">By learning experience</h2></div>'
            '<div class="ae-th"><span>Learning experience</span><span>Learners</span><span>Completion</span><span>Rating</span><span>Earned</span><span></span></div><ul class="ae-l">' + erows + '</ul></section>')
REP = [('Overview', 'Learners, completion, ratings and earnings', True), ('Learners', 'One row per learner and experience', False), ('Earnings', 'One row per sale and payout', False)]
reps = ''.join(f'<button type="button" class="ex-o {"on" if on else ""}"><span><b>{t}</b><span>{d}</span></span>' + (f'<i class="ex-ck">{CHK}</i>' if on else '') + '</button>' for t, d, on in REP)
export = ('<sc-if value="{{vExport}}" hint-placeholder-val="{{false}}"><div class="ex-wrap"><div class="ex-dim"></div><section class="ex-dlg" role="dialog" aria-labelledby="ex-h">'
          '<div class="ex-hd"><h2 id="ex-h" class="ex-h">Export a report</h2><a href="CR-ANA-001.dc.html" class="ex-x" aria-label="Close">' + X + '</a></div>'
          '<div class="ex-os">' + reps + '</div>'
          '<div class="ex-f"><label class="ex-fl"><span>Dates</span><span class="ex-in">Last 30 days' + CHEVD + '</span></label><label class="ex-fl"><span>Learning experiences</span><span class="ex-in">All 4' + CHEVD + '</span></label></div>'
          '<div class="ex-ft"><span class="ex-note">CSV' + tip('Learner names are replaced with IDs. Opens in Excel, Numbers or Google Sheets.', 'dn') + '</span><a href="#" class="ds-btn hp-btn"><span>Download</span><span class="ob-arrow">' + ARR + '</span></a></div>'
          '</section></div></sc-if>')
main = '<main class="ds-main hp">\n' + overview + export + '\n</main>'
js = '''    const v = props.variant || 'overview';
    return { navCls: S.nav ? 'ds-open' : '', toggleNav: () => this.setState({ nav: !S.nav }), vExport: v === 'export' };'''
CHART_CSS = '''
.ch{display:grid;grid-template-columns:40px 1fr;grid-template-rows:auto auto;column-gap:10px}
.ch-y{position:relative}
.ch-y span{position:absolute;right:0;transform:translateY(-50%);font-size:12px;color:#8A93AD;font-variant-numeric:tabular-nums}
.ch-plot{position:relative;height:240px}
.ch-plot svg{position:absolute;inset:0;width:100%;height:100%;overflow:visible}
.ch-grid line{stroke:#EEF1F7;stroke-width:1}
.ch-line{fill:none;stroke:#1652F0;stroke-width:2;stroke-linejoin:round;stroke-linecap:round}
.ch-pts{position:absolute;inset:0}
.ch-pt{position:absolute;top:0;bottom:0;width:3.4%;transform:translateX(-50%);cursor:crosshair}
.ch-pt::before{content:"";position:absolute;left:50%;top:0;bottom:0;border-left:1px dashed #AFC1F5;opacity:0}
.ch-pt i{position:absolute;left:50%;width:10px;height:10px;margin:-5px 0 0 -5px;border-radius:50%;background:#1652F0;box-shadow:0 0 0 2px #FFFFFF;opacity:0}
.ch-tt{position:absolute;left:50%;transform:translate(-50%,calc(-100% - 14px));padding:6px 10px;border-radius:10px;background:#0B1433;color:#FFFFFF;font-size:12px;white-space:nowrap;opacity:0;pointer-events:none;z-index:3}
.ch-tt b{font-weight:600}
.ch-pt:hover::before,.ch-pt:hover i,.ch-pt:hover .ch-tt{opacity:1}
.ch-pt:last-child i{opacity:1}
.ch-x{grid-column:2;display:flex;justify-content:space-between;margin-top:10px;font-size:12px;color:#8A93AD}
'''
css = COMMON + CHART_CSS + '''
.an-acts{display:flex;gap:10px}
.an-chart{margin-top:20px;padding:22px 26px 18px 18px}
.an-ch{display:flex;align-items:center;justify-content:space-between;padding:0 0 18px 8px}
.an-tbl{font-size:13.5px;font-weight:600;color:#1652F0}
.an-nova{margin-top:20px;display:flex;align-items:center;gap:18px;padding:18px 22px;border-radius:20px;background:#EAF0FF url(''' + NOVA_BG + ''') center/cover no-repeat}
.an-nl{display:inline-flex;align-items:center;gap:6px;flex-shrink:0;font-size:13px;font-weight:600;color:#0E3BB8}
.an-nova p{flex:1;margin:0;font-size:14.5px;line-height:1.5;color:#1E2742}.an-nova p b{font-weight:600}
.an-nova .hp-rb{background:#FFFFFF}
.ae{margin-top:20px;padding:22px 16px 8px 16px}
.ae-hd{padding:0 12px 10px 12px}
.ae-th,.ae-r{display:grid;grid-template-columns:minmax(0,2fr) 90px minmax(0,1.3fr) 70px 90px 20px;align-items:center;gap:18px;padding:0 12px}
.ae-th{padding-top:8px;padding-bottom:10px;font-size:12.5px;font-weight:500;color:#8A93AD}
.ae-l{list-style:none;margin:0;padding:0}.ae-l li{border-top:1.5px solid #F0F2F8}
.ae-r{padding:16px 12px;border-radius:14px;color:#0B1433;text-decoration:none}
.ae-r:hover{background:#F7F9FD}
.ae-n{font-size:15px;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.ae-c{font-size:14.5px;font-variant-numeric:tabular-nums}.ae-e{font-weight:600}
.ae-p{display:flex;align-items:center;gap:10px}.ae-p .bar{flex:1;max-width:140px}.ae-p em{font-style:normal;font-size:14px;font-weight:600;font-variant-numeric:tabular-nums}
.ae-r > svg{color:#8A93AD}
/* export dialog */
.ex-wrap{position:fixed;inset:0;z-index:40;display:flex;align-items:center;justify-content:center;padding:24px}
.ex-dim{position:absolute;inset:0;background:rgba(11,20,51,.36)}
.ex-dlg{position:relative;width:520px;max-width:100%;padding:24px 26px;border-radius:24px;background:#FFFFFF;box-shadow:0 30px 80px rgba(11,20,51,.25)}
.ex-hd{display:flex;align-items:center;justify-content:space-between}
.ex-h{margin:0;font-size:20px;font-weight:600}
.ex-x{width:34px;height:34px;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;color:#5B6582;margin-right:-6px}
.ex-os{margin-top:20px;display:flex;flex-direction:column;gap:10px}
.ex-o{position:relative;display:flex;align-items:center;padding:14px 48px 14px 16px;border-radius:16px;border:1.5px solid #E6EAF3;background:#FFFFFF;font-family:inherit;text-align:left;color:#0B1433;cursor:pointer}
.ex-o > span{display:flex;flex-direction:column;gap:2px}.ex-o b{font-size:15px;font-weight:600}.ex-o > span > span{font-size:13.5px;color:#5B6582}
.ex-o.on{border-color:#1652F0;background:#F5F8FF;box-shadow:0 0 0 4px rgba(22,82,240,.10)}
.ex-ck{position:absolute;right:16px;top:50%;margin-top:-10px;width:20px;height:20px;border-radius:50%;background:#1652F0;color:#FFFFFF;display:inline-flex;align-items:center;justify-content:center}
.ex-f{margin-top:20px;display:grid;grid-template-columns:1fr 1fr;gap:12px}
.ex-fl{display:flex;flex-direction:column;gap:7px}.ex-fl > span:first-child{font-size:13.5px;font-weight:500;color:#4A5578}
.ex-in{display:flex;align-items:center;justify-content:space-between;height:46px;padding:0 14px;border-radius:12px;border:1.5px solid #D6DDEE;font-size:14.5px}.ex-in svg{color:#8A93AD}
.ex-ft{margin-top:24px;padding-top:18px;border-top:1.5px solid #F0F2F8;display:flex;align-items:center;justify-content:space-between}
.ex-note{display:inline-flex;align-items:center;font-size:14px;font-weight:500;color:#5B6582}
@media (max-width: 960px){
.hp-head{flex-direction:row;align-items:center}
.an-acts .rb-ic{display:inline-flex !important;height:36px;padding:0 12px;font-size:13px}
.an-ex{width:36px;padding:0 !important;justify-content:center;font-size:0 !important;gap:0}
.an-chart{padding:16px 14px 14px 6px}
.an-ch{padding:0 0 12px 10px}
.ch{grid-template-columns:32px 1fr;column-gap:6px}
.ch-plot{height:180px}
.ch-x span:nth-child(2),.ch-x span:nth-child(4){display:none}
.an-nova{flex-direction:column;align-items:flex-start;gap:10px;padding:16px 18px}
.ae{padding:16px 6px 4px 6px}
.ae-th{display:none}
.ae-r{grid-template-columns:minmax(0,1fr) auto;gap:8px 12px;padding:14px 10px}
.ae-r > .ae-c:not(.ae-e),.ae-r > svg{display:none}
.ae-p{grid-column:1 / -1;grid-row:2}
.ae-e{grid-row:1;grid-column:2}
.ex-wrap{align-items:flex-end;padding:0}
.ex-dlg{width:100%;border-radius:24px 24px 0 0;padding:22px 18px 26px 18px}
.ex-f{grid-template-columns:1fr}
.ex-ft .hp-btn{flex:1;justify-content:space-between;margin-left:16px}
}
'''
B.page('CR-ANA', 'Analytics', main, js, css, 'Credalio · Analytics', "{ nav: false }")
props_patch('CR-ANA')
wrap('CR-ANA', [('CR-ANA-001', 'overview', 1320), ('CR-ANA-004', 'export', 844)])

# ======================= CR-ANX · experience analytics =======================
FUN = [('1 · Getting started', 100), ('2 · Selecting data', 91), ('3 · Joining tables', 83), ('4 · Grouping & aggregates', 64), ('5 · Window functions', 58), ('6 · Capstone', 54)]
fun = ''.join(f'<li class="{"big" if n.startswith("4") else ""}"><span class="fu-n">{n}</span><span class="fu-b"><i style="width:{p}%"></i></span><b>{p}%</b>'
              + ('<span class="fu-flag">Biggest drop' + tip('19 points fewer learners reach Chapter 4 than finish Chapter 3.', 'r') + '</span>' if n.startswith('4') else '<span class="fu-flag"></span>') + '</li>' for n, p in FUN)
ASM = [('Quiz 1 · Selecting data', '86%', '94%'), ('Quiz 2 · Joins', '74%', '81%'), ('Final assessment', '79%', '76%')]
asm = ''.join(f'<li><span>{t}</span><b>{a}</b><b>{p}</b></li>' for t, a, p in ASM)
BINS = [(40, 2), (45, 4), (50, 7), (55, 11), (60, 19), (65, 28), (70, 41), (75, 52), (80, 47), (85, 38), (90, 27), (95, 12)]
mx = max(c for _, c in BINS)
hist = ''.join(f'<div class="hi-b {"lo" if b < 70 else ""}"><i style="height:{c / mx * 100:.1f}%"><span class="ch-tt2">{b}–{b + 4}: <b>{c}</b></span></i><em>{b}</em></div>' for b, c in BINS)
DOM = [('Data cleaning', 82), ('SQL', 77), ('Visualisation', 69), ('Statistics', 61)]
dom = ''.join(f'<li><span class="fu-n">{n}</span><span class="fu-b"><i style="width:{p}%"></i></span><b>{p}%</b></li>' for n, p in DOM)
course = ('<sc-if value="{{vCourse}}" hint-placeholder-val="{{true}}"><a href="CR-ANA-001.dc.html" class="pg-back">' + BACK + 'Analytics</a>'
          '<div class="hp-head ob-in"><div><h1 class="ds-h1">Data Analysis with SQL</h1></div><div class="an-acts">' + RANGE + '</div></div>'
          '<section class="ds-card kpi ob-in2"><div><span class="hp-lab">Learners</span><b>1,284</b></div><div><span class="hp-lab">Completion</span><b>68%</b></div>'
          '<div><span class="hp-lab">Average quiz score</span><b>81%</b></div><div><span class="hp-lab">Rating</span><b>4.8</b></div></section>'
          '<div class="ax-g"><section class="ds-card ax-c ob-in3" aria-labelledby="ax-h1"><h2 id="ax-h1" class="h2c">How far learners get' + tip('Share of enrolled learners who reached each chapter.') + '</h2><ol class="fu">' + fun + '</ol></section>'
          '<section class="ds-card ax-c ob-in3" aria-labelledby="ax-h2"><h2 id="ax-h2" class="h2c">Assessments</h2><div class="as-th"><span></span><span>Average</span><span>Pass rate</span></div><ul class="as-l">' + asm + '</ul></section></div></sc-if>')
cert = ('<sc-if value="{{vCert}}" hint-placeholder-val="{{false}}"><a href="CR-ANA-001.dc.html" class="pg-back">' + BACK + 'Analytics</a>'
        '<div class="hp-head ob-in"><div><h1 class="ds-h1">Certified Data Analyst</h1></div><div class="an-acts">' + RANGE + '</div></div>'
        '<section class="ds-card kpi ob-in2"><div><span class="hp-lab">Candidates</span><b>312</b></div><div><span class="hp-lab">Pass rate</span><b>71%</b></div>'
        '<div><span class="hp-lab">Average score</span><b>76%</b></div><div><span class="hp-lab">Certificates issued</span><b>198</b></div></section>'
        '<div class="ax-g"><section class="ds-card ax-c ob-in3" aria-labelledby="ax-h3"><h2 id="ax-h3" class="h2c">Exam scores' + tip('Pass mark is 70%. Lighter bars fell short.') + '</h2>'
        '<div class="hi"><div class="hi-pass" style="left:calc(100% / 12 * 6)"><span>Pass 70%</span></div>' + hist + '</div></section>'
        '<section class="ds-card ax-c ob-in3" aria-labelledby="ax-h4"><h2 id="ax-h4" class="h2c">By skill area</h2><ol class="fu fu-sm">' + dom + '</ol></section></div></sc-if>')
main = '<main class="ds-main hp">\n' + course + cert + '\n</main>'
js = '''    const v = props.variant || 'course';
    return { navCls: S.nav ? 'ds-open' : '', toggleNav: () => this.setState({ nav: !S.nav }), vCourse: v === 'course', vCert: v === 'cert' };'''
css = COMMON + '''
.an-acts{display:flex;gap:10px}
.ax-g{margin-top:20px;display:grid;grid-template-columns:minmax(0,1.5fr) minmax(0,1fr);gap:20px;align-items:start}
.ax-c{padding:24px 26px}
.ax-c .h2c{display:flex;align-items:center}
.fu{list-style:none;margin:18px 0 0 0;padding:0;display:flex;flex-direction:column;gap:6px}
.fu li{display:grid;grid-template-columns:minmax(0,180px) minmax(0,1fr) 46px 110px;align-items:center;gap:14px;padding:8px 0}
.fu-sm li{grid-template-columns:minmax(0,130px) minmax(0,1fr) 46px}
.fu-n{font-size:14px;color:#3A4566;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.fu li.big .fu-n{color:#0B1433;font-weight:600}
.fu-b{display:block;height:12px;border-radius:4px;background:#F1F3F8;overflow:hidden}.fu-b i{display:block;height:100%;border-radius:4px;background:#1652F0}
.fu li b{font-size:14px;font-weight:600;font-variant-numeric:tabular-nums;text-align:right}
.fu-flag{display:inline-flex;align-items:center;font-size:12.5px;font-weight:500;color:#9A5B00}
.as-th,.as-l li{display:grid;grid-template-columns:minmax(0,1fr) 72px 80px;gap:12px;align-items:center}
.as-th{margin-top:16px;padding-bottom:8px;font-size:12.5px;font-weight:500;color:#8A93AD}.as-th span{text-align:right}
.as-l{list-style:none;margin:0;padding:0}.as-l li{padding:14px 0;border-top:1.5px solid #F0F2F8;font-size:14.5px}
.as-l b{text-align:right;font-weight:600;font-variant-numeric:tabular-nums}
.hi{position:relative;margin-top:44px;height:220px;display:grid;grid-template-columns:repeat(12,1fr);gap:2px;align-items:end;padding-bottom:24px;border-bottom:1.5px solid #E6EAF3}
.hi-b{position:relative;height:100%;display:flex;align-items:flex-end}
.hi-b i{position:relative;display:block;width:100%;border-radius:4px 4px 0 0;background:#1652F0;cursor:crosshair}
.hi-b.lo i{background:#AFC1F5}
.hi-b em{position:absolute;bottom:-22px;left:0;font-style:normal;font-size:11.5px;color:#8A93AD}
.ch-tt2{position:absolute;left:50%;bottom:calc(100% + 8px);transform:translateX(-50%);padding:5px 9px;border-radius:9px;background:#0B1433;color:#FFFFFF;font-size:12px;white-space:nowrap;opacity:0;pointer-events:none;z-index:3}
.hi-b i:hover .ch-tt2{opacity:1}
.hi-pass{position:absolute;top:-6px;bottom:24px;border-left:1.5px dashed #0B1433;z-index:2}
.hi-pass span{position:absolute;top:-26px;left:-30px;font-size:12px;font-weight:600;white-space:nowrap}
@media (max-width: 1080px){.ax-g{grid-template-columns:minmax(0,1fr)}}
@media (max-width: 960px){
.hp-head{flex-direction:column;align-items:stretch;gap:12px}
.an-acts .rb-ic{display:inline-flex !important;height:36px;padding:0 12px;font-size:13px;align-self:flex-start}
.ax-g{gap:14px;margin-top:14px}
.ax-c{padding:18px 16px}
.fu li{grid-template-columns:minmax(0,1fr) 40px;gap:6px 10px;padding:6px 0}
.fu-n{grid-column:1 / -1}
.fu-b{grid-column:1}
.fu-flag{grid-column:1 / -1}.fu li:not(.big) .fu-flag{display:none}
.fu-sm li{grid-template-columns:minmax(0,1fr) 40px}
.hi{height:180px}
.hi-b em{font-size:10px}
.hi-b:nth-child(odd) em{display:none}
}
'''
B.page('CR-ANX', 'Analytics', main, js, css, 'Credalio · Analytics', "{ nav: false }")
props_patch('CR-ANX')
wrap('CR-ANX', [('CR-ANA-002', 'course', 1100), ('CR-ANA-002c', 'cert', 1000)])
print('build30 ok')
