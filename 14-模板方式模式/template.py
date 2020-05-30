
from abc import ABCMeta, abstractmethod
from time import sleep

# 内容：定义一个操作中的算法的骨架，而将一些步骤延迟到子类中。模板方法使得子类可以不改变一个算法的结构即可重定义该算法的某些特定步骤。

# 角色：
#   1.抽象类（AbstractClass）：定义抽象的原子操作（钩子操作）；实现一个模板方法作为算法的骨架。
#   2.具体类（ConcreteClass）：实现原子操作

# 适用场景：
#   1.一次性实现一个算法的不变的部分
#   2.各个子类中的公共行为应该被提取出来并集中到一个公共父类中以避免代码重复
#   3.控制子类扩展


class Window(metaclass=ABCMeta):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def repaint(self):
        pass

    def run(self):
        self.start()
        while True:
            try:
                self.repaint()
                sleep(2)
            except KeyboardInterrupt:
                break
        self.stop()


class MyWindow(Window):
    def __init__(self, msg):
        self.msg = msg

    def start(self):
        print("Window Run...")

    def stop(self):
        print("Window Stop...")

    def repaint(self):
        print(self.msg)


MyWindow("Hello...").run()