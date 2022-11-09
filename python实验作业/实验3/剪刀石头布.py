import random   #引入随机数模块
user=''
def caiquan(a):  #自定义函数，将最后电脑随机出拳输出由数字变成汉字
    if a==0:
        return "剪刀"
    elif a==1:
        return "石头"
    elif a==2:
        return "布"
while user!=-1:  #使该游戏成为一个死循环
    slist1=[0,1,2]
    userwin=[[1,0],[0,2],[2,1]]  #用列表形式声明用户获胜条件
    pc=random.choice(slist1)  #令程序随机“出拳”
    user=int(input('请输入0，1，2中的一个数(0为剪刀，1为石头，2为布）(输入-1则退出)'))   #获取用户输入
    if user==pc:  #平局条件判断
        print('平局')
        print('系统出的是:',caiquan(pc))
    elif [user,pc] in userwin:   #将程序出拳和用户出拳也变为列表形式，直接在slist1中判断是否获胜
        print('你赢了')
        print('系统出的是:',caiquan(pc))
    else:   #用户输，进行如下语句
        print('你输了')
        print('系统出的是:',caiquan(pc))

