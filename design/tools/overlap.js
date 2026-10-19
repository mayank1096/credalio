// node overlap.js <root> name:WxH ...  -> text overlapping text, icons or halos overlapping text (render QA)
const {chromium}=require('playwright');const http=require('http'),fs=require('fs'),path=require('path');
const root=process.argv[2];const L=process.argv.slice(3).map(a=>a.split(':'));
const ty=f=>f.endsWith('.js')?'text/javascript':f.endsWith('.css')?'text/css':f.endsWith('.woff2')?'font/woff2':'text/html';
const srv=http.createServer((q,r)=>{const f=path.join(root,decodeURIComponent(q.url.split('?')[0]));fs.readFile(f,(e,d)=>{if(e){r.writeHead(404);r.end();return}r.writeHead(200,{'content-type':ty(f)});r.end(d)})}).listen(8792);
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'}).catch(()=>chromium.launch());
for(const [f,wh] of L){const[w,h]=wh.split('x').map(Number);const ctx=await b.newContext({viewport:{width:w,height:h}});const pg=await ctx.newPage();
 await pg.addInitScript(()=>{document.addEventListener('DOMContentLoaded',()=>{const st=document.createElement('style');st.textContent='*,*::before,*::after{animation:none!important;transition:none!important}';document.head.appendChild(st)})});
 try{await pg.goto('http://localhost:8792/'+f+'.dc.html');await pg.waitForTimeout(1200);
 const out=await pg.evaluate(()=>{
  const vis=e=>{const s=getComputedStyle(e);if(s.visibility==='hidden'||s.display==='none'||+s.opacity===0)return false;let p=e;while(p&&p!==document.body){const c=getComputedStyle(p);if(c.display==='none'||c.visibility==='hidden'||+c.opacity===0)return false;p=p.parentElement}const r=e.getBoundingClientRect();return r.width>0&&r.height>0};
  const name=e=>(e.tagName.toLowerCase()+(e.className&&typeof e.className==='string'?'.'+e.className.trim().split(/\s+/).slice(0,2).join('.'):''));
  const txt=e=>{let t='';for(const n of e.childNodes)if(n.nodeType===3)t+=n.textContent;return t.trim()};
  const all=[...document.querySelectorAll('body *')].filter(e=>!e.closest('svg')||e.tagName==='svg');
  // text boxes via ranges (tight)
  const T=[];for(const e of all){const t=txt(e);if(!t||!vis(e)||e.closest('.sr-only,[role=tooltip],.po-tip'))continue;for(const n of e.childNodes){if(n.nodeType!==3||!n.textContent.trim())continue;const rg=document.createRange();rg.selectNodeContents(n);for(const r of rg.getClientRects()){if(r.width>1&&r.height>1)T.push({e,r,t:t.slice(0,30)})}}}
  const I=[];for(const e of all){if(!vis(e))continue;const s=getComputedStyle(e);const r=e.getBoundingClientRect();
    let sp=0;const m=s.boxShadow.match(/0px 0px 0px (\d+(?:\.\d+)?)px/);if(m)sp=+m[1];
    const isIcon=e.tagName==='svg'||e.tagName==='IMG'||(sp>0&&r.width<120&&r.height<120);
    if(isIcon&&r.width>=8&&r.width<200)I.push({e,r:{left:r.left-sp,right:r.right+sp,top:r.top-sp,bottom:r.bottom+sp},sp})}
  const ovw=(a,b)=>Math.min(Math.min(a.right,b.right)-Math.max(a.left,b.left),Math.min(a.bottom,b.bottom)-Math.max(a.top,b.top));const ov=(a,b,pad=0)=>ovw(a,b)>pad;const box=(a,b)=>[Math.max(0,Math.min(a.left,b.left)-30),Math.max(0,Math.min(a.top,b.top)-30),Math.max(a.right,b.right)+30,Math.max(a.bottom,b.bottom)+30].map(Math.round).join(',');
  const rel=(a,b)=>a.contains(b)||b.contains(a);
  const fixedish=e=>{let p=e;while(p&&p!==document.body){const c=getComputedStyle(p).position;if(c==='fixed'||c==='sticky')return true;p=p.parentElement}return false};
  const res=new Set();
  for(let i=0;i<T.length;i++)for(let j=i+1;j<T.length;j++){const a=T[i],b=T[j];if(a.e===b.e||rel(a.e,b.e))continue;if(fixedish(a.e)!==fixedish(b.e))continue;if(ov(a.r,b.r,4))res.add(Math.round(ovw(a.r,b.r))+'px @'+box(a.r,b.r)+' TEXT/TEXT "'+a.t+'" ['+name(a.e)+'] x "'+b.t+'" ['+name(b.e)+']')}
  for(const ic of I)for(const t of T){if(rel(ic.e,t.e)||ic.e.parentElement&&ic.e.parentElement.contains(t.e)&&ic.e.parentElement===t.e)continue;if(fixedish(ic.e)!==fixedish(t.e))continue;if(ov(ic.r,t.r,3))res.add(Math.round(ovw(ic.r,t.r))+'px @'+box(ic.r,t.r)+' '+(ic.sp?'HALO':'ICON')+'/TEXT ['+name(ic.e)+'] x "'+t.t+'" ['+name(t.e)+']')}
  return [...res]});
 if(out.length)console.log('## '+f+'\n'+out.map(x=>'  '+x).join('\n'));}catch(e){console.log('ERR '+f+' '+e.message)}
 await ctx.close()}
await b.close();srv.close()})();
