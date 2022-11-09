#冒泡排序

import configparser  #用于从ini读取结构化文件数据
import random

#定义了一个Country类
class Country:
    def __init__(self,name,gdp):
        self.sName = name
        self.fGdp = gdp

#从countries.ini读取全球GDP前15位至countries列表
countries = []
data = configparser.ConfigParser()
data.read("countries.ini")
data = data["Countries"]
iSize = int(data.get("countries.size", 0))
for i in range(iSize):
    name = data.get("countries[{}].sName".format(i), "ERROR").strip()
    gdp = float(data.get("countries[{}].fGdp".format(i), "0"))
    countries.append(Country(name, gdp))
random.shuffle(countries)   #打乱顺序
def bubblesort(countries):  #定义一个关于冒泡排序的函数
    for i in range (0,len(countries)): #设定一个i，使程序从countries的第一个元素开始进行冒泡排序比较
        for j in range (i+1,len(countries)):  #设定j，使程序从i之后逐个选取进行比较
            if countries[i].fGdp> countries[j].fGdp:  #将countries[i]和countries[j]的GDP进行比较
                countries[i],countries[j]=countries[j],countries[i]  #若i的GDP大于j的，就将两者交换
    return countries
countries=bubblesort(countries)  #将countries进行冒泡排序函数操作
countries.reverse()   #由于要得到非递增序列，而冒泡程序得到的是递增序列，因而用reverse函数将countries倒序
print('Countries sorted by gdp:')
for i in countries:
    print(i.sName,"'s GDP:$",i.fGdp,"in billions")



#插入排序
import configparser  #用于从ini读取结构化文件数据
import random

#定义了一个Country类
class Country:
    def __init__(self,name,gdp):
        self.sName = name
        self.fGdp = gdp

#从countries.ini读取全球GDP前15位至countries列表
countries = []
data = configparser.ConfigParser()
data.read("countries.ini")
data = data["Countries"]
iSize = int(data.get("countries.size", 0))
for i in range(iSize):
    name = data.get("countries[{}].sName".format(i), "ERROR").strip()
    gdp = float(data.get("countries[{}].fGdp".format(i), "0"))
    countries.append(Country(name, gdp))
random.shuffle(countries)   #打乱顺序
def insertsort(countries):  #定义一个插入排序的函数
    for i in range (1,len(countries)):  #引入i，用for语句在countries进行定位
        for j in range(i,0,-1):  #将i之前的元素从后往前进行遍历比较
            if countries[j].fGdp<countries[j-1].fGdp:  #如果j之前的元素比j大，就将两者对调
                countries[j],countries[j-1]=countries[j-1],countries[j]
    return countries
countries=insertsort(countries) #将countries用insertsort函数进行插入排序
countries.reverse()  #将countries倒序，获得非递增序列
print('countries sorted by gdp:')
for i in countries:
    print(i.sName,"'s GDP:$",i.fGdp,'in billions')
