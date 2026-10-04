exec(open('build4.py').read())
# ---------- 007 Copilot style, same stage as 006
CHAR=c[c.index('<div style="position: relative; align-self: start">'):c.index('</svg>\n</div>',c.index('class="cp-floor"'))+len('</svg>\n</div>')]
ST_CSS=CP_CSS+'''@media (max-width: 960px){.cp-opts-m{display:grid !important;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px;width:100%;margin-top:16px}.cp-opts-m .ob-opt{flex-direction:column;align-items:flex-start !important;gap:10px !important;padding:14px !important}}
'''
def cards(cls,style):
    out=''
    for k,t,d in [('concise','Concise','Short, direct suggestions.'),('collab','Collaborative','Thinks it through with you.'),('detailed','Detailed','Explains the why.'),('proactive','Proactive','Spots gaps before you do.')]:
        out+=f'''<button type="button" role="radio" class="ob-opt" onClick="{{{{o.{k}.pick}}}}" aria-checked="{{{{o.{k}.checked}}}}" style="display: flex; align-items: center; gap: 12px; padding: 12px 14px; min-height: 72px; box-sizing: border-box; border-radius: 16px; border: 1.5px solid {{{{o.{k}.border}}}}; background: {{{{o.{k}.bg}}}}; box-shadow: {{{{o.{k}.shadow}}}}; cursor: pointer; text-align: left; font-family: inherit">
<span style="width: 40px; height: 40px; flex-shrink: 0; border-radius: 12px; background: {{{{o.{k}.iconBg}}}}; color: {{{{o.{k}.iconFg}}}}; display: flex; align-items: center; justify-content: center; transition: all .25s ease">{ICONS[k].replace('width="22" height="22"','width="20" height="20"')}</span>
<span style="display: flex; flex-direction: column; gap: 2px; flex-grow: 1; min-width: 0"><span style="font-size: 16px; font-weight: 600; letter-spacing: -0.01em; color: #0B1433">{t}</span><span style="font-size: 13px; line-height: 1.35; color: #4A5578">{d}</span></span>
</button>'''
    return f'<div role="radiogroup" aria-label="Copilot working style" class="{cls} cp-pop" style="{style}; animation-delay: .15s">'+out+'</div>'
c=H1('How should Nova work with you?')+'\n'+SUB('Pick a style. You can change it anytime.',520)+'\n'
c+='''<div class="cp-stage" style="margin-top: clamp(16px, 3vh, 28px); width: 100%; display: grid; grid-template-columns: clamp(170px, 17vw, 230px) minmax(0, 1fr); gap: 28px; align-items: start; text-align: left">
'''+CHAR+'''
<div class="cp-chat" style="display: flex; flex-direction: column; gap: 10px; margin-top: calc(clamp(170px, 17vw, 230px) * 0.2); min-width: 0">
<span class="cp-pop cp-label" style="display: flex; align-items: center; gap: 8px; font-size: 13px; color: #5B6582"><span style="width: 8px; height: 8px; border-radius: 50%; background: #0F6B45; box-shadow: 0 0 0 3px rgba(15, 107, 69, 0.15)"></span><span style="font-weight: 600; color: #0B1433">Nova</span> · your Creator Copilot</span>
<div class="cp-pop" style="max-width: 560px; padding: 16px 18px; border-radius: 20px 20px 20px 6px; background: #F5F8FF; border: 1.5px solid #E6EAF3; font-size: 16px; line-height: 1.55; color: #0B1433; min-height: 104px; box-sizing: border-box"><sc-if value="{{waiting}}" hint-placeholder-val="{{false}}"><span style="display: inline-flex; gap: 5px; padding: 6px 0" aria-label="typing"><span class="cp-dot"></span><span class="cp-dot" style="animation-delay: .15s"></span><span class="cp-dot" style="animation-delay: .3s"></span></span></sc-if><span aria-live="polite">{{typed}}</span><sc-if value="{{typing}}" hint-placeholder-val="{{false}}"><span class="cp-caret" aria-hidden="true"></span></sc-if></div>
'''+cards('cp-d','max-width: 560px; margin-top: 6px; display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px')+'''
'''+BTN('CR-ONB-008.dc.html','<span>Continue</span>','10px').replace('class="ob-btn" style="','class="ob-btn cp-pop cp-cta-d" style="align-self: flex-start; animation-delay: .3s; ')+'''
</div>
</div>
'''+cards('cp-opts-m','display: none')+'''
'''+BTN('CR-ONB-008.dc.html','<span>Continue</span>','20px').replace('class="ob-btn" style="','class="ob-btn cp-pop cp-cta-m" style="animation-delay: .3s; ')
S007='''class Component extends DCLogic {
  constructor(props) { super(props); this.state = { sel: 'concise', i: 0, phase: 'wait' }; }
  componentDidMount() {
    this.reduce = typeof matchMedia === 'function' && matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (this.reduce) { this.setState({ phase: 'done' }); return; }
    this.t0 = setTimeout(() => this.type(), 1100);
  }
  componentWillUnmount() { clearTimeout(this.t0); clearInterval(this.iv); }
  type() {
    clearInterval(this.iv);
    this.setState({ phase: 'typing', i: 0 });
    this.iv = setInterval(() => {
      if (this.state.i >= this.full().length) { clearInterval(this.iv); this.setState({ phase: 'done' }); return; }
      this.setState({ i: this.state.i + 2 });
    }, 22);
  }
  full() {
    return {
      concise: 'Outcome 2 is vague. Try: “Write SQL joins to combine two tables.” The rest look good.',
      collab: 'Who is this course for, analysts or managers? Outcome 2 reads differently for each. Shall we start there?',
      detailed: 'Outcomes 1 and 3 are measurable. Outcome 2 uses “understand”, which is hard to assess. I’d rewrite it with an action verb and a clear context.',
      proactive: 'I sharpened outcome 2 for you. I also noticed lesson 4 has no practice task. Want me to draft one?'
    }[this.state.sel];
  }
  renderVals() {
    const { sel, i, phase } = this.state;
    const full = this.full();
    const o = {};
    ['concise', 'collab', 'detailed', 'proactive'].forEach((id) => {
      const on = sel === id;
      o[id] = { pick: () => { if (id === this.state.sel) return; clearTimeout(this.t0); this.setState({ sel: id }, () => { if (this.reduce) this.setState({ phase: 'done' }); else this.type(); }); }, checked: on ? 'true' : 'false', border: on ? '#1652F0' : '#E6EAF3', bg: on ? '#F5F8FF' : '#FFFFFF', shadow: on ? '0 0 0 4px rgba(22, 82, 240, 0.12), 0 12px 28px rgba(22, 82, 240, 0.14)' : '0 1px 2px rgba(11, 20, 51, 0.04)', iconBg: on ? '#1652F0' : '#EAF0FF', iconFg: on ? '#FFFFFF' : '#1652F0' };
    });
    return { o, typed: phase === 'wait' ? '' : (phase === 'done' ? full : full.slice(0, i)), waiting: phase === 'wait', typing: phase === 'typing' };
  }
}'''
make('CR-ONB-007.dc.html','Credalio onboarding: Copilot style',940,c,back='CR-ONB-006.dc.html',login=False,script=S007,step=(4,'Meet your Copilot'),extra_css=ST_CSS)
p=P+'CR-ONB-007.dc.html'; s=open(p).read()
a=s.index('<div class="ob-illus"'); b=s.index('</div>\n</x-dc>',a)
s=s[:a]+s[b:]
open(p,'w').write(s); print('007 rebuilt', s.count('ob-illus"'))
