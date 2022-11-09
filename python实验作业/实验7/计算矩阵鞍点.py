import numpy as np 
def findandian(x):
    for r in range(len(x)):
        c = x[r].index(max(x[r]))
        k = 0
        while k < len(x):
            if x[r][c] <= x[k][c]:
                k += 1
                if k == len(x):
                    print('鞍点在第{}行，第{}列，值为：{}'.format(r , c, x[r][c]))
            else:
                break
row=int(input('请输入行数:'))
col=int(input('请输入列数:'))
a=np.random.randint(1,100,(row,col))
print(a)
a=a.tolist()
print(findandian(a))             


