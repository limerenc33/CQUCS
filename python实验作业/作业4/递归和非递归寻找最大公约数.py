#递归求最大公约数
def gcd(a,b):
    while b!=0:
        temp=max(a,b)%min(a,b)
        if temp==0:
            return min(a,b)
        else:
            return(gcd(temp,min(a,b)))
print(gcd(120,44))


#非递归求最大公约数
def gcd (a,b):
    while a!=0 and b!=0:
        if a>b:
            a,b=b,a
        if b%a==0:
            return a
        gcdlist=[]
        for i in range (1,a):
            if b%i==0 and a%i==0:
                gcdlist.append(i)
        return max(gcdlist)
print(gcd(125,55))
    
    