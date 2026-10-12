# build40: Link 1 batch 2. PATCHES live CR-ONB-007 (variant proactive = ONB-007p), CR-RDY-001 (variant done = RDY-001d),
# CR-ORI-001 (variants start / done = ORI-001n / ORI-001c); writes CR-ORI-M1-00 (module 1 overview, from LIVE CR-ORI-002) + wrappers.
# Asserts if already patched. usage: python3 build40.py <dir>  (scratch copy; copy back printed files)
import re, sys, os
P = sys.argv[1]
def rd(f): return open(os.path.join(P, f), encoding='utf-8').read()
def wr(f, s): open(os.path.join(P, f), 'w', encoding='utf-8').write(s)
OUT = []
def sub1(s, a, b):
    assert s.count(a) == 1, (s.count(a), a[:90]); return s.replace(a, b, 1)
def add_css(s, css):
    i = s.rfind('</style>', 0, s.find('</helmet>')); return s[:i] + css + s[i:]
def wrap(src, n, var, hd, hm):
    d = rd('CR-SET-001.dc.html').replace('<dc-import name="CR-SET" variant="account"', f'<dc-import name="{src}"' + (f' variant="{var}"' if var else '')).replace('CR-SET-001', n)
    d = d.replace('height: 820px', f'height: {hd}px').replace('hint-size="1440px,820px"', f'hint-size="1440px,{hd}px"').replace('"height":820}', f'"height":{hd}}}')
    wr(n + '.dc.html', d); OUT.append(n + '.dc.html')
    m = rd(src + '-Mobile.dc.html').replace(f'<dc-import name="{src}"', f'<dc-import name="{src}"' + (f' variant="{var}"' if var else ''))
    m = re.sub(r'<title>.*?</title>', f'<title>{n} mobile preview</title>', m)
    m = re.sub(r'height: \d+px; overflow', f'height: {hm}px; overflow', m, count=1)
    m = re.sub(r'hint-size="390px,\d+px"', f'hint-size="390px,{hm}px"', m)
    m = re.sub(r'"\$preview":\{"width":390,"height":\d+\}', f'"$preview":{{"width":390,"height":{hm}}}', m)
    wr(n + '-Mobile.dc.html', m); OUT.append(n + '-Mobile.dc.html')
TICK = '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"></path></svg>'
DONE_PILL = f'<span class="st-pill" style="background: #E7F5EE; color: #0F6B45">{TICK}Complete</span>'

# ======================= ONB-007p · Proactive selected =======================
s = rd('CR-ONB-007.dc.html')
assert 'build40' not in s, 'CR-ONB-007 already patched'
s = sub1(s, "constructor(props) { super(props); this.state = { sel: 'concise', i: 0, phase: 'wait' }; }",
         "constructor(props) { super(props); this.state = { sel: (props && props.variant === 'proactive') ? 'proactive' : 'concise', i: 0, phase: 'wait' }; } /* build40 */")
wr('CR-ONB-007.dc.html', s); OUT.append('CR-ONB-007.dc.html')
wrap('CR-ONB-007', 'CR-ONB-007p', 'proactive', 820, 900)

# ======================= RDY-001d · all tasks complete =======================
s = rd('CR-RDY-001.dc.html')
assert 'isDone' not in s, 'CR-RDY-001 already patched'
m = re.search(r'<sc-if value="\{\{isNew\}\}" hint-placeholder-val="\{\{false\}\}">', s)
end = s.index('</div></sc-if>', m.start()) + len('</div></sc-if>')
blk = s[m.start():end].replace('{{isNew}}', '{{isDone}}')
blk = sub1(blk, 'stroke="#1652F0" stroke-width="9" stroke-linecap="round" pathLength="100" stroke-dasharray="20 100"', 'stroke="#0F6B45" stroke-width="9" stroke-linecap="round" pathLength="100" stroke-dasharray="100 100"')
blk = sub1(blk, '<b class="rd-pct">20%</b>', '<b class="rd-pct">100%</b>')
blk = sub1(blk, '<span class="rd-sc"><b>1 of 5 done</b><span>4 to go before you can submit</span></span>', '<span class="rd-sc"><b>All 5 done</b><span>Every check is complete</span></span>')
blk = sub1(blk, '<h1 class="ds-h1">Your readiness</h1><p class="ds-sub">Keep creating while you complete the checks for validation.</p>', '<h1 class="ds-h1">You’re ready to submit.</h1>')
blk = re.sub(r'<b>Start with your identity\.[^<]*</b>', '<b>When a draft feels ready, send it for validation. I can check it with you first.</b>', blk)
blk = re.sub(r'<a href="CR-KYC-001\.dc\.html" class="ds-btn rd-go"><span>Verify my identity</span>', '<a href="CR-HOME-EXP.dc.html" class="ds-btn rd-go"><span>Open my drafts</span>', blk)
# every requirement row: complete, no description, no action
ul_s = blk.index('<ul class="ds-card rd-list">'); ul_e = blk.index('</ul>', ul_s)
rows = blk[ul_s:ul_e]
rows = rows.replace('<li class="rd-row">', '<li class="rd-row rd-done">')
rows = re.sub(r'<span class="rd-d">[^<]*</span>', '', rows)
rows = re.sub(r'<span class="rd-st"><span class="st-pill"[^>]*>Not started</span></span><a href="[^"]*" class="rd-cta"[^>]*>[^<]*<svg.*?</svg></a>', '<span class="rd-st">' + DONE_PILL + '</span><span class="rd-cta-sp"></span>', rows, flags=re.S)
assert rows.count('Complete</span>') == 5, rows.count('Complete</span>')
blk = blk[:ul_s] + rows + blk[ul_e:]
s = s[:end] + '\n' + blk + s[end:]
s = sub1(s, '<span class="ds-badge" aria-label="3 to do">3</span>', '<sc-if value="{{badge}}" hint-placeholder-val="{{true}}"><span class="ds-badge" aria-label="3 to do">3</span></sc-if>')
s = sub1(s, "return { navCls: this.state.nav ? 'ds-open' : '', toggleNav: () => this.setState({ nav: !this.state.nav }), isNew, isMid: !isNew };",
         "const isDone = (this.props || {}).variant === 'done';\n    return { navCls: this.state.nav ? 'ds-open' : '', toggleNav: () => this.setState({ nav: !this.state.nav }), isNew, isDone, badge: !isDone, isMid: !isNew && !isDone };")
wr('CR-RDY-001.dc.html', s); OUT.append('CR-RDY-001.dc.html')
wrap('CR-RDY-001', 'CR-RDY-001d', 'done', 1160, 1400)

# ======================= ORI-001n / 001c =======================
s = rd('CR-ORI-001.dc.html')
assert 'isStart' not in s, 'CR-ORI-001 already patched'
gs = s.index('<div class="or-grid">'); ge = s.index('</main>')
mid = s[gs:ge]
MODS = [('Welcome to Credalio', '2 lessons · check · 8 min', '8 min'), ('Creating trusted learning', '2 lessons · check · 10 min', '10 min'),
        ('Outcomes, skills & evidence', '3 lessons · check · 12 min', '12 min'), ('Understanding validation', '3 lessons · check · 12 min', '12 min'),
        ('AI & responsible creation', '2 lessons · check · scenario · 10 min', '10 min'), ('Creator economy', '2 lessons · check · 10 min', '10 min'),
        ('Creator responsibilities', '2 lessons · check · scenario · 8 min', '8 min')]
done_li = re.search(r'<li class="or-m or-done">.*?</li>', mid, re.S).group(0)
lock_li = re.search(r'<li class="or-m"><span class="or-n">5</span>.*?</li>', mid, re.S).group(0)
cur_li = re.search(r'<li class="or-m or-cur">.*?</ol></div>.*?</li>', mid, re.S).group(0)
def li_done(i, t, meta): return re.sub(r'Module 1 · </span>Welcome to Credalio</b><span>[^<]*</span>', f'Module {i} · </span>{t}</b><span>{meta}</span>', done_li)
def li_lock(i, t, meta, mins): return lock_li.replace('<span class="or-n">5</span>', f'<span class="or-n">{i}</span>').replace('Module 5 · </span>AI & responsible creation</b><span>2 lessons · check · scenario · 10 min</span>', f'Module {i} · </span>{t}</b><span>{meta}</span>').replace('10 min</span></li>', f'{mins}</span></li>')
# start: module 1 open with its steps, nothing done yet
c1 = cur_li.replace('<span class="or-n">4</span>', '<span class="or-n">1</span>')
c1 = re.sub(r'Module 4 · </span>Understanding validation</b><span>[^<]*</span>', 'Module 1 · </span>Welcome to Credalio</b><span>2 lessons · check · 8 min</span>', c1)
c1 = c1.replace('<p class="or-desc">Learn what validators review and how your case moves forward.</p>', '<p class="or-desc">What Credalio is for, and how creating here works from idea to published learning.</p>')
st_s = c1.index('<ol class="or-steps">'); st_e = c1.index('</ol>', st_s) + 5
nxt = re.search(r'<li class="or-s or-s-next">.*?</li>', c1, re.S).group(0); todo = re.search(r'<li class="or-s or-s-todo">.*?</li>', c1, re.S).group(0)
steps = ('<ol class="or-steps">' + nxt.replace('The validation case', 'What Credalio is for')
         + todo.replace('Tiers and revalidation', 'How creating on Credalio works') + todo.replace('Tiers and revalidation', 'Quick knowledge check') + '</ol>')
c1 = c1[:st_s] + steps + c1[st_e:]
c1 = re.sub(r'<span class="st-pill" style="background: #EAF0FF; color: #1652F0">In progress</span>', '', c1)
ring = re.search(r'<span class="rg" style="width: 88px; height: 88px">.*?</span></span>', mid, re.S).group(0)
def rail(pct, col, lab, title, sub, href, cta, stats):
    r = ring.replace('stroke-dasharray="44 100"', f'stroke-dasharray="{pct} 100"' + (' stroke-opacity="0"' if pct == 0 else '')).replace('stroke="#1652F0" stroke-width="9" stroke-linecap="round"', f'stroke="{col}" stroke-width="9" stroke-linecap="round"').replace('>44%<', f'>{pct}%<')
    return (f'<aside class="or-rail"><div class="ds-card or-next ob-in2"><div class="or-nt">{r}<span style="display: flex; flex-direction: column; gap: 3px; min-width: 0">'
            f'<span class="or-lab">{lab}</span><b class="or-nb">{title}</b><span class="or-ns">{sub}</span></span></div>'
            f'<a href="{href}" class="ds-btn or-cta"><span>{cta}</span><span class="ob-arrow">' + re.search(r'<span class="ob-arrow">(.*?)</span>', mid, re.S).group(1) + '</span></a>'
            + (f'<dl class="or-stats">{stats}</dl>' if stats else '') + '</div></aside>')
start = ('<div class="or-grid"><section class="or-col ob-in2" aria-label="Modules"><ol class="or-list or-l0">' + c1
         + ''.join(li_lock(i + 1, t, m, mm) for i, (t, m, mm) in enumerate(MODS) if i > 0) + '</ol></section>'
         + rail(0, '#1652F0', 'Up next', 'Welcome to Credalio', 'Module 1 · about 8 min', 'CR-ORI-M1-00.dc.html', 'Start', '<div><dt>Modules</dt><dd>7</dd></div><div><dt>Total</dt><dd>~70 min</dd></div>') + '</div>')
done = ('<div class="or-grid"><section class="or-col ob-in2" aria-label="Modules"><ol class="or-list or-l100">'
        + ''.join(li_done(i + 1, t, m) for i, (t, m, mm) in enumerate(MODS)) + '</ol></section>'
        + rail(100, '#0F6B45', 'Complete', 'All 7 modules done', 'Orientation counts toward your readiness.', 'CR-RDY-001d.dc.html', 'Back to readiness', '') + '</div>')
s = s[:gs] + '<sc-if value="{{isMid}}" hint-placeholder-val="{{true}}">' + mid + '</sc-if><sc-if value="{{isStart}}" hint-placeholder-val="{{false}}">' + start + '</sc-if><sc-if value="{{isDone}}" hint-placeholder-val="{{false}}">' + done + '</sc-if>\n' + s[ge:]
s = sub1(s, "renderVals() { return { navCls: this.state.nav ? 'ds-open' : '', toggleNav: () => this.setState({ nav: !this.state.nav }) }; }",
         "renderVals() { const v = (this.props || {}).variant || ''; return { navCls: this.state.nav ? 'ds-open' : '', toggleNav: () => this.setState({ nav: !this.state.nav }), isStart: v === 'start', isDone: v === 'done', isMid: v !== 'start' && v !== 'done' }; }")
s = add_css(s, '\n/* build40 line per state */\n.or-list.or-l0::before{background:#E6EAF3 !important}\n.or-list.or-l100::before{background:#1652F0 !important}\n')
wr('CR-ORI-001.dc.html', s); OUT.append('CR-ORI-001.dc.html')
wrap('CR-ORI-001', 'CR-ORI-001n', 'start', 1050, 900)
wrap('CR-ORI-001', 'CR-ORI-001c', 'done', 1050, 880)

# ======================= ORI-M1-00 · module 1 overview =======================
s = rd('CR-ORI-002.dc.html')
s = sub1(s, '<span class="lp-t2">Module 4 · Understanding validation</span>', '<span class="lp-t2">Module 1 · Welcome to Credalio</span>')
s = sub1(s, '<div class="lp-segs" aria-hidden="true"><span class="lp-seg lp-seg-done"></span><span class="lp-seg lp-seg-cur"></span><span class="lp-seg lp-seg-todo"></span><span class="lp-seg lp-seg-todo"></span></div>',
         '<div class="lp-segs" aria-hidden="true"><span class="lp-seg lp-seg-cur"></span><span class="lp-seg lp-seg-todo"></span><span class="lp-seg lp-seg-todo"></span></div>')
s = sub1(s, '<span class="lp-tn">4 steps</span>', '<span class="lp-tn">3 steps</span>')
s = sub1(s, '<span class="lp-eb ob-in">Module 4 of 7</span>', '<span class="lp-eb ob-in">Module 1 of 7</span>')
s = sub1(s, '<h1 class="lp-h1 ob-in">Understanding validation</h1>', '<h1 class="lp-h1 ob-in">Welcome to Credalio</h1>')
s = sub1(s, 'Learn what validators review and how your case moves forward.', 'What Credalio is for, and how creating here works from idea to published learning.')
s = sub1(s, 'About 12 minutes</span>', 'About 8 minutes</span>')
s = sub1(s, '3 lessons</span>', '2 lessons</span>')
# not started: no progress box; the start button sits under the facts
a0 = s.index('<div class="mo2-act ob-in2">'); a1 = s.index('</div>', s.index('</a>', a0)) + 6
btn = s[s.index('<a href="CR-ORI-003.dc.html" class="ds-btn mo-go">', a0):s.index('</a>', a0) + 4]
s = s[:a0] + s[a1:]
btn = btn.replace('href="CR-ORI-003.dc.html"', 'href="CR-ORI-M1-L1.dc.html"').replace('<span>Continue</span>', '<span>Start module</span>').replace('class="ds-btn mo-go"', 'class="ds-btn mo-go mo-go-new ob-in2"')
f0 = s.index('<div class="mo-facts ob-in2">'); f1 = s.index('</div>', f0) + 6
s = s[:f1] + btn + s[f1:]
l0 = s.index('<ol class="mo-list">'); l1 = s.index('</ol>', l0) + 5
nx = re.search(r'<li class="mo-r mo-next">.*?</li>', s[l0:l1], re.S).group(0); td = re.search(r'<li class="mo-r mo-todo">.*?</li>', s[l0:l1], re.S).group(0)
steps = ('<ol class="mo-list">' + nx.replace('The validation case', 'What Credalio is for') + td.replace('Tiers and revalidation', 'How creating on Credalio works')
         + td.replace('Tiers and revalidation', 'Quick knowledge check').replace('<span>Lesson</span>', '<span>Check</span>') + '</ol>')
s = s[:l0] + steps + s[l1:]
s = sub1(s, '<span>Validators are independent and criteria-based</span>', '<span>Credalio is built on validated, verifiable learning</span>')
s = sub1(s, '<span>One learning experience has one validation case</span>', '<span>The path is create, validate, publish</span>')
s = sub1(s, '<span>Material changes may need revalidation</span>', '<span>Readiness gates submitting, never drafting</span>')
s = add_css(s, '\n/* build40 module not started */\n.mo-go.mo-go-new{margin-top:28px;width:auto}\n@media (max-width: 960px){.mo-go.mo-go-new{width:100%;margin-top:22px}}\n')
s = re.sub(r'<title>.*?</title>', '<title>Credalio · Orientation · Module 1</title>', s)
wr('CR-ORI-M1-00.dc.html', s); OUT.append('CR-ORI-M1-00.dc.html')
m = rd('CR-ORI-002-Mobile.dc.html').replace('<dc-import name="CR-ORI-002"', '<dc-import name="CR-ORI-M1-00"')
m = re.sub(r'<title>.*?</title>', '<title>CR-ORI-M1-00 mobile preview</title>', m)
wr('CR-ORI-M1-00-Mobile.dc.html', m); OUT.append('CR-ORI-M1-00-Mobile.dc.html')
print('build40 ok'); print(' '.join(OUT))
