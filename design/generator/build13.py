# Batch 13 · CR-KYC-002d (review & submit = KYC-002 variant "review") · CR-KYC-003 identity outcome (variants: review / verified / action / failed = 003 / 004 / 005 / 006)
import builtins, os
_ALLOW = {'CR-KYC-002.dc.html', 'CR-KYC-002d.dc.html', 'CR-KYC-002d-Mobile.dc.html',
          'CR-KYC-003.dc.html', 'CR-KYC-003-Mobile.dc.html', 'CR-KYC-004.dc.html', 'CR-KYC-004-Mobile.dc.html',
          'CR-KYC-005.dc.html', 'CR-KYC-005-Mobile.dc.html', 'CR-KYC-006.dc.html', 'CR-KYC-006-Mobile.dc.html'}
_ropen = builtins.open
def open(p, mode='r', *a, **k):
    # only the files of this batch may be written; everything else goes to a scratch dir
    if 'w' in mode and '/design/canvas/project/' in str(p) and os.path.basename(str(p)) not in _ALLOW:
        os.makedirs('/tmp/claude-0/-home-user-credalio/ac3a299a-59c2-576d-8df6-3f8bf66b6d40/scratchpad/discard', exist_ok=True)
        p = '/tmp/claude-0/-home-user-credalio/ac3a299a-59c2-576d-8df6-3f8bf66b6d40/scratchpad/discard/' + os.path.basename(str(p))
    return _ropen(p, mode, *a, **k)
exec(_ropen('build12.py').read())

HG_I = '<path d="M7 3h10M7 21h10"></path><path d="M8 3c0 5 8 5 8 9s-8 4-8 9"></path><path d="M16 3c0 5-8 5-8 9s8 4 8 9"></path>'
RETRY_I = '<path d="M3 12a9 9 0 0 1 15.5-6.2L21 8"></path><path d="M21 3v5h-5"></path><path d="M21 12a9 9 0 0 1-15.5 6.2L3 16"></path><path d="M3 21v-5h5"></path>'
INFO_I = '<circle cx="12" cy="12" r="9"></circle><path d="M12 11v5"></path><path d="M12 7.5h.01"></path>'
MAIL_I = '<rect x="3" y="5" width="18" height="14" rx="2.5"></rect><path d="m4 7 8 6 8-6"></path>'
CHAT_I = '<path d="M20 15a2 2 0 0 1-2 2H8l-4 4V6a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2z"></path>'
CRED_I = '<circle cx="12" cy="9" r="5"></circle><path d="m8.5 13.2-1.5 7.8 5-2.6 5 2.6-1.5-7.8"></path>'

c = '''<main class="ko {{koCls}}">
<div class="ko-emb ob-in" aria-hidden="true"><span class="ko-halo"></span><span class="ko-disc">
<sc-if value="{{r}}" hint-placeholder-val="{{true}}">''' + ik(HG_I, 30, 2) + '''</sc-if>
<sc-if value="{{v}}" hint-placeholder-val="{{false}}"><svg class="ko-tick" width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"><path d="m5 12.5 4.5 4.5L19 7.5" pathLength="1"></path></svg></sc-if>
<sc-if value="{{a}}" hint-placeholder-val="{{false}}">''' + ik(CAM_I, 30, 2) + '''</sc-if>
<sc-if value="{{f}}" hint-placeholder-val="{{false}}">''' + ik(INFO_I, 30, 2) + '''</sc-if>
</span></div>
<span class="ko-pill ob-in2">{{pill}}</span>
<h1 class="lp-h1 ko-h ob-in2">{{h1}}</h1>
<p class="ko-sub ob-in2">{{sub}}</p>

<sc-if value="{{r}}" hint-placeholder-val="{{true}}">
<div class="ko-row">
<section class="ko-card ob-in3" aria-label="What happens next">
<span class="sec-h">What happens next</span>
<ol class="ko-path">
<li class="ko-done"><span class="ko-dot">''' + ic('check', 11, 3.4) + '''</span><span><b>Submitted to Sumsub</b><span>Today, 10:42</span></span></li>
<li class="ko-now"><span class="ko-dot"></span><span><b>Sumsub checks your ID</b><span>Usually a few minutes, at most one business day</span></span></li>
<li><span class="ko-dot"></span><span><b>We let you know</b><span>By email and here in your Studio</span></span></li>
</ol>
</section>
<section class="ko-next ob-in4" aria-label="Next for you">
<span class="ko-ni">''' + ik(CRED_I, 22, 1.9) + '''</span>
<span class="ko-nt"><span class="ko-nl">Meanwhile, next for you</span><b>Credentials &amp; expertise</b><span>Add a degree or certificate. It doesn’t need to wait for this check.</span></span>
<a href="#" class="ds-btn sm ko-go"><span>Add credentials</span><span class="ob-arrow">''' + ic('arrow', 16, 2.4) + '''</span></a>
</section>
</div>
</sc-if>

<sc-if value="{{v}}" hint-placeholder-val="{{false}}">
<div class="ko-row">
<section class="ko-card ko-idc ob-in3" aria-label="Verified identity">
<span class="ko-ii">''' + ik(ID_I, 22, 1.9) + '''</span>
<span class="ko-it"><b>Ada Ononuju</b><span>National ID card · Nigeria · verified 7 October 2026</span></span>
<span class="ko-vb">''' + ic('check', 11, 3.4) + '''<span>Verified</span></span>
<div class="ko-rd"><span class="ko-rl">Readiness</span><span class="ko-bar"><span class="ko-was"></span><span class="ko-up"></span></span><span class="ko-rv"><b>40%</b><em>+20%</em></span></div>
</section>
<section class="ko-next ob-in4" aria-label="Next for you">
<span class="ko-ni">''' + ik(CRED_I, 22, 1.9) + '''</span>
<span class="ko-nt"><span class="ko-nl">Next for you</span><b>Credentials &amp; expertise</b><span>Show learners what you know. About 5 minutes.</span></span>
<a href="#" class="ds-btn sm ko-go"><span>Add credentials</span><span class="ob-arrow">''' + ic('arrow', 16, 2.4) + '''</span></a>
</section>
</div>
</sc-if>

<sc-if value="{{a}}" hint-placeholder-val="{{false}}">
<section class="ko-card ob-in3" aria-label="What to fix">
<span class="sec-h">What to fix</span>
<ul class="ko-fix">
<li class="ko-bad"><span class="ko-th" aria-hidden="true"><span></span></span><span class="ko-ft"><b>Front of your ID</b><span>Too blurry to read the name and date of birth.</span></span><span class="ko-tag">Retake</span></li>
<li><span class="ko-ok">''' + ic('check', 11, 3.4) + '''</span><span class="ko-ft"><b>Back of your ID</b><span>Clear and readable</span></span></li>
<li><span class="ko-ok">''' + ic('check', 11, 3.4) + '''</span><span class="ko-ft"><b>Liveness check</b><span>Passed</span></span></li>
</ul>
<p class="ko-tip">''' + ik(SUN_I, 15, 2) + '''<span>Lay the card flat in good light and hold still until it focuses.</span></p>
</section>
<div class="ko-cta ob-in4"><a href="CR-KYC-002b.dc.html" class="ds-btn"><span>Retake front photo</span><span class="ob-arrow">''' + ic('arrow', 18, 2.4) + '''</span></a><span class="ko-cn">About 2 minutes. Everything else is kept.</span></div>
</sc-if>

<sc-if value="{{f}}" hint-placeholder-val="{{false}}">
<section class="ko-card ob-in3" aria-label="What you can do">
<span class="sec-h">What you can do</span>
<div class="ko-opts">
<a href="CR-KYC-002.dc.html" class="ko-opt"><span class="ko-oi">''' + ik(RETRY_I, 20, 1.9) + '''</span><span><b>Try again with another ID</b><span>A passport or driver’s licence often works best. 1 attempt left.</span></span>''' + ic('arrow', 16, 2.2) + '''</a>
<a href="#" class="ko-opt"><span class="ko-oi">''' + ik(CHAT_I, 20, 1.9) + '''</span><span><b>Talk to our team</b><span>A person reviews your case and helps you finish. Usually within a day.</span></span>''' + ic('arrow', 16, 2.2) + '''</a>
</div>
</section>
<div class="ko-cta ob-in4"><a href="#" class="ds-btn"><span>Contact support</span><span class="ob-arrow">''' + ic('arrow', 18, 2.4) + '''</span></a><span class="ko-cn">You can keep drafting while this is sorted.</span></div>
</sc-if>

<div class="ko-links ob-in4"><a href="CR-RDY-001.dc.html">View readiness</a><span aria-hidden="true">·</span><a href="CR-DASH-NEW.dc.html">Back to my Studio</a></div>
</main>'''

KO_CSS = '''.ko{flex-grow:1;width:min(920px,100%);box-sizing:border-box;margin:0 auto;padding:clamp(20px,3.6vh,40px) 24px 32px 24px;display:flex;flex-direction:column;align-items:center;text-align:center;--k:#1652F0;--kb:#EAF0FF}
.tk-root:has(.ko){background:radial-gradient(55% 40% at 50% 0%,rgba(22,82,240,.08),rgba(22,82,240,0) 70%),#FFFFFF}
.ko-v{--k:#0F6B45;--kb:#E7F5EE}.ko-a{--k:#B26A00;--kb:#FFF3DC}.ko-f{--k:#3A4566;--kb:#EEF1F7}
.ko-emb{position:relative;width:84px;height:84px;display:flex;align-items:center;justify-content:center}
.ko-halo{position:absolute;inset:0;border-radius:50%;background:var(--kb)}
.ko-r .ko-halo::after{content:'';position:absolute;inset:-6px;border-radius:50%;border:2px solid transparent;border-top-color:#1652F0;animation:koSpin 1.4s linear infinite}
@keyframes koSpin{to{transform:rotate(360deg)}}
.ko-disc{position:relative;width:58px;height:58px;border-radius:50%;background:var(--k);color:#FFFFFF;display:flex;align-items:center;justify-content:center;box-shadow:0 12px 28px rgba(11,20,51,.16)}
.ko-tick path{stroke-dasharray:1;stroke-dashoffset:1;animation:koDraw .6s ease .3s forwards}
@keyframes koDraw{to{stroke-dashoffset:0}}
.ko-pill{margin-top:14px;display:inline-flex;align-items:center;height:30px;padding:0 13px;border-radius:999px;background:var(--kb);color:var(--k);font-size:13px;font-weight:500}
.ko-h{margin-top:10px;font-size:clamp(28px,4.4vh,38px)}
.ko-sub{margin:10px 0 0 0;font-size:16.5px;line-height:1.55;color:#4A5578;max-width:520px}
.ko-card{margin-top:22px;width:100%;box-sizing:border-box;padding:18px 20px;border-radius:20px;background:#FFFFFF;border:1.5px solid #E6EAF3;text-align:left}
.ko-path{list-style:none;margin:12px 0 0 0;padding:0;display:flex;flex-direction:column}
.ko-path li{position:relative;display:flex;align-items:flex-start;gap:12px;padding-bottom:12px}
.ko-path li:last-child{padding-bottom:0}
.ko-path li:not(:last-child)::before{content:'';position:absolute;left:10px;top:24px;bottom:2px;width:2px;border-radius:2px;background:#E6EAF3}
.ko-path li.ko-done::before{background:#1652F0}
.ko-dot{width:22px;height:22px;flex-shrink:0;box-sizing:border-box;border-radius:50%;border:2px solid #D6DDEE;background:#FFFFFF;display:flex;align-items:center;justify-content:center;color:#FFFFFF}
.ko-done .ko-dot{background:#1652F0;border-color:#1652F0}
.ko-now .ko-dot{border-color:#1652F0;box-shadow:0 0 0 4px rgba(22,82,240,.14)}
.ko-now .ko-dot::after{content:'';width:8px;height:8px;border-radius:50%;background:#1652F0;animation:koBlink 1.6s ease-in-out infinite}
@keyframes koBlink{50%{opacity:.3}}
.ko-path li > span:last-child{display:flex;flex-direction:column;gap:2px;padding-top:1px}
.ko-path b{font-size:15px;font-weight:600}
.ko-path li > span:last-child > span{font-size:13.5px;color:#5B6582}
.ko-path li:not(.ko-done):not(.ko-now) b{color:#5B6582;font-weight:500}
.ko-next{margin-top:12px;width:100%;box-sizing:border-box;display:flex;align-items:center;gap:14px;padding:16px 16px 16px 18px;border-radius:20px;background:#F7F9FD;border:1.5px solid #E6EAF3;text-align:left}
.ko-ni{width:44px;height:44px;flex-shrink:0;border-radius:14px;background:#FFFFFF;color:#1652F0;display:flex;align-items:center;justify-content:center;border:1.5px solid #E6EAF3}
.ko-nt{flex-grow:1;display:flex;flex-direction:column;gap:2px}
.ko-nl{font-size:12.5px;font-weight:500;color:#8A93AD}
.ko-nt b{font-size:16px;font-weight:600}
.ko-nt > span:last-child{font-size:13.5px;line-height:1.45;color:#3A4566}
.ko-go{flex-shrink:0}
.ko-idc{display:grid;grid-template-columns:auto minmax(0,1fr) auto;align-items:center;gap:12px 14px;background:#FFFFFF url(''' + BGI + ''') center top / cover no-repeat;border-color:#CBD7F5;box-shadow:0 18px 40px rgba(22,82,240,.08)}
.ko-ii{width:44px;height:44px;border-radius:14px;background:#0F6B45;color:#FFFFFF;display:flex;align-items:center;justify-content:center}
.ko-it{display:flex;flex-direction:column;gap:2px}
.ko-it b{font-size:17px;font-weight:600}
.ko-it span{font-size:13.5px;color:#3A4566}
.ko-vb{display:inline-flex;align-items:center;gap:6px;height:30px;padding:0 12px 0 9px;border-radius:999px;background:#E7F5EE;color:#0F6B45;font-size:13px;font-weight:500}
.ko-rd{grid-column:1 / -1;display:flex;align-items:center;gap:12px;padding-top:14px;border-top:1.5px solid rgba(203,211,230,.6)}
.ko-rl{font-size:13px;color:#5B6582}
.ko-bar{position:relative;flex-grow:1;height:8px;border-radius:8px;background:#E6EAF3;overflow:hidden}
.ko-was,.ko-up{position:absolute;top:0;bottom:0;border-radius:8px}
.ko-was{left:0;width:20%;background:#1652F0}
.ko-up{left:20%;width:20%;background:#6E96FF;transform-origin:left;animation:koGrow 1s cubic-bezier(.3,.8,.3,1) .7s both}
@keyframes koGrow{from{transform:scaleX(0)}to{transform:none}}
.ko-rv{display:flex;align-items:baseline;gap:6px}
.ko-rv b{font-size:16px;font-weight:600}
.ko-rv em{font-style:normal;font-size:12.5px;font-weight:500;color:#0F6B45;background:#E7F5EE;border-radius:999px;padding:2px 8px}
.ko-fix{list-style:none;margin:12px 0 0 0;padding:0;display:flex;flex-direction:column;gap:8px}
.ko-fix li{display:flex;align-items:center;gap:12px;min-height:56px;padding:8px 12px;box-sizing:border-box;border-radius:14px;background:#F7F9FD}
.ko-fix li.ko-bad{background:#FFF8EC;border:1.5px solid #F4D98E}
.ko-th{width:56px;height:38px;flex-shrink:0;border-radius:7px;background:linear-gradient(135deg,#DCE4F5,#C7D3EE);overflow:hidden;display:flex;align-items:center;justify-content:center;filter:blur(1.2px)}
.ko-th span{width:30px;height:4px;border-radius:2px;background:#9AA8CC;box-shadow:0 8px 0 #9AA8CC,0 -8px 0 #AFBBD8}
.ko-ok{width:24px;height:24px;margin:0 16px;flex-shrink:0;border-radius:50%;background:#0F6B45;color:#FFFFFF;display:flex;align-items:center;justify-content:center}
.ko-ft{flex-grow:1;display:flex;flex-direction:column;gap:2px}
.ko-ft b{font-size:15px;font-weight:600}
.ko-ft span{font-size:13.5px;color:#5B6582}
.ko-bad .ko-ft span{color:#8A5300}
.ko-tag{flex-shrink:0;display:inline-flex;align-items:center;height:28px;padding:0 11px;border-radius:999px;background:#FFE9BF;color:#8A5300;font-size:12.5px;font-weight:500}
.ko-tip{margin:12px 0 0 0;display:flex;align-items:flex-start;gap:8px;font-size:13.5px;line-height:1.5;color:#3A4566}
.ko-tip svg{flex-shrink:0;margin-top:2px;color:#1652F0}
.ko-opts{margin-top:12px;display:flex;flex-direction:column;gap:8px}
.ko-opt{display:flex;align-items:center;gap:12px;padding:12px 14px;border-radius:16px;border:1.5px solid #E6EAF3;background:#FFFFFF;color:#0B1433;text-decoration:none;transition:all .2s ease}
.ko-opt:hover{border-color:#AFC1F5;background:#F5F8FF;color:#0B1433}
.ko-opt > span:nth-child(2){flex-grow:1;display:flex;flex-direction:column;gap:2px}
.ko-opt b{font-size:15px;font-weight:600}
.ko-opt > span:nth-child(2) > span{font-size:13.5px;line-height:1.45;color:#5B6582}
.ko-opt > svg{flex-shrink:0;color:#8A93AD}
.ko-oi{width:40px;height:40px;flex-shrink:0;border-radius:12px;background:#F5F8FF;color:#1652F0;display:flex;align-items:center;justify-content:center}
.ko-cta{margin-top:20px;display:flex;flex-direction:column;align-items:center;gap:10px}
.ko-cn{font-size:13.5px;color:#5B6582}
.ko-row{margin-top:24px;width:100%;display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,1fr);gap:14px;align-items:stretch}
.ko-row .ko-card,.ko-row .ko-next{margin-top:0}
.ko-row .ko-next{flex-direction:column;align-items:flex-start;gap:10px;padding:18px 20px}
.ko-row .ko-go{margin-top:auto}
.ko-row .ko-idc{align-content:start}
.ko-sub{max-width:600px}
.ko-card:not(.ko-row .ko-card){max-width:640px}
.ko-opts{display:grid !important;grid-template-columns:minmax(0,1fr) minmax(0,1fr)}
.ko-a .ko-card{max-width:none}
.ko-a .ko-fix{display:grid;grid-template-columns:1.3fr 1fr 1fr;gap:10px}
.ko-a .ko-fix li{flex-direction:column;align-items:flex-start;gap:10px;padding:14px;min-height:0}
.ko-a .ko-ok{margin:0}
.ko-a .ko-tag{position:absolute;top:12px;right:12px}
.ko-a .ko-fix li.ko-bad{position:relative}
.ko-links{margin-top:18px;display:flex;align-items:center;gap:10px;font-size:14.5px;color:#8A93AD}
.ko-links a{font-weight:600;text-decoration:none;color:#3A4566}
.ko-links a:hover{color:#1652F0}
@media (prefers-reduced-motion: reduce){.ko-r .ko-halo::after,.ko-now .ko-dot::after,.ko-up{animation:none}.ko-tick path{animation:none;stroke-dashoffset:0}}
@media (max-width: 960px){
.ko{padding:36px 16px 32px 16px;align-items:stretch;text-align:center}
.ko-emb{width:72px;height:72px;align-self:center}
.ko-disc{width:48px;height:48px}.ko-disc svg{width:24px;height:24px}
.ko-pill{align-self:center;margin-top:14px}
.ko-h{font-size:24px;margin-top:10px}
.ko-sub{font-size:14.5px;margin-top:8px}
.ko-card{margin-top:20px;padding:14px 16px;border-radius:18px}
.ko-row{grid-template-columns:minmax(0,1fr);gap:10px;margin-top:20px}
.ko-opts{grid-template-columns:minmax(0,1fr) !important}
.ko-a .ko-fix{grid-template-columns:minmax(0,1fr)}
.ko-a .ko-fix li{flex-direction:row;align-items:center;padding:8px 12px}
.ko-a .ko-ok{margin:0 16px}
.ko-a .ko-tag{position:static}
.ko-card:not(.ko-row .ko-card){max-width:none}
.ko-next{flex-wrap:wrap;padding:14px 16px;border-radius:18px}
.ko-ni{display:none}
.ko-go{width:100%;justify-content:space-between}
.ko-idc{grid-template-columns:auto minmax(0,1fr)}
.ko-vb{grid-column:1 / -1;justify-self:start}
.ko-cta{position:sticky;bottom:0;margin:20px -16px 0 -16px;padding:12px 16px;background:#FFFFFF;border-top:1.5px solid #EEF1F7;align-items:stretch}
.ko-cta .ds-btn{justify-content:space-between}
.ko-cn{text-align:center;font-size:13px}
.ko-links{justify-content:center;font-size:14px}
}
'''

S_KO = '''class Component extends DCLogic {
  constructor(props) {
    super(props);
    this.v = (props || {}).variant || 'review';
  }
  renderVals() {
    const v = this.v;
    const T = {
      review: ['ko-r', 'In review', 'Thanks, Ada. We’re checking your ID.', 'Sumsub is comparing your photos and selfie with your ID. You can keep building while it runs.'],
      verified: ['ko-v', 'Verified', 'You’re verified, Ada.', 'Your identity is confirmed. Learners and validators will see you’re a real, verified creator.'],
      action: ['ko-a', 'Action needed', 'One photo needs a retake.', 'Almost there. The front of your ID was hard to read, so Sumsub couldn’t finish the check.'],
      failed: ['ko-f', 'Not verified', 'We couldn’t verify your ID this time.', 'Your selfie didn’t match the photo on your ID clearly enough. This happens, and it’s fixable.']
    }[v];
    return { koCls: T[0], pill: T[1], h1: T[2], sub: T[3], r: v === 'review', v: v === 'verified', a: v === 'action', f: v === 'failed' };
  }
}'''

TASK('CR-KYC-003.dc.html', 'Credalio · Identity check in review', c, S_KO, KO_CSS)
for n, t, prop in [('CR-KYC-004', 'Credalio · Identity verified', ' variant="verified"'),
                   ('CR-KYC-005', 'Credalio · Identity: action needed', ' variant="action"'),
                   ('CR-KYC-006', 'Credalio · Identity not verified', ' variant="failed"')]:
    WRAP(n + '.dc.html', 'CR-KYC-003', 1440, 820, t, prop)
    s = open(P + n + '.dc.html').read().replace('background: #F7F9FD', 'background: #FFFFFF'); open(P + n + '.dc.html', 'w').write(s)
WRAP('CR-KYC-002d.dc.html', 'CR-KYC-002', 1440, 820, 'Credalio · Verify your identity: review and submit', ' variant="review"')
s = open(P + 'CR-KYC-002d.dc.html').read().replace('background: #F7F9FD', 'background: #FFFFFF'); open(P + 'CR-KYC-002d.dc.html', 'w').write(s)
for n, tg, prop in [('CR-KYC-002d', 'CR-KYC-002', ' variant="review"'), ('CR-KYC-003', 'CR-KYC-003', ''),
                    ('CR-KYC-004', 'CR-KYC-003', ' variant="verified"'), ('CR-KYC-005', 'CR-KYC-003', ' variant="action"'),
                    ('CR-KYC-006', 'CR-KYC-003', ' variant="failed"')]:
    WRAP(n + '-Mobile.dc.html', tg, 390, 844, n + ' mobile preview', prop)
    s = open(P + n + '-Mobile.dc.html').read().replace('background: #F7F9FD', 'background: #FFFFFF'); open(P + n + '-Mobile.dc.html', 'w').write(s)
print('build13 done')
