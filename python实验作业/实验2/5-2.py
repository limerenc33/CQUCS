value=b'\x45'
value1=int.from_bytes(value,'little')
value2=bin(value1)
slist=list(value2)
slist1=[]
for i in slist:
    if i=='0':
       slist1.append(False)
    elif i=='1':
       slist1.append(True)
print(slist1)