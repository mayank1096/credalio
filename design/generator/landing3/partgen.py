# Partner inquiry (ENT-010). Built from LIVE shared pieces, never redrawn:
#   OnbAbout.dc.html  -> field label / input / error (ob-lab, ob-f, ob-err)
#   kit               -> ds-chip selection, ds-btn, ko-* success emblem with confetti, tip
#   Pricing           -> back link (pc-back), step track (ko-path, Link 2 CR-WAL-OUT)
# Usage: python3 partgen.py -> design/canvas3/project/Partner.dc.html
import os, re, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from kit import KIT_CSS, btn, ck, emblem, tip
from shell import BASE_CSS, nav, FOOT
import pricegen, cregen

P = os.path.join(HERE, '../../canvas3/project/')
OUT = P + 'Partner.dc.html'
L = cregen.L
style = pricegen.style
OB = open(P + 'OnbAbout.dc.html').read()
OBCSS = '\n'.join(l for l in style(OB).split('\n') if re.match(r'\.ob-(lab|err|help)\b|\.ob-err svg|\.ob-f(\{|::placeholder|:focus)', l) and 'appearance' not in l and 'height:46px' not in l and 'height:auto' not in l)

ERRI = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"></circle><path d="M12 7.5v5.5"></path><path d="M12 16.4v.2"></path></svg>'
BACK = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 12H5"></path><path d="m11 18-6-6 6-6"></path></svg>'
CK = ck(13, 3)

def err(k):
    return '<sc-if value="{{e.%s}}" hint-placeholder-val="{{ false }}"><span class="ob-err" role="alert">%s{{e.%sT}}</span></sc-if>' % (k, ERRI, k)

def field(id_, label, key, ph, typ='text', ac='', opt=False):
    return '<div class="pt-f"><label for="%s" class="ob-lab">%s%s</label><input id="%s" class="ob-f {{f.%sCls}}" type="%s" placeholder="%s" value="{{f.%s}}" onInput="{{f.%sOn}}" aria-invalid="{{f.%sInv}}"%s>%s</div>' % (
        id_, label, ' <span class="pt-opt">(optional)</span>' if opt else '', id_, key, typ, ph, key, key, key, (' autocomplete="%s"' % ac) if ac else '', err(key))

def chips(label, key, help_=''):
    return '<fieldset class="pt-f pt-fs"><legend class="ob-lab">%s%s</legend><div class="pt-chips"><sc-for list="{{c.%s}}" as="o" hint-placeholder-count="4"><button type="button" class="ds-chip {{o.cls}}" aria-pressed="{{o.on}}" onClick="{{o.pick}}">%s{{o.label}}</button></sc-for></div>%s</fieldset>' % (label, help_, key, CK, err(key))

NEXT = [('Partnership inquiry', 'You’re here'), ('A conversation', 'We explore your goals together'), ('Institution setup', 'Roles, branding, SSO and content'), ('Your workspace goes live', 'Your learning ecosystem, ready')]
STEPS = ''.join('<li><span class="ko-dot">%d</span><span><b>%s</b><span>%s</span></span></li>' % (i + 1, t, d) for i, (t, d) in enumerate(NEXT))

FORM = '''<sc-if value="{{isForm}}" hint-placeholder-val="{{ true }}">
<div class="pt-wrap">
<a class="pc-back" href="Institutions.dc.html">''' + BACK + '''<span>Credalio for Institutions</span></a>
<div class="pt-grid">
<div class="pt-main">
<span class="pc-k">Partner with Credalio</span>
<h1 class="pc-ph1">Tell us about your institution.</h1>
<p class="pc-p">A few details help our Enterprise Team prepare for your first conversation.</p>
<sc-if value="{{hasErr}}" hint-placeholder-val="{{ false }}"><div class="pt-sum" role="alert">''' + ERRI + '''<span>{{errN}}</span></div></sc-if>
<form class="ds-card pt-card" novalidate onSubmit="{{submit}}">
<div class="pt-sec"><h2>Your institution</h2>
''' + field('pt-inst', 'Institution name', 'inst', 'Meridian University', ac='organization') + '''
''' + chips('Institution type', 'type') + '''
''' + chips('Approximate number of learners', 'size') + '''
</div>
<div class="pt-sec"><h2>Your goals</h2>
''' + chips('What would you like to do?', 'goals', ' <span class="pt-opt">Choose any</span>') + '''
''' + chips('Do you already have learning content?', 'content') + '''
</div>
<div class="pt-sec"><h2>About you</h2>
<div class="pt-two">''' + field('pt-name', 'Your name', 'name', 'Ada Ononuju', ac='name') + field('pt-email', 'Work email', 'email', 'ada@meridian.ac.uk', 'email', 'email') + '''</div>
''' + field('pt-role', 'Role', 'role', 'Head of Digital Learning', ac='organization-title') + '''
<div class="pt-f"><label for="pt-notes" class="ob-lab">Anything else we should know? <span class="pt-opt">(optional)</span></label><textarea id="pt-notes" class="ob-f pt-ta" rows="3" placeholder="Timelines, systems you use, programs you want to bring" value="{{f.notes}}" onInput="{{f.notesOn}}"></textarea></div>
</div>
<div class="pt-act">''' + btn('Send request', tag='button').replace('type="button"', 'type="submit"') + '''<span class="pt-pv">We only use these details to reply to you.''' + tip('Your request goes to the Credalio Enterprise Team. We don’t add you to marketing lists.') + '''</span></div>
</form>
</div>
<aside class="pt-side" aria-label="What happens next">
<div class="ds-card pt-next"><span class="pc-k">What happens next</span><ol class="ko-path pt-path">''' + STEPS + '''</ol></div>
</aside>
</div>
</div>
</sc-if>'''

DONE = '''<sc-if value="{{isDone}}" hint-placeholder-val="{{ false }}">
<div class="pt-done ko-v">
''' + emblem() + '''
<span class="ko-pill">Request sent</span>
<h1 class="pc-ph1">Thanks. We’ll take it from here.</h1>
<p class="pc-p">Your request is with the Credalio Enterprise Team. We’ll reply to <b>{{f.email}}</b>.</p>
<div class="ds-card pt-ref">
<dl><div><dt>Reference</dt><dd>{{ref}}</dd></div><div><dt>Institution</dt><dd>{{f.inst}}</dd></div></dl>
<span class="pc-k">Next for you</span>
<ol class="ko-path pt-path">''' + ''.join('<li%s><span class="ko-dot">%s</span><span><b>%s</b><span>%s</span></span></li>' % (' class="pt-ok"' if i == 0 else '', CK if i == 0 else str(i + 1), t, d) for i, (t, d) in enumerate([('Request received', 'A partnership case is open for {{f.inst}}.'), ('We review your goals', 'The Enterprise Team reads your request.'), ('We talk, then set up', 'A conversation first, then your institution setup.')])) + '''</ol>
</div>
''' + btn('Back to Credalio for Institutions', 'Institutions.dc.html', 'pt-cta') + '''
<button type="button" class="ds-link pt-again" onClick="{{reset}}">Send another request</button>
</div>
</sc-if>'''

CSS = OBCSS + r'''
.pt-m{overflow-x:clip}
.ob-f.err{border-color:#D92D20}
.ob-f.err:focus{box-shadow:0 0 0 4px rgba(217,45,32,.12)}
.pt-wrap{max-width:1216px;margin:0 auto;padding:28px 48px 96px;box-sizing:border-box}
.pt-grid{display:grid;grid-template-columns:minmax(0,1fr) 340px;gap:48px;align-items:start;margin-top:16px}
.pt-main{display:flex;flex-direction:column}
.pt-main .pc-ph1{margin-top:8px}
.pt-sum{display:flex;align-items:center;gap:10px;margin-top:20px;padding:12px 16px;border-radius:14px;background:#FEF3F2;border:1.5px solid #FECDCA;color:#B42318;font-size:14px;font-weight:500}
.pt-card{margin-top:28px;padding:8px 32px 32px;border-radius:22px}
.pt-sec{display:flex;flex-direction:column;gap:22px;padding:28px 0;border-bottom:1.5px solid #EEF1F7}
.pt-sec h2{margin:0;font-size:18px;font-weight:600;letter-spacing:-.2px}
.pt-f{display:flex;flex-direction:column;text-align:left}
.pt-fs{margin:0;padding:0;border:0;min-width:0}
.pt-fs legend{padding:0}
.pt-opt{font-weight:500;color:#5B6582}
.pt-chips{display:flex;flex-wrap:wrap;gap:8px;margin-top:4px}
.pt-two{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:16px}
.pt-ta{height:auto;padding:12px 16px;line-height:1.5;resize:vertical;min-height:96px}
.pt-act{display:flex;align-items:center;gap:20px;padding-top:28px}
.pt-pv{display:inline-flex;align-items:center;gap:6px;font-size:13.5px;color:#5B6582}
.pt-side{position:sticky;top:96px;margin-top:106px}
.pt-next{padding:24px;border-radius:22px}
.pt-path{grid-template-columns:minmax(0,1fr);gap:0;margin-top:18px}
.pt-path li{flex-direction:row;align-items:flex-start;text-align:left;gap:14px;padding:0 0 22px}
.pt-path li:last-child{padding-bottom:0}
.pt-path li:not(:last-child)::before{left:13px;right:auto;top:30px;bottom:2px;width:2px;height:auto}
.pt-path li > span:last-child{align-items:flex-start}
.pt-path b{font-size:15px}
.pt-path li > span:last-child > span{max-width:none}
.pt-path li > span:last-child > span{font-size:13.5px}
.pt-path li:first-child .ko-dot{background:#1652F0;color:#FFFFFF}
.pt-path li.pt-ok .ko-dot{background:#0F6B45;border-color:#0F6B45}
.pt-done{max-width:640px;margin:0 auto;padding:56px 24px 96px;box-sizing:border-box;display:flex;flex-direction:column;align-items:center;text-align:center}
.pt-done .pc-ph1{margin-top:14px}
.pt-done .pc-p b{font-weight:600;color:#0B1433}
.pt-ref{width:100%;box-sizing:border-box;margin-top:28px;padding:24px;border-radius:22px;text-align:left;display:flex;flex-direction:column;gap:16px}
.pt-ref dl{margin:0;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:12px;padding-bottom:18px;border-bottom:1.5px solid #EEF1F7}
.pt-ref dt{font-size:12.5px;color:#8A93AD}
.pt-ref dd{margin:3px 0 0;font-size:15px;font-weight:600}
.pt-ref .pt-path{margin-top:0}
.pt-cta{margin-top:28px}
.pt-again{margin-top:14px;position:relative}
@media (max-width: 960px){
.pt-wrap{padding:16px 20px 72px}
.pt-grid{grid-template-columns:minmax(0,1fr);gap:24px}
.pt-side{position:static;margin-top:0;order:-1}
.pt-next{padding:0;border:0;background:none;box-shadow:none}
.pt-next .pc-k{display:none}
.pt-next .pt-path{display:flex;margin-top:0;flex-direction:row;gap:6px}
.pt-next .pt-path li{flex:1;flex-direction:column;gap:8px;padding:0}
.pt-next .pt-path li::before{display:none}
.pt-next .pt-path li > span:last-child > span{display:none}
.pt-next .pt-path li > span:last-child{gap:0}
.pt-next .pt-path b{font-size:12.5px;font-weight:500;line-height:1.3;color:#3A4566}
.pt-next .pt-path li:first-child b{color:#0B1433;font-weight:600}
}
@media (max-width: 760px){
.pt-card{margin-top:20px;padding:0 18px 22px;border-radius:20px}
.pt-sec{padding:22px 0;gap:18px}
.pt-two{grid-template-columns:minmax(0,1fr)}
.pt-chips{gap:6px}
.pt-act{flex-direction:column;align-items:stretch;gap:12px}
.pt-act .ds-btn{justify-content:space-between}
.pt-pv{justify-content:center}
.pt-done{padding:32px 20px 64px}
.pt-ref{padding:20px 18px}
.pt-cta{align-self:stretch;justify-content:space-between}
.pt-again::after{content:'';position:absolute;inset:-12px -8px}
}
'''

NAVH = nav('For institutions').replace('<a class="sx-cta" href="#">Create account</a>', '<a class="sx-cta" href="OnbWelcome.dc.html">Create account</a>')
BODY = '''<div style="font-family: 'Google Sans', system-ui, sans-serif; color: #0B1433; background: #FFFFFF; min-height: 100%">
''' + NAVH + '''
<main class="pt-m">
''' + FORM + '''
''' + DONE + '''
</main>
''' + FOOT + '''
</div>'''

LISTS = {'type': ['University', 'Company', 'Training provider', 'Professional body', 'Government', 'Other'],
         'size': ['Up to 100', '101–1,000', '1,001–10,000', '10,000+'],
         'goals': ['Deliver learning', 'Create learning', 'Upskill employees', 'Issue credentials', 'Use Credalio AI', 'Validate learning', 'Manage cohorts', 'Other'],
         'content': ['Yes', 'Some', 'Not yet']}
JS = '''
var LISTS = ''' + json.dumps(LISTS, ensure_ascii=False) + ''';
var MSG = { inst: 'Enter your institution’s name.', type: 'Choose your institution type.', size: 'Choose roughly how many learners.', goals: 'Choose at least one.', content: 'Tell us if you have content already.', name: 'Enter your name.', email: 'Enter a valid work email.', role: 'Enter your role.' };
class Component extends DCLogic {
  constructor(props) {
    super(props);
    var st = (props && props.step) || 'form';
    this.state = st === 'done' ? { step: 'done', inst: 'Meridian University', type: 'University', size: '1,001–10,000', goals: { 'Deliver learning': 1, 'Issue credentials': 1 }, content: 'Some', name: 'Ada Ononuju', email: 'ada@meridian.ac.uk', role: 'Head of Digital Learning', notes: '', tried: true, ref: 'ENT-4821' }
      : st === 'error' ? { step: 'form', inst: 'Meridian University', type: 'University', size: null, goals: {}, content: null, name: 'Ada Ononuju', email: 'ada@meridian', role: '', notes: '', tried: true, ref: '' }
      : { step: 'form', inst: '', type: null, size: null, goals: {}, content: null, name: '', email: '', role: '', notes: '', tried: false, ref: '' };
  }
  errors() {
    var S = this.state, e = {};
    if (!S.inst.trim()) e.inst = 1; if (!S.type) e.type = 1; if (!S.size) e.size = 1; if (!Object.keys(S.goals).length) e.goals = 1; if (!S.content) e.content = 1;
    if (!S.name.trim()) e.name = 1; if (!/^\\S+@\\S+\\.\\S+$/.test(S.email)) e.email = 1; if (!S.role.trim()) e.role = 1;
    return e;
  }
  renderVals() {
    var self = this, S = this.state, E = S.tried ? this.errors() : {}, n = Object.keys(E).length, e = {}, f = {}, c = {};
    Object.keys(MSG).forEach(function (k) { e[k] = !!E[k]; e[k + 'T'] = MSG[k]; });
    ['inst', 'name', 'email', 'role', 'notes'].forEach(function (k) {
      f[k] = S[k]; f[k + 'Cls'] = E[k] ? 'err' : ''; f[k + 'Inv'] = E[k] ? 'true' : 'false';
      f[k + 'On'] = function (ev) { var o = {}; o[k] = ev.target.value; self.setState(o); };
    });
    ['type', 'size', 'content'].forEach(function (k) {
      c[k] = LISTS[k].map(function (x) { var on = S[k] === x; return { label: x, cls: on ? 'on' : '', on: on ? 'true' : 'false', pick: function () { var o = {}; o[k] = x; self.setState(o); } }; });
    });
    c.goals = LISTS.goals.map(function (x) { var on = !!S.goals[x]; return { label: x, cls: on ? 'on' : '', on: on ? 'true' : 'false', pick: function () { var g = Object.assign({}, S.goals); if (g[x]) delete g[x]; else g[x] = 1; self.setState({ goals: g }); } }; });
    return {
      isForm: S.step === 'form', isDone: S.step === 'done', e: e, f: f, c: c, ref: S.ref,
      hasErr: n > 0, errN: n === 1 ? 'One thing needs your attention.' : n + ' things need your attention.',
      submit: function (ev) { if (ev && ev.preventDefault) ev.preventDefault(); var bad = Object.keys(self.errors()).length; if (bad) { self.setState({ tried: true }); return; } self.setState({ step: 'done', ref: 'ENT-' + (1000 + Math.floor(Math.random() * 9000)) }); },
      reset: function () { self.setState({ step: 'form', inst: '', type: null, size: null, goals: {}, content: null, name: '', email: '', role: '', notes: '', tried: false, ref: '' }); }
    };
  }
}
'''

def page(props_default='form'):
    return '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Partner with Credalio</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500;600;700&amp;display=swap">
<style>
''' + BASE_CSS + KIT_CSS + '\n' + pricegen.CSS + '\n' + CSS + '''</style>
</helmet>
''' + BODY + '''
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{"step":{"editor":"enum","options":["form","error","done"],"default":"''' + props_default + '''"},"$preview":{"width":1440,"height":1740}}'>''' + JS + '''</script>
</body>
</html>
'''

if __name__ == '__main__':
    open(OUT, 'w').write(page())
    print('wrote', OUT)
