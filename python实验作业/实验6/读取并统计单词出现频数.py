def getText():
    txt=open("poem.txt","r").read()
    txt=txt.lower()
    for ch in '~!@#$%^&*()_+"{}[]|?.<>?':
        txt=txt.replace(ch,"")
    return txt
Txt=getText()
words=Txt.split()
counts={}
for word in words:
    counts[word]=counts.get(word,0)+1
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range (len(items)): 
    word,count=items[i]
    print(word,count)



