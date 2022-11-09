import random
dongkou=[0]*5
user=''
while user!=-1:
    weizhi=random.randint(0,4)
    dongkou[weizhi]=1
    user=int(input('请选取0-4号洞口其中一个(输入-1则退出游戏)'))
    if dongkou[user]==1:
        print('你真厉害')
        break
    else:
        print('没抓到狐狸噢，明天再来试试吧')
        xinweizhi=random.randint(0,4)
        dongkou[xinweizhi]=1