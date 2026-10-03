import re, json
P='/home/user/credalio/design/canvas/project/'
src=open(P+'CR-ONB-002.dc.html').read()
head, rest = src.split('<div style="width: 100%; max-width: 540px">',1)
# shell tail after content
tail = '\n</div>\n</div>\n</main>\n</div>\n</x-dc>\n'
BTN='<a href="{href}" class="ob-btn" style="margin-top: {mt}; display: flex; align-items: center; justify-content: space-between; height: 56px; padding: 0 6px 0 26px; border-radius: 999px; background: #1652F0; color: #FFFFFF; font-size: 16px; font-weight: 600; text-decoration: none; box-shadow: 0 1px 0 rgba(255, 255, 255, 0.25) inset, 0 10px 24px rgba(22, 82, 240, 0.26)">{label}<span class="ob-arrow" style="width: 44px; height: 44px; border-radius: 50%; background: #FFFFFF; color: #1652F0; display: flex; align-items: center; justify-content: center"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14"></path><path d="m13 6 6 6-6 6"></path></svg></span></a>'
def btn(href,label,mt='clamp(20px, 3.4vh, 28px)'): return BTN.format(href=href,label=label,mt=mt)
H1='<h1 class="ob-h1 ob-in" style="margin: 0; font-size: clamp(32px, 5vh, 40px); line-height: 1.12; font-weight: 600; letter-spacing: -0.03em; color: #0B1433">{}</h1>'
SUB='<p class="ob-in2" style="margin: 12px 0 0 0; font-size: 16px; line-height: 1.55; color: #4A5578">{}</p>'
def make(name,title,h2,p,back,login,content,script,props='{"$preview":{"width":1440,"height":820}}'):
    h=head
    h=h.replace('<title>Credalio onboarding: how will you create</title>','<title>'+title+'</title>')
    h=h.replace('Create your way.</h2>',h2+'</h2>')
    h=h.replace('Start as yourself today. Institutions and organisations are joining soon.</p>',p+'</p>')
    h=h.replace('<a href="Main.dc.html" class="ob-ghost"','<a href="'+back+'" class="ob-ghost"')
    if not login:
        h=h.replace('<div style="display: flex; align-items: center; gap: 14px; font-size: 14px; color: #3A4566">Already have an account? <a href="#" class="ob-ghost" style="display: flex; align-items: center; height: 42px; padding: 0 20px; border-radius: 999px; border: 1.5px solid #D6DDEE; background: #FFFFFF; color: #0B1433; font-weight: 600; text-decoration: none">Log in</a></div>','<span></span>')
        h=h.replace('<a href="#" class="ob-ghost" style="display: flex; align-items: center; height: 44px; padding: 0 18px; border-radius: 999px; border: 1.5px solid #D6DDEE; background: #FFFFFF; color: #0B1433; font-size: 14px; font-weight: 600; text-decoration: none">Log in</a>','')
    s=h+'<div style="width: 100%; max-width: 500px">\n'+content+tail+"<script type=\"text/x-dc\" data-dc-script data-props='"+props+"'>\n"+script+'\n</script>\n</body>\n</html>\n'
    open(P+name,'w').write(s); print(name,len(s))
NOSCRIPT='class Component extends DCLogic {\n  renderVals() { return {}; }\n}'
