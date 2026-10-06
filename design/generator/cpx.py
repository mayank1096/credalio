B={'Nova':'b8f0756720795e1bd3b02e9c2655cb25','Maya':'0539eaee91dd97c09ad321718b4b2947','Alex':'180b8d793cf8025b7bf4a7efeb6da0a2','Sage':'e77858d41b6ddf496fcf2ad82ab9d64a'}
W,H=941,1672
STAGE={'Nova':(150,150,610),'Maya':(90,360,760),'Alex':(80,360,760),'Sage':(90,360,760)}
HEAD={'Nova':(440,345,320),'Maya':(475,620,400),'Alex':(455,600,370),'Sage':(465,610,370)}
def stage(n):
    x,y,w=STAGE[n]; h=w*530/375
    return dict(l=f'{-x/w*100:.2f}%',t=f'{-y/h*100:.2f}%',w=f'{W/w*100:.2f}%')
def head(n):
    cx,cy,s=HEAD[n]
    return dict(l=f'{-(cx-s/2)/s*100:.2f}%',t=f'{-(cy-s/2)/s*100:.2f}%',w=f'{W/s*100:.2f}%')
if __name__=='__main__':
    o='<html><body style="margin:0;padding:20px;display:flex;gap:20px;flex-wrap:wrap">'
    for n in B:
        a=stage(n); o+=f'<div style="position:relative;width:230px;aspect-ratio:375/530;overflow:hidden;outline:1px solid red"><img src="_blob/{B[n]}" style="position:absolute;left:{a["l"]};top:{a["t"]};width:{a["w"]};max-width:none"></div>'
    for n in B:
        a=head(n); o+=f'<div style="position:relative;width:120px;height:120px;border-radius:50%;overflow:hidden;background:#EAF0FF"><img src="_blob/{B[n]}" style="position:absolute;left:{a["l"]};top:{a["t"]};width:{a["w"]};max-width:none;mix-blend-mode:multiply"></div>'
    open('c/croptest.html','w').write(o)
