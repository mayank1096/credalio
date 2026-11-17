const {chromium}=require('playwright');const http=require('http'),fs=require('fs'),path=require('path');
const root=process.argv[2];
const ty=f=>f.endsWith('.js')?'text/javascript':f.endsWith('.css')?'text/css':f.endsWith('.woff2')?'font/woff2':f.endsWith('.webp')?'image/webp':f.endsWith('.png')?'image/png':'text/html';
const srv=http.createServer((q,r)=>{const f=path.join(root,decodeURIComponent(q.url.split('?')[0]));fs.readFile(f,(e,d)=>{if(e){r.writeHead(404);r.end();return}r.writeHead(200,{'content-type':ty(f)});r.end(d)})}).listen(8797);
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});const fails=new Set();let errs=0,n=0;
const files=fs.readdirSync(path.join(root,'screens')).filter(f=>f.endsWith('.dc.html'));
for(const f of ['../index.html',...files]){const p=await b.newPage({viewport:{width:1440,height:900}});
 p.on('response',r=>{if(r.status()>=400)fails.add(r.url())});p.on('requestfailed',r=>fails.add(r.url()));p.on('pageerror',e=>{errs++;console.log(f,e.message)});
 await p.goto('http://localhost:8797/screens/'+f);await p.waitForTimeout(f.includes('index')?300:700);
 const broken=await p.evaluate(()=>[...document.images].filter(i=>i.complete&&i.naturalWidth===0).map(i=>i.src));broken.forEach(u=>fails.add(u));n++;await p.close()}
await b.close();srv.close();console.log('pages',n,'errors',errs,'failed requests',fails.size);[...fails].slice(0,10).forEach(u=>console.log(u))})();
