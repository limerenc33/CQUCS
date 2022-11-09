#json文件读取和绘图
import json  #导入模块
from datetime import datetime
from matplotlib import pyplot as plt 
with open('co2-mm-gl.json','r') as f :  #打开json文件
    data = json.load(f)
    Averages,Trends,Dates=[],[],[]  #设置3个空列表，便于数据导出和存储
    for x in range(0,len(data)):   #遍历data中每一行，将相应数据存放在相应列表中
        Averages.append(int(float(data[x]['Average'])))   #将其变成整形，便于绘图
        Trends.append(int(float(data[x]['Trend'])))
        Dates.append(data[x]['Date'])
fig=plt.figure(dpi=128,figsize=(10,6))  #设置画布各项参数
plt.plot(Dates,Averages,c='orange')
plt.plot(Dates,Trends,c='blue')
plt.title("Average&Trend",fontsize=24)
plt.xlabel('Date',fontsize=5)
plt.xticks(Dates[0:len(Dates):100])   #将x，y轴的坐标间隔显示，避免数据过多堆叠在一起
plt.yticks(Trends[0:len(Trends):100])
fig.autofmt_xdate()
plt.ylabel('',fontsize=5)
plt.show()