#寻找100以内质数
#在一般领域，对正整数n，如果用2到根号n之间的所有整数去除，均无法整除，则n为质数。
from math import sqrt
def sushu():
    sushulist=[2,3]
    for n in range (5,100):
        for i in range (2,int(sqrt(n)+1)):
            if n%i==0:
                break
        else:
            sushulist.append(n)
    print(sushulist)
sushu()
