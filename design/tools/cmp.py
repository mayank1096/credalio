import sys,os
from PIL import Image,ImageChops
bad=[]
for b,a in [('b1','a1'),('b2','a2')]:
    for f in sorted(os.listdir(b)):
        if not f.endswith('.png'): continue
        x=Image.open(f'{b}/{f}').convert('RGB');y=Image.open(f'{a}/{f}').convert('RGB')
        if x.size!=y.size: bad.append((b,f,'size',x.size,y.size));continue
        d=ImageChops.difference(x,y);bb=d.getbbox()
        if bb:
            px=sum(1 for p in d.getdata() if max(p)>24)
            bad.append((b,f,bb,px))
print(len(bad));[print(r) for r in bad]
