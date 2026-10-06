const http=require('http'),fs=require('fs'),path=require('path');
module.exports=(root,port)=>http.createServer((q,r)=>{const f=path.join(root,decodeURIComponent(q.url.split('?')[0]));fs.readFile(f,(e,d)=>{if(e){r.writeHead(404);r.end();return;}r.writeHead(200,{'content-type':f.endsWith('.js')?'text/javascript':(f.includes('_blob')?'image/webp':'text/html')});r.end(d);});}).listen(port);
