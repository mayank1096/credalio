const {chromium}=require('playwright');const http=require('http'),fs=require('fs'),path=require('path');
const [root,page,out,land]=process.argv.slice(2);
const ty=f=>f.endsWith('.woff2')?'font/woff2':f.endsWith('.png')?'image/png':f.endsWith('.jpg')?'image/jpeg':f.endsWith('.webp')?'image/webp':'text/html';
const srv=http.createServer((q,r)=>{const f=path.join(root,decodeURIComponent(q.url.split('?')[0]));fs.readFile(f,(e,d)=>{if(e){r.writeHead(404);r.end();return}r.writeHead(200,{'content-type':ty(f)});r.end(d)})}).listen(8799);
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});const p=await b.newPage();let bad=0;p.on('response',r=>{if(r.status()>=400){bad++;console.log('404',r.url())}});
await p.goto('http://localhost:8799/'+page,{waitUntil:'networkidle',timeout:300000});await p.evaluate(()=>document.fonts.ready);
await p.pdf({path:out,format:'A4',landscape:land==='l',printBackground:true,preferCSSPageSize:true});await b.close();srv.close();console.log('pdf ok, missing',bad)})();
