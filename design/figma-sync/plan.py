import json,subprocess,re
rows=[l.rstrip('\n').split('\t') for l in open('boards.txt')]
PAGES={'ONB-D':'2:4','ONB-M':'2:5','STU':'25:12','RDY':'25:13','ORI':'25:14','KYC':'25:15'}
def grp(f):
    if f.startswith('Main') or 'ONB' in f: return 'ONB'
    if 'DASH' in f or 'CREATE' in f: return 'STU'
    if 'RDY' in f or 'CTR' in f: return 'RDY'
    if 'ORI' in f: return 'ORI'
    return 'KYC'
cnt={}; plan=[]
dt={}
for spec,title in rows:
    f=spec.split(':')[0]
    if not f.endswith('-Mobile.dc.html'): dt[re.sub(r'\.dc\.html$','',f)]=title
dt['Main']=dt.get('Main')

for spec,title in rows:
    f,wh=spec.split(':'); w=int(wh.split('x')[0]); mob=w<500
    key=f.replace('.dc.html','')+'@'+str(w)
    g=grp(f); base=re.sub(r'-Mobile$','',f.replace('.dc.html',''))
    if g=='ONB':
        pg=PAGES['ONB-M' if mob else 'ONB-D']; i=cnt.setdefault(('ONB',mob),[]); 
        if base not in i: i.append(base)
        x=(i.index(base))*(470 if mob else 1600); y=0
    else:
        pg=PAGES[g]; i=cnt.setdefault(g,[])
        if base not in i: i.append(base)
        x=i.index(base)*2000+(1520 if mob else 0); y=0
    if mob:
        b2='Main' if base=='CR-ONB-001' else base
        if dt.get(b2): title=re.sub(r'·\s*Desktop.*$','· Mobile',dt[b2])
        if base=='CR-ONB-001': title='CR-ONB-001 · Who will you become next? · Mobile'
    else: title=re.sub(r'\s*\(responsive source\)','',title).replace('CR-ONB-001 · Desktop','CR-ONB-001 · Who will you become next? · Desktop')
    plan.append(dict(key=key,page=pg,x=x,y=y,title=title,grp=g))
json.dump(plan,open('plan.json','w'),indent=0,ensure_ascii=False)
for p in plan:
    subprocess.run(['python3','post.py','out/'+p['key']],check=True,capture_output=True)
    r=subprocess.run(['python3','gen.py','out/'+p['key'],p['page'],str(p['x']),str(p['y']),p['title']],check=True,capture_output=True,text=True)
    p['jobs']=[l.split()[0] for l in r.stdout.strip().split('\n')]
    p['sizes']=[int(l.split()[1]) for l in r.stdout.strip().split('\n')]
json.dump(plan,open('plan.json','w'),indent=0,ensure_ascii=False)
tot=sum(sum(p['sizes']) for p in plan); print('jobs',sum(len(p['jobs']) for p in plan),'chars',tot)
for p in plan: print(p['key'],p['sizes'])
