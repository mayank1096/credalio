P='/home/user/credalio/design/canvas/project/'
ILL=open('illus_create.html').read()
HEAD='''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500;600;700&amp;display=swap">
<style>
body{{margin:0;background:#FFFFFF}}
a{{color:#1652F0}}a:hover{{color:#0E3BB8}}
.sr-only{{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}}
@keyframes cdFade{{from{{opacity:0}}to{{opacity:1}}}}
@keyframes cdDraw{{from{{stroke-dashoffset:1}}to{{stroke-dashoffset:0}}}}
@keyframes cdComet{{0%{{stroke-dashoffset:0.08;opacity:0}}10%{{opacity:1}}85%{{opacity:1}}100%{{stroke-dashoffset:-1;opacity:0}}}}
@keyframes cdPulse{{0%{{transform:scale(.7);opacity:.9}}100%{{transform:scale(2.6);opacity:0}}}}
@keyframes cdChip{{from{{opacity:0;margin-top:10px}}to{{opacity:1;margin-top:0}}}}
@keyframes cdOrb{{0%,100%{{opacity:.55}}50%{{opacity:1}}}}
@keyframes obIn{{from{{opacity:0;transform:translateY(8px)}}to{{opacity:1;transform:none}}}}
.cd-fade{{animation:cdFade .6s ease both}}
.cd-draw{{stroke-dasharray:1;animation:cdDraw 1s cubic-bezier(.4,0,.2,1) .2s both}}
.cd-comet{{stroke-dasharray:0.07 2;stroke-dashoffset:0.08;animation:cdComet 2.6s ease-in-out 1.2s infinite}}
.cd-pulse{{transform-box:fill-box;transform-origin:center;animation:cdPulse 2s ease-out 1.1s infinite}}
.cd-chip{{animation:cdChip .5s ease .9s both}}
.cd-orb{{animation:cdOrb 2.4s ease-in-out infinite}}
.ob-pulse{{animation:cdPulse 2s ease-out infinite}}
.ob-in{{animation:obIn .5s ease both}}
.ob-in2{{animation:obIn .5s ease .08s both}}
.ob-in3{{animation:obIn .5s ease .16s both}}
.ob-btn{{transition:background .2s ease,transform .2s ease}}
.ob-btn:hover{{background:#0E3BB8 !important;color:#FFFFFF;transform:translateY(-1px)}}
.ob-btn:active{{transform:scale(.98)}}
.ob-arrow{{transition:transform .3s cubic-bezier(.3,1.4,.5,1)}}
.ob-btn:hover .ob-arrow{{transform:translateX(4px)}}
.ob-ghost{{transition:border-color .2s ease,background .2s ease}}
.ob-ghost:hover{{border-color:#1652F0 !important;background:#F5F8FF !important;color:#0B1433}}
.ob-opt{{transition:all .25s ease}}
.ob-opt:hover{{transform:translateY(-2px);border-color:#AFC1F5 !important}}
.ob-opt:active{{transform:scale(.985)}}
.ob-input:focus{{border-color:#1652F0 !important;box-shadow:0 0 0 4px rgba(22,82,240,.12)}}
.ob-input::placeholder{{color:#8A93AD}}
.ob-btn:focus-visible,.ob-opt:focus-visible,.ob-ghost:focus-visible,.ob-link:focus-visible{{outline:3px solid rgba(22,82,240,.45);outline-offset:3px}}
@media (prefers-reduced-motion: reduce){{.cd-fade,.cd-draw,.cd-comet,.cd-pulse,.cd-chip,.cd-orb,.ob-pulse,.ob-in,.ob-in2,.ob-in3{{animation:none}}.cd-comet{{opacity:0}}}}
@media (max-height: 760px){{.cd-chip{{display:none !important}}}}
@media (max-width: 960px){{
.ob-root{{height:auto !important;min-height:100vh !important;display:flex;flex-direction:column}}
.ob-header{{position:relative !important;height:64px !important;padding:0 20px !important;flex-shrink:0;order:0}}
.ob-logo{{width:28px !important;height:28px !important;border-radius:8px !important}}
.ob-brand{{font-size:18px !important}}
.ob-hide-sm{{display:none}}
.ob-track{{position:relative !important;top:0 !important;height:auto !important;padding:4px 20px 0 20px !important;justify-content:flex-start !important;gap:12px;flex-shrink:0;order:1}}
.ob-back{{position:static !important;width:44px;height:44px !important;padding:0 !important;justify-content:center;flex-shrink:0}}
.ob-back-t{{display:none}}
.ob-steps{{width:auto !important;flex-grow:1;align-items:flex-start !important}}
.ob-illus{{position:relative !important;flex-shrink:0;align-self:flex-start;height:170px !important;width:510px !important;order:2;margin-top:4px;transform:translateX(calc(-50% + var(--pan))) !important}}
.ob-main{{order:3;position:relative !important;top:0 !important;padding:8px 20px 32px 20px;box-sizing:border-box}}
.ob-col{{width:100% !important}}
.ob-h1{{font-size:30px !important}}
.ob-grid3{{grid-template-columns:minmax(0,1fr) !important;gap:10px !important}}
.ob-row{{flex-direction:column !important;align-items:stretch !important;width:100%}}
.ob-row > a,.ob-row > input{{flex:none !important}}
.ob-h1{{width:auto !important}}
.ob-btn{{justify-content:space-between !important;align-self:stretch !important}}
.ob-wide{{align-self:stretch !important}}
.cd-chip{{font-size:11.5px !important;padding:5px 10px 5px 8px !important}}
}}
</style>
</helmet>
'''
LOGO='''<div style="display: flex; align-items: center; gap: 10px">
<div class="ob-logo" style="width: 32px; height: 32px; border-radius: 9px; background: #1652F0; display: flex; align-items: center; justify-content: center"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round" aria-hidden="true"><path d="M17.5 7.2A7 7 0 1 0 17.5 16.8"></path></svg></div>
<span class="ob-brand" style="font-size: 21px; font-weight: 600; letter-spacing: -0.02em; color: #0B1433">Credalio</span>
</div>'''
LOGIN='<div style="display: flex; align-items: center; gap: 14px; font-size: 14px; color: #3A4566"><span class="ob-hide-sm">Already have an account?</span> <a href="#" class="ob-ghost" style="display: flex; align-items: center; height: 44px; padding: 0 20px; border-radius: 999px; border: 1.5px solid #D6DDEE; background: #FFFFFF; color: #0B1433; font-weight: 600; text-decoration: none">Log in</a></div>'
def BACK(href): return '<a href="'+href+'" class="ob-ghost ob-back" aria-label="Back" style="position: absolute; left: clamp(24px, 6.67vw, 96px); top: 2px; display: flex; align-items: center; gap: 8px; height: 40px; padding: 0 16px 0 12px; box-sizing: border-box; border-radius: 999px; border: 1.5px solid #E6EAF3; background: #FFFFFF; color: #3A4566; font-size: 14px; font-weight: 500; text-decoration: none"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 12H5"></path><path d="m11 18-6-6 6-6"></path></svg><span class="ob-back-t">Back</span></a>'
def STEPS(n=1,label='Your account'):
    seg=''.join('<span style="height: 4px; border-radius: 4px; background: '+('#1652F0' if i<n else '#E6EAF3')+'"></span>' for i in range(5))
    return '<div class="ob-steps" role="group" aria-label="Step '+str(n)+' of 5: '+label+'" style="width: 320px; display: flex; flex-direction: column; align-items: center; gap: 8px">\n<div aria-hidden="true" style="width: 100%; display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 6px">'+seg+'</div>\n<span style="font-size: 13px; color: #5B6582">Step '+str(n)+' of 5 · <span style="color: #0B1433; font-weight: 600">'+label+'</span></span>\n</div>'
def ILLUS(chip):
    import re
    ill=re.sub(r'<div class="cd-chip"[^>]*>\s*<span[^>]*></span>[^<]*</div>\n?','',ILL)
    return '''<div class="ob-illus" aria-hidden="true" style="position: absolute; left: 50%; bottom: 0; height: min(40vh, 33.33vw); aspect-ratio: 2172 / 724; transform: translateX(-50%); --pan: 55px; overflow: hidden; z-index: 1">
<img src="/_blob/bad84659fa9f24b3a7efb7e88696e531" alt="" style="position: absolute; left: 0; top: 0; width: 100%; height: 100%; display: block; filter: brightness(1.012)">
'''+ill+'''
<svg viewBox="0 0 2172 724" preserveAspectRatio="none" aria-hidden="true" style="position: absolute; left: 0; top: 0; width: 100%; height: 100%; pointer-events: none"><circle class="cd-orb" cx="1060" cy="627" r="7" fill="#1652F0" stroke="#FFFFFF" stroke-width="2.5"></circle></svg>
</div>'''
ARROW='<span class="ob-arrow" style="width: 44px; height: 44px; border-radius: 50%; background: #FFFFFF; color: #1652F0; display: flex; align-items: center; justify-content: center"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14"></path><path d="m13 6 6 6-6 6"></path></svg></span>'
def BTN(href,label,mt='0'): return '<a href="'+href+'" class="ob-btn" style="margin-top: '+mt+'; display: flex; align-items: center; gap: 16px; height: 56px; padding: 0 6px 0 28px; box-sizing: border-box; border-radius: 999px; background: #1652F0; color: #FFFFFF; font-size: 16px; font-weight: 600; letter-spacing: -0.005em; text-decoration: none; white-space: nowrap; box-shadow: 0 1px 0 rgba(255, 255, 255, 0.25) inset, 0 12px 28px rgba(22, 82, 240, 0.28)">'+label+ARROW+'</a>'
def GHOST(href,label): return '<a href="'+href+'" class="ob-ghost ob-wide" style="display: flex; align-items: center; justify-content: center; height: 56px; padding: 0 26px; box-sizing: border-box; border-radius: 999px; border: 1.5px solid #D6DDEE; background: #FFFFFF; color: #0B1433; font-size: 15px; font-weight: 600; text-decoration: none; white-space: nowrap">'+label+'</a>'
def H1(t): return '<h1 class="ob-h1 ob-in" style="margin: 0; font-size: clamp(36px, 6vh, 52px); line-height: 1.1; font-weight: 600; letter-spacing: -0.035em; color: #0B1433; text-align: center; width: max-content; max-width: calc(100vw - 48px)">'+t+'</h1>'
def SUB(t,mw=560): return '<p class="ob-in2" style="margin: 12px 0 0 0; max-width: '+str(mw)+'px; font-size: 16px; line-height: 1.55; color: #4A5578; text-align: center">'+t+'</p>'
NOSCRIPT='class Component extends DCLogic {\n  renderVals() { return {}; }\n}'
def make(name,title,width,content,back=None,login=True,chip='You start as a Creator',script=NOSCRIPT,step=(1,'Your account'),illh='min(40vh, 33.33vw)',extra_css=''):
    s=HEAD.format(title=title).replace('</style>\n</helmet>',extra_css+'</style>\n</helmet>',1)
    s+='''<div class="ob-root" style="width: 100%; height: 100vh; min-height: 680px; position: relative; overflow: hidden; background: #FFFFFF; font-family: 'Google Sans', 'Google Sans Text', 'Helvetica Neue', system-ui, sans-serif; color: #0B1433">
<header class="ob-header" style="position: absolute; left: 0; top: 0; width: 100%; height: 88px; box-sizing: border-box; padding: 0 clamp(24px, 6.67vw, 96px); display: flex; align-items: center; justify-content: space-between; z-index: 3">
'''+LOGO+'\n'+(LOGIN if login else '<span></span>')+'''
</header>
<div class="ob-track" style="position: absolute; left: 0; top: 88px; width: 100%; height: 44px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; z-index: 3">
'''+(BACK(back) if back else '')+'\n'+STEPS(*step)+'''
</div>
<main class="ob-main" style="position: absolute; z-index: 2; left: 0; top: clamp(140px, 19vh, 176px); width: 100%; display: flex; flex-direction: column; align-items: center">
<div class="ob-col" style="width: min('''+str(width)+'''px, calc(100% - 48px)); display: flex; flex-direction: column; align-items: center">
'''+content+'''
</div>
</main>
'''+ILLUS(chip).replace('height: min(40vh, 33.33vw);','height: '+illh+';')+'''
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":1440,"height":820}}'>
'''+script+'''
</script>
</body>
</html>
'''
    open(P+name,'w').write(s); print(name,len(s))
