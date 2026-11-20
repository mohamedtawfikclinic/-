const { chromium } = require('playwright'); const path=require('path'); const fs=require('fs');
(async()=>{ const [,,html,out,times,fps,total]=process.argv; fs.mkdirSync(out,{recursive:true});
 const b=await chromium.launch(); const p=await b.newPage({viewport:{width:1080,height:1920}});
 await p.goto('file://'+path.resolve(html)); await p.evaluate(()=>window.ready); await p.waitForTimeout(200);
 const ts= times!=='all' ? times.split(',').map(Number) : [...Array(Math.round(+total*+fps)).keys()].map(i=>i/+fps);
 for(let i=0;i<ts.length;i++){ await p.evaluate(t=>window.render(t),ts[i]);
   await p.screenshot({path:path.join(out, times!=='all'?`t${ts[i]}.jpg`:`f_${String(i).padStart(5,'0')}.jpg`),type:'jpeg',quality:92}); }
 await b.close(); })();
