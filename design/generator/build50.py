# build50: M7 scenario CR-ORI-M7-S (from LIVE CR-ORI-005; variants none / right / wrong = boards M7-S1 / S2 / S3), M7-DONE (final module),
# M4-L2 "The validation case" (new lesson; M4-L1 next and M4-L3 prev re-pointed to it; our CR-ORI-003 untouched). usage: python3 build50.py <dir>
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
def sub(s, a, b, n=1):
    assert s.count(a) >= 1, a; return s.replace(a, b, n)
# ---- M7 scenario ----
s = rd('CR-ORI-005.dc.html')
s = sub(s, '<span class="lp-t2">Module 5 · AI & responsible creation</span>', '<span class="lp-t2">Module 7 · Creator responsibilities</span>')
for a, b in [('Using your Copilot well', 'Your obligations to learners'), ('Review, disclose, own', 'Declarations and changes')]:
    s = sub(s, f'<b>{a}</b>', f'<b>{b}</b>')
s = sub(s, '<h1 class="lp-h1 ob-in">An AI-drafted lesson</h1>', '<h1 class="lp-h1 ob-in">Changing a published course</h1>')
s = sub(s, 'A creator uses AI to generate an entire lesson. <b>What must happen before it goes to validation?</b>',
        'Your course is live and learners are enrolled. You want to replace Chapter 3. <b>What happens next?</b>')
s = re.sub(r'<span class="sc-tag"><svg.*?</svg>AI-drafted · not reviewed yet</span><b>Cleaning messy data, fast</b>',
           '<span class="sc-tag">' + O.svg('pen', 12, 2.2) + 'Draft update · not live yet</span><b>Chapter 3 · Joins in practice</b>', s, count=1, flags=re.S)
assert 'Draft update' in s
s = sub(s, "const O = ['Nothing, AI content is pre-approved', 'The creator reviews it, checks sources and discloses AI help', 'The validator rewrites it'];",
        "const O = ['Swap it in now, learners won’t notice', 'Save it as a draft update. Credalio checks it before it goes live', 'Unpublish the course'];")
s = sub(s, "'Creators stay accountable for everything they submit, however it was made.'", "'Bigger changes are checked first, and learners keep what they enrolled in.'")
s = sub(s, "'Think about who is accountable for the content.'", "'Think about what learners were promised.'")
s = sub(s, '<a href="CR-ORI-M5-K1.dc.html" class="lp-prev">', '<a href="CR-ORI-M7-K1.dc.html" class="lp-prev">')
s = sub(s, '<a href="CR-ORI-006.dc.html" class="ds-btn lp-next', '<a href="CR-ORI-M7-DONE.dc.html" class="ds-btn lp-next')
s = re.sub(r'<title>.*?</title>', '<title>Credalio · Orientation · Module 7 scenario</title>', s)
wr('CR-ORI-M7-S.dc.html', s)
for b, v in [('S1', 'none'), ('S2', 'right'), ('S3', 'wrong')]:
    board('CR-ORI-M7-' + b, 'CR-ORI-M7-S', v); mob('CR-ORI-005', 'CR-ORI-M7-' + b, 'CR-ORI-M7-S', v, 960)
# ---- M7 complete (last module) ----
s = O.done(rd('CR-ORI-006.dc.html'), 7, 'Creator responsibilities', 4, 'That’s all seven. Orientation is done.', [],
           ['Keep content accurate and current', 'Support learners as promised'], 'CR-ORI-001c.dc.html', 'Credalio · Orientation · Module 7 complete')
s = re.sub(r'(class="ds-btn dn-go">\s*<span>)[^<]*(</span>)', r'\1Finish orientation\2', s, count=1); assert 'Finish orientation' in s
s = sub(s, '<a href="CR-ORI-001.dc.html" class="dn-back">Back to Orientation</a>', '')
wr('CR-ORI-M7-DONE.dc.html', s); mob('CR-ORI-006', 'CR-ORI-M7-DONE', 'CR-ORI-M7-DONE', h=900)
# ---- M4 Lesson 2 ----
O.ICO['chat'] = '<path d="M20 12a8 8 0 0 1-11.6 7.1L4 20l1-4.2A8 8 0 1 1 20 12z"></path><path d="M8.5 11h7M8.5 14h4"></path>'
O.ICO['cal'] = '<rect x="4" y="5.5" width="16" height="14.5" rx="3"></rect><path d="M8 3.5v4M16 3.5v4M4 10h16"></path>'
STEPS4 = [('What validators look at', 'Lesson'), ('The validation case', 'Lesson'), ('Tiers and revalidation', 'Lesson'), ('Quick knowledge check', 'Check')]
s = O.lesson(rd('CR-ORI-003.dc.html'), 4, 'Understanding validation', STEPS4, 1, 2, 'The validation case',
             'One learning experience has one case. Everything with validators happens in the Validation Workspace.',
             None, O.roles([('chat', 'Ask', 'For clarification or evidence.'), ('cal', 'Meet', 'Propose a short call.'), ('doc', 'Raise findings', 'Things to fix before a tier.')]),
             ('CR-ORI-M4-L1.dc.html', 'What validators look at'), ('CR-ORI-M4-L3.dc.html', 'Next lesson'), 'Credalio · Orientation · The validation case', scene=True)
s = sub(s, '<b>Ask</b>', '<b>Ask' + tipx.tip('With several creators, a request about Mary’s chapter goes to Mary. The Lead Creator sees it too.') + '</b>')
wr('CR-ORI-M4-L2.dc.html', O.with_css(s, '\n/* build50 tooltip */' + tipx.TIP_CSS + '.ls-roles .tip{margin-left:4px}\n')); mob('CR-ORI-003', 'CR-ORI-M4-L2', 'CR-ORI-M4-L2', h=900)
s = sub(rd('CR-ORI-M4-L1.dc.html'), 'href="CR-ORI-003.dc.html" class="ds-btn lp-next"', 'href="CR-ORI-M4-L2.dc.html" class="ds-btn lp-next"'); wr('CR-ORI-M4-L1.dc.html', s)
s = sub(rd('CR-ORI-M4-L3.dc.html'), 'href="CR-ORI-003.dc.html" class="lp-prev"', 'href="CR-ORI-M4-L2.dc.html" class="lp-prev"'); wr('CR-ORI-M4-L3.dc.html', s)
print('build50 ok'); print(' '.join(OUT))
