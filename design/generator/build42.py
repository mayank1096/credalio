# build42: M1-DONE + Module 2 (00, L1, L2, check source CR-ORI-M2-K with board K1). Templates: LIVE CR-ORI-006 (done),
# LIVE CR-ORI-M1-00 (overview with Nova), LIVE CR-ORI-003 (lesson), LIVE CR-ORI-004 (check). usage: python3 build42.py <dir>
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ori_m as O
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
# ---- M1 complete ----
wr('CR-ORI-M1-DONE.dc.html', O.done(rd('CR-ORI-006.dc.html'), 1, 'Welcome to Credalio', 3, 'One of seven done. A good start.',
   ['Credalio is built on validated, verifiable learning', 'The path is create, validate, publish', 'Readiness gates submitting, never drafting'],
   ['Create in good faith for real learners', 'Finish readiness before you submit'], 'CR-ORI-M2-00.dc.html', 'Credalio · Orientation · Module 1 complete'))
mob('CR-ORI-006', 'CR-ORI-M1-DONE', 'CR-ORI-M1-DONE', h=960)
# ---- Module 2 ----
MOD, MN = 2, 'Creating trusted learning'
STEPS = [('What makes learning trustworthy', 'Lesson'), ('Evidence of learning', 'Lesson'), ('Quick knowledge check', 'Check')]
wr('CR-ORI-M2-00.dc.html', O.overview(rd('CR-ORI-M1-00.dc.html'), MOD, MN, STEPS, 10,
   'What makes learning trustworthy, and how learners show what they can do.',
   'Nice start, Ada. This one is about why people trust what they learn.',
   ['Trust comes from outcomes, accuracy and evidence', 'Evidence is something learners do'], 'CR-ORI-M2-L1.dc.html', 'Credalio · Orientation · Module 2'))
mob('CR-ORI-002', 'CR-ORI-M2-00', 'CR-ORI-M2-00')
L = rd('CR-ORI-003.dc.html')
s = O.lesson(L, MOD, MN, STEPS, 0, 3, 'What makes learning trustworthy',
             'Trusted learning is accurate, current and honest about what learners will be able to do. It is built around outcomes, not the amount of content.',
             None, O.roles([('target', 'Clear outcomes', 'Learners know what they’ll be able to do.'), ('check', 'Accurate content', 'Sources are sound and current.'), ('doc', 'Real evidence', 'Practice and assessment prove the outcome.')]),
             ('CR-ORI-M2-00.dc.html', 'Module overview'), ('CR-ORI-M2-L2.dc.html', 'Next lesson'), 'Credalio · Orientation · What makes learning trustworthy', scene=True)
wr('CR-ORI-M2-L1.dc.html', s); mob('CR-ORI-003', 'CR-ORI-M2-L1', 'CR-ORI-M2-L1', h=900)
s = O.lesson(L, MOD, MN, STEPS, 1, 3, 'Evidence of learning',
             'Watching a video isn’t evidence. Evidence is something a learner does that shows the outcome: a query that runs, a model that balances, a project that works.',
             None, O.compare('“Watch the lesson on joins.”', '“Write a query that joins orders to customers and returns each customer’s total spend.”'),
             ('CR-ORI-M2-L1.dc.html', 'What makes learning trustworthy'), ('CR-ORI-M2-K1.dc.html', 'Next'), 'Credalio · Orientation · Evidence of learning', scene=True)
wr('CR-ORI-M2-L2.dc.html', O.with_css(s, O.COMPARE_CSS)); mob('CR-ORI-003', 'CR-ORI-M2-L2', 'CR-ORI-M2-L2', h=900)
Q = [['Scenario', 'Which is the strongest evidence that a learner can join tables in SQL?', ['They watched the joins video', 'They wrote a working join in a practice task', 'They rated the lesson 5 stars'], 1, 'Evidence is something the learner does that shows the outcome.'],
     ['True or false', 'More content always makes a course more trustworthy.', ['True', 'False'], 1, 'Trust comes from clear outcomes, accuracy and evidence, not volume.']]
wr('CR-ORI-M2-K.dc.html', O.check(rd('CR-ORI-004.dc.html'), MOD, MN, STEPS, Q, ('CR-ORI-M2-L2.dc.html', 'Evidence of learning'), 'CR-ORI-M2-DONE.dc.html', 'Credalio · Orientation · Module 2 check'))
SETW = rd('CR-SET-001.dc.html')
wr('CR-ORI-M2-K1.dc.html', SETW.replace('<dc-import name="CR-SET" variant="account"', '<dc-import name="CR-ORI-M2-K" variant="none"').replace('CR-SET-001', 'CR-ORI-M2-K1'))
mob('CR-ORI-004', 'CR-ORI-M2-K1', 'CR-ORI-M2-K', 'none', 960)
print('build42 ok'); print(' '.join(OUT))
