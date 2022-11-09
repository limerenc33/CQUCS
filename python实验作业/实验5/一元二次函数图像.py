#y=x**2+2x+1的图像
import matplotlib.pyplot as plt  #导入模块
import numpy as np 
fig=plt.figure()  #设定画布
ax=fig.add_subplot(111) #设定画布各项参数
ax.set(xlim=[-5,5],ylim=[-1,20],title="tuxiang",
xlabel='X',ylabel='Y')
x=np.arange(-5,5,0.01)  #规定x取值范围
y=x*x+x*2+1
plt.plot(x,y)
plt.show()