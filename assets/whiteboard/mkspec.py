import json,sys
# usage: mkspec.py out.json words.tsv total scenes.json
words=[]
for l in open(sys.argv[2],encoding='utf-8'):
    l=l.strip()
    if not l: continue
    t,a,b=l.split('|'); words.append({"text":t,"start":float(a),"end":float(b)})
scenes=json.load(open(sys.argv[4],encoding='utf-8'))
json.dump({"words":words,"total":float(sys.argv[3]),"scenes":scenes},open(sys.argv[1],'w',encoding='utf-8'),ensure_ascii=False)
