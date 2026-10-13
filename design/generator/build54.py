# build54: fill the two Link 1 orientation gaps. CR-ORI-M3-L1 "Writing observable outcomes" (new lesson, weak/strong compare figure) and
# board CR-ORI-M5-K2 (= CR-ORI-M5-K variant right). Re-points M3-00 Start + M3-L2 Back -> M3-L1 and CR-ORI-002 (M4 overview) Continue -> M4-L2.
# Templates CR-ORI-003 / CR-ORI-004 stay as files (ori_m templates) but move to page p2. usage: python3 build54.py <dir>
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ori_m as O
P = sys.argv[1]
def rd(f): return open(os.path.join(P, f), encoding='utf-8').read()
def wr(f, s): open(os.path.join(P, f), 'w', encoding='utf-8').write(s); OUT.append(f)
OUT = []
def sub(s, a, b, n=1):
    assert s.count(a) >= 1, a[:90]; return s.replace(a, b, n)
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
s = O.lesson(rd('CR-ORI-003.dc.html'), MOD, MN, STEPS, 0, 3, 'Writing observable outcomes',
             'An outcome says what a learner can do at the end. Start with a verb a validator could actually see.',
             None, O.compare('Understand data cleaning', 'Clean a dataset by removing duplicates and fixing formats'),
             ('CR-ORI-M3-00.dc.html', 'Module overview'), ('CR-ORI-M3-L2.dc.html', 'Next lesson'), 'Credalio · Orientation · Writing observable outcomes', scene=True)
wr('CR-ORI-M3-L1.dc.html', O.with_css(s, O.COMPARE_CSS)); mob('CR-ORI-003', 'CR-ORI-M3-L1', 'CR-ORI-M3-L1', h=900)
SETW = rd('CR-ORI-M5-K1.dc.html')
wr('CR-ORI-M5-K2.dc.html', SETW.replace('variant="none"', 'variant="right"').replace('CR-ORI-M5-K1', 'CR-ORI-M5-K2'))
wr('CR-ORI-M5-K2-Mobile.dc.html', rd('CR-ORI-M5-K1-Mobile.dc.html').replace('variant="none"', 'variant="right"').replace('CR-ORI-M5-K1', 'CR-ORI-M5-K2'))
wr('CR-ORI-M3-00.dc.html', sub(rd('CR-ORI-M3-00.dc.html'), 'href="CR-ORI-003.dc.html" class="ds-btn mo-go mo-go-new', 'href="CR-ORI-M3-L1.dc.html" class="ds-btn mo-go mo-go-new'))
s = sub(rd('CR-ORI-M3-L2.dc.html'), 'href="CR-ORI-003.dc.html" class="lp-prev"', 'href="CR-ORI-M3-L1.dc.html" class="lp-prev"')
wr('CR-ORI-M3-L2.dc.html', re.sub(r'(class="lp-prev">.*?<span class="lp-hide-sm">)[^<]*', r'\1Writing observable outcomes', s, count=1, flags=re.S))
wr('CR-ORI-002.dc.html', sub(rd('CR-ORI-002.dc.html'), 'href="CR-ORI-003.dc.html" class="ds-btn mo-go"', 'href="CR-ORI-M4-L2.dc.html" class="ds-btn mo-go"'))
print('build54 ok'); print(' '.join(OUT))
