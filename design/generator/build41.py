# build41: Orientation Module 1 lessons + check (Link 1): CR-ORI-M1-L1, CR-ORI-M1-L2, CR-ORI-M1-K (variants none / right / wrong
# = boards CR-ORI-M1-K1 / K2 / K3). Templates: LIVE CR-ORI-003 (lesson) / CR-ORI-004 (check) via ori_m.py.
# usage: python3 build41.py <dir>  (scratch copy; copy back printed files)
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ori_m as O
P = sys.argv[1]
def rd(f): return open(os.path.join(P, f), encoding='utf-8').read()
def wr(f, s): open(os.path.join(P, f), 'w', encoding='utf-8').write(s)
OUT = []
def mob(src_tpl, n, imp, var=None, h=None):
    m = rd(src_tpl + '-Mobile.dc.html').replace(f'<dc-import name="{src_tpl}"', f'<dc-import name="{imp}"' + (f' variant="{var}"' if var else ''))
    m = re.sub(r'<title>.*?</title>', f'<title>{n} mobile preview</title>', m)
    if h:
        m = re.sub(r'height: \d+px; overflow', f'height: {h}px; overflow', m, count=1)
        m = re.sub(r'hint-size="390px,\d+px"', f'hint-size="390px,{h}px"', m)
        m = re.sub(r'"\$preview":\{"width":390,"height":\d+\}', f'"$preview":{{"width":390,"height":{h}}}', m)
    wr(n + '-Mobile.dc.html', m); OUT.append(n + '-Mobile.dc.html')
MOD, MN = 1, 'Welcome to Credalio'
STEPS = [('What Credalio is for', 'Lesson'), ('How creating on Credalio works', 'Lesson'), ('Quick knowledge check', 'Check')]
L = rd('CR-ORI-003.dc.html'); K = rd('CR-ORI-004.dc.html')

s = O.lesson(L, MOD, MN, STEPS, 0, 3, 'What Credalio is for',
             'A marketplace for trusted learning. Independent experts validate every learning experience, and employers can verify every credential.',
             None,
             O.video('Welcome from the Credalio team · 2:40')
             + O.roles([('cap', 'Learners', 'Gain skills they can prove.'), ('pen', 'Creators', 'Turn expertise into validated learning.'), ('shield', 'Validators', 'Independent experts who check quality.')]),
             ('CR-ORI-M1-00.dc.html', 'Module overview'), ('CR-ORI-M1-L2.dc.html', 'Next lesson'), 'Credalio · Orientation · What Credalio is for')
wr('CR-ORI-M1-L1.dc.html', s); OUT.append('CR-ORI-M1-L1.dc.html'); mob('CR-ORI-003', 'CR-ORI-M1-L1', 'CR-ORI-M1-L1', h=1000)

s = O.lesson(L, MOD, MN, STEPS, 1, 3, 'How creating on Credalio works',
             'You build in your Studio, independent validators review it, then you publish. Three stages, always in this order.',
             O.note('Good to know', 'Readiness never stops you drafting. It only gates submitting and publishing.'),
             O.flow([('pen', 'Create', 'Build in your Studio, with Nova.'), ('shield', 'Validate', 'Independent experts review the work.'), ('rocket', 'Publish', 'Set a price and welcome learners.')]),
             ('CR-ORI-M1-L1.dc.html', 'What Credalio is for'), ('CR-ORI-M1-K1.dc.html', 'Next'), 'Credalio · Orientation · How creating works')
wr('CR-ORI-M1-L2.dc.html', s); OUT.append('CR-ORI-M1-L2.dc.html'); mob('CR-ORI-003', 'CR-ORI-M1-L2', 'CR-ORI-M1-L2', h=900)

Q = [['Multiple choice', 'Who checks a learning experience before learners rely on it?', ['The creator', 'Independent validators', 'Other learners'], 1, 'Independent experts validate it, not the creator or learner ratings.'],
     ['True or false', 'You must finish Creator Readiness before you can start drafting.', ['True', 'False'], 1, 'Drafting is always open. Readiness only gates validation and publishing.']]
s = O.check(K, MOD, MN, STEPS, Q, ('CR-ORI-M1-L2.dc.html', 'How creating on Credalio works'), 'CR-ORI-M1-DONE.dc.html', 'Credalio · Orientation · Module 1 check')
wr('CR-ORI-M1-K.dc.html', s); OUT.append('CR-ORI-M1-K.dc.html')
SETW = rd('CR-SET-001.dc.html')
for b, v in [('K1', 'none'), ('K2', 'right'), ('K3', 'wrong')]:
    n = 'CR-ORI-M1-' + b
    wr(n + '.dc.html', SETW.replace('<dc-import name="CR-SET" variant="account"', f'<dc-import name="CR-ORI-M1-K" variant="{v}"').replace('CR-SET-001', n)); OUT.append(n + '.dc.html')
    mob('CR-ORI-004', n, 'CR-ORI-M1-K', v, 960)
print('build41 ok'); print(' '.join(OUT))
