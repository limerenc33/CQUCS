#csv文件读取和绘图
import csv   #导入模块
from datetime import datetime
from matplotlib import pyplot as plt 
filename='co2-mm-mlo.csv'
with open(filename) as f:  #打开csv文件
    reader=csv.reader(f)  #读取csv文件中数据
    header_row=next(reader)  #遍历reader中的每一行
    dates,interpolatedlist,trendlist=[],[],[]  #设定3个空列表，以便于后续将数据导出并存储
    for row in reader:  #将每一行中的相应数据取出并放在相应列表中
            current_date=row[0]
            dates.append(current_date)
            interpolated=int(float(row[3]))  #将数据变成整形，便于作图
            interpolatedlist.append(interpolated)
            trend=int(float(row[4]))
            trendlist.append(trend)
fig=plt.figure(dpi=128,figsize=(10,6))  #设置画布各项参数
plt.plot(dates,interpolatedlist,c='orange')
plt.plot(dates,trendlist,c='blue')
plt.title("Interpolated&Trend",fontsize=24)
plt.xlabel('Date',fontsize=5)
plt.xticks(dates[0:len(dates):100])
plt.yticks(trendlist[0:len(trendlist):100])
fig.autofmt_xdate()  #避免日期过长重叠，将其倾斜显示
plt.ylabel('',fontsize=5)
plt.show()
