# build27: discussions follow-ups + calendar month. CR-DISC variant unanswered (= DISC-001u, patches build26 source via wrapper only),
# CR-DTH thread one source, variants answered / reply / deep (= DISC-002 / 002b / 003), CR-CAL month (= CAL-001).
# Studio pages via build17 page(). usage: python3 build27.py <canvas project dir>
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build17 as B
from tipx import tip, TIP_CSS
P, rd, wr, ic, I, ARR = B.P, B.rd, B.wr, B.ic, B.I, B.ARR
CHK = ic('<path d="m5 12.5 4.5 4.5L19 7.5"></path>', 12, 3)
BACK = ic('<path d="M19 12H5"></path><path d="m11 6-6 6 6 6"></path>', 16, 2.2)
CODE = ic('<path d="m8 8-4 4 4 4M16 8l4 4-4 4"></path>', 17, 2.1)
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
.av.me{background:#0B1433;color:#FFFFFF}
@media (max-width: 960px){.pg-back{margin-top:12px}}
'''

# ======================= DISC-001u = CR-DISC variant unanswered =======================
wrap('CR-DISC', [('CR-DISC-001u', 'unanswered', 760)])

# ======================= CR-DTH · discussion thread =======================
Q_GB = ('Tunde A.', 'TA', '3 h ago', 'Why does my GROUP BY return duplicates?',
        'I still get repeated customers when I add the city column. What am I doing wrong?', 'SELECT customer_id, city, SUM(amount)\nFROM orders\nGROUP BY customer_id;')
main = ('<main class="ds-main hp">\n<a href="CR-DISC-001.dc.html" class="pg-back">' + BACK + 'Discussions</a>'
        '<div class="hp-head ob-in"><div><h1 class="ds-h1 dt-h1">{{title}}</h1></div><span class="st {{stCls}}">{{stTxt}}</span></div>'
        '<div class="dt-g">'
        '<div class="dt-col">'
        '<article class="ds-card dt-q ob-in2"><div class="dt-by"><span class="av">{{qAv}}</span><span><b>{{qBy}}</b><span>{{qTm}}</span></span></div>'
        '<p class="dt-p">{{qTx}}</p><sc-if value="{{hasCode}}" hint-placeholder-val="{{true}}"><pre class="dt-code">{{qCode}}</pre></sc-if></article>'
        '<sc-if value="{{hasReplies}}" hint-placeholder-val="{{true}}"><span class="hp-lab dt-n">{{nTxt}}</span>'
        '<ol class="dt-rl"><sc-for list="{{replies}}" as="r" hint-placeholder-count="3"><li class="dt-r {{r.cls}}">'
        '<sc-if value="{{r.ans}}" hint-placeholder-val="{{false}}"><span class="dt-ans">' + CHK + 'Answer</span></sc-if>'
        '<sc-if value="{{r.isNew}}" hint-placeholder-val="{{false}}"><span class="dt-new">New</span></sc-if>'
        '<div class="dt-by"><span class="av {{r.avc}}">{{r.av}}</span><span><b>{{r.by}}<sc-if value="{{r.cr}}" hint-placeholder-val="{{false}}"><em class="dt-cr">Creator</em></sc-if></b><span>{{r.tm}}</span></span></div>'
        '<p class="dt-p">{{r.tx}}</p></li></sc-for></ol></sc-if>'
        '<sc-if value="{{isReply}}" hint-placeholder-val="{{false}}"><div class="ds-card dt-cmp ob-in3">'
        '<div class="dt-ta">Add <code>city</code> to the GROUP BY as well. Every column in the SELECT that isn’t inside SUM, COUNT and so on has to be grouped, or the database can’t decide which city to show for each customer.<i></i></div>'
        '<div class="dt-cf"><button type="button" class="dt-tool" aria-label="Insert code">' + CODE + '</button><button type="button" class="dt-nova">' + ic(I['ai'], 15, 2) + 'Polish with Nova</button>'
        '<span style="flex:1"></span><label class="dt-mk"><span class="dt-box on">' + CHK + '</span>Mark as answer' + tip('Pins your reply to the top for anyone who asks this later.', 'r') + '</label><a href="CR-DISC-002.dc.html" class="ds-btn hp-btn"><span>Post answer</span><span class="ob-arrow">' + ARR + '</span></a></div></div></sc-if>'
        '<sc-if value="{{isQuick}}" hint-placeholder-val="{{true}}"><a href="CR-DISC-002b.dc.html" class="dt-qr ob-in3"><span class="av me">AO</span><span>Write a reply…</span></a></sc-if>'
        '</div>'
        '<aside class="ds-card dt-side ob-in2" aria-label="Asked in"><span class="hp-lab">Asked in</span><b>{{course}}</b><span>{{lesson}}</span>'
        '<a href="#" class="ds-link">Open lesson</a></aside>'
        '</div>\n</main>')
js = '''    const v = props.variant || 'answered';
    const gb = v === 'reply';
    const R = [
      { av: 'AO', avc: 'me', by: 'Ada Ononuju', cr: true, tm: 'Yesterday', ans: true, tx: 'An INNER JOIN only keeps customers that have orders. Use LEFT JOIN from customers to orders and every customer stays, with NULL where there’s no order.' },
      { av: 'CO', avc: '', by: 'Chioma O.', cr: false, tm: 'Yesterday', ans: false, tx: 'That makes sense. So COUNT(o.id) gives 0 for them instead of dropping them?' },
      { av: 'AO', avc: 'me', by: 'Ada Ononuju', cr: true, tm: '20 h ago', ans: false, tx: 'Exactly. COUNT of a column skips NULLs, so they show as 0.' }];
    if (v === 'deep') R.push({ av: 'CO', avc: '', by: 'Chioma O.', cr: false, tm: '2 min ago', ans: false, isNew: true, tx: 'It worked, all 214 customers show up now. Thank you!' });
    return { navCls: S.nav ? 'ds-open' : '', toggleNav: () => this.setState({ nav: !S.nav }),
      title: gb ? 'Why does my GROUP BY return duplicates?' : 'LEFT JOIN vs INNER JOIN with missing customers',
      stCls: gb ? 'am' : 'gr', stTxt: gb ? 'Unanswered' : 'Answered',
      qAv: gb ? 'TA' : 'CO', qBy: gb ? 'Tunde A.' : 'Chioma O.', qTm: gb ? '3 h ago' : '2 days ago',
      qTx: gb ? 'I still get repeated customers when I add the city column. What am I doing wrong?' : 'My report is missing customers who never ordered. I joined customers to orders. Why do they disappear?',
      hasCode: true, qCode: gb ? 'SELECT customer_id, city, SUM(amount)\\nFROM orders\\nGROUP BY customer_id;' : 'SELECT c.name, COUNT(o.id)\\nFROM customers c\\nJOIN orders o ON o.customer_id = c.id\\nGROUP BY c.name;',
      hasReplies: !gb, nTxt: R.length + ' replies', replies: R.map((r) => Object.assign({ isNew: false }, r, { cls: (r.ans ? 'is-ans' : '') + (r.isNew ? ' is-new' : '') })),
      isReply: gb, isQuick: !gb,
      course: 'Data Analysis with SQL', lesson: gb ? 'Chapter 4 · Lesson 4.2 Grouping' : 'Chapter 3 · Lesson 3.1 Joins' };'''
css = COMMON + '''
.dt-h1{max-width:960px}
.dt-g{margin-top:4px}
main .hp-head:has(.dt-h1){align-items:center}
.dt-g{display:grid;grid-template-columns:minmax(0,1fr) 300px;gap:24px;align-items:start}
.dt-col{display:flex;flex-direction:column;min-width:0}
.dt-q{padding:24px 28px}
.dt-by{display:flex;align-items:center;gap:12px}
.dt-by > span:last-child{display:flex;flex-direction:column;gap:2px}
.dt-by b{display:inline-flex;align-items:center;gap:8px;font-size:15px;font-weight:600}.dt-by > span:last-child > span{font-size:13px;color:#5B6582}
.dt-cr{font-style:normal;height:22px;padding:0 9px;border-radius:999px;background:#EAF0FF;color:#0E3BB8;font-size:12px;font-weight:500;display:inline-flex;align-items:center}
.dt-p{margin:14px 0 0 0;font-size:15px;line-height:1.6;color:#1E2742}
.dt-code{margin:16px 0 0 0;padding:16px 18px;border-radius:14px;background:#0B1433;color:#DCE4FF;font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:13.5px;line-height:1.6;white-space:pre-wrap;overflow-x:auto}
.dt-n{margin:32px 0 12px 4px}
.dt-rl{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:12px}
.dt-r{position:relative;padding:20px 24px;border-radius:18px;background:#FFFFFF;border:1.5px solid #E6EAF3}
.dt-r .dt-p{margin-top:10px;padding-left:48px}
.dt-r.is-ans{border-color:#BFE3CF;background:linear-gradient(#F6FCF9,#FFFFFF)}
.dt-r.is-new{border-color:#AFC1F5;box-shadow:0 0 0 4px rgba(22,82,240,.10)}
.dt-ans,.dt-new{position:absolute;top:20px;right:22px;display:inline-flex;align-items:center;gap:6px;height:26px;padding:0 11px;border-radius:999px;font-size:12.5px;font-weight:500}
.dt-ans{background:#E7F5EE;color:#0F6B45}
.dt-new{background:#1652F0;color:#FFFFFF}
.dt-qr{margin-top:20px;display:flex;align-items:center;gap:12px;padding:14px 18px;border-radius:18px;background:#FFFFFF;border:1.5px solid #E6EAF3;color:#8A93AD;font-size:15px;text-decoration:none}
.dt-qr:hover{border-color:#AFC1F5}
.dt-qr .av{width:30px;height:30px;font-size:11px}
.dt-cmp{margin-top:20px;padding:22px 24px 18px 24px;border-color:#AFC1F5;box-shadow:0 0 0 4px rgba(22,82,240,.08)}
.dt-cmp .dt-by .av{width:30px;height:30px;font-size:11px}
.dt-ta{position:relative;margin-top:0;font-size:15px;line-height:1.6;color:#0B1433;min-height:96px}
.dt-ta code{padding:1px 6px;border-radius:6px;background:#F1F3F8;font-size:13.5px}
.dt-ta i{display:inline-block;width:2px;height:18px;margin-left:2px;vertical-align:-3px;background:#1652F0;animation:dtBlink 1s steps(1) infinite}
@keyframes dtBlink{50%{opacity:0}}
.dt-cf{margin-top:16px;padding-top:14px;border-top:1.5px solid #F0F2F8;display:flex;align-items:center;gap:10px}
.dt-tool{width:38px;height:38px;border-radius:12px;border:1.5px solid #E6EAF3;background:#FFFFFF;color:#4A5578;display:inline-flex;align-items:center;justify-content:center;cursor:pointer}
.dt-nova{display:inline-flex;align-items:center;gap:7px;height:38px;padding:0 14px;border-radius:999px;border:1.5px solid #D6DDEE;background:#FFFFFF;color:#0E3BB8;font-family:inherit;font-size:13.5px;font-weight:500;cursor:pointer}
.dt-mk{display:inline-flex;align-items:center;gap:8px;font-size:14px;color:#3A4566;margin-right:6px;cursor:pointer}
.dt-box{width:20px;height:20px;border-radius:6px;border:1.5px solid #CBD3E6;display:inline-flex;align-items:center;justify-content:center;color:#FFFFFF}
.dt-box.on{background:#1652F0;border-color:#1652F0}
.dt-side{position:sticky;top:96px;padding:22px 24px;display:flex;flex-direction:column;gap:4px}
.dt-side b{margin-top:8px;font-size:15.5px;font-weight:600}.dt-side > span:not(.hp-lab){font-size:14px;color:#5B6582}
.dt-side .ds-link{margin-top:14px;font-size:14px;font-weight:600}
@media (max-width: 1080px){.dt-g{grid-template-columns:minmax(0,1fr)}.dt-side{position:static;order:-1;flex-direction:row;flex-wrap:wrap;align-items:baseline;gap:4px 8px;padding:14px 18px}.dt-side .hp-lab{width:100%}.dt-side b{margin:0;font-size:14.5px}.dt-side .ds-link{margin:0 0 0 auto}}
@media (max-width: 960px){
.hp-head{flex-direction:row;align-items:flex-start}
.dt-h1{font-size:22px !important;line-height:1.25}
.dt-g{gap:14px}
.dt-side{display:none}
.dt-q{padding:18px}
.dt-p{font-size:14.5px}
.dt-code{font-size:12.5px;padding:14px}
.dt-n{margin:26px 0 10px 2px}
.dt-r{padding:16px 16px}
.dt-r .dt-p{padding-left:0}
.dt-ans,.dt-new{top:16px;right:14px}
.dt-cmp{padding:16px 16px 14px 16px}
.dt-cf{flex-wrap:wrap}
.dt-cf .hp-btn{width:100%;justify-content:space-between}
}
'''
B.page('CR-DTH', 'Discussions', main, js, css, 'Credalio · Discussion', "{ nav: false }")
props_patch('CR-DTH')
wrap('CR-DTH', [('CR-DISC-002', 'answered', 1240), ('CR-DISC-002b', 'reply', 860), ('CR-DISC-003', 'deep', 1260)])

# CR-CAL moved to build28.py (all calendar views).
print('build27 ok')
