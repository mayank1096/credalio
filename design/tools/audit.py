import json,re,os,sys,collections
OLD={'bad84659fa9f24b3a7efb7e88696e531':'scene v1','877e6d93c070677634b4956192180989':'scene v2','cd614cd8bd65153391f42811624f1c50':'scene v3','35f92c519316f253dc620c3c4b2d859c':'scene v4','c6a3cfeead45b159745cbe37bd22bc3f':'scene v5'}
def walk(o):
    if isinstance(o,dict):
        yield o
        for v in o.values(): yield from walk(v)
    elif isinstance(o,list):
        for v in o: yield from walk(v)
for D in sys.argv[1:]:
    print('=====',D)
    c=json.load(open(f'{D}/canvas.json'))
    boards=c['boards']; print('pages',[(p.get('id'),p.get('name')) for p in c['pages']] if isinstance(c['pages'],list) else c['pages'])
    files=[f for f in os.listdir(D) if f.endswith('.dc.html')]
    onb=set(boards.keys()) if isinstance(boards,dict) else set()
    imp=collections.Counter()
    for f in files:
        s=open(f'{D}/{f}').read()
        for m in re.findall(r'<dc-import[^>]*name="([^"]+)"',s): imp[m+'.dc.html']+=1
    orph=[f for f in files if f not in onb and imp[f]==0]
    print('files',len(files),'boards',len(onb),'orphans',orph)
    pg=collections.Counter(v.get('page') for v in boards.values())
    print('boards per page',dict(pg))
    notes=c.get('notes',{}); print('notes',len(notes))
    nn=collections.Counter()
    for k,v in (notes.items() if isinstance(notes,dict) else enumerate(notes)):
        t=(v.get('text') or v.get('content') or '') if isinstance(v,dict) else str(v)
        nn[(k.split('-')[0] if isinstance(k,str) else 'x')]+=1
    print('note id prefixes',dict(nn))
    tot=collections.Counter()
    for f in sorted(files):
        s=open(f'{D}/{f}').read()
        if len(s)<1200: continue
        styles=''.join(re.findall(r'<style[^>]*>(.*?)</style>',s,re.S))
        rest=re.sub(r'<style[^>]*>.*?</style>','',s,flags=re.S)
        cls=set(re.findall(r'\.(-?[A-Za-z_][\w-]*)',re.sub(r'url\([^)]*\)','',styles)))
        unused=sorted(x for x in cls if not re.search(r'(?<![\w-])'+re.escape(x)+r'(?![\w-])',rest))
        kf=set(re.findall(r'@keyframes\s+([\w-]+)',styles))
        ku=sorted(k for k in kf if not re.search(r'animation[^;{}]*\b'+re.escape(k)+r'\b',s))
        com=len(re.findall(r'<!--.*?-->',s,re.S))
        old=[OLD[b] for b in re.findall(r'/_blob/([0-9a-f]{32})',s) if b in OLD]
        misc=[w for w in ['sessionStorage','localStorage','console.','TODO','FIXME','debugger','lorem','Lorem'] if w in s]
        tot['unused']+=len(unused);tot['kf']+=len(ku)
        if unused or ku or com or old or misc:
            print(f'{f}: unusedCSS={len(unused)} {unused[:12]} | unusedKF={ku} | comments={com} | old={sorted(set(old))} | misc={misc}')
    print(dict(tot))
