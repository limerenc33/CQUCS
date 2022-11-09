def move(n, a, b, c):
    if n==1:
        print (a, '-->', c)
        return
    move(n-1, a, c, b)
    print (a, '-->', c)
    move(n-1, b, a, c)
m=int(input('请输入汉诺塔层数'))
move(m, 'A', 'B', 'C')