# Batch 10 · CR-CREATE-002B (focus mode), CR-RDY-001 (+ variant "new" = 001s), CR-CTR-001, CR-ORI-001
exec(open('dash.py').read())
def H(n): return '{{'+n+'}}'
def ic(k, s=18, w=2): return ICON(I[k], s, w)
BGI='/_blob/d268046654a4206d2a726e62005bcc59'
ID_I='<rect x="3" y="5" width="18" height="14" rx="2.5"></rect><circle cx="9" cy="11" r="2.2"></circle><path d="M5.8 16a3.4 3.4 0 0 1 6.4 0M14.5 10h4M14.5 13.5h3"></path>'
DOC_I='<rect x="5" y="3" width="14" height="18" rx="2.5"></rect><path d="M9 8h6M9 12h6M9 16h3"></path>'
LOCK_I='<rect x="5" y="11" width="14" height="10" rx="2.5"></rect><path d="M8 11V8a4 4 0 0 1 8 0v3"></path>'
CLOCK_I='<circle cx="12" cy="12" r="9"></circle><path d="M12 7.5V12l3 2"></path>'
ALERT_I='<circle cx="12" cy="12" r="9"></circle><path d="M12 7.5v5.5M12 16.5h.01"></path>'
CHEV_I='<path d="m9 6 6 6-6 6"></path>'
DOWN_I='<path d="m6 9 6 6 6-6"></path>'
COMPASS_I='<circle cx="12" cy="12" r="9"></circle><path d="m15.5 8.5-2 5-5 2 2-5z"></path>'
PEN_I='<path d="M4 20h4L19 9a2.8 2.8 0 0 0-4-4L4 16z"></path><path d="m13.5 6.5 4 4"></path>'
ROCKET_I='<path d="M5 15c-1 1-1.5 4-1.5 4.5 .5 0 3.5-.5 4.5-1.5"></path><path d="M9 15l-3-3c1.5-4 5-8 12-8.5C17.5 10.5 13.5 14 9 15z"></path><circle cx="14.5" cy="9.5" r="1.6"></circle>'
SPK='<svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2l1.9 6.1L20 10l-6.1 1.9L12 18l-1.9-6.1L4 10l6.1-1.9z"></path></svg>'
def ik(d, s=18, w=2): return ICON(d, s, w)

ST={'complete':('#E7F5EE','#0F6B45',ic('check',12,3),'Complete'),
    'review':('#EAF0FF','#0E3BB8',ik(CLOCK_I,13,2.2),'In review'),
    'action':('#FFF4E2','#8A5300',ik(ALERT_I,13,2.2),'Action required'),
    'progress':('#EAF0FF','#1652F0',None,'In progress'),
    'todo':('#F1F3F8','#4A5578',None,'Not started')}
def pill(k, label=None):
    bg,fg,icn,l=ST[k]
    return f'<span class="st-pill" style="background: {bg}; color: {fg}">{icn or ""}{label or l}</span>'
def ring(pct, size, stroke, uid, inner=''):
    r=50-stroke/2
    return f'''<span class="rg" style="width: {size}px; height: {size}px"><svg viewBox="0 0 100 100" width="{size}" height="{size}" aria-hidden="true"><circle cx="50" cy="50" r="{r}" fill="none" stroke="#E6EAF3" stroke-width="{stroke}"></circle><circle class="rg-arc" cx="50" cy="50" r="{r}" fill="none" stroke="#1652F0" stroke-width="{stroke}" stroke-linecap="round" pathLength="100" stroke-dasharray="{pct} 100" transform="rotate(-90 50 50)"></circle></svg><span class="rg-in">{inner}</span></span>'''

COMMON_CSS='''.st-pill{display:inline-flex;align-items:center;gap:5px;height:26px;padding:0 10px;border-radius:999px;font-size:12.5px;font-weight:500;white-space:nowrap}
.rg{position:relative;display:inline-flex;flex-shrink:0}
.rg svg{display:block}
.rg-in{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}
.rg-arc{animation:rgIn 1.1s cubic-bezier(.3,.8,.3,1) .2s both}
@keyframes rgIn{from{stroke-dasharray:0 100}}
@keyframes ndPulse{0%{box-shadow:0 0 0 0 rgba(22,82,240,.35)}100%{box-shadow:0 0 0 10px rgba(22,82,240,0)}}
.sec-h{margin:0;font-size:13.5px;font-weight:600;color:#8A93AD}
.nova-card{padding:18px;border-radius:18px;background:#FFFFFF url('''+BGI+''') center top / 100% auto no-repeat;border:1.5px solid #E6EAF3}
.nova-card p{margin:10px 0 0 0;font-size:14.5px;line-height:1.55;color:#0B1433}
.know{padding:16px 18px;border-radius:18px;background:#F5F8FF;border:1.5px solid #E6EAF3;font-size:13.5px;line-height:1.55;color:#3A4566}
.know b{display:block;font-size:13px;font-weight:600;color:#0B1433;margin-bottom:4px}
.ds-btn.sm{height:44px;padding:0 5px 0 18px;font-size:14.5px;gap:10px}
.ds-btn.sm .ob-arrow{width:34px;height:34px}
@media (prefers-reduced-motion: reduce){.rg-arc{animation:none}}
'''

# =====================================================================
# CR-RDY-001 · Readiness (mid) / variant "new" (= CR-RDY-001s)
# =====================================================================
def rdy(state):
    mid = state=='mid'
    pct, done = (40,2) if mid else (20,1)
    gates=[('open','Draft and build','Open now, always',ik(PEN_I,18,2)),
           ('lock','Submit for validation','Needs '+('identity, credentials and orientation' if mid else 'identity, credentials, orientation and policies'),ik(I['valid'],18,2)),
           ('lock','Publish and earn','Also needs payout setup, once you have earnings',ik(ROCKET_I,18,2))]
    g=''
    for i,(k,t,d,icn) in enumerate(gates):
        on=k=='open'
        g+=f'''<li class="rd-gate{' rd-on' if on else ''}"><span class="rd-gn">{icn if on else ik(LOCK_I,16,2.2)}</span><span class="rd-gt"><b>{t}</b><span>{d}</span></span></li>'''
    hero=f'''<section class="ds-card rd-hero ob-in2" aria-label="Your readiness">
<div class="rd-score">{ring(pct,92,9,'r1','<b class="rd-pct">'+str(pct)+'%</b><span class="rd-pl">ready</span>')}<span class="rd-sc"><b>{done} of 5 done</b><span>{'3 to go before you can submit' if mid else '4 to go before you can submit'}</span></span></div>
<div class="rd-unl"><ol class="rd-gates">{g}</ol></div>
</section>'''
    rows=[('profile','Creator profile','Completed during setup.','complete',None,None,None),
          (ID_I,'Verify your identity','A government ID and a quick selfie check, through Sumsub.','review' if mid else 'todo','Usually reviewed within 1 business day.' if mid else None,None if mid else 'Start','CR-KYC-001.dc.html'),
          ('cert','Credentials & expertise','Degrees, certifications like AWS, licences, experience and other evidence.','action' if mid else 'todo','MSc scan unreadable. Upload a clearer copy.' if mid else None,'Fix now' if mid else 'Start','#'),
          ('centre','Creator Orientation','Seven short modules on creating trusted learning.','progress' if mid else 'todo',None,'Continue' if mid else 'Start','CR-ORI-001.dc.html'),
          (DOC_I,'Creator policies','The creator terms, content and AI policies.','complete' if mid else 'todo',None,None if mid else 'Review','#')]
    def row(r, extra=''):
        icon,t,d,k,note,cta,href=r
        icn = ic(icon,20,1.9) if icon in I else ik(icon,20,1.9)
        prog=''
        if k=='progress': prog='<span class="rd-mini"><span style="width: 43%"></span></span><span class="rd-note">3 of 7 modules</span>'
        nt=f'<span class="rd-note{" rd-warn" if k=="action" else ""}">{note}</span>' if note else ''
        tone=' rd-done' if k=='complete' else (' rd-act' if k=='action' else '')
        act=f'<a href="{href}" class="rd-cta{" rd-cta-p" if k=="action" else ""}">{cta}{ik(CHEV_I,15,2.4)}</a>' if cta else '<span class="rd-cta-sp"></span>'
        return f'''<li class="rd-row{tone}"><span class="rd-ic">{icn}</span><span class="rd-tx"><b>{t}</b><span class="rd-d">{d}</span></span><span class="rd-st">{pill(k)}{nt}{prog}</span>{act}</li>'''
    lst=''.join(row(r) for r in rows)
    later=row(('wallet','Payout setup','Only needed the first time you have earnings to withdraw.','todo',None,'Set up','#'))
    if mid:
        nova='Fix the MSc scan first, it’s the only thing waiting on you. Then pick up Orientation at module 4. Identity is already with the reviewers.'
        nb='Fix my credentials'
    else:
        nova='Start with your identity. It’s reviewed within a business day, so it runs in the background while you draft your first course.'
        nb='Verify my identity'
    rail=f'''<aside class="rd-rail">
<div class="nova-card ob-in3"><span style="display: flex; align-items: center; gap: 10px">{NOVA_AV(34)}<span style="display: flex; flex-direction: column"><b style="font-size: 14.5px">Nova suggests</b><span style="font-size: 12.5px; color: #5B6582">Your fastest route to submitting</span></span></span><p>{nova}</p><a href="{"#" if mid else "CR-KYC-001.dc.html"}" class="ds-link" style="margin-top: 12px; font-size: 14px">{nb}{ik(I['arrow'],15,2.4)}</a></div>
<div class="know ob-in4 rd-know"><b>Drafting is never blocked</b>Readiness only unlocks the trusted steps. Your Studio stays open the whole time.</div>
</aside>'''
    return f'''<div class="rd-head ob-in"><h1 class="ds-h1">Your readiness</h1><p class="ds-sub">Draft freely. These steps unlock submitting for validation, publishing and getting paid.</p></div>
{hero}
<div class="rd-grid">
<div class="rd-col">
<section class="ob-in3"><h2 class="sec-h rd-sh">Requirements</h2><ul class="ds-card rd-list">{lst}</ul></section>
<section class="ob-in4" style="margin-top: 22px"><h2 class="sec-h rd-sh">When you start earning</h2><ul class="ds-card rd-list">{later}</ul></section>
</div>
{rail}
</div>'''

RD_CSS=COMMON_CSS+'''.rd-head{margin-top:8px}
.rd-hero{margin-top:22px;padding:20px 28px;display:grid;grid-template-columns:auto minmax(0,1fr);gap:40px;align-items:center}
.rd-score{display:flex;align-items:center;gap:20px}
.rd-pct{font-size:22px;font-weight:600;letter-spacing:-0.03em;line-height:1}
.rd-pl{font-size:11px;color:#5B6582;margin-top:2px}
.rd-sc{display:flex;flex-direction:column;gap:4px}
.rd-sc b{font-size:17px;font-weight:600}
.rd-sc span{font-size:14px;color:#5B6582}
.rd-unl{min-width:0;padding-left:36px;border-left:1.5px solid #EEF1F7}
.rd-gates{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px;position:relative}
.rd-gates::before{content:'';position:absolute;left:20px;right:calc(33.33% - 6px);top:19px;height:3px;border-radius:3px;background:linear-gradient(90deg,#1652F0 0%,#1652F0 34%,#E6EAF3 34%)}
.rd-gate{position:relative;display:flex;flex-direction:column;gap:10px}
.rd-gn{flex-shrink:0;width:40px;height:40px;border-radius:50%;box-sizing:border-box;border:2px solid #D6DDEE;background:#FFFFFF;color:#8A93AD;display:flex;align-items:center;justify-content:center;position:relative;z-index:1}
.rd-on .rd-gn{background:#1652F0;border-color:#1652F0;color:#FFFFFF;box-shadow:0 6px 16px rgba(22,82,240,.28)}
.rd-gt{display:flex;flex-direction:column;gap:3px}
.rd-gt b{font-size:14.5px;font-weight:600}
.rd-gt span{font-size:13px;line-height:1.45;color:#5B6582}
.rd-on .rd-gt span{color:#0F6B45;font-weight:500}
.rd-grid{margin-top:26px;display:grid;grid-template-columns:minmax(0,1fr) 320px;gap:24px;align-items:start}
.rd-sh{margin:0 0 10px 4px}
.rd-list{list-style:none;margin:0;padding:6px 0}
.rd-row{display:grid;grid-template-columns:44px minmax(0,1fr) 220px 112px;align-items:center;gap:16px;padding:16px 22px}
.rd-row + .rd-row{border-top:1.5px solid #F0F2F8}
.rd-ic{width:44px;height:44px;border-radius:14px;background:#F5F8FF;color:#1652F0;display:flex;align-items:center;justify-content:center}
.rd-done .rd-ic{background:#E7F5EE;color:#0F6B45}
.rd-act .rd-ic{background:#FFF4E2;color:#8A5300}
.rd-tx{display:flex;flex-direction:column;gap:3px;min-width:0}
.rd-tx b{font-size:15px;font-weight:600}
.rd-d{font-size:13.5px;line-height:1.45;color:#5B6582}
.rd-note{font-size:11.5px;line-height:1.4;color:#5B6582}
.rd-warn{color:#8A5300;font-weight:500}
.rd-mini{display:block;width:140px;height:5px;border-radius:5px;background:#E6EAF3;margin-top:2px;overflow:hidden}
.rd-mini span{display:block;height:100%;border-radius:5px;background:#1652F0}
.rd-st{display:flex;flex-direction:column;align-items:flex-start;gap:6px;min-width:0}
.rd-cta{justify-self:end;display:inline-flex;align-items:center;gap:4px;height:38px;padding:0 10px 0 14px;border-radius:999px;border:1.5px solid #D6DDEE;background:#FFFFFF;color:#0B1433;font-size:14px;font-weight:600;text-decoration:none;white-space:nowrap;transition:border-color .2s ease,background .2s ease}
.rd-cta:hover{border-color:#1652F0;background:#F5F8FF;color:#0B1433}
.rd-cta-p{background:#1652F0;border-color:#1652F0;color:#FFFFFF}
.rd-cta-p:hover{background:#0E3BB8;border-color:#0E3BB8;color:#FFFFFF}
.rd-rail{display:flex;flex-direction:column;gap:14px;position:sticky;top:88px;margin-top:29px}
@media (max-width: 1180px){.rd-grid{grid-template-columns:minmax(0,1fr)}.rd-rail{position:static;margin-top:0;display:grid;grid-template-columns:1fr 1fr}.rd-row{grid-template-columns:44px minmax(0,1fr) auto auto}}
@media (max-width: 960px){
.rd-head .ds-sub{font-size:14px}
.rd-hero{margin-top:24px;padding:20px 18px 22px 18px;grid-template-columns:minmax(0,1fr);gap:0;border-radius:18px}
.rd-score{gap:14px}
.rd-score .rg,.rd-score .rg svg{width:68px !important;height:68px !important}
.rd-pct{font-size:19px}.rd-pl{display:none}
.rd-sc b{font-size:15.5px}.rd-sc span{font-size:13px}
.rd-unl{margin-top:20px;padding:22px 0 0 0;border-left:0;border-top:1.5px solid #F0F2F8}
.rd-unl .sec-h{display:none}
.rd-gates{margin:0;grid-template-columns:minmax(0,1fr);gap:28px}
.rd-gates::before{left:15px;right:auto;top:18px;bottom:18px;width:3px;height:auto;background:linear-gradient(180deg,#1652F0 0%,#1652F0 30%,#E6EAF3 30%)}
.rd-gate{flex-direction:row;align-items:center;gap:12px}
.rd-gn{width:32px;height:32px}
.rd-gn svg{width:14px;height:14px}
.rd-gt{gap:2px}.rd-gt b{font-size:14.5px}.rd-gt span{font-size:13px;line-height:1.4}
.rd-grid{margin-top:28px;gap:28px}
.rd-sh{margin-left:2px;font-size:13px}
.rd-list{padding:2px 0;border-radius:18px}
.rd-row{grid-template-columns:36px minmax(0,1fr) auto;grid-template-areas:"i t t" "i s a";row-gap:8px;column-gap:12px;padding:13px 14px}
.rd-ic{grid-area:i;align-self:start;width:36px;height:36px;border-radius:11px}
.rd-ic svg{width:18px;height:18px}
.rd-tx{grid-area:t}.rd-st{grid-area:s}
.rd-cta,.rd-cta-sp{grid-area:a;align-self:center}
.rd-cta-sp{height:36px}
.rd-row{min-height:89px;box-sizing:border-box;align-content:center}
.rd-tx b{font-size:14.5px}
.rd-d{display:none}
.rd-note{font-size:11.5px}

.rd-mini{width:120px;margin-top:4px}
.rd-cta{height:36px;padding:0 8px 0 12px;font-size:13.5px}
.st-pill{height:24px;font-size:12px;padding:0 9px}
.rd-rail{grid-template-columns:minmax(0,1fr)}
.rd-know{display:none}
.rd-grid{display:flex;flex-direction:column;align-items:stretch}.rd-rail{order:-1}.rd-col{width:100%}
.nova-card{padding:18px}.nova-card p{font-size:14.5px;line-height:1.6;margin-top:12px}
}
'''
S_RD='''class Component extends DCLogic {
  constructor(props) { super(props); this.state = { nav: false }; this.isNew = (props || {}).variant === 'new'; }
  renderVals() {
    const isNew = this.isNew;
    return { NAVJS, isNew, isMid: !isNew };
  }
}'''.replace('NAVJS', NAV_JS)
c='<sc-if value="'+H('isMid')+'" hint-placeholder-val="'+H('true')+'">'+rdy('mid')+'</sc-if>\n<sc-if value="'+H('isNew')+'" hint-placeholder-val="'+H('false')+'">'+rdy('new')+'</sc-if>'
open(P+'CR-RDY-001.dc.html','w').write(SHELL('Verification & readiness',c,'Credalio · Your readiness',S_RD,RD_CSS,1000))

# =====================================================================
# CR-CTR-001 · Creator Centre
# =====================================================================
GUIDES=[(COMPASS_I,'Getting started','Your first learning experience, step by step.',['Choosing what to create','Starting with your Copilot','Inviting collaborators']),
 (I['valid'],'Creating trusted learning','Outcomes, evidence and quality.',['Writing observable outcomes','Designing practice that proves skills','Accessibility basics']),
 (I['assigned'],'Validation guide','How validation works and how to prepare.',['What validators look for','Responding to requests','Tiers and revalidation']),
 (I['earn'],'Pricing & creator economy','DLP, Credits, your wallet and earnings.',['How permitted ranges work','Credit Wallet vs Earnings','Revenue shares']),
 ('SPARK','AI creation guide','Working well with your Copilot.',['What Nova can and can’t do','Reviewing AI-assisted content','Disclosure']),
 (DOC_I,'Policies & standards','The rules that keep learning trustworthy.',['Creator terms','Content and IP policy','AI policy'])]
gc=''
for i,(icn,t,d,arts) in enumerate(GUIDES):
    gi = '<svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'+SPARK_D.replace(' fill="currentColor" stroke="none"','')+'</svg>' if icn=='SPARK' else ik(icn,20,1.9)
    al=''.join(f'<li><a href="#" class="ct-art"><span>{a}</span>{ik(CHEV_I,15,2.2)}</a></li>' for a in arts)
    gc+=f'''<article class="ds-card ct-g {H('g'+str(i))}"><button type="button" class="ct-gh" onClick="{H('t'+str(i))}" aria-expanded="{H('e'+str(i))}"><span class="ct-gi">{gi}</span><span class="ct-gt"><b>{t}</b><span>{d}</span></span><span class="ct-gx">{ik(DOWN_I,18,2.2)}</span></button><ul class="ct-arts">{al}</ul><a href="#" class="ct-all">See all{ik(I['arrow'],14,2.4)}</a></article>'''
nodes=''.join(f'<span class="ct-n {"ct-nd" if i<3 else ("ct-nc" if i==3 else "")}">{ic("check",13,3) if i<3 else i+1}</span>' for i in range(7))
c=f'''<section class="ct-hero ob-in" aria-labelledby="ct-h">
<h1 id="ct-h" class="ds-h1">Creator Centre</h1>
<p class="ds-sub">Guides, policies and help for creating on Credalio. Look anything up, whenever you need it.</p>
<label class="ct-search">{ic('search',20,2)}<span class="sr-only">Search the Creator Centre</span><input placeholder="Search guides, policies and help…"></label>
<div class="ct-pop"><span>Popular</span><a href="#" class="ds-chip ct-chip">Writing observable outcomes</a><a href="#" class="ds-chip ct-chip">What validators look for</a><a href="#" class="ds-chip ct-chip">Credit Wallet vs Earnings</a></div>
</section>
<a href="CR-ORI-001.dc.html" class="ds-card ct-ori ob-in2">
<span class="ct-oi">{ring(43,64,10,'co','<b style="font-size: 15px">3/7</b>')}</span>
<span class="ct-ot"><span class="ct-ol">Orientation · up next</span><b>Understanding validation</b><span class="ct-os">Module 4 of 7 · about 12 min</span></span>
<span class="ct-path" aria-hidden="true">{nodes}</span>
<span class="ds-btn sm ct-ob"><span>Continue</span><span class="ob-arrow">{ic('arrow',16,2.4)}</span></span>
</a>
<div class="ct-gh2 ob-in3"><h2 class="sec-h">Guides</h2></div>
<div class="ct-grid ob-in3">{gc}</div>
<section class="ds-card ct-help ob-in4" aria-label="Help and support">
<span style="display: flex; align-items: center; gap: 14px; min-width: 0">{NOVA_AV(44)}<span class="ct-ht"><b>Can’t find it? Ask Nova.</b><span>Nova knows the guides and your setup. A person is always one step away.</span></span></span>
<span class="ct-ha"><a href="#" class="ds-ghost">Contact support</a><a href="#" class="ds-link">My requests</a></span>
</section>'''
CT_CSS=COMMON_CSS+'''.ct-hero{margin-top:8px;padding:30px 32px 26px 32px;border-radius:24px;border:1.5px solid #E6EAF3;background:#FFFFFF url('''+BGI+''') center top / cover no-repeat}
.ct-search{margin-top:20px;max-width:640px;height:56px;box-sizing:border-box;display:flex;align-items:center;gap:12px;padding:0 20px;border-radius:999px;background:#FFFFFF;border:1.5px solid #D6DDEE;color:#5B6582;box-shadow:0 12px 30px rgba(22,82,240,.08);transition:border-color .2s ease,box-shadow .2s ease}
.ct-search:focus-within{border-color:#1652F0;box-shadow:0 0 0 4px rgba(22,82,240,.12),0 12px 30px rgba(22,82,240,.08)}
.ct-search input{flex-grow:1;min-width:0;border:0;outline:none;background:transparent;font-family:inherit;font-size:16px;color:#0B1433}
.ct-search input::placeholder{color:#8A93AD}
.ct-pop{margin-top:14px;display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.ct-pop > span{font-size:13.5px;color:#5B6582;margin-right:4px}
.ct-chip{height:34px;font-size:13.5px;padding:0 14px;text-decoration:none;background:rgba(255,255,255,.9)}
.ct-ori{margin-top:16px;padding:18px 22px;display:grid;grid-template-columns:auto minmax(0,1fr) auto auto;gap:20px;align-items:center;text-decoration:none;color:#0B1433;transition:border-color .2s ease,box-shadow .2s ease}
.ct-ori:hover{border-color:#AFC1F5;box-shadow:0 12px 30px rgba(22,82,240,.08)}
.ct-ot{display:flex;flex-direction:column;gap:3px;min-width:0}
.ct-ol{font-size:12.5px;font-weight:500;color:#1652F0}
.ct-ot b{font-size:16px;font-weight:600}
.ct-os{font-size:13.5px;color:#5B6582}
.ct-path{position:relative;display:flex;gap:14px}
.ct-path::before{content:'';position:absolute;left:12px;right:12px;top:12px;height:3px;border-radius:3px;background:linear-gradient(90deg,#1652F0 0%,#1652F0 50%,#E6EAF3 50%)}
.ct-n{position:relative;width:26px;height:26px;box-sizing:border-box;border-radius:50%;border:2px solid #D6DDEE;background:#FFFFFF;color:#8A93AD;font-size:11.5px;font-weight:600;display:flex;align-items:center;justify-content:center}
.ct-nd{background:#1652F0;border-color:#1652F0;color:#FFFFFF}
.ct-nc{border-color:#1652F0;color:#1652F0;animation:ndPulse 2s ease-out infinite}
.ct-gh2{margin:28px 0 12px 4px}
.ct-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}
.ct-g{padding:20px 20px 16px 20px;display:flex;flex-direction:column}
.ct-gh{display:flex;align-items:flex-start;gap:14px;margin-bottom:14px;border:0;background:none;padding:0;text-align:left;font-family:inherit;color:#0B1433;cursor:default}
.ct-gi{width:42px;height:42px;flex-shrink:0;border-radius:13px;background:#F5F8FF;color:#1652F0;display:flex;align-items:center;justify-content:center}
.ct-gt{display:flex;flex-direction:column;gap:3px;min-width:0}
.ct-gt b{font-size:15.5px;font-weight:600}
.ct-gt span{font-size:13.5px;line-height:1.45;color:#5B6582}
.ct-gx{display:none}
.ct-arts{list-style:none;margin:auto 0 0 0;padding:0;border-top:1.5px solid #F0F2F8}
.ct-art{display:flex;align-items:center;justify-content:space-between;gap:10px;min-height:40px;border-bottom:1px solid #F3F5FA;color:#0B1433;font-size:14px;text-decoration:none}
.ct-art svg{color:#8A93AD;flex-shrink:0;transition:transform .2s ease,color .2s ease}
.ct-art:hover{color:#1652F0}.ct-art:hover svg{color:#1652F0;transform:translateX(2px)}
.ct-all{margin-top:12px;align-self:flex-start;display:inline-flex;align-items:center;gap:6px;font-size:13.5px;font-weight:600;text-decoration:none}
.ct-help{margin-top:16px;padding:18px 22px;display:flex;align-items:center;justify-content:space-between;gap:20px;background:#FFFFFF url('''+BGI+''') center top / cover no-repeat}
.ct-help .ds-ghost{background:rgba(255,255,255,.9)}
.ct-ht{display:flex;flex-direction:column;gap:3px;min-width:0}
.ct-ht b{font-size:15.5px;font-weight:600}
.ct-ht span{font-size:13.5px;color:#5B6582}
.ct-ha{display:flex;align-items:center;gap:18px;flex-shrink:0}
@media (max-width: 1180px){.ct-grid{grid-template-columns:repeat(2,minmax(0,1fr))}.ct-path{display:none}}
@media (max-width: 960px){
.ct-hero{margin-top:4px;padding:12px 0 0 0;border:0;border-radius:0;background:transparent}
.ct-hero .ds-sub{font-size:14px}
.ct-search{margin-top:14px;height:50px;padding:0 16px}
.ct-search input{font-size:15px}
.ct-pop{flex-wrap:nowrap;overflow-x:auto;margin:12px -16px 0 -16px;padding:0 16px;scrollbar-width:none}
.ct-pop::-webkit-scrollbar{display:none}
.ct-pop > span{display:none}
.ct-chip{flex-shrink:0;white-space:nowrap;height:34px !important;font-size:13px !important}
.ct-ori{margin-top:22px;padding:22px 18px 18px 18px;grid-template-columns:auto minmax(0,1fr);gap:16px 14px;border-radius:20px;align-items:center}
.ct-ot{gap:5px}
.ct-ob{margin-top:6px}
.ct-oi .rg,.ct-oi svg{width:52px !important;height:52px !important}
.ct-oi b{font-size:13px !important}
.ct-ot b{font-size:15px;line-height:1.35}.ct-os{font-size:12.5px;line-height:1.45}
.ct-ob{grid-column:1 / -1;width:100%;justify-content:space-between}
.ct-gh2{margin:24px 0 10px 2px}
.ct-grid{grid-template-columns:minmax(0,1fr);gap:0;border:1.5px solid #E6EAF3;border-radius:18px;background:#FFFFFF;overflow:hidden}
.ct-g{padding:0;border:0;border-radius:0;box-shadow:none}
.ct-g + .ct-g{border-top:1.5px solid #F0F2F8}
.ct-gh{width:100%;margin:0;padding:13px 14px;align-items:center;gap:12px;cursor:pointer;min-height:60px;box-sizing:border-box}
.ct-gi{width:36px;height:36px;border-radius:11px}
.ct-gi svg{width:18px;height:18px}
.ct-gt b{font-size:14.5px}
.ct-gt span{font-size:12.5px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.ct-gx{display:flex;margin-left:auto;color:#8A93AD;transition:transform .25s ease}
.ct-arts,.ct-all{display:none}
.ct-open .ct-gx{transform:rotate(180deg)}
.ct-open .ct-arts{display:block;margin:0 14px;border-top:1px solid #F0F2F8}
.ct-open .ct-all{display:inline-flex;margin:8px 14px 14px 14px}
.ct-art{font-size:14px;min-height:44px}
.ct-help{flex-direction:column;align-items:stretch;gap:14px;padding:16px;border-radius:18px;margin-top:18px}
.ct-help .ds-ghost{flex-grow:1}
}
'''
S_CT='''class Component extends DCLogic {
  constructor(props) { super(props); this.state = { nav: false, open: 0 }; }
  renderVals() {
    const v = { NAVJS };
    for (let i = 0; i < 6; i++) { const on = this.state.open === i; v['g' + i] = on ? 'ct-open' : ''; v['e' + i] = on ? 'true' : 'false'; v['t' + i] = () => this.setState({ open: on ? -1 : i }); }
    return v;
  }
}'''.replace('NAVJS', NAV_JS)
open(P+'CR-CTR-001.dc.html','w').write(SHELL('Creator Centre',c,'Credalio · Creator Centre',S_CT,CT_CSS,1000))

# =====================================================================
# CR-ORI-001 · Creator Orientation home
# =====================================================================
MODS=[('Welcome to Credalio','2 lessons · check · 8 min'),
 ('Creating trusted learning','2 lessons · check · 10 min'),
 ('Outcomes, skills & evidence','3 lessons · check · 12 min'),
 ('Understanding validation','3 lessons · check · 12 min'),
 ('AI & responsible creation','2 lessons · check · scenario · 10 min'),
 ('Creator economy','2 lessons · check · 10 min'),
 ('Creator responsibilities','2 lessons · check · scenario · 8 min')]
M4=[('What validators look at','done'),('The validation case','next'),('Tiers and revalidation','todo'),('Quick knowledge check','todo')]
ml=''
for i,(t,meta) in enumerate(MODS):
    n=i+1
    if i<3:
        ml+=f'''<li class="or-m or-done"><span class="or-n">{ic('check',14,3)}</span><span class="or-mt"><b><span class="or-mn">Module {n} · </span>{t}</b><span>{meta}</span></span>{pill('complete','Done')}<a href="#" class="or-rv">Review</a><span class="or-chev">{ik(CHEV_I,16,2.2)}</span></li>'''
    elif i==3:
        st=''
        for (lt,k) in M4:
            mk = ic('check',11,3.2) if k=='done' else ''
            st+=f'<li class="or-s or-s-{k}"><span class="or-sd">{mk}</span><span>{lt}</span>{"<em>Up next</em>" if k=="next" else ""}</li>'
        ml+=f'''<li class="or-m or-cur"><span class="or-n">{n}</span><div class="or-cb"><span class="or-mt"><b><span class="or-mn">Module {n} · </span>{t}</b><span>{meta} · 1 of 4 steps done</span></span><p class="or-desc">What validators look at, how a case runs, and what tiers mean.</p><ol class="or-steps">{st}</ol></div>{pill('progress')}</li>'''
    else:
        ml+=f'''<li class="or-m"><span class="or-n">{n}</span><span class="or-mt"><b><span class="or-mn">Module {n} · </span>{t}</b><span>{meta}</span></span><span class="or-lock">{ik(CLOCK_I,13,2.2)}{meta.split(" · ")[-1]}</span></li>'''
c=f'''<a href="CR-CTR-001.dc.html" class="ds-back ob-in">{ic('back',16,2.2)}Creator Centre</a>
<div class="or-head ob-in"><h1 class="ds-h1">Creator Orientation</h1><p class="ds-sub">Seven short modules on creating trusted learning, with quick checks and real scenarios.</p></div>
<div class="or-grid">
<section class="or-col ob-in2" aria-label="Modules"><ol class="or-list">{ml}</ol></section>
<aside class="or-rail">
<div class="ds-card or-next ob-in2">
<div class="or-nt">{ring(44,88,9,'or','<b style="font-size: 20px; letter-spacing: -0.02em">44%</b>')}<span style="display: flex; flex-direction: column; gap: 3px; min-width: 0"><span class="or-lab">Up next</span><b class="or-nb">The validation case</b><span class="or-ns">Module 4 · lesson 2 of 3</span></span></div>
<a href="CR-ORI-003.dc.html" class="ds-btn or-cta"><span>Continue Orientation</span><span class="ob-arrow">{ic('arrow',18,2.4)}</span></a>
<dl class="or-stats"><div><dt>Modules</dt><dd>3 of 7</dd></div><div><dt>Time left</dt><dd>~37 min</dd></div><div><dt>Total</dt><dd>~70 min</dd></div></dl>
</div>
<div class="know ob-in3 or-know"><b>Never blocks your drafting</b>Orientation is one of the steps that unlock submitting for validation. <a href="CR-RDY-001.dc.html" class="ds-link" style="font-size: 13.5px">See your readiness</a></div>
</aside>
</div>'''
OR_CSS=COMMON_CSS+'''.or-head{margin-top:6px}
.or-grid{margin-top:24px;display:grid;grid-template-columns:minmax(0,1fr) 340px;gap:24px;align-items:start}
.or-list{list-style:none;margin:0;padding:0;position:relative}
.or-list::before{content:'';position:absolute;left:21px;top:30px;bottom:30px;width:3px;border-radius:3px;background:linear-gradient(180deg,#1652F0 0%,#1652F0 47%,#E6EAF3 47%)}
.or-m{position:relative;display:grid;grid-template-columns:44px minmax(0,1fr) auto auto;align-items:center;gap:16px;padding:12px 0}
.or-n{position:relative;z-index:1;width:44px;height:44px;box-sizing:border-box;border-radius:50%;border:2px solid #D6DDEE;background:#F7F9FD;color:#8A93AD;font-size:15px;font-weight:600;display:flex;align-items:center;justify-content:center}
.or-done .or-n{background:#1652F0;border-color:#1652F0;color:#FFFFFF}
.or-cur{align-items:start}
.or-cur .or-n{background:#FFFFFF;border-color:#1652F0;color:#1652F0;animation:ndPulse 2s ease-out infinite;margin-top:18px}
.or-cur > .st-pill{position:absolute;right:20px;top:30px}
.or-mt{display:flex;flex-direction:column;gap:3px;min-width:0}
.or-mt b{font-size:15.5px;font-weight:600}
.or-mt span{font-size:13px;color:#5B6582}
.or-done .or-mt b{color:#3A4566}
.or-chev{display:none}
.or-rv{font-size:14px;font-weight:600;text-decoration:none;padding:0 4px}
.or-lock{display:inline-flex;align-items:center;gap:5px;font-size:13px;color:#8A93AD;white-space:nowrap}
.or-m:not(.or-done):not(.or-cur) .or-mt > span{display:none}
.or-mt b .or-mn{display:inline;font:inherit;color:inherit;margin:0}
.or-cb{grid-column:2 / -1;padding:18px 20px 20px 20px;border-radius:20px;background:#FFFFFF;border:1.5px solid #CBD7F5;box-shadow:0 0 0 4px rgba(22,82,240,.06),0 14px 34px rgba(22,82,240,.08)}
.or-cb .or-mt{padding-right:110px}
.or-desc{margin:10px 0 0 0;font-size:14.5px;line-height:1.55;color:#3A4566}
.or-steps{list-style:none;margin:14px 0 0 0;padding:0;display:flex;flex-direction:column;gap:2px}
.or-s{display:flex;align-items:center;gap:10px;min-height:36px;font-size:14px;color:#3A4566}
.or-s em{font-style:normal;font-size:12px;font-weight:500;color:#1652F0;background:#EAF0FF;border-radius:999px;padding:3px 9px}
.or-sd{width:20px;height:20px;box-sizing:border-box;border-radius:50%;border:2px solid #D6DDEE;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.or-s-done{color:#5B6582}
.or-s-done .or-sd{background:#0F6B45;border-color:#0F6B45;color:#FFFFFF}
.or-s-next{color:#0B1433;font-weight:600}
.or-s-next .or-sd{border-color:#1652F0;border-width:6px}
.or-go{margin-top:14px}
.or-rail{position:sticky;top:88px;display:flex;flex-direction:column;gap:14px}
.or-next{padding:20px}
.or-nt{display:flex;align-items:center;gap:16px}
.or-lab{font-size:12.5px;font-weight:500;color:#1652F0}
.or-nb{font-size:17px;font-weight:600;letter-spacing:-0.01em}
.or-ns{font-size:13.5px;color:#5B6582}
.or-cta{margin-top:18px;width:100%;justify-content:space-between}
.or-stats{margin:16px 0 0 0;padding-top:14px;border-top:1.5px solid #F0F2F8;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px}
.or-stats div{display:flex;flex-direction:column;gap:2px}
.or-stats dt{font-size:12px;color:#5B6582}
.or-stats dd{margin:0;font-size:14px;font-weight:600}
@media (max-width: 1180px){.or-grid{grid-template-columns:minmax(0,1fr) 300px}}
@media (max-width: 960px){
.or-head .ds-sub{font-size:14px}
.or-grid{margin-top:16px;display:flex;flex-direction:column-reverse;gap:20px}
.or-rail{position:static;width:100%}
.or-know{display:none}
.or-next{padding:14px 16px;border-radius:18px}
.or-nt{gap:12px}
.or-nt .rg,.or-nt svg{width:60px !important;height:60px !important}
.or-nt .rg-in b{font-size:14px !important}
.or-nb{font-size:15.5px}.or-ns{font-size:12.5px}
.or-cta{margin-top:14px}
.or-stats{display:none}
.or-list::before{left:15px;top:22px;bottom:22px}
.or-m{grid-template-columns:32px minmax(0,1fr) auto;gap:12px;padding:9px 0}
.or-n{width:32px;height:32px;font-size:13px}
.or-n svg{width:12px;height:12px}
.or-mt b{font-size:14.5px}.or-mt span{font-size:12.5px}
.or-done > .st-pill{display:none}
.or-cur .or-n{margin-top:14px}
.or-cur > .st-pill{display:none}
.or-cb{grid-column:2 / -1;padding:14px;border-radius:16px}
.or-cb .or-mt{padding-right:0}
.or-desc{display:none}
.or-steps,.or-lock,.or-rv,.or-mt b .or-mn{display:none}
.or-chev{display:flex;color:#AFC1F5}
.or-m:not(.or-done):not(.or-cur) .or-mt > span{display:block}
.or-mt{gap:2px}
.or-mt b{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.or-list{margin-top:4px}
.or-list::before{top:26px;bottom:26px}
.or-m{padding:12px 0}
.or-done .or-mt b{font-weight:600}
.or-cur{align-items:center}
.or-cur .or-n{margin-top:0}
.or-cb{grid-column:2 / -1;padding:12px 14px;border-radius:16px;box-shadow:0 0 0 3px rgba(22,82,240,.06)}
}
'''
S_OR='''class Component extends DCLogic {
  constructor(props) { super(props); this.state = { nav: false }; }
  renderVals() { return { NAVJS }; }
}'''.replace('NAVJS', NAV_JS)
open(P+'CR-ORI-001.dc.html','w').write(SHELL('Creator Centre',c,'Credalio · Creator Orientation',S_OR,OR_CSS,1000))

# =====================================================================
# CR-CREATE-002B · Build from scratch (focus mode)
# =====================================================================
FMT=[('course','Course'),('cert','Professional certification'),('path','Career path'),('program','Learning program')]
fm=''
for i,(k,l) in enumerate(FMT):
    fm+=f'''<button type="button" role="radio" class="xb-f {H('c'+str(i))}" aria-checked="{H('a'+str(i))}" onClick="{H('p'+str(i))}"><span class="xb-fi">{ic(k,18,1.9)}</span><span>{l}</span><span class="xb-ck">{ic('check',10,3.4)}</span></button>'''
c='''<div class="xb-root">
<header class="xb-top">
<a href="CR-CREATE-001.dc.html" class="xb-x" aria-label="Close and go back">'''+ic('close',18,2.2)+'''</a>
<div class="xb-title"><span class="xb-t1">{{newTitle}}</span><span class="xb-t2">From scratch</span></div>
<span style="flex-grow: 1"></span>
<a href="#" class="ds-tok xb-tok" aria-label="20,000 AI Tokens">'''+COIN('xbc',26)+'''<span>20K</span></a>
</header>
<main class="xb-main">
<div class="xb-col">
<h1 class="xb-h1 ob-in">Build it your way.</h1>
<p class="xb-sub ob-in2">You lead every step of {{lower}} setup. Nova is one tap away on every screen, if you want a hand.</p>
<div class="xb-fmts ob-in2" role="radiogroup" aria-label="What are you building?">'''+fm+'''</div>
<section class="xb-route ob-in3" aria-label="Your route">
<div class="xb-rh"><span class="sec-h">Your route</span><span class="xb-rn">{{count}} steps · save and come back anytime</span></div>
<ol class="xb-steps">
<sc-for list="{{steps}}" as="s" hint-placeholder-count="8"><li class="xb-s {{s.cls}}"><span class="xb-sn">{{s.n}}</span><span class="xb-sl">{{s.label}}</span></li></sc-for>
</ol>
</section>
<div class="xb-acts ob-in4">
<a href="#" class="ds-btn xb-go"><span>Start {{lower}} setup</span><span class="ob-arrow">'''+ic('arrow',18,2.4)+'''</span></a>
<a href="CR-CREATE-002A.dc.html" class="xb-alt">'''+SPK+'''Rather sketch it with Nova first?</a>
</div>
</div>
</main>
</div>'''
XB_CSS=COMMON_CSS+'''body{background:#FFFFFF}
.xb-root{min-height:100vh;display:flex;flex-direction:column;background:#FFFFFF;font-family:'Google Sans','Google Sans Text','Helvetica Neue',system-ui,sans-serif;color:#0B1433;position:relative;isolation:isolate}
.xb-root::before{content:'';position:absolute;z-index:-1;left:0;right:0;top:64px;height:320px;pointer-events:none;background:linear-gradient(90deg,rgba(22,82,240,0) 0%,rgba(22,82,240,.14) 18%,rgba(140,175,255,.22) 34%,rgba(22,82,240,0) 50%,rgba(22,82,240,.14) 68%,rgba(140,175,255,.22) 84%,rgba(22,82,240,0) 100%);background-size:200% 100%;-webkit-mask-image:linear-gradient(180deg,#000 0%,rgba(0,0,0,.4) 50%,transparent 100%);mask-image:linear-gradient(180deg,#000 0%,rgba(0,0,0,.4) 50%,transparent 100%);animation:fxFlow 12s linear infinite}
@keyframes fxFlow{from{background-position:0% 0}to{background-position:-200% 0}}
.xb-top{height:64px;flex-shrink:0;box-sizing:border-box;display:flex;align-items:center;gap:16px;padding:0 20px;border-bottom:1.5px solid #EEF1F7;background:#FFFFFF}
.xb-x{width:40px;height:40px;flex-shrink:0;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#3A4566;text-decoration:none}
.xb-x:hover{background:#F5F8FF;color:#0B1433}
.xb-title{display:flex;align-items:baseline;gap:8px;min-width:0}
.xb-t1{font-size:16px;font-weight:600;white-space:nowrap}
.xb-t2{font-size:14px;color:#5B6582;white-space:nowrap}
.xb-main{flex-grow:1;display:flex;justify-content:center;align-items:center;padding:clamp(32px,7vh,72px) 24px 48px 24px}
.xb-col{width:min(860px,100%);display:flex;flex-direction:column;align-items:center;text-align:center}
.xb-h1{margin:0;font-size:clamp(34px,5.4vh,46px);line-height:1.1;font-weight:600;letter-spacing:-0.035em}
.xb-sub{margin:12px 0 0 0;max-width:560px;font-size:16.5px;line-height:1.55;color:#4A5578}
.xb-fmts{margin-top:28px;display:flex;flex-wrap:wrap;justify-content:center;gap:8px}
.xb-f{display:inline-flex;align-items:center;gap:8px;height:44px;padding:0 14px 0 8px;box-sizing:border-box;border-radius:14px;border:1.5px solid #D6DDEE;background:#FFFFFF;color:#0B1433;font-family:inherit;font-size:14.5px;font-weight:500;cursor:pointer;transition:border-color .2s ease,background .2s ease,box-shadow .2s ease}
.xb-f:hover{border-color:#AFC1F5}
.xb-fi{width:30px;height:30px;border-radius:9px;background:#F5F8FF;color:#1652F0;display:flex;align-items:center;justify-content:center}
.xb-ck{display:none;width:16px;height:16px;border-radius:50%;background:#1652F0;color:#FFFFFF;align-items:center;justify-content:center}
.xb-on{border-color:#1652F0;background:#F5F8FF;color:#0E3BB8;box-shadow:0 0 0 4px rgba(22,82,240,.12)}
.xb-on .xb-fi{background:#FFFFFF}
.xb-on .xb-ck{display:inline-flex}
.xb-f:focus-visible{outline:3px solid rgba(22,82,240,.45);outline-offset:2px}
.xb-route{margin-top:28px;width:100%;box-sizing:border-box;padding:22px 26px 20px 26px;border-radius:22px;background:rgba(255,255,255,.92);border:1.5px solid #E6EAF3;box-shadow:0 18px 44px rgba(22,82,240,.08);text-align:left}
.xb-rh{display:flex;align-items:baseline;justify-content:space-between;gap:12px}
.xb-rn{font-size:13px;color:#5B6582}
.xb-steps{list-style:none;margin:22px 0 4px 0;padding:0;display:flex;position:relative}
.xb-steps::before{content:'';position:absolute;left:16px;right:16px;top:15px;height:3px;border-radius:3px;background:linear-gradient(90deg,#1652F0,#AFC1F5 30%,#E6EAF3 60%)}
.xb-s{flex:1 1 0;min-width:0;display:flex;flex-direction:column;align-items:center;gap:10px;text-align:center;position:relative}
.xb-s:first-child{align-items:flex-start;text-align:left}
.xb-s:last-child{align-items:flex-end;text-align:right}
.xb-sn{position:relative;z-index:1;width:32px;height:32px;box-sizing:border-box;border-radius:50%;border:2px solid #D6DDEE;background:#FFFFFF;color:#5B6582;font-size:13px;font-weight:600;display:flex;align-items:center;justify-content:center}
.xb-sl{font-size:13px;line-height:1.3;color:#3A4566;padding:0 2px}
.xb-first .xb-sn{background:#1652F0;border-color:#1652F0;color:#FFFFFF;animation:ndPulse 2s ease-out infinite}
.xb-first .xb-sl{color:#0B1433;font-weight:600}
.xb-desc{margin:18px 0 0 0;padding-top:14px;border-top:1.5px solid #F0F2F8;font-size:14px;line-height:1.5;color:#4A5578}
.xb-acts{margin-top:28px;display:flex;flex-direction:column;align-items:center;gap:14px}
.xb-alt{display:inline-flex;align-items:center;gap:7px;font-size:14.5px;font-weight:500;color:#3A4566;text-decoration:none}
.xb-alt svg{color:#1652F0}
.xb-alt:hover{color:#1652F0}
@media (prefers-reduced-motion: reduce){.xb-root::before{animation:none}}
@media (max-width: 960px){
.xb-top{height:56px;padding:0 12px 0 6px;gap:8px}
.xb-t2{display:none}
.xb-main{padding:33px 16px 24px 16px}
.xb-col{align-items:stretch;text-align:left}
.xb-h1{font-size:26px}
.xb-sub{font-size:14.5px;margin-top:8px}
.xb-fmts{margin:18px -16px 0 -16px;padding:0 16px;flex-wrap:nowrap;overflow-x:auto;justify-content:flex-start;scrollbar-width:none}
.xb-fmts::-webkit-scrollbar{display:none}
.xb-f{flex-shrink:0;height:42px;font-size:13.5px}
.xb-route{margin-top:18px;padding:16px;border-radius:18px}
.xb-rn{font-size:12px}
.xb-steps{flex-direction:column;margin-top:14px;gap:0}
.xb-steps::before{left:13px;right:auto;top:14px;bottom:14px;width:3px;height:auto;background:linear-gradient(180deg,#1652F0,#AFC1F5 30%,#E6EAF3 60%)}
.xb-s,.xb-s:first-child,.xb-s:last-child{flex-direction:row;align-items:center;text-align:left;gap:12px;min-height:34px}
.xb-sn{width:28px;height:28px;font-size:12px}
.xb-sl{font-size:14px}
.xb-desc{display:none}
.xb-acts{margin-top:18px;align-items:stretch}
.xb-go{justify-content:space-between}
.xb-alt{justify-content:center;font-size:14px}
}
'''
S_XB='''class Component extends DCLogic {
  constructor(props) { super(props); this.state = { f: 0 }; }
  renderVals() {
    const F = [
      ['Course', 'course', 'Build a structured learning experience around a subject or skill.', ['Course setup', 'Delivery', 'Collaboration', 'Basics', 'Audience', 'Skills', 'Outcomes', 'Curriculum']],
      ['Professional certification', 'certification', 'Assess and verify professional competencies.', ['Certification setup', 'Purpose', 'Authority', 'Collaboration', 'Standard', 'Competencies', 'Assessment blueprint']],
      ['Career path', 'career path', 'Create a structured journey toward a career outcome.', ['Path setup', 'Starting point', 'Destination', 'Collaboration', 'Competency map', 'Journey builder']],
      ['Learning program', 'program', 'Deliver coordinated learning over a structured period.', ['Program setup', 'Delivery', 'Duration', 'Collaboration', 'Design', 'Program builder', 'Cohorts']]
    ];
    const f = this.state.f, cur = F[f];
    const v = {
      newTitle: 'New ' + cur[1], lower: cur[1], desc: cur[2], count: cur[3].length,
      steps: cur[3].map((label, i) => ({ label, n: i + 1, cls: i === 0 ? 'xb-first' : '' }))
    };
    for (let i = 0; i < 4; i++) { v['c' + i] = i === f ? 'xb-on' : ''; v['a' + i] = i === f ? 'true' : 'false'; v['p' + i] = () => this.setState({ f: i }); }
    return v;
  }
}'''
open(P+'CR-CREATE-002B.dc.html','w').write(f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Credalio · Build from scratch</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500;600;700&amp;display=swap">
<style>
{DASH_CSS}{XB_CSS}</style>
</helmet>
{c}
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":1440,"height":820}}}}'>
{S_XB}
</script>
</body>
</html>
''')

# ---------------- preview wrappers ----------------
WRAP('CR-CREATE-002B-Mobile.dc.html','CR-CREATE-002B',390,844,'CR-CREATE-002B mobile preview')
WRAP('CR-RDY-001-Mobile.dc.html','CR-RDY-001',390,1520,'CR-RDY-001 mobile preview')
WRAP('CR-RDY-001s.dc.html','CR-RDY-001',1440,1080,'Credalio · Your readiness (new creator)',' variant="new"')
WRAP('CR-RDY-001s-Mobile.dc.html','CR-RDY-001',390,1450,'CR-RDY-001s mobile preview',' variant="new"')
WRAP('CR-CTR-001-Mobile.dc.html','CR-CTR-001',390,1340,'CR-CTR-001 mobile preview')
WRAP('CR-ORI-001-Mobile.dc.html','CR-ORI-001',390,880,'CR-ORI-001 mobile preview')
print('build10 done')
