exec(open('build3.py').read())
import re
CP_CSS=FORM_CSS+'''@keyframes cpRise{from{opacity:0;transform:translateY(18px)}to{opacity:1;transform:none}}
@keyframes cpPop{from{opacity:0;transform:translateY(8px) scale(.98)}to{opacity:1;transform:none}}
@keyframes cpDraw{from{stroke-dashoffset:1}to{stroke-dashoffset:0}}
@keyframes cpBlink{0%,49%{opacity:1}50%,100%{opacity:0}}
@keyframes cpDot{0%,80%,100%{opacity:.25;transform:translateY(0)}40%{opacity:1;transform:translateY(-3px)}}
.cp-char{animation:cpRise .9s cubic-bezier(.2,.8,.2,1) .15s both}
.cp-line{stroke-dasharray:1;animation:cpDraw 1.1s ease .7s both}
.cp-pop{animation:cpPop .45s ease both}
.cp-caret{display:inline-block;width:2px;height:1.05em;margin-left:2px;vertical-align:-0.15em;background:#1652F0;animation:cpBlink 1s steps(1) infinite}
.cp-dot{display:inline-block;width:6px;height:6px;border-radius:50%;background:#1652F0;animation:cpDot 1.2s ease-in-out infinite}
.ob-arrow{flex-shrink:0}
@media (prefers-reduced-motion: reduce){.cp-char,.cp-line,.cp-pop,.cp-caret,.cp-dot{animation:none}}
@media (max-width: 960px){.cp-stage{grid-template-columns:72px minmax(0,1fr) !important;gap:10px !important;align-items:start !important}.cp-char{width:72px !important}.cp-stage > div:first-child{align-self:start !important;margin-top:24px}.cp-floor{display:none}.cp-chips{justify-content:flex-start !important}.cp-chat{margin-top:0 !important}.cp-label{display:none !important}.cp-stage{margin-top:28px !important}.cp-stage > div:first-child{margin-top:0 !important}.cp-cta-d,.cp-d{display:none !important}.cp-chips-m{display:grid !important;grid-template-columns:repeat(4,minmax(0,1fr));gap:8px;width:100%;margin-top:16px}.cp-chips-m button{padding:0 !important;width:100%}.ob-main{padding-top:28px !important}}
@media (min-width: 961px){.cp-cta-m,.cp-chips-m{display:none !important}}
'''
IMG='/_blob/bad84659fa9f24b3a7efb7e88696e531'
c=H1('Meet your Copilot.')+'\n'+SUB('It already knows your expertise, and it will build alongside you.',520)+'\n'
c+='''<div class="cp-stage" style="margin-top: clamp(16px, 3vh, 28px); width: 100%; display: grid; grid-template-columns: clamp(170px, 17vw, 230px) minmax(0, 1fr); gap: 28px; align-items: start; text-align: left">
<div style="position: relative; align-self: start">
<div class="cp-char" aria-hidden="true" style="position: relative; width: clamp(170px, 17vw, 230px); aspect-ratio: 200 / 450; overflow: hidden; -webkit-mask-image: linear-gradient(to bottom, #000 86%, transparent), linear-gradient(to right, transparent, #000 12%, #000 80%, transparent); -webkit-mask-composite: source-in; mask-image: linear-gradient(to bottom, #000 86%, transparent), linear-gradient(to right, transparent, #000 12%, #000 80%, transparent); mask-composite: intersect">
<img src="'''+IMG+'''" alt="" style="position: absolute; left: -672.5%; top: -37.78%; width: 1086%; max-width: none; height: auto; mix-blend-mode: multiply">
</div>
<svg class="cp-floor" aria-hidden="true" viewBox="0 0 260 40" style="position: absolute; left: 10%; bottom: -6px; width: 150%; height: 40px; overflow: visible"><ellipse cx="70" cy="22" rx="70" ry="9" fill="#1652F0" fill-opacity="0.10"></ellipse></svg>
</div>
<div class="cp-chat" style="display: flex; flex-direction: column; gap: 10px; margin-top: calc(clamp(170px, 17vw, 230px) * 0.2); min-width: 0">
<span class="cp-pop cp-label" style="display: flex; align-items: center; gap: 8px; font-size: 13px; color: #5B6582"><span style="width: 8px; height: 8px; border-radius: 50%; background: #0F6B45; box-shadow: 0 0 0 3px rgba(15, 107, 69, 0.15)"></span><span style="font-weight: 600; color: #0B1433">{{name}}</span> · your Creator Copilot</span>
<div class="cp-pop" style="max-width: 560px; padding: 16px 18px; border-radius: 20px 20px 20px 6px; background: #F5F8FF; border: 1.5px solid #E6EAF3; font-size: 16px; line-height: 1.55; color: #0B1433; min-height: 52px; box-sizing: border-box"><sc-if value="{{waiting}}" hint-placeholder-val="{{false}}"><span style="display: inline-flex; gap: 5px; padding: 6px 0" aria-label="typing"><span class="cp-dot"></span><span class="cp-dot" style="animation-delay: .15s"></span><span class="cp-dot" style="animation-delay: .3s"></span></span></sc-if><span aria-live="polite">{{typed}}</span><sc-if value="{{typing}}" hint-placeholder-val="{{false}}"><span class="cp-caret" aria-hidden="true"></span></sc-if></div>
<sc-if value="{{askShown}}" hint-placeholder-val="{{true}}">
<div class="cp-pop" style="align-self: flex-start; padding: 12px 16px; border-radius: 20px 20px 20px 6px; background: #F5F8FF; border: 1.5px solid #E6EAF3; font-size: 16px; color: #0B1433">What would you like to call me?</div>
<div class="cp-chips cp-pop cp-d" role="radiogroup" aria-label="Name your Copilot" style="display: flex; flex-wrap: wrap; justify-content: flex-start; gap: 8px; margin-top: 4px; animation-delay: .15s">
<sc-for list="{{names}}" as="n" hint-placeholder-count="4"><button type="button" role="radio" aria-checked="{{n.on}}" class="ob-chip" onClick="{{n.pick}}" style="height: 44px; padding: 0 16px; border-radius: 14px; border: 1.5px solid {{n.bd}}; background: {{n.bg}}; color: {{n.fg}}; box-shadow: {{n.sh}}; font-family: inherit; font-size: 14.5px; font-weight: 500; cursor: pointer; display: inline-flex; align-items: center; justify-content: center; gap: 7px"><span aria-hidden="true" style="display: {{n.ckd}}; width: 16px; height: 16px; border-radius: 50%; background: #1652F0; color: #FFFFFF; align-items: center; justify-content: center"><svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"><path d="m5 12.5 4.5 4.5L19 7.5"></path></svg></span>{{n.label}}</button></sc-for>
</div>
'''+BTN('CR-ONB-007.dc.html','<span>Continue with {{name}}</span>','10px').replace('class="ob-btn" style="','class="ob-btn cp-pop cp-cta-d" style="align-self: flex-start; animation-delay: .3s; ')+'''
</sc-if>
</div>
</div>
<sc-if value="{{askShown}}" hint-placeholder-val="{{true}}"><div class="cp-chips-m cp-pop" role="radiogroup" aria-label="Name your Copilot" style="display: none; animation-delay: .15s"><sc-for list="{{names}}" as="n" hint-placeholder-count="4"><button type="button" role="radio" aria-checked="{{n.on}}" class="ob-chip" onClick="{{n.pick}}" style="height: 44px; border-radius: 14px; border: 1.5px solid {{n.bd}}; background: {{n.bg}}; color: {{n.fg}}; box-shadow: {{n.sh}}; font-family: inherit; font-size: 14.5px; font-weight: 500; cursor: pointer; display: inline-flex; align-items: center; justify-content: center; gap: 6px"><span aria-hidden="true" style="display: {{n.ckd}}; width: 16px; height: 16px; border-radius: 50%; background: #1652F0; color: #FFFFFF; align-items: center; justify-content: center"><svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"><path d="m5 12.5 4.5 4.5L19 7.5"></path></svg></span>{{n.label}}</button></sc-for></div>
'''+BTN('CR-ONB-007.dc.html','<span>Continue with {{name}}</span>','20px').replace('class="ob-btn" style="','class="ob-btn cp-pop cp-cta-m" style="animation-delay: .3s; ')+'''</sc-if>'''
S='''class Component extends DCLogic {
  constructor(props) { super(props); this.state = { names: ['Nova', 'Maya', 'Alex', 'Sage'], sel: 'Nova', i: 0, phase: 'wait' }; }
  componentDidMount() {
    const reduce = typeof matchMedia === 'function' && matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (reduce) { this.setState({ phase: 'done', i: 9999 }); return; }
    this.t0 = setTimeout(() => {
      this.setState({ phase: 'typing' });
      this.iv = setInterval(() => {
        const full = this.full();
        if (this.state.i >= full.length) { clearInterval(this.iv); this.t1 = setTimeout(() => this.setState({ phase: 'done' }), 350); return; }
        this.setState({ i: this.state.i + 2 });
      }, 28);
    }, 1300);
  }
  componentWillUnmount() { clearTimeout(this.t0); clearTimeout(this.t1); clearInterval(this.iv); }
  name() { return this.state.sel; }
  full() { return 'Hi Ada, I’m ' + this.name() + '. I already know your 8+ years in Data & Analytics. Together we’ll shape courses, outcomes and assessments, and get your work ready for validation.'; }
  renderVals() {
    const { names, sel, i, phase } = this.state;
    const full = this.full();
    return {
      name: this.name(),
      typed: phase === 'wait' ? '' : (phase === 'done' ? full : full.slice(0, i)),
      waiting: phase === 'wait', typing: phase === 'typing', askShown: phase === 'done',
      names: names.map((label) => { const on = sel === label; return { label, on: on ? 'true' : 'false', pick: () => this.setState({ sel: label }), bd: on ? '#1652F0' : '#D6DDEE', bg: on ? '#F5F8FF' : '#FFFFFF', fg: on ? '#0E3BB8' : '#0B1433', sh: on ? '0 0 0 4px rgba(22, 82, 240, 0.12)' : 'none', ckd: on ? 'inline-flex' : 'none' }; })
    };
  }
}'''
make('CR-ONB-006.dc.html','Credalio onboarding: meet your Copilot',940,c,back='CR-ONB-005b.dc.html',login=False,script=S,step=(4,'Meet your Copilot'),extra_css=CP_CSS)
p=P+'CR-ONB-006.dc.html'; s=open(p).read()
a=s.index('<div class="ob-illus"'); b=s.index('</div>\n</x-dc>',a)
s=s[:a]+s[b:]
open(p,'w').write(s); print('006 rebuilt', s.count('ob-illus"'))
