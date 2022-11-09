import random  #引入随机数模块
a=random.randint(100,1000)   #随机产生一个三位数
print(a)
b=int(input('请输入一个三位数:'))   #获取用户输入的三位数
slist1=list(str(a))    #下面2行分别将2个三位数变成列表形式，以便于进行单个数字是否相同的判断
slist2=list(str(b))
slist1.sort()  #分别将2个列表中数字进行排序，便于比较
slist2.sort()
if a==b:    #进行（1）的条件判断
    print('你赢得了10000元')
elif slist1==slist2 :   #进行（2）的判断
    print('你赢得了3000元')
elif slist1!=slist2:   #前两个条件均不符合，进行如下语句
    for x in slist1:   #对slist1中的元素进行循环遍历 
        if x in slist2:   #判断元素是否在slist2中
          print('你赢得了1000元')    
          break  #如有元素相同，即满足（2）的获奖条件，通过break语句结束当前循环遍历比较
    else:   #假如未能获奖，进行如下else语句
        print('你未能获奖')
print('中奖号码是:',a)
