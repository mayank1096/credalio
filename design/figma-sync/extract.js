// usage: node extract.js <renderDir> <outDir> board:WxH ...
const {chromium}=require('playwright');const fs=require('fs'),path=require('path');
const root=process.argv[2], out=process.argv[3]; const srv=require('./srv.js')(root,8772);
const fontCss=fs.readFileSync(__dirname+'/fonts/gs.css','utf8'); const fmap={}; for(const l of fs.readFileSync(__dirname+'/fonts/map.txt','utf8').trim().split('\n')){const [u,f]=l.split(' ');fmap[u]=f;}
const SER=fs.readFileSync(__dirname+'/ser.js','utf8');
const CAPCSS=`html.__cap,html.__cap body{background:transparent!important}html.__cap *{visibility:hidden!important;transition:none!important;caret-color:transparent!important}html.__cap .__tt,html.__cap .__tt *{visibility:visible!important}html.__cap .__t{visibility:visible!important;-webkit-text-fill-color:transparent!important}html.__cap .__t::before,html.__cap .__t::after{-webkit-text-fill-color:initial!important}`;
(async()=>{const b=await chromium.launch();
for(const spec of process.argv.slice(4)){const [file,wh]=spec.split(':');const [w,h]=wh.split('x').map(Number);const name=file.replace('.dc.html','')+'@'+w;
 const pg=await b.newPage({viewport:{width:w,height:h},deviceScaleFactor:2});
 await pg.route(/fonts\.googleapis\.com/,r=>r.fulfill({body:fontCss,contentType:'text/css'}));
 await pg.route(/fonts\.gstatic\.com/,r=>{const f=fmap[r.request().url()];f?r.fulfill({body:fs.readFileSync(__dirname+'/fonts/'+f),contentType:'font/woff2'}):r.abort();});
 const errs=[];pg.on('pageerror',e=>errs.push(e.message));
 await pg.goto('http://localhost:8772/'+file);await pg.waitForTimeout(+process.env.WAIT||4500);
 await pg.evaluate(()=>document.fonts.ready);
 await pg.evaluate(()=>{for(const a of document.getAnimations()){try{const t=a.effect.getComputedTiming();if(t.iterations===Infinity){a.pause();a.currentTime=0;}else a.finish();}catch(e){}}});
 await pg.waitForTimeout(300);
 const d=await pg.evaluate(SER);
 const dir=path.join(out,name);fs.mkdirSync(dir,{recursive:true});
 await pg.screenshot({path:path.join(dir,'_full.png')});
 await pg.addStyleTag({content:CAPCSS});
 for(const c of d.caps){
  const box=await pg.evaluate(([id,mode])=>{const el=document.querySelector(`[data-cap="${id}"]`);document.documentElement.classList.add('__cap');el.classList.add(mode==='self'?'__t':'__tt');const r=el.getBoundingClientRect();return [r.left,r.top,r.width,r.height];},[c.id,c.mode]);
  const pad=120; const x=Math.max(0,box[0]-pad),y=Math.max(0,box[1]-pad); const x2=Math.min(w,box[0]+box[2]+pad), y2=Math.min(h,box[1]+box[3]+pad);
  if(x2-x>=1&&y2-y>=1){await pg.screenshot({path:path.join(dir,c.id+'.png'),clip:{x,y,width:x2-x,height:y2-y},omitBackground:true});c.clip=[x,y];}
  await pg.evaluate(([id])=>{const el=document.querySelector(`[data-cap="${id}"]`);el.classList.remove('__t','__tt');document.documentElement.classList.remove('__cap');},[c.id]);
 }
 fs.writeFileSync(path.join(dir,'tree.json'),JSON.stringify({w,h,root:d.root,caps:d.caps}));
 console.log(name,'caps',d.caps.length,'bytes',JSON.stringify(d.root).length,errs.slice(0,1).join(''));
 await pg.close();}
await b.close();srv.close();})();
