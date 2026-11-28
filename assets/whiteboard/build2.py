import json,sys
spec=json.load(open(sys.argv[1],encoding='utf-8'))
s=open('wb2.html',encoding='utf-8').read().replace('__SPEC__',json.dumps(spec,ensure_ascii=False))
open(sys.argv[2],'w',encoding='utf-8').write(s)
