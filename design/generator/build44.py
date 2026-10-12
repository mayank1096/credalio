# build44: Module 3 Lesson 3 (Linking evidence), check (CR-ORI-M3-K → K1/K2/K3), Module 3 complete. usage: python3 build44.py <dir>
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
MOD, MN = 3, 'Outcomes, skills & evidence'
STEPS = [('Writing observable outcomes', 'Lesson'), ('Skills and proficiency', 'Lesson'), ('Linking evidence', 'Lesson'), ('Quick knowledge check', 'Check')]
s = O.lesson(rd('CR-ORI-003.dc.html'), MOD, MN, STEPS, 2, 2, 'Linking evidence',
             'Every outcome needs at least one practice, assessment or project behind it. Your Studio and Nova flag any outcome with nothing linked.',
             None, O.links([('Write SQL queries that join two or more tables', ['Practice 2.1', 'Quiz 2']), ('Present a recommendation backed by data', [])]),
             ('CR-ORI-M3-L2.dc.html', 'Skills and proficiency'), ('CR-ORI-M3-K1.dc.html', 'Next'), 'Credalio · Orientation · Linking evidence', scene=True)
wr('CR-ORI-M3-L3.dc.html', O.with_css(s, O.LINKS_CSS)); mob('CR-ORI-003', 'CR-ORI-M3-L3', 'CR-ORI-M3-L3', h=900)
Q = [['Multiple choice', 'Which outcome is observable?', ['Understand data cleaning', 'Know the main SQL functions', 'Clean a dataset by removing duplicates and fixing formats'], 2, 'It describes something a validator could see the learner do.'],
     ['Scenario', 'An outcome has no practice or assessment linked to it. What does that mean?', ['Nothing, it’s fine', 'Learners can’t show they’ve reached it', 'The course will be cheaper'], 1, 'Without evidence, the outcome can’t be shown or validated.']]
wr('CR-ORI-M3-K.dc.html', O.check(rd('CR-ORI-004.dc.html'), MOD, MN, STEPS, Q, ('CR-ORI-M3-L3.dc.html', 'Linking evidence'), 'CR-ORI-M3-DONE.dc.html', 'Credalio · Orientation · Module 3 check'))
SETW = rd('CR-SET-001.dc.html')
for b, v in [('K1', 'none'), ('K2', 'right'), ('K3', 'wrong')]:
    n = 'CR-ORI-M3-' + b
    wr(n + '.dc.html', SETW.replace('<dc-import name="CR-SET" variant="account"', f'<dc-import name="CR-ORI-M3-K" variant="{v}"').replace('CR-SET-001', n))
    mob('CR-ORI-004', n, 'CR-ORI-M3-K', v, 1000)
wr('CR-ORI-M3-DONE.dc.html', O.done(rd('CR-ORI-006.dc.html'), 3, MN, 4, 'Almost halfway there.', [],
   ['Write outcomes validators can observe', 'Link evidence to every outcome'], 'CR-ORI-002.dc.html', 'Credalio · Orientation · Module 3 complete'))
mob('CR-ORI-006', 'CR-ORI-M3-DONE', 'CR-ORI-M3-DONE', h=900)
print('build44 ok'); print(' '.join(OUT))
# ---- M4 Lesson 1 (What validators look at); M4 overview = our CR-ORI-002, lesson 2 = our CR-ORI-003 ----
STEPS4 = [('What validators look at', 'Lesson'), ('The validation case', 'Lesson'), ('Tiers and revalidation', 'Lesson'), ('Quick knowledge check', 'Check')]
s = O.lesson(rd('CR-ORI-003.dc.html'), 4, 'Understanding validation', STEPS4, 0, 3, 'What validators look at',
             'Validators are independent experts. They review against published criteria, never personal taste.',
             None, O.roles([('book', 'Educational', 'Structure, outcomes, sequencing and assessment design.'), ('check', 'Subject matter', 'Accuracy, currency and depth of the content.'), ('doc', 'Assessment', 'Whether assessments fairly measure the outcomes.')]),
             ('CR-ORI-002.dc.html', 'Module overview'), ('CR-ORI-003.dc.html', 'Next lesson'), 'Credalio · Orientation · What validators look at', scene=True)
wr('CR-ORI-M4-L1.dc.html', s); mob('CR-ORI-003', 'CR-ORI-M4-L1', 'CR-ORI-M4-L1', h=900)
print(' '.join(OUT[-2:]))
