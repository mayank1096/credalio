import os,sys
from PIL import Image, ImageChops, ImageStat
res=[]
for f in sorted(os.listdir('cmp')):
    k=f[:-4]
    if not os.path.exists(f'out/{k}/_full.png'): continue
    w=Image.open(f'out/{k}/_full.png').convert('L'); g=Image.open(f'cmp/{f}').convert('L')
    sz=(w.width//8,w.height//8); w=w.resize(sz); g=g.resize(sz)
    d=ImageChops.difference(w,g); res.append((round(ImageStat.Stat(d).mean[0],2),k))
for s,k in sorted(res,reverse=True): print(s,k)
