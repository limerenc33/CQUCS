import math

def cal_shortest_length():

    # 计算公式为
    # 加速度^2 / 2*加速度
    start_speed = float(input("请输入起飞速度:"))
    acc_speed = float(input("请输入加速度:"))
    shortest_len = math.pow(start_speed, 2) / (2*acc_speed)

    return shortest_len

shortest_len = cal_shortest_length()
print(shortest_len)