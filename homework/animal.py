# @Author   : Clifford
# @File     : animal
# @Time     : 2022/3/27 17:53

# 1、创建一个类（Animal）【动物类】
class Animal:

    # 类里有属性（名称，颜色，年龄，性别）
    name = ''
    color = ''
    age = ''
    gender = ''

    def __init__(self, name, color, age, gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender


    # 类中有方法：会叫，会跑
    def speak(self):
        print(f"{self.name}会叫")

    def run(self):
        print(f"{self.name}会跑")

# 2、创建子类【猫】, 继承【动物类】，
class Cat(Animal):
    # 重写父类的__init__方法，继承父类的属性
    def __init__(self, name, color, age, gender):
        # 共性
        super().__init__(name, color, age, gender)
        # 个性
        # 添加一个新的属性，毛发=短毛
        self.fur = "短毛"

    # 添加一个新的方法， 会捉老鼠，
    def catch_mouse(self):
        print("会捉老鼠")
    # 重写父类的【会叫】的方法，改成【喵喵叫】

    def speak(self):
        print("喵喵叫")


# 3、创建子类【狗】
# 继承【动物类】，
class Dog(Animal):

    # 复写父类的__init__方法，继承父类的属性
    def __init__(self, name, color, age, gender):
        super().__init__(name, color, age, gender)
        # 添加一个新的属性，毛发=长毛
        self.fur = "长毛"
    # 添加一个新的方法， 会看家
    def house_keeping(self):
        print("会看家")

    # 重写父类的【会叫】的方法，改成【汪汪叫】
    def speak(self):
        print("汪汪叫")

    def __repr__(self):
        return f"{self.name}, {self.age}"

# 4、在入口函数中创建类的实例
if __name__ == '__main__':

    # 创建一个猫猫实例，调用捉老鼠的方法
    kitty = Cat(name="Kitty", color="白色", age=2, gender="母")
    # 打印【猫猫的姓名，颜色，年龄，性别，毛发，捉到了老鼠】
    print(kitty.name, kitty.color, kitty.age, kitty.gender, kitty.fur, "捉到了老鼠")
    print(f"{kitty.name}")
    kitty.catch_mouse()
    # 创建一个狗狗实例，调用【会看家】的方法
    wang_cai = Dog("旺财", "黄色", 3, "公")
    wang_cai.house_keeping()
    # 打印【狗狗的姓名，颜色，年龄，性别，毛发】
    print(f"{wang_cai.name}, {wang_cai.color}, {wang_cai.age}, {wang_cai.gender}, {wang_cai.fur}")
