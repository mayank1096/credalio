// node shots.js <package dir> <rows.json> <outdir> -> numbered full-page JPGs in flow order (desktop then mobile)
const {chromium}=require('playwright');const http=require('http'),fs=require('fs'),path=require('path');
const [root,rowsF,out]=process.argv.slice(2);fs.mkdirSync(out,{recursive:true});
const rows=JSON.parse(fs.readFileSync(rowsF)).filter(r=>r.kind==='screen');
const ty=f=>f.endsWith('.js')?'text/javascript':f.endsWith('.css')?'text/css':f.endsWith('.woff2')?'font/woff2':f.endsWith('.webp')?'image/webp':f.endsWith('.png')?'image/png':'text/html';
const srv=http.createServer((q,r)=>{const f=path.join(root,decodeURIComponent(q.url.split('?')[0]));fs.readFile(f,(e,d)=>{if(e){r.writeHead(404);r.end();return}r.writeHead(200,{'content-type':ty(f)});r.end(d)})}).listen(8798);
const safe=s=>s.replace(/[\/\\:*?"<>|]/g,'-');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});let i=0,errs=0;const list=[];
for(const r of rows){for(const [file,w,h,lab] of [[r.desk,1440,820,'Desktop'],[r.mob,390,844,'Mobile']]){if(!file)continue;i++;
 const p=await b.newPage({viewport:{width:w,height:h},deviceScaleFactor:w<500?2:1});p.on('pageerror',()=>errs++);
 await p.addInitScript(()=>{document.addEventListener('DOMContentLoaded',()=>{const st=document.createElement('style');st.textContent='*,*::before,*::after{animation:none!important;transition:none!important}';document.head.appendChild(st)})});
 await p.goto('http://localhost:8798/screens/'+file);await p.waitForTimeout(800);
 const id=file.replace('.dc.html','').replace('-Mobile','');const name=String(i).padStart(3,'0')+' '+id+' - '+safe(lab==='Desktop'?r.title.replace(id+' · ',''):'Mobile')+' - '+lab+'.jpg';
 await p.screenshot({path:path.join(out,name),fullPage:true,type:'jpeg',quality:84});list.push({name,sec:r.sec,title:r.title,lab,file});await p.close()}}
fs.writeFileSync(path.join(out,'..','shots.json'),JSON.stringify(list,null,1));
await b.close();srv.close();console.log('shots',i,'errors',errs)})();
