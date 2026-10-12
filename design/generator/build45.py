# build45: Module 4 Lesson 3 (Tiers and revalidation), check (CR-ORI-M4-K -> K1/K2/K3), Module 4 complete. usage: python3 build45.py <dir>
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
O.ICO['star'] = '<path d="m12 3.5 2.6 5.3 5.9.9-4.3 4.1 1 5.8-5.2-2.7-5.2 2.7 1-5.8-4.3-4.1 5.9-.9z"></path>'
MOD, MN = 4, 'Understanding validation'
STEPS = [('What validators look at', 'Lesson'), ('The validation case', 'Lesson'), ('Tiers and revalidation', 'Lesson'), ('Quick knowledge check', 'Check')]
s = O.lesson(rd('CR-ORI-003.dc.html'), MOD, MN, STEPS, 2, 2, 'Tiers and revalidation',
             'A successful case ends with a tier: Gold, Silver or Bronze. It describes the learning experience, not you.',
             O.note('Good to know', 'Learners keep access to the version they enrolled in.'),
             O.flow([('star', 'Validated', 'Your experience earns its tier.'), ('pen', 'You update it', 'Bigger changes start as a draft update.'), ('shield', 'Revalidation', 'Validators check only what changed.')], hub=2),
             ('CR-ORI-003.dc.html', 'The validation case'), ('CR-ORI-M4-K1.dc.html', 'Next'), 'Credalio · Orientation · Tiers and revalidation', scene=True)
wr('CR-ORI-M4-L3.dc.html', s); mob('CR-ORI-003', 'CR-ORI-M4-L3', 'CR-ORI-M4-L3', h=960)
Q = [['Multiple choice', 'Where do you answer a validator’s evidence request?', ['In Messages', 'In the Validation Workspace', 'By email'], 1, 'Everything about a case stays in the Validation Workspace.'],
     ['True or false', 'A course with three creators gets three validation cases.', ['True', 'False'], 1, 'One learning experience, one case. Requests go to the creator they concern.']]
wr('CR-ORI-M4-K.dc.html', O.check(rd('CR-ORI-004.dc.html'), MOD, MN, STEPS, Q, ('CR-ORI-M4-L3.dc.html', 'Tiers and revalidation'), 'CR-ORI-M4-DONE.dc.html', 'Credalio · Orientation · Module 4 check'))
SETW = rd('CR-SET-001.dc.html')
for b, v in [('K1', 'none'), ('K2', 'right'), ('K3', 'wrong')]:
    n = 'CR-ORI-M4-' + b
    wr(n + '.dc.html', SETW.replace('<dc-import name="CR-SET" variant="account"', f'<dc-import name="CR-ORI-M4-K" variant="{v}"').replace('CR-SET-001', n))
    mob('CR-ORI-004', n, 'CR-ORI-M4-K', v, 1000)
wr('CR-ORI-M4-DONE.dc.html', O.done(rd('CR-ORI-006.dc.html'), MOD, MN, 4, 'More than halfway there.', [],
   ['Answer requests in the Validation Workspace', 'Keep your evidence and sources ready'], 'CR-ORI-M5-00.dc.html', 'Credalio · Orientation · Module 4 complete'))
mob('CR-ORI-006', 'CR-ORI-M4-DONE', 'CR-ORI-M4-DONE', h=900)
print('build45 ok'); print(' '.join(OUT))
