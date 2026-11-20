import json,sys
words=json.load(open(sys.argv[1])); total=float(sys.argv[2])
s=open('wb.html',encoding='utf-8').read().replace('__WORDS__',json.dumps(words,ensure_ascii=False)).replace('__TOTAL__',str(total))
open('wb_build.html','w',encoding='utf-8').write(s)
