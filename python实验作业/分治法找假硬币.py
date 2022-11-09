#falsecoin.py
from math import floor
def findfalsecoin(coins,start,n):  #在coin列表中下标start开始的n个硬币中查找假硬币
    if n==1:
        return start #查找范围里只剩下一枚硬币，直接返回下标
    nhalf=floor(n/2.0) #nhalf为硬币数量的一半，下取整
    wl=sum(coins[start:start+nhalf]) #左：start下标开始的nhalf个硬币总重量
    wr=sum(coins[start+nhalf:start+nhalf+nhalf]) #右：另外nhalf个硬币总重量
    