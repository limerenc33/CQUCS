slist=[]
for i in range(11,100000):
    a=str(i)
    b=a[::-1]
    c=int(b)
    if c==i:
     slist.append(i)
print(slist)

