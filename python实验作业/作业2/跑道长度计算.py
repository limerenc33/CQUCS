a=float(input('请输入起飞加速度:'))
v=float(input('请输入起飞速度:'))
def lengthcal(a,v):
    L=v**2/(2*a)
    return L
M=lengthcal(a,v)
print('所需最短跑道长度为:',M,'米')
