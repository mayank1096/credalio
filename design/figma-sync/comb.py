import sys,subprocess,os
# comb.py out.js "KEY|PAGE|X|NAME|OLDNAME" ...
B=open('builder.js').read().replace("return {ok:true,id:target.id,imgs};","return {name:NAME,id:target.id,imgs};")
o="async function build(PG,NAME,KEY,POS,FONTS,SV,IM,JOB){\n"+B+"\n}\nconst R=[];\n"
for spec in sys.argv[2:]:
    k,pg,x,name,old=(spec.split('|')+[''])[:5]
    subprocess.run(['python3','post.py','out/'+k],check=True,capture_output=True)
    for f in os.listdir('out/'+k):
        if f.startswith('job_'): os.remove('out/'+k+'/'+f)
    subprocess.run(['python3','gen.py','out/'+k,pg,x,'0',name],check=True,capture_output=True)
    js=sorted(f for f in os.listdir('out/'+k) if f.startswith('job_'))
    assert js==['job_0.js'],(k,js)
    head=open('out/'+k+'/job_0.js').read().split('\nconst page=')[0]
    pre=f"{{const _p=await figma.getNodeByIdAsync('{pg}');_p.children.filter(c=>c.name==={old!r}).forEach(c=>c.remove());}}\n" if old else ''
    o+=pre+"{\n"+head+"\nR.push(await build(PG,NAME,KEY,POS,FONTS,SV,IM,JOB));\n}\n"
o+="return R;"
open(sys.argv[1],'w').write(o);print(sys.argv[1],len(o))
