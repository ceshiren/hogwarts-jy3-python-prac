# @Author   : Clifford
# @File     : red
# @Time     : 2022/3/27 16:44

"""
抢红包案例

某群有多个成员，群主给成员发普通红包。

发红包的规则是：
1、群主负责发红包，不能抢红包。红包金额从群主余额中扣除，按成员人数平均分成n等份，以备领取。
每个红包的金额为整数，如果有余数则加到最后一个红包中。
2、成员负责抢红包。抢到的红包金额存到自己余额中。
Done：3、抢完红包后需要进行报数，打印格式“我是XX，现在有 XX 块钱。”。

请根据描述信息，完成案例中所有类的定义、类之间的继承关系，以及发红包、抢红包的操作。

一、分析
二、编码
"""
import random


class Person:

    def __init__(self, name, money):
        self.name = name
        self.money = money

    def show(self):
        print(f"我是{self.name}，现在有 {self.money} 块钱。")

class Manager(Person):
    """
    群主负责发红包，不能抢红包。
    红包金额从群主余额中扣除，按成员人数平均分成n等份，以备领取。
    每个红包的金额为整数，如果有余数则加到最后一个红包中。
    """

    def send(self, money, num):

        if self.money < money:
            print("逗你玩")
            return None

        # 空的红包容器
        red_list = []

        # 扣钱
        self.money -= money

        # 瓜分算法(整除)
        avg = money // num
        rest = money % num

        for i in range(num):
            red_list.append(avg)

        red_list[-1] += rest

        return red_list

class Member(Person):

    def grab(self, red_list):
        """
        成员负责抢红包。抢到的红包金额存到自己余额中。
        """
        if not red_list:
            print("一毛钱都不给")
            return None

        random_index = random.randint(0, len(red_list) - 1)
        lucky_money = red_list.pop(random_index)

        # 存钱
        self.money += lucky_money


if __name__ == '__main__':

    manager = Manager("嘿", 10)
    reds = manager.send(100, 3)

    zhuang = Member("壮壮", 0)
    zhuang.grab(reds)


    sun_xiao = Member("孙小", 0)
    sun_xiao.grab(reds)

