import math


def cal_distance():

    """
        两点间距离计算公式为：
        sqrt((x1-x2)^2 + (y1-y2)^2)
    """

    x1, y1 = input("请输入第一个坐标点的坐标， 使用英文逗号分隔").split(',')
    x2, y2 = input("请输入第二个坐标点的坐标， 使用英文逗号分隔").split(',')
    x1 = float(x1.strip())
    x2 = float(x2.strip())
    y1 = float(y1.strip())
    y2 = float(y2.strip())

    result_dis = math.sqrt(math.pow(x1-x2, 2) + math.pow(y1-y2, 2))
    return result_dis


dis = cal_distance()
print(dis)