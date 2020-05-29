
from abc import ABCMeta, abstractmethod

# 内容：将对象组合成树形结构以表示“部分-整体”的层次结构。组合模式使得用户对单个对象和组合对象的使用具有一致性。
# 角色：
#   1.抽象组件（Component）
#   2.叶子组件（Leaf）
#   3.复合组件（Composite）
#   4.客户端（Client）

#
# 适用场景：
#   1.表示对象的“部分-整体”层次结构（特别是结构是递归的）
#   2.希望用户忽略组合对象与单个对象的不同，用户统一地使用组合结构中的所有对象
# 优点：
#   1.定义了包含基本对象和组合对象的类层次结构
#   2.简化客户端代码，即客户端可以一致地使用组合对象和单个对象
#   3.更容易增加新类型的组件


# 抽象组件
class Graphic(metaclass=ABCMeta):
    @abstractmethod
    def draw(self):
        pass


# 叶子组件
class Point(Graphic):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(self)

    def __str__(self):
        return '点(%s, %s)' % (self.x, self.y)


# 叶子组件
class Line(Graphic):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self):
        print(self)

    def __str__(self):
        return '线 ( (%s, %s) , (%s, %s) )' % (self.p1.x, self.p1.y, self.p2.x, self.p2.y)


# 复合组件
class Picture(Graphic):
    def __init__(self, iterable):
        self._pic_list = []
        for i in iterable:
            self._pic_list.append(i)

    def draw(self):
        print("------复合图形------")
        for g in self._pic_list:
            g.draw()
        print("------复合图形------")


# 客户端
line1 = Line(Point(1, 2), Point(3, 4))
line2 = Line(Point(2, 1), Point(4, 3))
pic = Picture([line1, line2])
pic.draw()
