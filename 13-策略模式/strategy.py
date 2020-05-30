
from abc import ABCMeta, abstractmethod

# 内容：定义一系列的算法，把它们一个个封装起来，并且使它们可相互替换。本模式使得算法可独立于使用它的客户而变化。

# 角色：
#   1.抽象策略（Strategy）
#   2.具体策略（ConcreteStrategy）
#   3.上下文（Context）

# 优点：
#   1.定义了一系列可重用的算法和行为
#   2.消除了一些条件语句
#   3.可以提供相同行为的不同实现
# 缺点：
#   1.客户必须了解不同的策略

class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, data):
        pass


class FasterStrategy(Strategy):
    def execute(self, data):
        print("[速度快 策略差] 执行完成 %s" % data)


class SlowStrategy(Strategy):
    def execute(self, data):
        print("[速度慢 策略好] 执行完成 %s" % data)


class Context(object):
    def __init__(self, Strategy, data):
        self.data = data
        self.strategy = Strategy

    def set_strategy(self, Strategy):
        self.strategy = Strategy

    def goMyContext(self):
        self.strategy.execute(self.data)


fs = FasterStrategy()
ct = Context(fs, "北京到浙江")
ct.goMyContext()
ss = SlowStrategy()
ct.set_strategy(ss)
ct.goMyContext()
