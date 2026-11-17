// node shots.js <package dir> <rows.json> <outdir> [only,boards] -> numbered full-page JPGs in flow order (desktop then mobile)
// Each page is scrolled through first so scroll-revealed content shows, then captured in pieces (so long mobile pages stay 2x)
// and stitched by stitch.py. A pinned scroll story (a full-screen sticky section with a tall track) is shown as one frame
// per step in place of its track, so the book shows the story the way a visitor sees it.
const {chromium}=require('playwright');const http=require('http'),fs=require('fs'),path=require('path'),{execFileSync}=require('child_process');
const [root,rowsF,out]=process.argv.slice(2);fs.mkdirSync(out,{recursive:true});
const only=process.argv[5]?process.argv[5].split(','):null;
const rows=JSON.parse(fs.readFileSync(rowsF)).filter(r=>r.kind==='screen'&&(!only||only.includes(r.desk)));
const ty=f=>f.endsWith('.js')?'text/javascript':f.endsWith('.css')?'text/css':f.endsWith('.woff2')?'font/woff2':f.endsWith('.webp')?'image/webp':f.endsWith('.png')?'image/png':'text/html';
const srv=http.createServer((q,r)=>{const f=path.join(root,decodeURIComponent(q.url.split('?')[0]));fs.readFile(f,(e,d)=>{if(e){r.writeHead(404);r.end();return}r.writeHead(200,{'content-type':ty(f)});r.end(d)})}).listen(8798);
const safe=s=>s.replace(/[\/\\:*?"<>|]/g,'-');
const tmp=path.join(out,'..','frames');const SAMPLES=24,CHUNK=6000;
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});let i=0,errs=0;const list=[];
for(const r of rows){for(const [file,w,h,lab] of [[r.desk,1440,820,'Desktop'],[r.mob,390,844,'Mobile']]){if(!file)continue;i++;
 const id=file.replace('.dc.html','').replace('-Mobile','');const name=String(i).padStart(3,'0')+' '+id+' - '+safe(r.title.replace(id+' · ',''))+' - '+lab+'.jpg';
 if(fs.existsSync(path.join(out,name))){list.push({name,sec:r.sec,title:r.title,lab,file,story:false});continue}
 const dpr=w<500?2:1;const p=await b.newPage({viewport:{width:w,height:h},deviceScaleFactor:dpr});p.on('pageerror',()=>errs++);
 await p.addInitScript(()=>{document.addEventListener('DOMContentLoaded',()=>{const st=document.createElement('style');st.textContent='*,*::before,*::after{animation:none!important;transition:none!important}';document.head.appendChild(st)})});
 await p.goto('http://localhost:8798/screens/'+file);await p.waitForTimeout(800);
 await p.evaluate(async()=>{const H=document.documentElement.scrollHeight;for(let y=0;y<H;y+=500){window.scrollTo(0,y);await new Promise(r=>setTimeout(r,60))}window.scrollTo(0,0)});await p.waitForTimeout(500);
 const H=await p.evaluate(()=>document.documentElement.scrollHeight);
 const story=await p.evaluate(vh=>{for(const e of document.querySelectorAll('*')){const s=getComputedStyle(e);if(s.position!=='sticky'||s.top!=='0px')continue;const ph=e.parentElement.getBoundingClientRect();
   if(e.tagName==='SECTION'&&e.getBoundingClientRect().height>=vh*0.9&&ph.height>vh*1.6&&ph.bottom+scrollY<=document.documentElement.scrollHeight-vh)return {top:Math.round(ph.top+scrollY),h:Math.round(ph.height)}}return null},h);
 fs.rmSync(tmp,{recursive:true,force:true});fs.mkdirSync(tmp,{recursive:true});const chunks=[],frames=[];
 for(let y=0;y<H;y+=CHUNK){const ch=Math.min(CHUNK,H-y);const f=path.join(tmp,'c'+chunks.length+'.png');await p.screenshot({path:f,fullPage:true,clip:{x:0,y,width:w,height:ch}});chunks.push(f)}
 if(story){// story frames with animations on: one frame per stage ("Stage N of M" label), sampled along the track
   const q=await b.newPage({viewport:{width:w,height:h},deviceScaleFactor:dpr});await q.goto('http://localhost:8798/screens/'+file);await q.waitForTimeout(1500);let last=null;
   for(let k=0;k<=SAMPLES;k++){const s=story.top+Math.round(k*(story.h-h)/SAMPLES);await q.evaluate(s=>window.scrollTo(0,s),s);await q.waitForTimeout(400);
    const st=await q.evaluate(()=>{const m=[...document.querySelectorAll('section')].find(e=>getComputedStyle(e).position==='sticky'&&getComputedStyle(e).top==='0px');const x=m&&m.innerText.match(/Stage (\d+) of (\d+)/);return x?x[1]:String(Math.random())});
    if(st===last)continue;last=st;await q.waitForTimeout(1200);const f=path.join(tmp,'f'+frames.length+'.png');await q.screenshot({path:f});frames.push(f)}
   await q.close()}
 fs.writeFileSync(path.join(tmp,'meta.json'),JSON.stringify({chunks,frames,story,dpr,H}));
 execFileSync('python3',[path.join(__dirname,'stitch.py'),path.join(tmp,'meta.json'),path.join(out,name)]);
 list.push({name,sec:r.sec,title:r.title,lab,file,story:!!story});await p.close()}}
fs.writeFileSync(path.join(out,'..','shots.json'),JSON.stringify(list,null,1));
await b.close();srv.close();console.log('shots',i,'errors',errs,'stories',list.filter(x=>x.story).map(x=>x.file).join(' '))})();
