// node renderall.js <root> <outdir> <listfile: name WxH per line>
const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
const FG=process.env.FG;const srv=require(FG+'/srv.js')(process.argv[2],+process.env.PORT||8790);
const css=fs.readFileSync(FG+'/fonts/gs.css','utf8');const fm={};for(const l of fs.readFileSync(FG+'/fonts/map.txt','utf8').trim().split('\n')){const[u,f]=l.split(' ');fm[u]=f}
const out=process.argv[3];fs.mkdirSync(out,{recursive:true});
const L=fs.readFileSync(process.argv[4],'utf8').trim().split('\n').map(l=>l.split(' '));
(async()=>{const b=await chromium.launch();let i=0;const errs=[];
async function worker(){while(i<L.length){const [f,wh]=L[i++];const[w,h]=wh.split('x').map(Number);
 const ctx=await b.newContext({viewport:{width:w,height:h}});const pg=await ctx.newPage();
 await pg.addInitScript(()=>{let s=42;Math.random=()=>{s=(s*1103515245+12345)%2147483648;return s/2147483648};
   document.addEventListener('DOMContentLoaded',()=>{const st=document.createElement('style');st.textContent='*,*::before,*::after{animation:none!important;transition:none!important;caret-color:transparent!important}';document.head.appendChild(st)})});
 pg.on('pageerror',e=>errs.push(f+': '+e.message));
 await pg.route(/fonts\.googleapis/,r=>r.fulfill({body:css,contentType:'text/css'}));await pg.route(/fonts\.gstatic/,r=>{const x=fm[r.request().url()];x?r.fulfill({body:fs.readFileSync(FG+'/fonts/'+x)}):r.abort()});
 try{await pg.goto('http://localhost:'+(process.env.PORT||8790)+'/'+f);await pg.waitForTimeout(1800);
 await pg.addStyleTag({content:'*,*::before,*::after{animation:none!important;transition:none!important}'});await pg.waitForTimeout(200);
 await pg.screenshot({path:path.join(out,f.replace('.dc.html','.png')),fullPage:false});}catch(e){errs.push(f+': '+e.message)}
 await ctx.close()}}
await Promise.all([worker(),worker(),worker(),worker()]);await b.close();srv.close();fs.writeFileSync(path.join(out,'_errors.txt'),errs.join('\n'));console.log('done',L.length,'errors',errs.length)})();
