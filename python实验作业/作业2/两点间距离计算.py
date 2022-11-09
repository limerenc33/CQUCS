x1=int(input('请输入第一个坐标值:'))
y1=int(input('请输入第二个坐标值:'))
x2=int(input('请输入第三个坐标值:'))
y2=int(input('请输入第四个坐标值:'))
import math
from math import sqrt
L=sqrt((x2-x1)**2+(y2-y1)**2)
print('两点间距离为:',L)