#!/usr/bin/env python3
# usage: up.py <file with lines: KEY/cid submitUrl>
import sys,subprocess,concurrent.futures as cf,os
D=os.path.dirname(os.path.abspath(__file__))
L=[l.split() for l in open(sys.argv[1]) if l.strip()]
def go(a):
    k,u=a; key,cid=k.rsplit('/',1); f=f'{D}/out/{key}/img/{cid}.png'
    r=subprocess.run(['curl','-sS','-X','POST','-H','Content-Type: image/png','--data-binary','@'+f,u],capture_output=True,text=True)
    return k, ('OK' if '"success":true' in r.stdout else r.stdout[:200]+r.stderr[:200])
with cf.ThreadPoolExecutor(8) as ex:
    for k,s in ex.map(go,L):
        if s!='OK': print(k,s)
print('done',len(L))
