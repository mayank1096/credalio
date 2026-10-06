const page=await figma.getNodeByIdAsync(PG);await figma.setCurrentPageAsync(page);
const FAM='Google Sans Flex',WS={300:'Light',400:'Regular',500:'Medium',600:'SemiBold',700:'Bold',800:'ExtraBold'};
const sty=(w,i)=>{let s=WS[w]||(w>=650?'Bold':w>=550?'SemiBold':w>=450?'Medium':'Regular');return i?(s==='Regular'?'Italic':s+' Italic'):s};
await Promise.all(FONTS.map(s=>figma.loadFontAsync({family:FAM,style:s})));
const vm={};const cols={};
for(const v of await figma.variables.getLocalVariablesAsync('COLOR')){let c=cols[v.variableCollectionId];if(!c){c=await figma.variables.getVariableCollectionByIdAsync(v.variableCollectionId);cols[v.variableCollectionId]=c}
let val=v.valuesByMode[c.defaultModeId],g=0;while(val&&val.type==='VARIABLE_ALIAS'&&g++<5){const t=await figma.variables.getVariableByIdAsync(val.id);val=Object.values(t.valuesByMode)[0]}
if(val&&'r' in val&&(val.a===undefined||val.a>0.99)){const h=[val.r,val.g,val.b].map(x=>Math.round(x*255).toString(16).padStart(2,'0')).join('');if(!vm[h]||c.name==='Color')vm[h]=v}}
const rgb=h=>({r:parseInt(h.slice(0,2),16)/255,g:parseInt(h.slice(2,4),16)/255,b:parseInt(h.slice(4,6),16)/255});
const al=h=>h.length>6?parseInt(h.slice(6,8),16)/255:1;
const paint=h=>{let p={type:'SOLID',color:rgb(h),opacity:al(h)};if(h.length===6&&vm[h])p=figma.variables.setBoundVariableForPaint(p,'color',vm[h]);return p};
function fill(f,w,h){if(typeof f==='string')return paint(f);const[,x0,y0,x1,y1,st]=f;const dx=x1-x0,dy=y1-y0,nx=-dy*h/w,ny=dx*w/h;
const a=dx,b=nx,c=x0-0.5*nx,d=dy,e=ny,f2=y0-0.5*ny,det=a*e-b*d||1e-6;
const T=[[e/det,-b/det,(b*f2-e*c)/det],[-d/det,a/det,(d*c-a*f2)/det]];
return{type:'GRADIENT_LINEAR',gradientTransform:T,gradientStops:st.map(s=>({color:{...rgb(s[0]),a:al(s[0])},position:Math.max(0,Math.min(1,s[1]))}))}}
const PH=[{type:'SOLID',color:{r:.93,g:.945,b:.97}}];
const svgs=typeof SV!=='undefined'?SV:[];
const imgs={};
function place(n,p,pr,x,y,inAL){p.appendChild(n);if(inAL){if(pr.a){n.layoutPositioning='ABSOLUTE';n.x=x;n.y=y}}else{n.x=x;n.y=y}}
function sizing(n,p,pr,k){if(!p.layoutMode||p.layoutMode==='NONE'||pr.a)return;const H=p.layoutMode==='HORIZONTAL';
if(pr.fc){if(H)n.layoutSizingVertical='FILL';else n.layoutSizingHorizontal='FILL'}
if(pr.fm){if(H)n.layoutSizingHorizontal='FILL';else n.layoutSizingVertical='FILL'}}
function mk(p,N){const[k,name,x,y,w,h,pr,ch]=N;const inAL=!!(p&&p.layoutMode&&p.layoutMode!=='NONE');let n;
if(k==='T'){const t=pr.t;n=figma.createText();n.fontName={family:FAM,style:sty(t.w,t.i)};n.characters=t.s;n.fontSize=t.z;n.fills=[paint(t.c)];
if(t.lh)n.lineHeight={unit:'PIXELS',value:t.lh};if(t.ls)n.letterSpacing={unit:'PIXELS',value:t.ls};
if(t.al)n.textAlignHorizontal=t.al==='C'?'CENTER':t.al==='R'?'RIGHT':'JUSTIFIED';if(t.d)n.textDecoration=t.d===1?'UNDERLINE':'STRIKETHROUGH';
if(t.r)for(const[s,e,x2]of t.r){if(e<=s)continue;if(x2.w||x2.i!==undefined)n.setRangeFontName(s,e,{family:FAM,style:sty(x2.w||t.w,x2.i!==undefined?x2.i:t.i)});if(x2.c)n.setRangeFills(s,e,[paint(x2.c)]);if(x2.z)n.setRangeFontSize(s,e,x2.z);if(x2.d)n.setRangeTextDecoration(s,e,x2.d===1?'UNDERLINE':'STRIKETHROUGH')}
n.name=name;
if(t.ml){n.resize(Math.max(1,w),Math.max(1,h));n.textAutoResize='HEIGHT'}else n.textAutoResize='WIDTH_AND_HEIGHT';
let xx=x;if(!t.ml&&!inAL){if(t.al==='C')xx=x+(w-n.width)/2;else if(t.al==='R')xx=x+w-n.width}
place(n,p,pr,xx,y,inAL);sizing(n,p,pr,k);return n}
if(k==='S'){const s=typeof pr.v==='number'?svgs[pr.v]:pr.v;try{n=figma.createNodeFromSvg(s)}catch(e){n=figma.createFrame();n.fills=[]}n.name=name;n.clipsContent=false;n.resize(Math.max(.01,w),Math.max(.01,h));place(n,p,pr,x,y,inAL);return n}
if(k==='I'){n=figma.createRectangle();n.name=name;n.resize(Math.max(.01,w),Math.max(.01,h));n.fills=PH;n.setSharedPluginData('crd','img',KEY+'/'+pr.i);imgs[pr.i]=n.id;if(pr.bm)n.blendMode=pr.bm.toUpperCase().replace(/-/g,'_');place(n,p,pr,x,y,inAL);sizing(n,p,pr,k);return n}
n=figma.createFrame();n.name=name;n.fills=pr.b?pr.b.map(f=>fill(f,w,h)):[];n.clipsContent=!!pr.c;
if(pr.r!=null){if(Array.isArray(pr.r)){n.topLeftRadius=pr.r[0];n.topRightRadius=pr.r[1];n.bottomRightRadius=pr.r[2];n.bottomLeftRadius=pr.r[3]}else n.cornerRadius=pr.r}
if(pr.s){const[c,sw,ds]=pr.s;n.strokes=[paint(c)];n.strokeAlign='INSIDE';if(Array.isArray(sw)){n.strokeTopWeight=sw[0];n.strokeRightWeight=sw[1];n.strokeBottomWeight=sw[2];n.strokeLeftWeight=sw[3]}else n.strokeWeight=sw;if(ds)n.dashPattern=ds===1?[5,4]:[1.5,3]}
if(pr.e)n.effects=pr.e.map(([i,ex,ey,bl,sp,c])=>({type:i?'INNER_SHADOW':'DROP_SHADOW',color:{...rgb(c),a:al(c)},offset:{x:ex,y:ey},radius:bl,spread:sp,visible:true,blendMode:'NORMAL'}));
if(pr.o)n.opacity=pr.o;
if(pr.l){const[d,g,pd,pa,ca]=pr.l;n.layoutMode=d==='H'?'HORIZONTAL':'VERTICAL';n.primaryAxisSizingMode='FIXED';n.counterAxisSizingMode='FIXED';n.itemSpacing=g;n.paddingTop=pd[0];n.paddingRight=pd[1];n.paddingBottom=pd[2];n.paddingLeft=pd[3];n.primaryAxisAlignItems=pa==='SB'?'SPACE_BETWEEN':pa;n.counterAxisAlignItems=ca}
n.resize(Math.max(.01,w),Math.max(.01,h));
if(p)place(n,p,pr,x,y,inAL);if(p)sizing(n,p,pr,k);
if(pr.si){const[id,sx,sy,sw2,sh]=pr.si;const r=figma.createRectangle();r.name='background';r.resize(Math.max(.01,sw2),Math.max(.01,sh));r.fills=PH;r.setSharedPluginData('crd','img',KEY+'/'+id);imgs[id]=r.id;n.appendChild(r);if(pr.l)r.layoutPositioning='ABSOLUTE';r.x=sx;r.y=sy;r.locked=false}
if(ch)for(const c of ch)mk(n,c);
return n}
let target;
if(JOB.root){const old=page.children.filter(c=>c.name===NAME);old.forEach(o=>o.remove());
const N=JOB.root;const r=mk(null,N);page.appendChild(r);r.x=POS[0];r.y=POS[1];r.name=NAME;r.clipsContent=true;target=r}
else{let t=page.children.find(c=>c.name===NAME);if(!t)throw new Error('root missing');for(const i of JOB.path)t=t.children[i];
while(t.children.length>JOB.start)t.children[t.children.length-1].remove();for(const c of JOB.nodes)mk(t,c);target=t}
return {ok:true,id:target.id,imgs};
