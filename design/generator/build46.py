# build46: Module 5 (AI & responsible creation): M5-00 overview, L1, L2, check CR-ORI-M5-K (boards K1 / K3). Our CR-ORI-005 = the M5 scenario
# exercise (check -> CR-ORI-005). usage: python3 build46.py <dir>
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
TIPCSS = '\n/* build46 tooltip */' + tipx.TIP_CSS + '.vc2-n .tip,.ls-roles .tip{margin-left:4px}\n'
O.ICO['spark'] = '<path d="M12 3.5v4M12 16.5v4M3.5 12h4M16.5 12h4"></path><path d="m12 8.5 1.2 2.3 2.3 1.2-2.3 1.2L12 15.5l-1.2-2.3L8.5 12l2.3-1.2z"></path>'
MOD, MN = 5, 'AI & responsible creation'
STEPS = [('Using your Copilot well', 'Lesson'), ('Review, disclose, own', 'Lesson'), ('Quick knowledge check', 'Check'), ('Scenario exercise', 'Exercise')]
s = O.overview(rd('CR-ORI-M1-00.dc.html'), MOD, MN, STEPS, 10,
   'Working with Nova, and owning everything you publish.',
   'This one’s about working with me, Ada. I help, you decide.',
   ['Nova explains, suggests and prepares', 'You confirm anything that matters', 'You own what you publish'], 'CR-ORI-M5-L1.dc.html', 'Credalio · Orientation · Module 5')
l0 = s.index('<ol class="mo-list">'); l1 = s.index('</ol>', l0)
s = s[:l0] + re.sub(r'(<b>[^<]*</b>)<span>(Lesson|Check|Exercise)</span>', r'\1', s[l0:l1]) + s[l1:]
wr('CR-ORI-M5-00.dc.html', s)
mob('CR-ORI-M1-00', 'CR-ORI-M5-00', 'CR-ORI-M5-00', h=1200)
s = O.lesson(rd('CR-ORI-003.dc.html'), MOD, MN, STEPS, 0, 3, 'Using your Copilot well',
             'Nova can explain, suggest and prepare changes. Publishing, paying and signing always wait for you.',
             None, O.roles([('info', 'Explain', 'Validation feedback, pricing and analytics.'), ('spark', 'Suggest', 'Outcomes, questions and structure.'), ('check', 'Act', 'Only after you confirm.')]),
             ('CR-ORI-M5-00.dc.html', 'Module overview'), ('CR-ORI-M5-L2.dc.html', 'Next lesson'), 'Credalio · Orientation · Using your Copilot well', scene=True)
wr('CR-ORI-M5-L1.dc.html', s); mob('CR-ORI-003', 'CR-ORI-M5-L1', 'CR-ORI-M5-L1', h=900)
s = O.lesson(rd('CR-ORI-003.dc.html'), MOD, MN, STEPS, 1, 2, 'Review, disclose, own',
             'You’re responsible for every word you publish, whoever drafted it.',
             None, O.flow([('check', 'Review', 'Check accuracy and sources.'), ('info', 'Disclose', 'Say where AI helped, when policy asks.'), ('shield', 'Own', 'It goes out under your name.')], hub=2),
             ('CR-ORI-M5-L1.dc.html', 'Using your Copilot well'), ('CR-ORI-M5-K1.dc.html', 'Next'), 'Credalio · Orientation · Review, disclose, own', scene=True)
s = s.replace('<b>Review</b>', '<b>Review' + tipx.tip('AI-assisted questions stay labelled in your Studio until you approve them.') + '</b>', 1)
assert 'tip-b' in s
wr('CR-ORI-M5-L2.dc.html', O.with_css(s, TIPCSS)); mob('CR-ORI-003', 'CR-ORI-M5-L2', 'CR-ORI-M5-L2', h=960)
Q = [['Scenario', 'Nova drafts 10 quiz questions for you. What do you do?', ['Publish them as they are', 'Review each one before approving', 'Delete them, AI isn’t allowed'], 1, 'AI help is welcome. It counts as yours once you’ve reviewed it.'],
     ['True or false', 'Nova can submit your course for validation on its own.', ['True', 'False'], 1, 'Nova prepares. Submitting, paying and signing always need you.']]
s = O.check(rd('CR-ORI-004.dc.html'), MOD, MN, STEPS, Q, ('CR-ORI-M5-L2.dc.html', 'Review, disclose, own'), 'CR-ORI-005.dc.html', 'Credalio · Orientation · Module 5 check', cur=2)
wr('CR-ORI-M5-K.dc.html', s)
SETW = rd('CR-SET-001.dc.html')
for b, v in [('K1', 'none'), ('K3', 'wrong')]:
    n = 'CR-ORI-M5-' + b
    wr(n + '.dc.html', SETW.replace('<dc-import name="CR-SET" variant="account"', f'<dc-import name="CR-ORI-M5-K" variant="{v}"').replace('CR-SET-001', n))
    mob('CR-ORI-004', n, 'CR-ORI-M5-K', v, 1000)
print('build46 ok'); print(' '.join(OUT))
