# grey1013: designer 2026-10-13 — "in review" outcome screens use GREY, not cobalt (emblem, spinner, pill, top glow,
# what-happens-next timeline). Applies to the ko-r state of KYC-003 / CRED-003 (= KYC-003, CRED-003b). CTA buttons stay cobalt.
import os, sys
P = sys.argv[1]
CSS = ("\n/* grey1013: in review = grey */\n"
       ".tk-root:has(.ko-r){--glow:91,101,130}\n"
       ".ko-r{--k:#5B6582;--kb:#EEF1F7}\n"
       ".ko-r .ko-halo::after{border-top-color:#5B6582}\n"
       ".ko-r .ko-done .ko-dot{background:#5B6582;border-color:#5B6582}\n"
       ".ko-r .ko-path li.ko-done::before{background:#5B6582}\n"
       ".ko-r .ko-now .ko-dot{border-color:#5B6582;box-shadow:0 0 0 4px rgba(91,101,130,.14)}\n"
       ".ko-r .ko-now .ko-dot::after{background:#5B6582}\n")
for f in ('CR-KYC-003.dc.html', 'CR-CRED-003.dc.html'):
    p = os.path.join(P, f); s = open(p, encoding='utf-8').read()
    assert 'grey1013' not in s and 'class="ko {{koCls}}"' in s
    i = s.rfind('</style>', 0, s.find('</helmet>')); s = s[:i] + CSS + s[i:]
    open(p, 'w', encoding='utf-8').write(s); print('ok', f)
