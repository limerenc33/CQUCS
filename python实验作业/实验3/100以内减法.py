import random   #引入随机数模块
import time   #引入时间模块
number=0   #设定循环（出题）次数
correct=0  #设定对题数
start=time.time()  #获取开始时间
while number<5:   #用while语句进行循环次数（出题数）的限定
    beijian=random.randint(0,101)  #随机选取被减数
    jian=random.randint(0,100)   #随机选取减数
    if beijian>=jian:   #判断被减数是否大于减数
        result=str(beijian-jian)  #由系统求出正确结果
        answer=input('{0:d}-{1:d}='.format(beijian,jian))  #获取用户输入的答案
        if result==answer:   #若答案正确，执行如下语句
            print('正确')
            correct+=1  #对题数+1
        else:  #假如结果不对，则执行下列语句
            print('错误')
        number+=1  #每执行一次循环，循环数就+1
end=time.time()   #获取结束时间
print('答对次数:{}'.format(correct))
print('答题时间:',int(end-start),'秒')
