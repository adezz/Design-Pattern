
from abc import ABCMeta, abstractmethod

# 内容：
#   将一个事物的两个维度分离，使其都可以独立地变化

# 角色：
#   1.抽象（Abstraction）
#   2.细化抽象（RefinedAbstraction）
#   3.实现者（Implementor）
#   4.具体实现者（ConcreteImplementor）

# 应用场景：
#   1.当事物有两个维度上的表现，两个维度都可能扩展的时候

# 优点：
#   1.抽象和实现相分离
#   2.优秀的扩展能力

# 适用场景：
#   1.表示对象的“部分-整体”层次结构（特别是结构是递归的）
#   2.希望用户忽略组合对象与单个对象的不同，用户统一地使用组合结构中的所有对象
# 优点：
#   1.定义了包含基本对象和组合对象的类层次结构
#   2.简化客户端代码，即客户端可以一致地使用组合对象和单个对象
#   3.更容易增加新类型的组件


# 抽象Abstraction
class Shape(metaclass=ABCMeta):
    def __init__(self, color):
        self.color = color  # 通过属性来进行低耦合

    @abstractmethod
    def draw(self):
        pass


# 实现者Implementor
class Color(metaclass=ABCMeta):
    @abstractmethod
    def paint(self, shape):
        pass


# 细化抽象RefinedAbstraction
class Rectangle(Shape):
    name = "长方形"

    def draw(self):
        self.color.paint(self)


class Circle(Shape):
    name = "圆形"

    def draw(self):
        self.color.paint(self)


# 具体实现者ConcreteImplementor
class BlueColor(Color):
    def paint(self, shape):
        print("蓝色的%s" % shape.name)


# 具体实现者ConcreteImplementor
class RedColor(Color):
    def paint(self, shape):
        print("红色的%s" % shape.name)


rect = Rectangle(BlueColor())
circle = Circle(BlueColor())
circle.draw()
rect.draw()







