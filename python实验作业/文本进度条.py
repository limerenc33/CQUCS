#progressbar.py
progressbefore=0
def printprogressbar(percent,prefix=''):
    global progressbefore
    if percent-progressbefore<0.001:  #只有当进度达到千分之一的时候才刷新，避免频繁刷新进度条
        return
    progressbefore=percent
    precentstr=("{0:.1f}").format(percent*100)  #格式化字符串
    filledlength=int(30*percent)
    bar='▮'*filledlength+'-'*(30-filledlength)
    print('\r%s|%s|%s%%'%(prefix,bar,precentstr),end='')

if __name__=='__main__':   #对模块进行测试
    import time 
    for i in range (1000):
        printprogressbar((i+1)/1000,prefix="progress:")
        time.sleep(0.01)   #当前进程暂停10ms
