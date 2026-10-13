# build49: Module 7 (Creator responsibilities) L1, L2, check CR-ORI-M7-K (K1/K2/K3; step 3 of 4, Next -> M7-S1). usage: python3 build49.py <dir>
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
TIPCSS = '\n/* build49 tooltip */' + tipx.TIP_CSS + '.vc2-n .tip{margin-left:4px}\n'
O.ICO['chat'] = '<path d="M20 12a8 8 0 0 1-11.6 7.1L4 20l1-4.2A8 8 0 1 1 20 12z"></path><path d="M8.5 11h7M8.5 14h4"></path>'
O.ICO['star'] = '<path d="m12 3.5 2.6 5.3 5.9.9-4.3 4.1 1 5.8-5.2-2.7-5.2 2.7 1-5.8-4.3-4.1 5.9-.9z"></path>'
MOD, MN = 7, 'Creator responsibilities'
STEPS = [('Your obligations to learners', 'Lesson'), ('Declarations and changes', 'Lesson'), ('Quick knowledge check', 'Check'), ('Scenario exercise', 'Exercise')]
s = O.lesson(rd('CR-ORI-003.dc.html'), MOD, MN, STEPS, 0, 2, 'Your obligations to learners',
             'Learners rely on what you publish. Three promises keep that trust.',
             None, O.roles([('check', 'Accurate', 'Keep content correct and current.'), ('chat', 'Responsive', 'Answer learner support in reasonable time.'), ('star', 'As promised', 'Deliver the sessions, feedback and support you offered.')]),
             ('CR-ORI-M7-00.dc.html', 'Module overview'), ('CR-ORI-M7-L2.dc.html', 'Next lesson'), 'Credalio · Orientation · Your obligations to learners', scene=True)
wr('CR-ORI-M7-L1.dc.html', s); mob('CR-ORI-003', 'CR-ORI-M7-L1', 'CR-ORI-M7-L1', h=900)
s = O.lesson(rd('CR-ORI-003.dc.html'), MOD, MN, STEPS, 1, 2, 'Declarations and changes',
             'Everyone vouches for their own work. After publishing, bigger changes are checked before they go live.',
             None, O.flow([('pen', 'Each contributor declares', 'Their own part, before validation.'), ('shield', 'The Lead Creator submits', 'Once every declaration is in.'), ('rocket', 'Changes start as drafts', 'Bigger ones may need revalidation.')], hub=1),
             ('CR-ORI-M7-L1.dc.html', 'Your obligations to learners'), ('CR-ORI-M7-K1.dc.html', 'Next'), 'Credalio · Orientation · Declarations and changes', scene=True)
s = s.replace('<b>Changes start as drafts</b>', '<b>Changes start as drafts' + tipx.tip('Learners keep access to what they enrolled in.', 'r') + '</b>', 1); assert 'tip-b' in s
wr('CR-ORI-M7-L2.dc.html', O.with_css(s, TIPCSS)); mob('CR-ORI-003', 'CR-ORI-M7-L2', 'CR-ORI-M7-L2', h=960)
Q = [['Multiple choice', 'Who confirms that Chapter 3, written by John, is accurate?', ['The Lead Creator, for John', 'John, in his own declaration', 'Nobody'], 1, 'Each contributor declares their own part.'],
     ['True or false', 'Learners keep access to what they enrolled in, even after you update the course.', ['True', 'False'], 0, 'Updates never take away what learners already have.']]
wr('CR-ORI-M7-K.dc.html', O.check(rd('CR-ORI-004.dc.html'), MOD, MN, STEPS, Q, ('CR-ORI-M7-L2.dc.html', 'Declarations and changes'), 'CR-ORI-M7-S1.dc.html', 'Credalio · Orientation · Module 7 check', cur=2))
SETW = rd('CR-SET-001.dc.html')
for b, v in [('K1', 'none'), ('K2', 'right'), ('K3', 'wrong')]:
    n = 'CR-ORI-M7-' + b
    wr(n + '.dc.html', SETW.replace('<dc-import name="CR-SET" variant="account"', f'<dc-import name="CR-ORI-M7-K" variant="{v}"').replace('CR-SET-001', n))
    mob('CR-ORI-004', n, 'CR-ORI-M7-K', v, 1000)
print('build49 ok'); print(' '.join(OUT))
