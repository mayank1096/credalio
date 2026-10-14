import re,sys,os,json
STYLE=re.compile(r'(<style[^>]*>)(.*?)(</style>)',re.S)
SCRIPT=re.compile(r'(<script type="text/x-dc"[^>]*>)(.*?)(</script>)',re.S)
def split_top(s,ch):
    out=[];d=0;cur=''
    for c in s:
        if c in '([':d+=1
        elif c in ')]':d-=1
        if c==ch and d==0: out.append(cur);cur=''
        else: cur+=c
    out.append(cur);return out
def classes_outside_parens(sel):
    t='';d=0
    for c in sel:
        if c=='(':d+=1
        elif c==')':d-=1;continue
        if d==0:t+=c
    return re.findall(r'\.(-?[A-Za-z_][\w-]*)',t)
def match_brace(s,i):
    d=0
    for j in range(i,len(s)):
        if s[j]=='{':d+=1
        elif s[j]=='}':
            d-=1
            if d==0:return j
    return len(s)-1
class Ctx:
    def __init__(s,used,kfused): s.used=used;s.kfused=kfused;s.dropped_sel=0;s.dropped_kf=0
def process(css,ctx):
    out=[];i=0;n=len(css)
    while i<n:
        j=css.find('{',i)
        if j<0: out.append(css[i:]);break
        pre=css[i:j]
        # statement at-rules (e.g. @import ...;) inside pre
        while ';' in pre and pre.strip().startswith('@') is False and False: pass
        k=match_brace(css,j);body=css[j+1:k];p=pre.strip()
        lead=pre[:len(pre)-len(pre.lstrip())]
        if p.startswith('@keyframes') or p.startswith('@-webkit-keyframes'):
            name=p.split()[1]
            if name in ctx.kfused: out.append(pre+'{'+body+'}')
            else: ctx.dropped_kf+=1; out.append(lead.replace('\n\n','\n') if '\n' in lead else '')
        elif p.startswith('@media') or p.startswith('@supports') or p.startswith('@container'):
            inner=process(body,ctx)
            if inner.strip(): out.append(pre+'{'+inner+'}')
            else: out.append(lead if '\n' in lead else '')
        elif p.startswith('@'):
            out.append(pre+'{'+body+'}')
        else:
            sels=split_top(pre,',');keep=[]
            for s in sels:
                cl=classes_outside_parens(s)
                if all(c in ctx.used for c in cl): keep.append(s)
                else: ctx.dropped_sel+=1
            if keep:
                ps=','.join(keep)
                if not ps.strip(): ps=pre
                # keep leading whitespace of original
                if not ps.startswith(lead): ps=lead+ps.lstrip()
                out.append(ps+'{'+body+'}')
            else:
                out.append(lead if '\n' in lead else '')
        i=k+1
    return ''.join(out)
def used_classes(nonstyle, allcls):
    used=set()
    lits=re.findall(r"""(['"`])((?:(?!\1).){1,40}?)\1\s*\+""",nonstyle)+[(None,m) for m in re.findall(r'([\w-]{2,})\$\{',nonstyle)]
    prefixes=set(m.split()[-1] for _,m in lits if m.split())
    for c in allcls:
        if re.search(r'(?<![\w-])'+re.escape(c)+r'(?![\w-])',nonstyle): used.add(c);continue
        if any(c.startswith(p) and (len(p)>=2 or re.fullmatch(r'\d+',c[len(p):])) for p in prefixes if p): used.add(c)
    return used
def clean_file(path):
    s=open(path).read();orig=s
    styles=''.join(m.group(2) for m in STYLE.finditer(s))
    if not styles: return None
    nonstyle=STYLE.sub('',s)
    nostyle_cm=re.sub(r'/\*.*?\*/','',styles,flags=re.S)
    allcls=set(re.findall(r'\.(-?[A-Za-z_][\w-]*)',re.sub(r'url\([^)]*\)','',nostyle_cm)))
    used=used_classes(nonstyle,allcls)
    kfused=set(re.findall(r'animation(?:-name)?\s*:\s*([^;}{]+)',s))
    kfn=set()
    for a in kfused: kfn|=set(re.findall(r'[A-Za-z_][\w-]*',a))
    ctx=Ctx(used,kfn)
    def fix(m):
        css=re.sub(r'/\*.*?\*/','',m.group(2),flags=re.S)
        css=process(css,ctx)
        css=re.sub(r'\n[ \t]*\n+','\n',css)
        return m.group(1)+css+m.group(3)
    s=STYLE.sub(fix,s)
    # pass 2: keyframes only used by rules that were just dropped
    nk=set()
    for a in re.findall(r'animation(?:-name)?\s*:\s*([^;}{]+)',s): nk|=set(re.findall(r'[A-Za-z_][\w-]*',a))
    ctx.kfused=nk
    s=STYLE.sub(fix,s)
    def fixjs(m):
        js=re.sub(r'[ \t]*/\*.*?\*/[ \t]*\n?','',m.group(2),flags=re.S)
        return m.group(1)+js+m.group(3)
    s=SCRIPT.sub(fixjs,s)
    if s!=orig: open(path,'w').write(s)
    return ctx.dropped_sel,ctx.dropped_kf,len(orig)-len(s)
if __name__=='__main__':
    tot=[0,0,0]
    for d in sys.argv[1:]:
        for f in sorted(os.listdir(d)):
            if not f.endswith('.dc.html'): continue
            r=clean_file(os.path.join(d,f))
            if r:
                tot=[a+b for a,b in zip(tot,r)]
    print('selectors dropped',tot[0],'keyframes dropped',tot[1],'bytes saved',tot[2])
