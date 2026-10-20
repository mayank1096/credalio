// node coins.js <root> name:WxH ... -> amounts in Creio/Credits shown without a coin nearby
const {chromium}=require('playwright');const http=require('http'),fs=require('fs'),path=require('path');
const root=process.argv[2];const L=process.argv.slice(3).map(a=>a.split(':'));
const ty=f=>f.endsWith('.js')?'text/javascript':f.endsWith('.css')?'text/css':f.endsWith('.woff2')?'font/woff2':'text/html';
const srv=http.createServer((q,r)=>{const f=path.join(root,decodeURIComponent(q.url.split('?')[0]));fs.readFile(f,(e,d)=>{if(e){r.writeHead(404);r.end();return}r.writeHead(200,{'content-type':ty(f)});r.end(d)})}).listen(8796);
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
for(const [f,wh] of L){const[w,h]=wh.split('x').map(Number);const pg=await b.newPage({viewport:{width:w,height:h}});
 try{await pg.goto('http://localhost:8796/'+f+'.dc.html');await pg.waitForTimeout(900);
 const out=await pg.evaluate(()=>{const res=[];
  const vis=e=>{let p=e;while(p&&p!==document.body){const c=getComputedStyle(p);if(c.display==='none'||c.visibility==='hidden')return false;p=p.parentElement}const r=e.getBoundingClientRect();return r.width>0};
  const coins=[...document.querySelectorAll('svg,img,[class*=coin],[class*=cr-ic],[class*=wf-c],[class*=cb-cn],[class*=cb-c]')].filter(vis).map(e=>e.getBoundingClientRect()).filter(r=>r.width>=12&&r.width<=48&&Math.abs(r.width-r.height)<4);
  for(const e of document.querySelectorAll('body *')){let t='';for(const n of e.childNodes)if(n.nodeType===3)t+=n.textContent;t=t.trim();
   if(!/^[+−-]?\$?\d{1,3}(,\d{3})+$|^[+−-]?\d{3,}$/.test(t)&&!/^[+−-]?[\d,]{3,}\s*(Creio|Credits|Cr)$/.test(t))continue;
   if(!vis(e))continue;
   const ctx=(e.parentElement.innerText+' '+(e.parentElement.parentElement||e).innerText).slice(0,300);
   if(!/Creio|Credit|\bCr\b/.test(ctx+getComputedStyle(e,'::after').content))continue;
   if(t.startsWith('$'))continue;
   const r=e.getBoundingClientRect();const near=coins.some(c=>Math.abs((c.top+c.bottom)/2-(r.top+r.bottom)/2)<Math.max(r.height,c.height)&&c.left<r.right&&r.left-c.right<60);
   if(!near)res.push(t+' «'+e.parentElement.innerText.replace(/\s+/g,' ').slice(0,50)+'»')}
  return res});
 if(out.length)console.log('## '+f+'\n'+out.map(x=>'  '+x).join('\n'))}catch(e){console.log('ERR '+f)}
 await pg.close()}
await b.close();srv.close()})();
