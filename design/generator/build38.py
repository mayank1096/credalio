# build38: Creio balance states. Writes CR-CREIO-POP (top-bar Creio popover over LIVE CR-DASH-NEW, variants top / low = AI-TOP / AI-010b),
# PATCHES live CR-NOVA-001 (variants low / empty = AI-010 / AI-011; asserts if patched), writes CR-CREIO-011b (= AI-011b, from LIVE CR-AI-001a:
# Nova says a full review needs more Creio than you have). AI-012 = CR-HOME-SET (no new design).
# usage: python3 build38.py <dir>  (scratch copy: build17 re-runs on import; copy back only the files printed at the end)
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build17 as B
from tipx import tip, TIP_CSS
P, rd, wr, ic, ARR = B.P, B.rd, B.wr, B.ic, B.ARR
OUT = []
BANG = ic('<path d="M12 7v6M12 16.5v.01"></path>', 14, 2.8)
HAND = ic('<path d="M12 20h9"></path><path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4z"></path>', 20, 1.9)
PILL = '<span>20K</span><span class="ds-hide-sm" style="margin-left: -2px">Creio</span></a>'
wd, wm, wa = rd('CR-SET-001.dc.html'), rd('CR-SET-001-Mobile.dc.html'), rd('CR-AI-001-Mobile.dc.html')
def wrap(src, n, var, hd=820, hm=844):
    t = wd.replace('<dc-import name="CR-SET" variant="account"', f'<dc-import name="{src}"' + (f' variant="{var}"' if var else '')).replace('CR-SET-001', n)
    wr(n + '.dc.html', t); OUT.append(n + '.dc.html')
    t = wa.replace('CR-AI-001 mobile', n + ' mobile').replace('<dc-import name="CR-AI-001"', f'<dc-import name="{src}"' + (f' variant="{var}"' if var else ''))
    wr(n + '-Mobile.dc.html', t); OUT.append(n + '-Mobile.dc.html')
def add_css(s, css):
    i = s.rfind('</style>', 0, s.find('</helmet>')); return s[:i] + css + s[i:]
def pill(s):
    p = PILL if PILL in s else PILL.replace(' style="margin-left: -2px"', '')
    m = re.search(r'<span>20K</span><span class="ds-hide-sm"[^>]*>Creio</span></a>', s)
    assert m, 'pill'
    s = s[:m.start()] + m.group(0).replace('<span>20K</span>', '<span>{{tokT}}</span>').replace('</a>', '<sc-if value="{{low}}" hint-placeholder-val="{{false}}"><span class="tk-low">Low</span></sc-if></a>') + s[m.end():]
    return s.replace('aria-label="20,000 Creio"', 'aria-label="{{tokL}}"', 1)
PILL_CSS = """
.tk-low{display:inline-flex;align-items:center;height:22px;margin-left:2px;padding:0 8px;border-radius:999px;background:#FFF3DC;border:1px solid #F0C774;color:#8A5300;font-size:12px;font-weight:500}
"""
LOWV = "tokT: LOW ? '8.2K' : (EMP ? '0' : '20K'), tokL: LOW ? '8,240 Creio, running low' : (EMP ? 'No Creio left' : '20,000 Creio'), low: LOW, low2: LOW || EMP,"

# ======================= CR-CREIO-POP · top-bar popover (AI-TOP / AI-010b) =======================
s = rd('CR-DASH-NEW.dc.html')
s = pill(s)
ts = s.index('<a href="#" class="ds-tok"'); te = s.index('</a>', s.index('{{tokT}}')) + 4
tok = s[ts:te].replace('href="#" class="ds-tok"', 'href="CR-NOVA-001.dc.html" class="ds-tok tp-on" aria-expanded="true"', 1)
pop = ('<div class="tp-w">' + tok + '<section class="tp-p" role="dialog" aria-label="Creio">'
       '<span class="tp-lab">Creio available' + tip('Creio powers Nova’s help. You can always create by hand.', 'r') + '</span>'
       '<span class="tp-big"><span class="tp-coin" aria-hidden="true"></span>{{bigT}}</span><span class="tp-sub">{{subT}}</span>'
       '<sc-if value="{{low}}" hint-placeholder-val="{{false}}"><p class="tp-warn"><span class="tp-i">' + BANG + '</span><span><b>Running low.</b> A full course review uses about 9,800.</span></p></sc-if>'
       '<div class="tp-f"><a href="CR-CREIO-003.dc.html" class="ds-btn tp-go"><span>Get more Creio</span></a><a href="CR-CREIO-USE.dc.html" class="ds-link tp-u">See usage</a></div></section></div>')
s = s[:ts] + pop + s[te:]
s = s.replace('<main class="ds-main">', '<div class="tp-scrim" aria-hidden="true"></div><main class="ds-main">', 1)
s = add_css(s, PILL_CSS + TIP_CSS + """
/* build38 Creio popover */
.tp-w{position:relative;flex-shrink:0}
.ds-tok.tp-on{box-shadow:0 0 0 4px rgba(244,217,142,.45)}
.tp-p{position:absolute;right:-6px;top:calc(100% + 12px);z-index:30;width:340px;box-sizing:border-box;padding:22px 22px 18px 22px;border-radius:20px;background:linear-gradient(170deg,#FFFAEB 0%,#FFFFFF 48%);border:1.5px solid #F4D98E;box-shadow:0 24px 60px rgba(11,20,51,.16);display:flex;flex-direction:column;align-items:flex-start;text-align:left}
.tp-lab{display:flex;align-items:center;gap:6px;font-size:12.5px;font-weight:500;color:#8A93AD}
.tp-big{margin-top:10px;display:flex;align-items:center;gap:10px;font-size:34px;font-weight:600;letter-spacing:-0.03em;color:#4A3300}
.tp-coin{width:30px;height:30px;border-radius:50%;background:linear-gradient(135deg,#FFE9A3,#F6C343 45%,#D08A12);box-shadow:inset 0 0 0 3px rgba(255,241,194,.6)}
.tp-sub{margin-top:6px;font-size:14px;color:#6B4E16}
.tp-warn{margin:16px 0 0 0;width:100%;box-sizing:border-box;display:flex;align-items:flex-start;gap:10px;padding:12px 14px;border-radius:14px;background:#FFF3DC;font-size:13.5px;line-height:1.45;color:#5C3B00}
.tp-warn b{font-weight:600}
.tp-i{width:20px;height:20px;flex-shrink:0;border-radius:50%;background:#B26A00;color:#FFFFFF;display:flex;align-items:center;justify-content:center;margin-top:1px}
.tp-f{margin-top:20px;width:100%;display:flex;align-items:center;justify-content:space-between;gap:12px}
.tp-go{height:44px;padding:0 20px;font-size:14.5px}
.tp-u{font-size:14px}
.tp-scrim{position:fixed;inset:0;z-index:9;background:rgba(11,20,51,.06);pointer-events:none}
@media (max-width: 960px){
.tp-w{position:static}
.tp-p{position:fixed;left:8px;right:8px;top:68px;width:auto;padding:22px 18px 16px 18px}
.tp-f{flex-direction:column;align-items:stretch;gap:6px}
.tp-go{justify-content:center}
.tp-u{align-self:center;padding:10px 0}
.tp-scrim{background:rgba(11,20,51,.28)}
}
""")
a = "constructor(props) { super(props); this.state = { nav: false, ask: false, idea: '' }; }"
assert a in s
s = s.replace(a, "constructor(props) { super(props); this.v = (props && props.variant) || 'top'; this.state = { nav: false, ask: false, idea: '' }; }", 1)
a = "return { navCls:"
assert s.count(a) == 1
s = s.replace(a, "const LOW = this.v === 'low', EMP = false;\n    return { " + LOWV + " bigT: LOW ? '8,240' : '20,000', subT: LOW ? 'About 55 replies from Nova' : 'About 130 replies from Nova',\n      navCls:", 1)
s = re.sub(r'<title>.*?</title>', '<title>Credalio · Creio balance</title>', s)
wr('CR-CREIO-POP.dc.html', s); OUT.append('CR-CREIO-POP.dc.html')
wrap('CR-CREIO-POP', 'CR-CREIO-TOP', 'top')
wrap('CR-CREIO-POP', 'CR-CREIO-010b', 'low')

# ======================= CR-NOVA-001 · low / empty (AI-010 / AI-011) =======================
s = rd('CR-NOVA-001.dc.html')
assert 'balCls' not in s, 'CR-NOVA-001 already patched'
s = pill(s)
s = s.replace('<section class="ds-card nv-bal"', '<section class="ds-card nv-bal {{balCls}}"', 1)
a = 'Creio available<span class="tip"'
assert s.count(a) == 1
s = s.replace(a, 'Creio available<sc-if value="{{low2}}" hint-placeholder-val="{{false}}"><span class="nv-st">{{stT}}</span></sc-if><span class="tip"', 1)
a = '<span class="nv-coin" aria-hidden="true"></span>20,000</span><span class="nv-sub">About 130 replies from Nova'
assert s.count(a) == 1
s = s.replace(a, '<span class="nv-coin" aria-hidden="true"></span>{{bigT}}</span><span class="nv-sub">{{subT}}', 1)
m = re.search(r'(\{\{subT\}\})(<span class="tip".*?</span></span>)(</span>)', s)
assert m
s = s[:m.start()] + m.group(1) + '<sc-if value="{{notEmp}}" hint-placeholder-val="{{true}}">' + m.group(2) + '</sc-if>' + m.group(3) + s[m.end():]
band = ('<sc-if value="{{emp}}" hint-placeholder-val="{{false}}"><section class="ds-card nv-hand ob-in3" aria-labelledby="nv-hh"><span class="nv-hi">' + HAND + '</span>'
        '<div class="nv-ht"><h2 id="nv-hh">Everything else still works</h2><p>Write, upload and build by hand. Nova picks up again when you add Creio.</p></div>'
        '<a href="CR-HOME-NEW.dc.html" class="nv-hb">Create by hand</a></section></sc-if>')
a = '<a href="#" class="ds-link nv-all">See all activity</a></section></div>'
assert s.count(a) == 1
s = s.replace(a, '<a href="CR-CREIO-USE.dc.html" class="ds-link nv-all">See all activity</a></section>' + band + '</div>', 1)
s = add_css(s, PILL_CSS + """
/* build38 low / empty */
.nv-st{display:inline-flex;align-items:center;height:22px;padding:0 9px;border-radius:999px;background:#FFF3DC;border:1px solid #F0C774;color:#8A5300;font-size:12px;font-weight:500}
.nv-bal.is-emp .nv-coin{background:linear-gradient(135deg,#EEF0F5,#CBD3E6);box-shadow:inset 0 0 0 4px rgba(255,255,255,.6)}
.nv-bal.is-emp .nv-big{color:#8A93AD}
.nv-hand{grid-column:1 / -1;padding:22px 26px;display:flex;align-items:center;gap:18px}
.nv-hi{width:48px;height:48px;flex-shrink:0;border-radius:14px;background:#EAF0FF;color:#1652F0;display:flex;align-items:center;justify-content:center}
.nv-ht{flex:1;min-width:0}
.nv-ht h2{margin:0;font-size:16.5px;font-weight:600}
.nv-ht p{margin:4px 0 0 0;font-size:14px;line-height:1.5;color:#4A5578}
.nv-hb{flex-shrink:0;box-sizing:border-box;height:44px;padding:0 20px;display:inline-flex;align-items:center;border-radius:999px;border:1.5px solid #D6DDEE;color:#0B1433;font-size:14.5px;font-weight:600;text-decoration:none}
.nv-hb:hover{border-color:#1652F0;color:#1652F0}
@media (max-width: 960px){
.nv-g{display:flex;flex-direction:column}.nv-bal{order:1}.nv-hand{order:2}.nv-use{order:3}
.nv-hand{padding:20px 18px;flex-wrap:wrap;align-items:flex-start;gap:14px}
.nv-hi{width:40px;height:40px}
.nv-ht{flex-basis:calc(100% - 60px)}
.nv-hb{width:100%;justify-content:center}
}
""")
a = "constructor(props) { super(props); this.state = { nav: false }; }"
assert a in s
s = s.replace(a, "constructor(props) { super(props); this.v = (props && props.variant) || ''; this.state = { nav: false }; }", 1)
a = "renderVals(){ const S=this.state; return {" if "renderVals(){ const S=this.state; return {" in s else None
m = re.search(r'renderVals\(\)\s*\{\s*const S\s*=\s*this\.state;\s*return \{', s)
assert m
s = s[:m.end()] + (" " + LOWV.replace('LOW', "this.v === 'low'").replace('EMP', "this.v === 'empty'") +
      " emp: this.v === 'empty', notEmp: this.v !== 'empty', balCls: this.v === 'empty' ? 'is-emp' : '', stT: this.v === 'empty' ? 'Used up' : 'Low',"
      " bigT: this.v === 'low' ? '8,240' : (this.v === 'empty' ? '0' : '20,000'),"
      " subT: this.v === 'low' ? 'About 55 replies from Nova' : (this.v === 'empty' ? 'Nova is paused for now' : 'About 130 replies from Nova'),") + s[m.end():]
wr('CR-NOVA-001.dc.html', s); OUT.append('CR-NOVA-001.dc.html')
wrap('CR-NOVA-001', 'CR-CREIO-010', 'low')
wrap('CR-NOVA-001', 'CR-CREIO-011', 'empty')

# ======================= CR-CREIO-011b · Copilot: not enough Creio =======================
s = rd('CR-AI-001a.dc.html')
s = s.replace('<span>20K</span>', '<span>8.2K</span>', 1).replace('aria-label="20,000 Creio"', 'aria-label="8,240 Creio"', 1)
a = '<div class="cp-me"><p>Add measurable outcomes to this course.</p></div>'
assert s.count(a) == 1
s = s.replace(a, '<div class="cp-me"><p>Review the whole course for clarity and gaps.</p></div>', 1)
cs = s.index('<div class="cp-col">'); ce = s.index('</div></div></div></div></div><footer') + len('</div></div></div>')
COIN = '<span class="ns-c" aria-hidden="true"></span>'
col = ('<div class="cp-col"><div class="cp-bub"><p>Happy to. A full review reads all 6 chapters.</p></div>'
       '<div class="ac ns"><span class="ns-h"><span class="tp-i">' + BANG + '</span>Not enough Creio</span>'
       '<dl class="ns-d"><div><dt>This review</dt><dd>' + COIN + '9,800</dd></div><div><dt>You have</dt><dd>' + COIN + '8,240</dd></div></dl>'
       '<p class="ns-p">Or review one chapter at a time, about 1,700 each.</p>'
       '<div class="ac-f"><a href="CR-CREIO-003.dc.html" class="ds-btn ac-go"><span>Get more Creio</span></a><a href="#" class="ac-x">Review chapter 1</a></div></div></div>')
s = s[:cs] + col + s[ce:]
s = s.replace('Applying uses about 400 Creio', 'About 150 Creio per reply', 1)
s = add_css(s, """
/* build38 not enough Creio */
.ns{border-color:#F0C774;background:linear-gradient(170deg,#FFF8EA 0%,#FFFFFF 55%)}
.ns-h{display:flex;align-items:center;gap:9px;font-size:14.5px;font-weight:600;color:#5C3B00}
.tp-i{width:20px;height:20px;flex-shrink:0;border-radius:50%;background:#B26A00;color:#FFFFFF;display:flex;align-items:center;justify-content:center}
.ns-d{margin:14px 0 0 0;display:grid;grid-template-columns:1fr 1fr;gap:10px}
.ns-d div{padding:10px 12px;border-radius:12px;background:#FFFFFF;border:1.5px solid #F3E6C4}
.ns-d dt{font-size:12.5px;color:#8A93AD}
.ns-d dd{margin:4px 0 0 0;display:flex;align-items:center;gap:7px;font-size:17px;font-weight:600;color:#4A3300;font-variant-numeric:tabular-nums}
.ns-c{width:16px;height:16px;border-radius:50%;background:linear-gradient(135deg,#FFE9A3,#F6C343 45%,#D08A12)}
.ns-p{margin:12px 0 0 0;font-size:13.5px;line-height:1.45;color:#4A5578}
""")
s = re.sub(r'<title>.*?</title>', '<title>Credalio · Nova · Not enough Creio</title>', s)
wr('CR-CREIO-011b.dc.html', s); OUT.append('CR-CREIO-011b.dc.html')
t = wa.replace('CR-AI-001 mobile', 'CR-CREIO-011b mobile').replace('<dc-import name="CR-AI-001"', '<dc-import name="CR-CREIO-011b"')
wr('CR-CREIO-011b-Mobile.dc.html', t); OUT.append('CR-CREIO-011b-Mobile.dc.html')
print('build38 ok'); print(' '.join(OUT))
