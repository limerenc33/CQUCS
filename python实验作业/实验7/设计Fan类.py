from enum import Enum
class Color(Enum):
    yellow = 1
    white = 2
    black = 3
    blue = 4


class Fan():
    def __init__(self):
        self.on = False
        self.color = 0
        self.power = 'none'
    def setColor(self):
        color = input("设置颜色为：")
        if color == "yellow":
            self.color = Color(1)
        elif color == "white":
            self.color = Color(2)
        elif color == "black":
            self.color = Color(3)
        elif color == "blue":
            self.color = Color(4)
        else:
            print("不存在这种颜色！")
            
    def on_off(self):
        if self.on:
            self.on = False
            self.power = "none"
        else:
            self.on = True

    def higherPower(self):
        powers = ["none", "low", "median", "high"]
        if self.power == "high":
            print("已调至最大值！")
        else:
            self.power = powers[powers.index(self.power)+1]

    def lowerpower(self):
        powers = ["none", "low", "median", "high"]
        if self.power == "low":
            print("已调至最高值！")
        else:
            self.power = powers[powers.index(self.power)-1]

    def showStatus(self):
        print(self.color)
        if self.on:
            print(self.power)
        else:
            print(False)
a=Fan()
a.setColor()
a.on_off()
a.higherPower()
a.showStatus()
