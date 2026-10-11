# build28: calendar. CR-CAL one source, variants month / week / event / day / agenda (= CAL-001 / 001w / 002 / 001d / 001a)
# and CR-CAL-003 weekly availability. Studio pages via build17 page(). Sample "now" = Tue 13 Oct 2026, 09:52 WAT.
# usage: python3 build28.py <canvas project dir>
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build17 as B
from tipx import tip, TIP_CSS
P, rd, wr, ic, I, ARR = B.P, B.rd, B.wr, B.ic, B.I, B.ARR
BACK = ic('<path d="M19 12H5"></path><path d="m11 6-6 6 6 6"></path>', 16, 2.2)
CLOCK = ic('<circle cx="12" cy="12" r="9"></circle><path d="M12 7v5l3 2"></path>', 17, 2)
VID = ic('<rect x="3" y="6" width="13" height="12" rx="3"></rect><path d="m16 10 5-3v10l-5-3"></path>', 17, 2)
X = ic('<path d="M6 6l12 12M18 6 6 18"></path>', 17, 2.2)
PLUS = ic('<path d="M12 5v14M5 12h14"></path>', 16, 2.2)
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
.st.cb{background:#EAF0FF;color:#0E3BB8}.st.gy{background:#F1F3F8;color:#5B6582}
.av{width:36px;height:36px;border-radius:50%;background:#EAF0FF;color:#0E3BB8;display:inline-flex;align-items:center;justify-content:center;font-size:12.5px;font-weight:600;flex-shrink:0}
.av.me{background:#0B1433;color:#FFFFFF}
@media (max-width: 960px){.pg-back{margin-top:12px}}
'''

# ---------- data ----------
EVM = {5: [('cb', '18:00 Live class')], 7: [('ol', '10:00 Validation call')], 13: [('ol', '10:00 Validation call'), ('cb', '18:00 Live class')], 14: [('gy', 'Office hours')],
       19: [('cb', '18:00 Live class'), ('ol', '15:00 Team sync')], 21: [('gy', 'Office hours')], 22: [('ol', '11:00 Validation call')],
       26: [('cb', '18:00 Live class')], 28: [('gy', 'Office hours')], 30: [('ol', '14:00 Team sync')]}
# week 12–18 Oct: (dayIndex 0=Mon, start, end, kind, title, sub)
EVW = [(1, 10, 11, 'ol', 'Validation call · Chapter 4', 'Dr. Bola O. · Mary Okafor'), (1, 18, 19, 'cb', 'Live class · Window functions', 'Advanced SQL for Analysts'),
       (2, 16, 17, 'gy', 'Office hours', 'Open to enrolled learners')]
UNAV = {0: [(8, 9), (19, 20)], 1: [(8, 9), (19, 20)], 2: [(8, 9), (19, 20)], 3: [(8, 9), (19, 20)], 4: [(8, 9), (19, 20)], 5: [(8, 10), (13, 20)], 6: [(8, 20)]}
DAYS = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
H0, H1 = 8, 20
NOW = 9 + 52 / 60

def mcell(i):
    n = i - 2
    out = n < 1 or n > 31
    lab = (28 + i if n < 1 else (n - 31 if n > 31 else n))
    ev = '' if out else ''.join(f'<span class="cl-e {c}">{t}</span>' for c, t in EVM.get(n, []))
    dots = '' if out else ''.join(f'<i class="{c}"></i>' for c, t in EVM.get(n, []))
    cls = 'out' if out else ('today' if n == 13 else '')
    return f'<div class="cl-c {cls}"><span class="cl-d">{lab}</span>{ev}<span class="cl-dots">{dots}</span></div>'
MONTH = ('<div class="cl-wd"><span>Mon</span><span>Tue</span><span>Wed</span><span>Thu</span><span>Fri</span><span>Sat</span><span>Sun</span></div>'
         '<div class="cl-grid">' + ''.join(mcell(i) for i in range(35)) + '</div>')
LEG = '<div class="cl-leg"><span><i class="cb"></i>Live classes</span><span><i class="ol"></i>Meetings</span><span><i class="gy"></i>Office hours</span></div>'

def hh(h):
    return f'{int(h):02d}:{int(round((h % 1) * 60)):02d}'
def col(di, detail=False, sel=False):
    sh = ''.join(f'<span class="tg-un" style="top:calc({a - H0} * var(--h));height:calc({b - a} * var(--h))"></span>' for a, b in UNAV[di])
    ev = ''
    for d, a, b, k, t, sub in EVW:
        if d != di: continue
        s_ = ' sel' if (sel and a == 10) else ''
        ev += (f'<a href="CR-CAL-002.dc.html" class="tg-ev {k}{s_}" style="top:calc({a - H0} * var(--h));height:calc({b - a} * var(--h))">'
               f'<b>{t}</b><span>{hh(a)} – {hh(b)}' + (f' · {sub}' if detail else '') + '</span></a>')
    now = f'<span class="tg-now" style="top:calc({NOW - H0:.3f} * var(--h))"></span>' if di == 1 else ''
    return f'<div class="tg-col">{sh}{ev}{now}</div>'
HOURS = ''.join(f'<span style="top:calc({h - H0} * var(--h))">{h:02d}:00</span>' for h in range(H0 + 1, H1))
LINES = ''.join(f'<i style="top:calc({h - H0} * var(--h))"></i>' for h in range(H0 + 1, H1))
def grid(days, detail=False, sel=False):
    head = ''.join(f'<span class="{"today" if d == 1 else ""}"><em>{DAYS[d]}</em><b>{12 + d}</b></span>' for d in days)
    return (f'<div class="tg" style="--n:{len(days)}"><div class="tg-hd"><span class="tg-tz">WAT</span>{head}</div>'
            f'<div class="tg-bd"><div class="tg-hr">{HOURS}</div><div class="tg-cols"><div class="tg-ln">{LINES}</div>' + ''.join(col(d, detail, sel) for d in days) + '</div></div></div>')
STRIP = '<div class="tg-strip">' + ''.join(f'<span class="{"on" if d == 1 else ""}"><em>{DAYS[d][0]}</em><b>{12 + d}</b>' + ('<i></i>' if any(e[0] == d for e in EVW) else '') + '</span>' for d in range(7)) + '</div>'

AG = [('Today · Tue 13 Oct', [('10:00', '11:00', 'ol', 'Validation call · Chapter 4', 'Dr. Bola O. · Mary Okafor', 'Join'), ('18:00', '19:00', 'cb', 'Live class · Window functions', 'Advanced SQL for Analysts', '')]),
      ('Wed 14 Oct', [('16:00', '17:00', 'gy', 'Office hours', 'Open to enrolled learners', '')]),
      ('Mon 19 Oct', [('15:00', '15:30', 'ol', 'Team sync', 'Ada, John, Mary', ''), ('18:00', '19:00', 'cb', 'Live class · Window functions', 'Advanced SQL for Analysts', '')]),
      ('Wed 21 Oct', [('16:00', '17:00', 'gy', 'Office hours', 'Open to enrolled learners', '')]),
      ('Thu 22 Oct', [('11:00', '12:00', 'ol', 'Validation call · Final assessment', 'Dr. Bola O.', '')])]
AGENDA = ''.join(f'<section class="ag-g"><span class="hp-lab">{g}</span><ul>' + ''.join(
    f'<li><span class="ag-t">{a}<em>{b}</em></span><i class="ag-k {k}"></i><span class="ag-x"><b>{t}</b><span>{s}</span></span>'
    + (f'<a href="CR-CAL-002.dc.html" class="ds-btn hp-btn ag-go"><span>{c}</span><span class="ob-arrow">{ARR}</span></a>' if c else '') + '</li>' for a, b, k, t, s, c in rows) + '</ul></section>' for g, rows in AG)

PANEL = ('<aside class="ev-p" aria-label="Event"><div class="ev-ph"><span class="st cb">Meeting</span><a href="CR-CAL-001w.dc.html" class="ev-x" aria-label="Close">' + X + '</a></div>'
         '<h2 class="ev-h">Validation call · Chapter 4</h2>'
         '<ul class="ev-rows"><li>' + CLOCK + '<span><b>Tue 13 Oct · 10:00 – 11:00</b><span>Starts in 8 min</span></span></li>'
         '<li>' + VID + '<span><b>Video call</b><span>Link opens 10 min before' + tip('Only invited people can join. Validators may record notes, never video.') + '</span></span></li></ul>'
         '<span class="hp-lab ev-lab">With</span><ul class="ev-ppl"><li><span class="av">BO</span><span><b>Dr. Bola O.</b><span>Lead validator</span></span></li>'
         '<li><span class="av">MO</span><span><b>Mary Okafor</b><span>Contributor</span></span></li></ul>'
         '<span class="hp-lab ev-lab">About</span><a href="CR-VAL-MC-001.dc.html" class="ev-ab">Data Analysis with SQL · Chapter 4 review' + ic('<path d="m9 6 6 6-6 6"></path>', 15, 2.2) + '</a>'
         '<div class="ev-f"><a href="#" class="ds-btn hp-btn"><span>Join call</span><span class="ob-arrow">' + ARR + '</span></a>'
         '<div class="ev-f2"><a href="#" class="hp-rb">Propose new time</a><a href="#" class="ev-dec">Decline</a></div></div></aside>')

head = ('<div class="hp-head ob-in"><div class="cl-hd"><h1 class="ds-h1">{{ttl}}</h1>'
        '<span class="cl-nav"><button type="button" aria-label="Previous">' + ic('<path d="m15 6-6 6 6 6"></path>', 17, 2.2) + '</button><button type="button" aria-label="Next">' + ic('<path d="m9 6 6 6-6 6"></path>', 17, 2.2) + '</button></span>'
        '<button type="button" class="hp-rb cl-today">Today</button></div>'
        '<div class="cl-r"><div class="cl-vw" role="tablist"><a href="CR-CAL-001.dc.html" class="{{sM}}">Month</a><a href="CR-CAL-001w.dc.html" class="{{sW}}">Week</a><a href="CR-CAL-001d.dc.html" class="{{sD}}">Day</a><a href="CR-CAL-001a.dc.html" class="{{sA}}">Agenda</a></div>'
        '<a href="CR-CAL-003.dc.html" class="hp-rb cl-av" aria-label="Availability">' + ic(I['cal'], 16, 2) + '<span>Availability</span></a></div></div>')
main = ('<main class="ds-main hp">\n' + head +
        '<sc-if value="{{vMonth}}" hint-placeholder-val="{{true}}"><section class="ds-card cl-card ob-in2" aria-label="Month">' + MONTH + LEG + '</section>'
        '<section class="cl-ag ob-in3" aria-label="Today"><span class="hp-lab">Tuesday 13 Oct</span><ul>'
        '<li><i class="ol"></i><span><b>Validation call · Chapter 4</b><span>With Dr. Bola O.</span></span><em>10:00</em></li>'
        '<li><i class="cb"></i><span><b>Live class · Window functions</b><span>Advanced SQL for Analysts</span></span><em>18:00</em></li></ul></section></sc-if>'
        '<sc-if value="{{vWeek}}" hint-placeholder-val="{{false}}"><div class="cw-g {{gCls}}"><section class="ds-card tg-card ob-in2" aria-label="Week">' + grid(range(7), False, True) + '</section>'
        '<sc-if value="{{vEvent}}" hint-placeholder-val="{{false}}"><div class="ev-wrap ob-in3">' + PANEL + '</div></sc-if></div>'
        '<section class="tg-m ob-in2" aria-label="Tuesday">' + STRIP + '<div class="ds-card tg-card">' + grid([1], True) + '</div></section></sc-if>'
        '<sc-if value="{{vDay}}" hint-placeholder-val="{{false}}"><div class="cd-g"><section class="ds-card tg-card cd-tl ob-in2" aria-label="Tuesday">' + grid([1], True) + '</section>'
        '<aside class="cd-side ob-in3"><section class="ds-card cl-card mini" aria-label="October">' + MONTH + '</section>'
        '<section class="ds-card cd-next"><span class="hp-lab">Next up</span><b>Validation call · Chapter 4</b><span>10:00 · starts in 8 min</span><a href="CR-CAL-002.dc.html" class="ds-link">Details</a></section></aside></div>'
        '<section class="tg-m ob-in2" aria-label="Tuesday">' + STRIP + '<div class="ds-card tg-card">' + grid([1], True) + '</div></section></sc-if>'
        '<sc-if value="{{vAgenda}}" hint-placeholder-val="{{false}}"><div class="ag ob-in2">' + AGENDA + '</div></sc-if>'
        '<sc-if value="{{vEvent}}" hint-placeholder-val="{{false}}"><div class="ev-sheet"><div class="ev-dim"></div>' + PANEL + '</div></sc-if>'
        '\n</main>')
js = '''    const v = props.variant || 'month';
    const wk = v === 'week' || v === 'event';
    return { navCls: S.nav ? 'ds-open' : '', toggleNav: () => this.setState({ nav: !S.nav }),
      vMonth: v === 'month', vWeek: wk, vEvent: v === 'event', vDay: v === 'day', vAgenda: v === 'agenda', gCls: v === 'event' ? 'has-ev' : '',
      ttl: { month: 'October 2026', week: '12 – 18 Oct 2026', event: '12 – 18 Oct 2026', day: 'Tuesday 13 Oct', agenda: 'Upcoming' }[v],
      sM: v === 'month' ? 'on' : '', sW: wk ? 'on' : '', sD: v === 'day' ? 'on' : '', sA: v === 'agenda' ? 'on' : '' };'''
css = COMMON + '''
.cl-hd{display:flex;align-items:center;gap:14px}
.cl-nav{display:inline-flex;gap:6px}
.cl-nav button{width:38px;height:38px;border-radius:50%;border:1.5px solid #D6DDEE;background:#FFFFFF;color:#0B1433;display:inline-flex;align-items:center;justify-content:center;cursor:pointer}
.cl-r{display:flex;align-items:center;gap:10px}
.cl-vw{display:inline-flex;padding:4px;border-radius:999px;background:#EEF1F7}
.cl-vw a{display:inline-flex;align-items:center;height:32px;padding:0 14px;border-radius:999px;font-size:13.5px;font-weight:500;color:#5B6582;text-decoration:none}
.cl-vw a.on{background:#FFFFFF;color:#0B1433;box-shadow:0 1px 4px rgba(11,20,51,.08)}
.cl-av{gap:8px}.cl-av svg{color:#5B6582}
.cl-card{padding:8px 8px 14px 8px;overflow:hidden}
.cl-wd{display:grid;grid-template-columns:repeat(7,1fr);padding:10px 4px 8px 4px}
.cl-wd span{padding:0 10px;font-size:12.5px;font-weight:500;color:#8A93AD}
.cl-grid{display:grid;grid-template-columns:repeat(7,1fr);grid-auto-rows:minmax(96px,1fr);border-top:1.5px solid #F0F2F8}
.cl-c{display:flex;flex-direction:column;gap:4px;padding:8px 8px;border-right:1.5px solid #F0F2F8;border-bottom:1.5px solid #F0F2F8;min-width:0}
.cl-c:nth-child(7n){border-right:0}.cl-c:nth-last-child(-n+7){border-bottom:0}
.cl-d{width:28px;height:28px;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-size:13.5px;font-weight:500;color:#0B1433}
.cl-c.out .cl-d{color:#B6BED3}
.cl-c.today .cl-d{background:#1652F0;color:#FFFFFF;font-weight:600}
.cl-e{display:block;padding:4px 8px;border-radius:8px;font-size:12px;font-weight:500;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.cl-e.cb{background:#EAF0FF;color:#0E3BB8}
.cl-e.ol{background:#FFFFFF;border:1.5px solid #AFC1F5;color:#0E3BB8;padding:2.5px 6.5px}
.cl-e.gy{background:#F1F3F8;color:#4A5578}
.cl-dots{display:none}
.cl-leg{display:flex;gap:20px;padding:14px 12px 0 12px;font-size:13px;color:#5B6582}
.cl-leg span{display:inline-flex;align-items:center;gap:8px}
.cl-leg i,.cl-ag i,.cl-dots i{width:10px;height:10px;border-radius:3px;display:inline-block;flex-shrink:0}
i.cb{background:#1652F0}i.ol{background:#FFFFFF;border:2px solid #1652F0;box-sizing:border-box}i.gy{background:#B6BED3}
.cl-ag{display:none}
/* mini month (day view side) */
.cl-card.mini{padding:4px 4px 8px 4px}
.mini .cl-wd{padding:8px 0 4px 0}.mini .cl-wd span{padding:0;text-align:center;font-size:11.5px}
.mini .cl-grid{grid-auto-rows:42px;border-top:0}
.mini .cl-c{align-items:center;padding:4px 2px;gap:2px;border:0 !important}
.mini .cl-e{display:none}.mini .cl-d{width:28px;height:28px;font-size:13px}
.mini .cl-dots{display:flex;gap:3px}.mini .cl-dots i{width:5px;height:5px;border-radius:50%}.mini .cl-dots i.ol{border-width:1.5px}
/* time grid */
.tg{--h:44px}
.tg-card{padding:0;overflow:hidden}
.tg-hd{display:grid;grid-template-columns:60px repeat(var(--n),1fr);border-bottom:1.5px solid #F0F2F8}
.tg-hd > span{display:flex;align-items:center;gap:6px;padding:12px 12px}
.tg-hd em{font-style:normal;font-size:12.5px;font-weight:500;color:#8A93AD}.tg-hd b{font-size:15px;font-weight:600}
.tg-hd .today b{width:28px;height:28px;border-radius:50%;background:#1652F0;color:#FFFFFF;display:inline-flex;align-items:center;justify-content:center;font-size:13.5px}
.tg-hd .tg-tz{font-size:11.5px;font-weight:500;color:#8A93AD;justify-content:center;padding:12px 0}
.tg-bd{display:grid;grid-template-columns:60px 1fr;height:calc(12 * var(--h))}
.tg-hr{position:relative}
.tg-hr span{position:absolute;right:10px;transform:translateY(-50%);font-size:11.5px;color:#8A93AD;font-variant-numeric:tabular-nums}
.tg-cols{position:relative;display:grid;grid-template-columns:repeat(var(--n),1fr)}
.tg-ln{position:absolute;inset:0;pointer-events:none}
.tg-ln i{position:absolute;left:0;right:0;border-top:1px solid #F0F2F8}
.tg-col{position:relative;border-left:1.5px solid #F0F2F8}
.tg-un{position:absolute;left:0;right:0;background:repeating-linear-gradient(135deg,#F5F7FB 0 6px,#EEF1F7 6px 12px)}
.tg-ev{position:absolute;left:5px;right:5px;padding:7px 10px;border-radius:10px;box-sizing:border-box;display:flex;flex-direction:column;gap:2px;overflow:hidden;text-decoration:none}
.tg-ev b{font-size:12.5px;font-weight:600;line-height:1.25;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.tg-ev span{font-size:11.5px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.tg-ev.cb{background:#1652F0;color:#FFFFFF}.tg-ev.cb span{color:#D9E3FF}
.tg-ev.ol{background:#FFFFFF;border:1.5px solid #AFC1F5;color:#0E3BB8}.tg-ev.ol span{color:#4A5578}
.tg-ev.gy{background:#EEF1F7;color:#3A4566}.tg-ev.gy span{color:#5B6582}
.tg-ev.sel{box-shadow:0 0 0 3px rgba(22,82,240,.25);border-color:#1652F0}
.tg-now{position:absolute;left:-1px;right:0;height:2px;background:#1652F0;z-index:2}
.tg-now::before{content:"";position:absolute;left:-5px;top:-4px;width:10px;height:10px;border-radius:50%;background:#1652F0}
.tg-m{display:none}
.cw-g.has-ev{display:grid;grid-template-columns:minmax(0,1fr) 360px;gap:20px;align-items:start}
.cw-g.has-ev .tg-hd > span:not(.tg-tz){padding:12px 8px}
/* event panel */
.ev-p{background:#FFFFFF;border:1.5px solid #E6EAF3;border-radius:20px;padding:22px 24px;box-shadow:0 18px 44px rgba(11,20,51,.08)}
.ev-ph{display:flex;align-items:center;justify-content:space-between}
.ev-x{width:34px;height:34px;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;color:#5B6582;margin-right:-6px}
.ev-h{margin:14px 0 0 0;font-size:20px;font-weight:600;letter-spacing:-0.01em;line-height:1.3}
.ev-rows{list-style:none;margin:18px 0 0 0;padding:0;display:flex;flex-direction:column;gap:14px}
.ev-rows li{display:flex;gap:12px;align-items:flex-start}.ev-rows svg{color:#5B6582;margin-top:2px;flex-shrink:0}
.ev-rows li > span{display:flex;flex-direction:column;gap:2px}.ev-rows b{font-size:14.5px;font-weight:600}.ev-rows li > span > span{display:flex;align-items:center;font-size:13.5px;color:#5B6582}
.ev-lab{margin-top:22px}
.ev-ppl{list-style:none;margin:10px 0 0 0;padding:0;display:flex;flex-direction:column;gap:10px}
.ev-ppl li{display:flex;align-items:center;gap:12px}.ev-ppl .av{width:32px;height:32px;font-size:11.5px}
.ev-ppl li > span:last-child{display:flex;flex-direction:column;gap:1px}.ev-ppl b{font-size:14px;font-weight:600}.ev-ppl li > span > span{font-size:13px;color:#5B6582}
.ev-ab{margin-top:10px;display:flex;align-items:center;justify-content:space-between;gap:10px;padding:12px 14px;border-radius:14px;background:#F7F9FD;font-size:14px;font-weight:500;color:#0B1433;text-decoration:none}
.ev-ab svg{color:#8A93AD}
.ev-f{margin-top:24px;padding-top:18px;border-top:1.5px solid #F0F2F8;display:flex;flex-direction:column;gap:12px}
.ev-f .hp-btn{justify-content:space-between}
.ev-f2{display:flex;align-items:center;justify-content:space-between}
.ev-dec{font-size:14px;font-weight:600;color:#5B6582;text-decoration:none;padding:8px 4px}
.ev-sheet{display:none}
/* day */
.cd-g{display:grid;grid-template-columns:minmax(0,1fr) 320px;gap:20px;align-items:start}
.cd-tl .tg-ev{flex-direction:row;align-items:center;gap:14px;padding:0 16px}.cd-tl .tg-ev b{font-size:14px}.cd-tl .tg-ev span{font-size:13px}
.cd-side{display:flex;flex-direction:column;gap:16px}
.cd-next{padding:20px 22px;display:flex;flex-direction:column;gap:4px}
.cd-next b{margin-top:8px;font-size:15px;font-weight:600}.cd-next > span:not(.hp-lab){font-size:13.5px;color:#5B6582}.cd-next .ds-link{margin-top:10px;font-size:14px;font-weight:600}
/* agenda */
.ag{display:flex;flex-direction:column;gap:28px;max-width:880px}
.ag-g ul{list-style:none;margin:10px 0 0 0;padding:6px 20px;background:#FFFFFF;border:1.5px solid #E6EAF3;border-radius:20px}
.ag-g li{display:flex;align-items:center;gap:16px;padding:16px 0}
.ag-g li + li{border-top:1.5px solid #F0F2F8}
.ag-t{width:64px;flex-shrink:0;display:flex;flex-direction:column;font-size:14.5px;font-weight:600;font-variant-numeric:tabular-nums}.ag-t em{font-style:normal;font-size:12.5px;font-weight:400;color:#8A93AD}
.ag-k{width:4px;align-self:stretch;border-radius:4px;flex-shrink:0}.ag-k.ol{background:#FFFFFF;border:1.5px solid #1652F0;width:5px}
.ag-x{flex:1;min-width:0;display:flex;flex-direction:column;gap:3px}.ag-x b{font-size:15px;font-weight:600}.ag-x span{font-size:13.5px;color:#5B6582}
.ag-go{height:42px}
@media (max-width: 1080px){.cw-g.has-ev{grid-template-columns:minmax(0,1fr)}.cw-g.has-ev .ev-wrap{display:none}.cd-g{grid-template-columns:minmax(0,1fr)}.cd-side{display:none}}
@media (max-width: 960px){
.hp-head{flex-direction:column;align-items:stretch;gap:14px}
.cl-hd{justify-content:space-between}.cl-hd h1{flex:1}
.cl-today{display:none !important}
.cl-r{justify-content:space-between}
.cl-vw a{padding:0 11px;font-size:13px}
.cl-av{display:inline-flex !important;width:38px;height:38px;padding:0;justify-content:center}.cl-av span{display:none}
.cl-card{padding:4px 4px 12px 4px}
.cl-wd{padding:8px 0 6px 0}.cl-wd span{padding:0;text-align:center;font-size:11.5px}
.cl-grid{grid-auto-rows:52px}
.cl-c{align-items:center;padding:6px 2px;gap:3px;border:0 !important}
.cl-e{display:none}
.cl-d{width:30px;height:30px;font-size:13.5px}
.cl-dots{display:flex;gap:3px}.cl-dots i{width:5px;height:5px;border-radius:50%}.cl-dots i.ol{border-width:1.5px}
.cl-leg{flex-wrap:wrap;gap:8px 16px;padding:10px 12px 0 12px;font-size:12.5px}
.cl-ag{display:block;margin-top:26px}
.cl-ag ul{list-style:none;margin:10px 0 0 0;padding:0;display:flex;flex-direction:column;gap:10px}
.cl-ag li{display:flex;align-items:center;gap:14px;padding:16px;border-radius:16px;background:#FFFFFF;border:1.5px solid #E6EAF3}
.cl-ag li > span{flex:1;display:flex;flex-direction:column;gap:2px;min-width:0}.cl-ag b{font-size:14.5px;font-weight:600}.cl-ag li > span > span{font-size:13px;color:#5B6582}
.cl-ag em{font-style:normal;font-size:13.5px;font-weight:600;color:#0B1433}
.cw-g,.cd-g{display:none !important}
.tg-m{display:block}
.tg-strip{display:grid;grid-template-columns:repeat(7,1fr);gap:4px;margin-bottom:14px}
.tg-strip span{position:relative;display:flex;flex-direction:column;align-items:center;gap:2px;padding:8px 0 12px 0;border-radius:14px}
.tg-strip em{font-style:normal;font-size:11.5px;color:#8A93AD}.tg-strip b{font-size:15px;font-weight:600}
.tg-strip span.on{background:#1652F0;color:#FFFFFF}.tg-strip span.on em{color:#D9E3FF}
.tg-strip i{position:absolute;bottom:5px;width:4px;height:4px;border-radius:50%;background:#1652F0}.tg-strip span.on i{background:#FFFFFF}
.tg-m .tg{--h:46px}
.tg-m .tg-hd{display:none}
.tg-m .tg-bd{grid-template-columns:52px 1fr}
.tg-m .tg-ev{left:8px;right:8px}
.ag{gap:22px}
.ag-g ul{padding:2px 14px}
.ag-g li{gap:12px;padding:14px 0;flex-wrap:wrap}
.ag-t{width:46px;font-size:14px}
.ag-x{flex-basis:calc(100% - 80px)}
.ag-go{width:100%;justify-content:space-between;margin-left:62px;width:calc(100% - 62px)}
.ev-sheet{display:block;position:fixed;inset:0;z-index:30}
.ev-dim{position:absolute;inset:0;background:rgba(11,20,51,.36)}
.ev-sheet .ev-p{position:absolute;left:0;right:0;bottom:0;border-radius:24px 24px 0 0;padding:22px 20px 26px 20px;border:0}
.ev-sheet .ev-p::before{content:"";display:block;width:40px;height:4px;border-radius:4px;background:#D6DDEE;margin:-8px auto 14px auto}
}
'''
B.page('CR-CAL', 'Calendar', main, js, css, 'Credalio · Calendar', "{ nav: false }")
props_patch('CR-CAL')
wrap('CR-CAL', [('CR-CAL-001', 'month', 820), ('CR-CAL-001w', 'week', 900), ('CR-CAL-002', 'event', 844), ('CR-CAL-001d', 'day', 900), ('CR-CAL-001a', 'agenda', 1060)])

# ======================= CR-CAL-003 · weekly availability =======================
AV = [('Monday', ['09:00 – 12:00', '14:00 – 19:00']), ('Tuesday', ['09:00 – 12:00', '14:00 – 19:00']), ('Wednesday', ['09:00 – 19:00']),
      ('Thursday', ['09:00 – 12:00', '14:00 – 19:00']), ('Friday', ['09:00 – 15:00']), ('Saturday', ['10:00 – 13:00']), ('Sunday', [])]
def avrow(d, ws):
    on = bool(ws)
    chips = ''.join(f'<span class="av-w">{w}<button type="button" aria-label="Remove">' + ic('<path d="M7 7l10 10M17 7 7 17"></path>', 13, 2.2) + '</button></span>' for w in ws)
    return (f'<li class="{"" if on else "off"}"><button type="button" class="hp-sw {"on" if on else ""}" aria-label="{d}" aria-pressed="{"true" if on else "false"}"><i></i></button>'
            f'<b class="av-d">{d}</b><span class="av-ws">' + (chips + f'<button type="button" class="av-add" aria-label="Add hours">{PLUS}</button>' if on else '<span class="av-no">Unavailable</span>') + '</span></li>')
main = ('<main class="ds-main hp">\n<a href="CR-CAL-001.dc.html" class="pg-back">' + BACK + 'Calendar</a>'
        '<div class="hp-head ob-in"><div><h1 class="ds-h1">Weekly availability' + tip('Learners and teammates can only book you inside these hours. Your calendar shades the rest.') + '</h1></div>'
        '<button type="button" class="hp-rb av-tz">WAT (UTC+1) · Lagos' + ic('<path d="m6 9 6 6 6-6"></path>', 15, 2.2) + '</button></div>'
        '<section class="ds-card av-card ob-in2" aria-label="Hours"><ul class="av-l">' + ''.join(avrow(d, w) for d, w in AV) + '</ul>'
        '<div class="av-f"><a href="#" class="ds-link">Add a day off or exception</a><a href="CR-CAL-001w.dc.html" class="ds-btn hp-btn"><span>Save hours</span><span class="ob-arrow">' + ARR + '</span></a></div></section>\n</main>')
js = '''    return { navCls: S.nav ? 'ds-open' : '', toggleNav: () => this.setState({ nav: !S.nav }) };'''
css = COMMON + '''
.ds-h1 .tip{margin-left:10px;vertical-align:4px}
.av-tz{gap:8px}.av-tz svg{color:#5B6582}
.av-card{padding:8px 28px 22px 28px;max-width:920px}
.av-l{list-style:none;margin:0;padding:0}
.av-l li{display:flex;align-items:center;gap:18px;padding:16px 0;border-bottom:1.5px solid #F0F2F8}
.av-d{width:110px;flex-shrink:0;font-size:15px;font-weight:600}
.av-l li.off .av-d{color:#8A93AD;font-weight:500}
.hp-sw i{position:absolute;top:3px;left:3px;width:20px;height:20px;border-radius:50%;background:#FFFFFF;box-shadow:0 1px 3px rgba(11,20,51,.2);transition:left .2s ease}
.hp-sw.on{background:#1652F0}.hp-sw.on i{left:21px}
.av-ws{flex:1;display:flex;flex-wrap:wrap;align-items:center;gap:8px}
.av-w{display:inline-flex;align-items:center;gap:6px;height:36px;padding:0 6px 0 14px;border-radius:12px;background:#F5F8FF;border:1.5px solid #D6DDEE;font-size:14px;font-weight:500;font-variant-numeric:tabular-nums}
.av-w button{width:24px;height:24px;border:0;border-radius:50%;background:transparent;color:#8A93AD;display:inline-flex;align-items:center;justify-content:center;cursor:pointer}
.av-add{width:36px;height:36px;border-radius:12px;border:1.5px dashed #CBD3E6;background:#FFFFFF;color:#1652F0;display:inline-flex;align-items:center;justify-content:center;cursor:pointer}
.av-no{font-size:14px;color:#8A93AD}
.av-f{margin-top:22px;display:flex;align-items:center;justify-content:space-between;gap:16px}
.av-f .ds-link{font-size:14px;font-weight:600}
@media (max-width: 960px){
.hp-head{flex-direction:column;align-items:stretch;gap:12px}
.av-tz{display:inline-flex !important;align-self:flex-start;height:36px;font-size:13px}
.av-card{padding:2px 16px 16px 16px}
.av-l li{flex-wrap:wrap;gap:10px 14px;padding:14px 0}
.av-d{width:auto;flex:1}
.hp-sw{order:2}
.av-ws{order:3;flex-basis:100%}
.av-l li.off .av-ws{display:none}
.av-ws{gap:6px}.av-w{height:34px;padding:0 2px 0 11px;gap:2px;font-size:13px}.av-add{width:34px;height:34px}
.av-f{flex-direction:column-reverse;align-items:stretch;gap:14px}
.av-f .hp-btn{width:100%;justify-content:space-between}
.av-f .ds-link{text-align:center}
}
'''
B.page('CR-CAL-003', 'Calendar', main, js, css, 'Credalio · Availability', "{ nav: false }")
t = mob(wm.replace('<dc-import name="CR-CRED-002" variant="badge"', '<dc-import name="CR-CAL-003"'), 1000)
wr('CR-CAL-003-Mobile.dc.html', re.sub(r'<title>.*?</title>', '<title>CR-CAL-003 mobile preview</title>', t))
print('build28 ok')
