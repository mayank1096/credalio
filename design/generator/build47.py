# build47: M5 scenario states (PATCH live CR-ORI-005: variant none / wrong = boards M5-S1 / M5-S3; ori_m.trim), M5-DONE = board of
# CR-ORI-006 (Next module -> M6-00), Module 6 (Creator economy): M6-00, M6-L1 (price ranges figure), M6-L2 (wallet vs earnings figure).
# usage: python3 build47.py <dir>
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ori_m as O, tipx
P = sys.argv[1]
def rd(f): return open(os.path.join(P, f), encoding='utf-8').read()
def wr(f, s): open(os.path.join(P, f), 'w', encoding='utf-8').write(s); OUT.append(f)
OUT = []
def mob(tpl, n, imp, var=None, h=None):
    m = rd(tpl + '-Mobile.dc.html').replace(f'<dc-import name="{tpl}"', f'<dc-import name="{imp}"' + (f' variant="{var}"' if var else ''))
    m = re.sub(r'<title>.*?</title>', f'<title>{n} mobile preview</title>', m)
    if h:
        m = re.sub(r'height: \d+px; overflow', f'height: {h}px; overflow', m, count=1)
        m = re.sub(r'hint-size="390px,\d+px"', f'hint-size="390px,{h}px"', m)
        m = re.sub(r'"\$preview":\{"width":390,"height":\d+\}', f'"$preview":{{"width":390,"height":{h}}}', m)
    wr(n + '-Mobile.dc.html', m)
SETW = rd('CR-SET-001.dc.html')
def board(n, imp, var=None):
    wr(n + '.dc.html', SETW.replace('<dc-import name="CR-SET" variant="account"', f'<dc-import name="{imp}"' + (f' variant="{var}"' if var else '')).replace('CR-SET-001', n))
# ---- M5 scenario states ----
s = rd('CR-ORI-005.dc.html'); assert 'props.variant' not in s
s = s.replace("constructor(props) { super(props); this.state = { a: 1 }; }",
              "constructor(props) { super(props); const v = (props && props.variant) || 'right'; this.state = { a: v === 'none' ? -1 : (v === 'wrong' ? 0 : 1) }; }", 1)
assert 'props.variant' in s
s, n = re.subn(r'<p class="sc-pol">.*?</p>', '', s, count=1, flags=re.S); assert n
s = s.replace("'The creator reviews, verifies and takes responsibility for it, and AI assistance is disclosed as policy requires.'", "'Creators stay accountable for everything they submit, however it was made.'", 1)
s = s.replace("'The creator reviews it for accuracy, checks sources, edits as needed and discloses AI assistance where required'", "'The creator reviews it, checks sources and discloses AI help'", 1)
s = s.replace('<a href="CR-ORI-004.dc.html" class="lp-prev">', '<a href="CR-ORI-M5-K1.dc.html" class="lp-prev">', 1)
assert 'however it was made' in s and 'CR-ORI-M5-K1' in s and 'discloses AI help' in s
wr('CR-ORI-005.dc.html', O.trim(s))
for b, v in [('S1', 'none'), ('S3', 'wrong')]:
    board('CR-ORI-M5-' + b, 'CR-ORI-005', v); mob('CR-ORI-005', 'CR-ORI-M5-' + b, 'CR-ORI-005', v, 960)
# ---- M5 complete = CR-ORI-006 ----
s = rd('CR-ORI-006.dc.html'); s = s.replace('<a href="#" class="ds-btn dn-go">', '<a href="CR-ORI-M6-00.dc.html" class="ds-btn dn-go">', 1); assert 'CR-ORI-M6-00' in s
wr('CR-ORI-006.dc.html', s)
board('CR-ORI-M5-DONE', 'CR-ORI-006'); mob('CR-ORI-006', 'CR-ORI-M5-DONE', 'CR-ORI-006', None, 900)
# ---- Module 6 ----
O.ICO['dollar'] = '<path d="M12 3v18"></path><path d="M16.5 7.5c-.8-1.2-2.4-2-4.5-2-2.6 0-4.2 1.3-4.2 3.1 0 4.3 8.9 2.2 8.9 6.6 0 1.9-1.8 3.3-4.7 3.3-2.3 0-4-.9-4.9-2.3"></path>'
O.ICO['lock'] = '<rect x="5" y="10.5" width="14" height="10" rx="2.5"></rect><path d="M8.5 10.5V8a3.5 3.5 0 0 1 7 0v2.5"></path>'
COIN = '<span class="pr-coin" aria-hidden="true">C</span>'
FIG_CSS = '\n/* build47 economy figures */' + tipx.TIP_CSS + """
.pr{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px;margin-top:40px}
.pr-c{display:flex;flex-direction:column;padding:22px 22px 20px;border-radius:18px;border:1.5px solid #E6EAF3;background:#FFFFFF}
.pr-l{font-size:13px;font-weight:500;color:#8A93AD;display:flex;align-items:center}
.pr-v{margin-top:8px;font-size:26px;font-weight:600;color:#0B1433;letter-spacing:-.01em;display:flex;align-items:baseline;gap:6px}
.pr-v small{font-size:14px;font-weight:500;color:#5B6582}
.pr-t{position:relative;margin-top:22px;height:6px;border-radius:999px;background:#EEF1F7}
.pr-t i{position:absolute;top:0;bottom:0;border-radius:999px;background:#C9D7FB}
.pr-t b{position:absolute;top:50%;width:18px;height:18px;margin:-9px 0 0 -9px;border-radius:50%;background:#1652F0;box-shadow:0 0 0 4px rgba(22,82,240,.16)}
.pr-r{margin-top:10px;display:flex;justify-content:space-between;font-size:12.5px;color:#8A93AD}
.pr-coin{display:inline-flex;align-items:center;justify-content:center;width:18px;height:18px;border-radius:50%;background:#1652F0;color:#FFFFFF;font-size:10.5px;font-weight:700;margin-right:6px}
.wv{display:grid;grid-template-columns:minmax(0,1fr) auto minmax(0,1fr);align-items:center;gap:14px;margin-top:40px}
.wv-c{display:flex;flex-direction:column;gap:4px;padding:22px;border-radius:18px;border:1.5px solid #E6EAF3;background:#FFFFFF}
.wv-i{width:40px;height:40px;border-radius:12px;display:flex;align-items:center;justify-content:center;margin-bottom:10px}
.wv-in .wv-i{background:#EAF0FF;color:#1652F0}.wv-out .wv-i{background:#E7F5EE;color:#0F6B45}
.wv-k{font-size:12.5px;font-weight:500;color:#8A93AD}
.wv-c b{font-size:16px;font-weight:600;color:#0B1433}
.wv-c span.wv-d{font-size:14px;line-height:1.5;color:#5B6582}
.wv-x{display:inline-flex;align-items:center;gap:6px;height:32px;padding:0 12px;border-radius:999px;background:#F5F8FF;border:1.5px solid #E6EAF3;color:#4A5578;font-size:13px;font-weight:500;white-space:nowrap}
.wv-x .tip{margin-left:2px}
@media (max-width: 960px){
.pr{grid-template-columns:minmax(0,1fr);gap:12px;margin-top:28px}.pr-c{padding:18px}.pr-v{font-size:22px}
.wv{grid-template-columns:minmax(0,1fr);gap:10px;margin-top:28px}.wv-c{padding:18px}.wv-x{justify-self:center}
.wv-x .tip-b{left:50%;margin-left:-125px}
}
"""
def track(lo, hi, me):  # positions in % of the full bar
    return f'<span class="pr-t" aria-hidden="true"><i style="left:{lo}%;right:{100 - hi}%"></i><b style="left:{me}%"></b></span>'
prices = ('<div class="pr ob-in3">'
          '<div class="pr-c"><span class="pr-l">Subscription access' + tipx.tip('DLP is the unit learners on a subscription use to access learning.') + '</span>'
          '<span class="pr-v">1,800 <small>DLP</small></span>' + track(18, 78, 52) + '<span class="pr-r"><span>1,200</span><span>2,400 DLP</span></span></div>'
          '<div class="pr-c"><span class="pr-l">Marketplace purchase' + tipx.tip('Ranges never include a free price.', 'r') + '</span>'
          f'<span class="pr-v">{COIN}420 <small>Credits</small></span>' + track(18, 78, 46) + '<span class="pr-r"><span>300</span><span>560 Credits</span></span></div></div>')
MOD, MN = 6, 'Creator economy'
STEPS = [('Setting your price', 'Lesson'), ('Credit Wallet vs Earnings', 'Lesson'), ('Quick knowledge check', 'Check')]
s = O.overview(rd('CR-ORI-M1-00.dc.html'), MOD, MN, STEPS, 10,
   'How pricing works, and where your money comes and goes.',
   'Money talk, Ada. I’ll keep it short and clear.',
   ['Credalio suggests a fair range, you choose', 'Your Credit Wallet and Earnings stay separate'], 'CR-ORI-M6-L1.dc.html', 'Credalio · Orientation · Module 6')
l0 = s.index('<ol class="mo-list">'); l1 = s.index('</ol>', l0)
s = s[:l0] + re.sub(r'(<b>[^<]*</b>)<span>(Lesson|Check|Exercise)</span>', r'\1', s[l0:l1]) + s[l1:]
wr('CR-ORI-M6-00.dc.html', s); mob('CR-ORI-M1-00', 'CR-ORI-M6-00', 'CR-ORI-M6-00', h=1140)
s = O.lesson(rd('CR-ORI-003.dc.html'), MOD, MN, STEPS, 0, 3, 'Setting your price',
             'Credalio measures your learning experience and suggests a fair range. You choose where your price sits.',
             None, prices, ('CR-ORI-M6-00.dc.html', 'Module overview'), ('CR-ORI-M6-L2.dc.html', 'Next lesson'), 'Credalio · Orientation · Setting your price', scene=True)
wr('CR-ORI-M6-L1.dc.html', O.with_css(s, FIG_CSS)); mob('CR-ORI-003', 'CR-ORI-M6-L1', 'CR-ORI-M6-L1', h=960)
wallet = ('<div class="wv ob-in3">'
          f'<div class="wv-c wv-in"><span class="wv-i">{O.svg("lock", 20)}</span><span class="wv-k">Money in</span><b>Credit Wallet</b><span class="wv-d">Pays for validation and other services.</span></div>'
          '<span class="wv-x">Kept separate' + tipx.tip('Earnings never top up your wallet on their own.') + '</span>'
          f'<div class="wv-c wv-out"><span class="wv-i">{O.svg("dollar", 20)}</span><span class="wv-k">Money out</span><b>Earnings</b><span class="wv-d">What learners pay you, ready to withdraw.</span></div></div>')
wallet = wallet.replace(O.svg('lock', 20), '<span class="pr-coin" style="margin:0;width:22px;height:22px;font-size:12px">C</span>', 1)
s = O.lesson(rd('CR-ORI-003.dc.html'), MOD, MN, STEPS, 1, 2, 'Credit Wallet vs Earnings',
             'Two separate places. One pays for services, the other holds what you earn.',
             None, wallet, ('CR-ORI-M6-L1.dc.html', 'Setting your price'), ('CR-ORI-M6-K1.dc.html', 'Next'), 'Credalio · Orientation · Credit Wallet vs Earnings', scene=True)
wr('CR-ORI-M6-L2.dc.html', O.with_css(s, FIG_CSS)); mob('CR-ORI-003', 'CR-ORI-M6-L2', 'CR-ORI-M6-L2', h=960)
print('build47 ok'); print(' '.join(OUT))
