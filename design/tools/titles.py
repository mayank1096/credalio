import json,re,sys,os,html
def run(D):
    cj=f'{D}/canvas.json';c=json.load(open(cj));b=c['boards']
    fix={'Main.dc.html':'CR-ONB-001 · Begin your journey · Desktop','CR-ONB-001-Mobile.dc.html':'CR-ONB-001 · Mobile',
         'CR-ONB-002S.dc.html':'CR-ONB-002S · Organizations are coming soon · Desktop'}
    for k,t in fix.items():
        if k in b: b[k]['title']=t
    name={}
    for k,v in b.items():
        m=re.match(r'^(CR-[\w-]+) · (.+) · Desktop$',v.get('title') or '')
        if m: name[m.group(1)]=m.group(2)
    n=0
    for k,v in b.items():
        t=v.get('title');f=f'{D}/{k}'
        s=open(f).read();m=re.search(r'<title>([^<]*)</title>',s)
        if not m: continue
        old=html.unescape(m.group(1))
        if t and re.match(r'^(CR-[\w-]+) · (.+) · Desktop$',t): new=t[:-len(' · Desktop')]
        elif t and re.match(r'^(CR-[\w-]+) · Mobile$',t):
            i=t.split(' · ')[0];new=f"{i} · {name.get(i,'')} · Mobile".replace(' ·  ·',' ·')
        elif t is None:
            i=k[:-8];desc=re.sub(r'^Credalio\s*·\s*','',old);new=f'{i} · {desc} · shared source'
        else:
            i=t.split(' · ')[0];new=t
        if new!=old:
            s=s[:m.start(1)]+html.escape(new,quote=False)+s[m.end(1):];open(f,'w').write(s);n+=1
    if isinstance(c.get('notes'),dict):
        for k in [k for k in c['notes'] if k.startswith('new-')]: del c['notes'][k]
    open(cj,'w').write(json.dumps(c,indent=2,ensure_ascii=False))
    print(D,'titles changed',n)
for D in sys.argv[1:]: run(D)
