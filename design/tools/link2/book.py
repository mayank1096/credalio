import json,html,os,sys
S=sys.argv[1]; L=json.load(open(S+'/shots/shots.json'))
from PIL import Image
pairs=[];cur=None
for x in L:
    if x['lab']=='Desktop': cur={'d':x,'m':None,'sec':x['sec'],'title':x['title']}; pairs.append(cur)
    else: cur['m']=x
secs=[];
for i,p in enumerate(pairs):
    if not secs or secs[-1][0]!=p['sec']: secs.append([p['sec'],i+3])
CSS='''@font-face{font-family:'GS';src:url(GoogleSans-latin.woff2) format('woff2');font-weight:400 700}
@page{size:A4 landscape;margin:0}*{box-sizing:border-box}body{margin:0;font-family:'GS',system-ui;color:#0B1433}
.pg{width:297mm;height:209.8mm;position:relative;overflow:hidden;page-break-after:always;padding:16mm 16mm 14mm}
.cov{background:linear-gradient(180deg,#F5F8FF,#FFFFFF 60%);display:flex;flex-direction:column;justify-content:center;padding-left:24mm}
.cov img{width:52mm}.cov h1{font-size:30pt;font-weight:600;letter-spacing:-.02em;margin:10mm 0 4mm}.cov p{font-size:10.5pt;color:#4A5578;line-height:1.6;max-width:150mm;margin:0}
h2{font-size:15pt;font-weight:600;margin:0 0 6mm}.toc{columns:2;column-gap:14mm;font-size:9.5pt}.toc div{display:flex;justify-content:space-between;padding:2.2mm 0;border-bottom:.3mm solid #EEF1F7;break-inside:avoid}.toc span:last-child{color:#8A93AD}
.lab{font-size:8pt;color:#1652F0;font-weight:500}.ttl{font-size:13pt;font-weight:600;margin:1mm 0 5mm}
.row{display:flex;gap:8mm;align-items:flex-start;height:150mm}.dk,.mb{border:.35mm solid #E6EAF3;border-radius:3mm;overflow:hidden;background:#fff;box-shadow:0 2mm 6mm rgba(11,20,51,.06)}
.dk img,.mb img{display:block;width:100%;height:auto}.cap{font-size:7.5pt;color:#8A93AD;margin-top:2mm}
.ft{position:absolute;left:16mm;right:16mm;bottom:8mm;display:flex;justify-content:space-between;font-size:7.5pt;color:#8A93AD}'''
def fit(path,maxw,maxh):
    w,h=Image.open(path).size; s=min(maxw/w,maxh/h); return w*s,h*s
out=['<!doctype html><html><head><meta charset="utf-8"><style>%s</style></head><body>'%CSS]
n=len(pairs)
out.append('<div class="pg cov"><img src="credalio-wordmark.png"><h1>Link 2 · Screen book</h1><p>Creator Studio: wallet, payments and revalidation, earnings and payouts, course overview, discussions, calendar, learners and analytics, profile, settings, Nova and Creio, help, account menu and message pop-ups.<br>%d screens, each shown on desktop (1440) and mobile (390), in flow order. Design handoff · October 2026.</p></div>'%n)
toc=''.join('<div><span>%s</span><span>%d</span></div>'%(html.escape(s),p) for s,p in secs)
out.append('<div class="pg"><h2>Contents</h2><div class="toc">%s</div><div class="ft"><span>Credalio · Link 2 · Screen book</span><span>2</span></div></div>'%toc)
MW,MH=176,150  # mm desktop box
for i,p in enumerate(pairs):
    dpath=S+'/shots/credalio-link2-screenshots/'+p['d']['name']
    dw,dh=fit(dpath,MW,MH)
    mob=''
    if p['m']:
        mpath=S+'/shots/credalio-link2-screenshots/'+p['m']['name']; mw,mh=fit(mpath,72,MH)
        mob='<div><div class="mb" style="width:%.1fmm"><img src="credalio-link2-screenshots/%s"></div><div class="cap">Mobile · 390</div></div>'%(mw,html.escape(p['m']['name']))
    out.append('<div class="pg"><div class="lab">%s</div><div class="ttl">%s</div><div class="row"><div><div class="dk" style="width:%.1fmm"><img src="credalio-link2-screenshots/%s"></div><div class="cap">Desktop · 1440</div></div>%s</div><div class="ft"><span>Credalio · Link 2 · Screen book</span><span>%d</span></div></div>'%(html.escape(p['sec']),html.escape(p['title']),dw,html.escape(p['d']['name']),mob,i+3))
out.append('</body></html>')
open(S+'/shots/book.html','w').write(''.join(out)); print(n,'screens',len(secs),'sections')
