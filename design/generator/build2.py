exec(open('gen2.py').read())
def OPT(k,icon,title,desc,soon=False):
    badge='<span style="padding: 2px 8px; border-radius: 999px; background: #EAF0FF; color: #0E3BB8; font-size: 11.5px; font-weight: 600">Soon</span>' if soon else ''
    return f'''<button type="button" role="radio" class="ob-opt" onClick="{{{{o.{k}.pick}}}}" aria-checked="{{{{o.{k}.checked}}}}" style="display: flex; align-items: center; gap: 14px; padding: 16px; min-height: 84px; box-sizing: border-box; border-radius: 18px; border: 1.5px solid {{{{o.{k}.border}}}}; background: {{{{o.{k}.bg}}}}; box-shadow: {{{{o.{k}.shadow}}}}; cursor: pointer; text-align: left; font-family: inherit">
<span style="width: 46px; height: 46px; flex-shrink: 0; border-radius: 13px; background: {{{{o.{k}.iconBg}}}}; color: {{{{o.{k}.iconFg}}}}; display: flex; align-items: center; justify-content: center; transition: all .25s ease">{icon}</span>
<span style="display: flex; flex-direction: column; gap: 3px; flex-grow: 1; min-width: 0">
<span style="display: flex; flex-wrap: wrap; align-items: center; gap: 4px 8px"><span style="font-size: 17px; font-weight: 600; letter-spacing: -0.01em; color: #0B1433">{title}</span>{badge}</span>
<span style="font-size: 13.5px; line-height: 1.35; color: #4A5578">{desc}</span>
</span>
<span style="width: 22px; height: 22px; flex-shrink: 0; box-sizing: border-box; border-radius: 50%; border: 1.5px solid {{{{o.{k}.radioBorder}}}}; background: {{{{o.{k}.radioBg}}}}; display: flex; align-items: center; justify-content: center; transition: all .25s ease"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="opacity: {{{{o.{k}.check}}}}"><path d="m5 12.5 4.5 4.5L19 7.5"></path></svg></span>
</button>'''
SV='<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
I_USER=SV+'<circle cx="12" cy="8" r="4"></circle><path d="M4 21a8 8 0 0 1 16 0"></path></svg>'
I_CAP=SV+'<path d="M22 9.5 12 5 2 9.5l10 4.5 10-4.5z"></path><path d="M6 11.5V16c3 2.2 9 2.2 12 0v-4.5"></path></svg>'
I_ORG=SV+'<rect x="4" y="3" width="16" height="18" rx="2"></rect><path d="M9 7h.01"></path><path d="M15 7h.01"></path><path d="M9 11h.01"></path><path d="M15 11h.01"></path><path d="M10 21v-4h4v4"></path></svg>'
SHIELD='<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1652F0" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="flex-shrink: 0; margin-top: 2px"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>'

# ---- 002
c=H1('How will you create?')+'\n'+SUB('Choose what fits today. You can change it anytime.')+'\n'
c+='<div role="radiogroup" aria-label="How you will create" class="ob-grid3 ob-in3" style="margin-top: clamp(22px, 4vh, 36px); width: 100%; display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 16px">\n'
c+=OPT('ind',I_USER,'As myself','Publish under your own name.')+'\n'+OPT('inst',I_CAP,'With my institution','With your school or workplace.',True)+'\n'+OPT('org',I_ORG,'As an organisation','Learning for your team or brand.',True)+'\n</div>\n'
c+='<p style="margin: 16px 0 0 0; display: flex; align-items: flex-start; gap: 8px; font-size: 13.5px; line-height: 1.5; color: #3A4566; text-align: left">'+SHIELD+'<span>{{note}}</span></p>\n'
c+='<sc-if value="{{isInd}}" hint-placeholder-val="{{true}}">'+BTN('CR-ONB-003.dc.html','Continue as myself','clamp(18px, 3vh, 28px)')+'</sc-if>\n'
c+='<sc-if value="{{notInd}}" hint-placeholder-val="{{false}}">'+BTN('CR-ONB-002S.dc.html','Continue','clamp(18px, 3vh, 28px)')+'</sc-if>'
S002='''class Component extends DCLogic {
  constructor(props) { super(props); this.state = { sel: 'ind' }; }
  renderVals() {
    const sel = this.state.sel;
    const notes = {
      ind: 'When you’re ready to publish, we’ll ask you to confirm it’s you. Not before.',
      inst: 'Later, your institution will confirm you’re part of it. Nothing to do now.',
      org: 'Later, we’ll verify your organisation and who can act for it. Nothing to do now.'
    };
    const o = {};
    ['ind', 'inst', 'org'].forEach((id) => {
      const on = sel === id;
      o[id] = {
        pick: () => this.setState({ sel: id }),
        checked: on ? 'true' : 'false',
        border: on ? '#1652F0' : '#E6EAF3',
        bg: on ? '#F5F8FF' : '#FFFFFF',
        shadow: on ? '0 0 0 4px rgba(22, 82, 240, 0.12), 0 12px 28px rgba(22, 82, 240, 0.14)' : '0 1px 2px rgba(11, 20, 51, 0.04)',
        iconBg: on ? '#1652F0' : '#EAF0FF',
        iconFg: on ? '#FFFFFF' : '#1652F0',
        radioBorder: on ? '#1652F0' : '#CBD3E6',
        radioBg: on ? '#1652F0' : '#FFFFFF',
        check: on ? 1 : 0
      };
    });
    return { o, note: notes[sel], isInd: sel === 'ind', notInd: sel !== 'ind' };
  }
}'''
make('CR-ONB-002.dc.html','Credalio onboarding: how will you create',1040,c,back='Main.dc.html',chip='You start as a Creator',script=S002)

# ---- 002S
def ITEM(icon,t): return '<div style="display: flex; align-items: center; gap: 12px; padding: 14px 16px; border-radius: 16px; background: #F5F8FF; text-align: left"><span style="width: 36px; height: 36px; flex-shrink: 0; border-radius: 11px; background: #FFFFFF; color: #1652F0; display: flex; align-items: center; justify-content: center">'+icon+'</span><span style="font-size: 14px; line-height: 1.4; color: #3A4566">'+t+'</span></div>'
S18='<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
c=H1('Organisation accounts are almost here.')+'\n'+SUB('We’re finishing institution and organisation accounts. Start as yourself today, and everything you make comes with you when they arrive.',600)+'\n'
c+='<p class="ob-in3" style="margin: clamp(20px, 3.6vh, 32px) 0 10px 0; font-size: 13px; font-weight: 600; color: #5B6582">As yourself, you can already</p>\n'
c+='<div class="ob-grid3 ob-in3" style="width: 100%; display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 12px">'
c+=ITEM(S18+'<path d="M12 20h9"></path><path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4z"></path></svg>','Build courses, certifications and programs')
c+=ITEM(S18+'<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M22 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>','Invite co-creators to build with you')
c+=ITEM(S18+'<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path><path d="m9 12 2 2 4-4"></path></svg>','Submit for validation under your name')
c+='</div>\n<div class="ob-row" style="margin-top: clamp(20px, 3.4vh, 28px); display: flex; align-items: center; gap: 12px">'+BTN('CR-ONB-003.dc.html','Start as myself')+GHOST('CR-ONB-002.dc.html','Choose again')+'</div>'
make('CR-ONB-002S.dc.html','Credalio onboarding: organisations coming soon',880,c,back='CR-ONB-002.dc.html',chip='Start as yourself')

# ---- 003
G='<svg width="18" height="18" viewBox="0 0 24 24" aria-hidden="true"><path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"></path><path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"></path><path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l3.66-2.84z"></path><path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"></path></svg>'
A='<svg width="18" height="18" viewBox="0 0 24 24" aria-hidden="true"><path fill="#0B1433" d="M16.37 12.63c-.02-2.2 1.8-3.26 1.88-3.31-1.03-1.5-2.62-1.7-3.19-1.73-1.36-.14-2.65.8-3.34.8-.69 0-1.75-.78-2.88-.76-1.48.02-2.85.86-3.61 2.19-1.54 2.67-.39 6.62 1.11 8.79.73 1.06 1.6 2.25 2.75 2.21 1.1-.04 1.52-.71 2.86-.71 1.33 0 1.71.71 2.88.69 1.19-.02 1.94-1.08 2.67-2.15.84-1.23 1.19-2.42 1.21-2.48-.03-.01-2.32-.89-2.34-3.54zM14.17 6.15c.61-.74 1.02-1.76.91-2.78-.88.04-1.94.59-2.57 1.32-.56.65-1.06 1.69-.93 2.69.98.08 1.98-.5 2.59-1.23z"></path></svg>'
def SOC(icon,label): return '<a href="CR-ONB-003b.dc.html" class="ob-ghost" style="flex: 1 1 0; display: flex; align-items: center; justify-content: center; gap: 10px; height: 52px; border-radius: 999px; border: 1.5px solid #D6DDEE; background: #FFFFFF; color: #0B1433; font-size: 15px; font-weight: 600; text-decoration: none">'+icon+'Continue with '+label+'</a>'
c=H1('Let’s save your place.')+'\n'+SUB('Create your account so everything you build stays safe, wherever you work.',600)+'\n'
c+='<div class="ob-row ob-in3" style="margin-top: clamp(22px, 4vh, 36px); width: 100%; display: flex; align-items: center; gap: 10px">\n<label for="ob-email" class="sr-only">Email</label>\n<input id="ob-email" class="ob-input" type="email" autocomplete="email" placeholder="Your email address" style="flex-grow: 1; min-width: 0; height: 56px; box-sizing: border-box; padding: 0 22px; border-radius: 999px; border: 1.5px solid #D6DDEE; background: #FFFFFF; font-family: inherit; font-size: 16px; color: #0B1433; outline: none">\n'+BTN('CR-ONB-003b.dc.html','Continue')+'\n</div>\n'
c+='<div aria-hidden="true" style="width: 100%; margin: clamp(14px, 2.6vh, 20px) 0; display: flex; align-items: center; gap: 14px; font-size: 13px; color: #5B6582"><span style="flex-grow: 1; height: 1px; background: #E6EAF3"></span>or<span style="flex-grow: 1; height: 1px; background: #E6EAF3"></span></div>\n'
c+='<div class="ob-row" style="width: 100%; display: flex; gap: 10px">'+SOC(G,'Google')+SOC(A,'Apple')+'</div>\n'
c+='<p style="margin: clamp(14px, 2.6vh, 20px) 0 0 0; font-size: 12.5px; line-height: 1.5; color: #5B6582; text-align: center">By continuing, you agree to Credalio’s <a href="#" class="ob-link" style="color: #3A4566; font-weight: 500">Terms</a> and <a href="#" class="ob-link" style="color: #3A4566; font-weight: 500">Privacy Policy</a>.</p>'
make('CR-ONB-003.dc.html','Credalio onboarding: create your account',540,c,back='CR-ONB-002.dc.html',chip='Saving your place')

# ---- 003b
c=H1('Check your inbox.')+'\n'
c+='<p class="ob-in2" style="margin: 12px 0 0 0; max-width: 520px; font-size: 16px; line-height: 1.55; color: #4A5578; text-align: center">We’ve sent a link to <span style="color: #0B1433; font-weight: 600">ada.ononuju@example.com</span>. Open it and we’ll pick up right where you left off.</p>\n'
c+='<div class="ob-in3" role="status" style="margin-top: clamp(16px, 3vh, 24px); display: inline-flex; align-items: center; gap: 10px; padding: 9px 16px 9px 14px; border-radius: 999px; background: #F5F8FF; font-size: 13.5px; color: #3A4566"><span style="position: relative; width: 8px; height: 8px; flex-shrink: 0"><span class="ob-pulse" style="position: absolute; left: -2px; top: -2px; width: 12px; height: 12px; box-sizing: border-box; border-radius: 50%; border: 2px solid #1652F0"></span><span style="position: absolute; left: 0; top: 0; width: 8px; height: 8px; border-radius: 50%; background: #1652F0"></span></span>Waiting for you. This page moves on by itself.</div>\n'
c+=BTN('#','Open my email','clamp(18px, 3.4vh, 28px)')+'\n'
c+='<p style="margin: 16px 0 0 0; font-size: 14px; line-height: 1.6; color: #4A5578; text-align: center">Nothing yet? Check spam, or <a href="#" class="ob-link" style="font-weight: 600">resend the link</a>. Wrong address? <a href="CR-ONB-003.dc.html" class="ob-link" style="font-weight: 600">Change it</a></p>\n'
c+='<a href="CR-ONB-003v.dc.html" class="ob-link" style="margin-top: 12px; display: inline-flex; padding: 5px 12px; border-radius: 999px; border: 1px dashed #CBD3E6; font-size: 12px; color: #5B6582; text-decoration: none">Prototype only: simulate opening the link</a>'
make('CR-ONB-003b.dc.html','Credalio onboarding: check your inbox',560,c,back='CR-ONB-003.dc.html',login=False,chip='Almost there')

# ---- 003v
MAIL='<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2.5"></rect><path d="m4 7 8 6 8-6"></path></svg>'
c=H1('Your email is confirmed.')+'\n'+SUB('Thanks for confirming. One last step: choose a password to keep your work safe.',480)+'\n'
c+='<div class="ob-in3" style="margin-top: clamp(18px, 3.4vh, 28px); max-width: 100%; display: inline-flex; align-items: center; gap: 12px; padding: 8px 10px 8px 8px; box-sizing: border-box; border-radius: 999px; border: 1.5px solid #E6EAF3; background: #FFFFFF"><span style="width: 36px; height: 36px; flex-shrink: 0; border-radius: 50%; background: #EAF0FF; color: #1652F0; display: flex; align-items: center; justify-content: center">'+MAIL+'</span><span style="min-width: 0; font-size: 15px; font-weight: 500; color: #0B1433; overflow: hidden; text-overflow: ellipsis; white-space: nowrap">ada.ononuju@example.com</span><span style="display: flex; align-items: center; gap: 5px; padding: 5px 10px; border-radius: 999px; background: #E7F4EE; color: #0F6B45; font-size: 12.5px; font-weight: 600; flex-shrink: 0"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"></path></svg>Verified</span></div>\n'
c+=BTN('#','Create a password','clamp(20px, 3.6vh, 32px)')
make('CR-ONB-003v.dc.html','Credalio onboarding: email confirmed',560,c,back=None,login=False,chip='You’re in')
