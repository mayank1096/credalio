# build43: M2-K2 / M2-K3 boards (variants of CR-ORI-M2-K), M2-DONE, Module 3 overview + Lesson 2 (Skills and proficiency).
# NOTE: Link 1 puts its own CR-ORI-003 in the M3 Lesson 1 slot; our CR-ORI-003 is a Module 4 lesson (flagged to designer).
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
SETW = rd('CR-SET-001.dc.html')
for b, v in [('K2', 'right'), ('K3', 'wrong')]:
    n = 'CR-ORI-M2-' + b
    wr(n + '.dc.html', SETW.replace('<dc-import name="CR-SET" variant="account"', f'<dc-import name="CR-ORI-M2-K" variant="{v}"').replace('CR-SET-001', n))
    mob('CR-ORI-004', n, 'CR-ORI-M2-K', v, 960)
wr('CR-ORI-M2-DONE.dc.html', O.done(rd('CR-ORI-006.dc.html'), 2, 'Creating trusted learning', 3, 'Two of seven done. Nicely paced.',
   ['Trust comes from outcomes, accuracy and evidence', 'Evidence is something learners do'],
   ['Design around outcomes', 'Add practice and assessment that prove them'], 'CR-ORI-M3-00.dc.html', 'Credalio · Orientation · Module 2 complete'))
mob('CR-ORI-006', 'CR-ORI-M2-DONE', 'CR-ORI-M2-DONE', h=960)
MOD, MN = 3, 'Outcomes, skills & evidence'
STEPS = [('Writing observable outcomes', 'Lesson'), ('Skills and proficiency', 'Lesson'), ('Linking evidence', 'Lesson'), ('Quick knowledge check', 'Check')]
wr('CR-ORI-M3-00.dc.html', O.overview(rd('CR-ORI-M1-00.dc.html'), MOD, MN, STEPS, 12,
   'Write outcomes validators can see, set skill targets, and link evidence to both.',
   'Two down, Ada. This is the one validators care about most, so take your time.',
   ['Observable verbs make outcomes assessable', 'Skill gaps tell you how much practice to add', 'Every outcome needs evidence'], 'CR-ORI-003.dc.html', 'Credalio · Orientation · Module 3'))
m = rd('CR-ORI-M1-00-Mobile.dc.html').replace('<dc-import name="CR-ORI-M1-00"', '<dc-import name="CR-ORI-M3-00"')
wr('CR-ORI-M3-00-Mobile.dc.html', re.sub(r'<title>.*?</title>', '<title>CR-ORI-M3-00 mobile preview</title>', m))
s = O.lesson(rd('CR-ORI-003.dc.html'), MOD, MN, STEPS, 1, 3, 'Skills and proficiency',
             'Each skill has a starting level and a target. The gap between them tells you how much practice the learning needs.',
             None, O.levels([('1', 'Beginner', 'Follows guided steps.', 'Start', False), ('2', 'Intermediate', 'Works independently on standard tasks.', 'Target', True), ('3', 'Advanced', 'Handles complex, new problems.', None, False)]),
             ('CR-ORI-003.dc.html', 'Writing observable outcomes'), ('CR-ORI-M3-L3.dc.html', 'Next lesson'), 'Credalio · Orientation · Skills and proficiency', scene=True)
wr('CR-ORI-M3-L2.dc.html', O.with_css(s, O.LEVELS_CSS)); mob('CR-ORI-003', 'CR-ORI-M3-L2', 'CR-ORI-M3-L2', h=900)
print('build43 ok'); print(' '.join(OUT))
