# build40b: redesign RDY-001d (CR-RDY-001 variant done) after designer comment "bad design" (2026-10-12).
# One calm success hero: green tick, pill, H1, one line, Open my drafts + the readiness path (5 green checks -> Validation next).
# No ring, no Nova band, no repeated requirement list. Payout row stays. usage: python3 build40b.py <dir>
import re, sys, os
P = sys.argv[1]
f = os.path.join(P, 'CR-RDY-001.dc.html'); s = open(f, encoding='utf-8').read()
assert 'rdd-hero' not in s, 'already applied'
m = re.search(r'<sc-if value="\{\{isDone\}\}" hint-placeholder-val="\{\{false\}\}">', s)
end = s.index('</div></sc-if>', m.start()) + len('</div></sc-if>')
old = s[m.start():end]
pay = re.search(r'<section class="ob-in4"[^>]*><h2[^>]*>When you start earning</h2>.*?</section>', old, re.S).group(0)
arrow = re.search(r'<span class="ob-arrow">(.*?)</span>', old, re.S).group(1)
CHK = '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"></path></svg>'
BIG = '<svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"></path></svg>'
steps = ''.join(f'<li class="rdd-s"><span class="rdd-d">{CHK}</span><span>{t}</span></li>' for t in
                ['Creator profile', 'Identity verified', 'Credentials & expertise', 'Creator Orientation', 'Creator policies'])
steps += '<li class="rdd-s rdd-nx"><span class="rdd-d"></span><span>Validation</span><em>Next</em></li>'
new = ('<sc-if value="{{isDone}}" hint-placeholder-val="{{false}}">'
       '<section class="ds-card rdd-hero ob-in" aria-labelledby="rdd-h"><div class="rdd-l">'
       f'<span class="rdd-em">{BIG}</span><span class="rdd-pill">All checks complete</span>'
       '<h1 id="rdd-h" class="ds-h1 rdd-h">You’re ready to submit.</h1>'
       '<p class="rdd-sub">Send a learning experience for validation whenever it feels ready.</p>'
       f'<a href="CR-HOME-EXP.dc.html" class="ds-btn rdd-go"><span>Open my drafts</span><span class="ob-arrow">{arrow}</span></a></div>'
       f'<ol class="rdd-path ob-in2" aria-label="Your readiness path">{steps}</ol></section>'
       '<div class="rd-grid"><div class="rd-col">' + pay + '</div></div></sc-if>')
s = s[:m.start()] + new + s[end:]
css = """
/* build40b readiness complete */
.rdd-hero{position:relative;z-index:1;margin-top:28px;padding:40px 44px;display:grid;grid-template-columns:minmax(0,1fr) 330px;gap:48px;align-items:center}
.rdd-l{display:flex;flex-direction:column;align-items:flex-start;min-width:0}
.rdd-em{width:60px;height:60px;border-radius:50%;background:#0F6B45;color:#FFFFFF;display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 9px #E7F5EE}
.rdd-pill{margin-top:26px;display:inline-flex;align-items:center;height:28px;padding:0 12px;border-radius:999px;background:#E7F5EE;color:#0F6B45;font-size:13px;font-weight:500}
.rdd-h{margin:12px 0 0 0}
.rdd-sub{margin:10px 0 0 0;font-size:16px;line-height:1.55;color:#4A5578;max-width:500px}
.rdd-go{margin-top:28px}
.rdd-path{list-style:none;margin:0;padding:8px 0 8px 44px;border-left:1.5px solid #EEF1F7;position:relative;display:flex;flex-direction:column;gap:16px}
.rdd-path::before{content:'';position:absolute;left:55px;top:18px;bottom:18px;width:2px;border-radius:2px;background:linear-gradient(180deg,#0F6B45 0%,#0F6B45 82%,#1652F0 82%)}
.rdd-s{position:relative;display:flex;align-items:center;gap:14px;font-size:14.5px;color:#3A4566}
.rdd-d{width:24px;height:24px;flex-shrink:0;border-radius:50%;background:#0F6B45;color:#FFFFFF;display:flex;align-items:center;justify-content:center}
.rdd-nx{color:#0B1433;font-weight:600}
.rdd-nx .rdd-d{background:#FFFFFF;border:2px solid #1652F0;box-sizing:border-box;box-shadow:0 0 0 5px rgba(22,82,240,.12)}
.rdd-nx em{margin-left:auto;font-style:normal;font-size:12.5px;font-weight:500;color:#0E3BB8;background:#EAF0FF;height:24px;padding:0 10px;border-radius:999px;display:inline-flex;align-items:center}
.ds-main{position:relative}
@media (max-width: 1080px){.rdd-hero{grid-template-columns:minmax(0,1fr);gap:32px;padding:32px}.rdd-path{padding:24px 0 0 0;border-left:0;border-top:1.5px solid #EEF1F7}.rdd-path::before{left:11px;top:42px}}
@media (max-width: 960px){
.rdd-hero{margin-top:24px;padding:26px 18px;gap:28px;border-radius:20px}
.rdd-em{width:52px;height:52px}.rdd-em svg{width:26px;height:26px}
.rdd-pill{margin-top:22px}
.rdd-sub{font-size:15px}
.rdd-go{width:100%;justify-content:space-between;margin-top:22px}
.rdd-path{gap:14px;padding:22px 0 0 0;border-left:0;border-top:1.5px solid #EEF1F7}.rdd-path::before{left:11px;top:40px}
}
"""
i = s.rfind('</style>', 0, s.find('</helmet>')); s = s[:i] + css + s[i:]
open(f, 'w', encoding='utf-8').write(s); print('build40b ok')
