# build48: Module 6 check (CR-ORI-M6-K -> K1/K2/K3), Module 6 complete, Module 7 overview. usage: python3 build48.py <dir>
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
MOD, MN = 6, 'Creator economy'
STEPS = [('Setting your price', 'Lesson'), ('Credit Wallet vs Earnings', 'Lesson'), ('Quick knowledge check', 'Check')]
Q = [['Multiple choice', 'You need to pay for validation. Where do the Credits come from?', ['Your earnings', 'Your Credit Wallet', 'The validator'], 1, 'Validation is paid from your Credit Wallet. Earnings stay separate.'],
     ['True or false', 'You can set any price you like for a course.', ['True', 'False'], 1, 'You choose within the range Credalio suggests.']]
wr('CR-ORI-M6-K.dc.html', O.check(rd('CR-ORI-004.dc.html'), MOD, MN, STEPS, Q, ('CR-ORI-M6-L2.dc.html', 'Credit Wallet vs Earnings'), 'CR-ORI-M6-DONE.dc.html', 'Credalio · Orientation · Module 6 check'))
SETW = rd('CR-SET-001.dc.html')
for b, v in [('K1', 'none'), ('K2', 'right'), ('K3', 'wrong')]:
    n = 'CR-ORI-M6-' + b
    wr(n + '.dc.html', SETW.replace('<dc-import name="CR-SET" variant="account"', f'<dc-import name="CR-ORI-M6-K" variant="{v}"').replace('CR-SET-001', n))
    mob('CR-ORI-004', n, 'CR-ORI-M6-K', v, 1000)
wr('CR-ORI-M6-DONE.dc.html', O.done(rd('CR-ORI-006.dc.html'), MOD, MN, 3, 'One module to go.', [],
   ['Price within the suggested range', 'Keep your payout details current'], 'CR-ORI-M7-00.dc.html', 'Credalio · Orientation · Module 6 complete'))
mob('CR-ORI-006', 'CR-ORI-M6-DONE', 'CR-ORI-M6-DONE', h=900)
STEPS7 = [('Your obligations to learners', 'Lesson'), ('Declarations and changes', 'Lesson'), ('Quick knowledge check', 'Check'), ('Scenario exercise', 'Exercise')]
s = O.overview(rd('CR-ORI-M1-00.dc.html'), 7, 'Creator responsibilities', STEPS7, 8,
   'What learners can count on, and what happens when you change things.',
   'Last one, Ada. After this, you’re ready to submit.',
   ['Learners rely on what you publish', 'Each contributor declares their own work', 'Bigger changes may need revalidation'], 'CR-ORI-M7-L1.dc.html', 'Credalio · Orientation · Module 7')
l0 = s.index('<ol class="mo-list">'); l1 = s.index('</ol>', l0)
s = s[:l0] + re.sub(r'(<b>[^<]*</b>)<span>(Lesson|Check|Exercise)</span>', r'\1', s[l0:l1]) + s[l1:]
wr('CR-ORI-M7-00.dc.html', s); mob('CR-ORI-M1-00', 'CR-ORI-M7-00', 'CR-ORI-M7-00', h=1200)
print('build48 ok'); print(' '.join(OUT))
