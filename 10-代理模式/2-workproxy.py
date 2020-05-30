import time
from abc import ABCMeta, abstractmethod

# 角色：
#   1.抽象实体（Subject）
#   2.实体（RealSubject）
#   3.代理（Proxy）


# 抽象类
class Manager(metaclass=ABCMeta):
    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def talk(self):
        pass


# 实体
class SalesManager(Manager):
    def __init__(self):
        self.busy = "No"  # "Yes"

    def work(self):
        print("Sales Manager working...")

    def talk(self):
        print("Sales Manager ready to talk")


# 代理
class ReceptionProxy(Manager):
    def __init__(self):
        # self.busy = 'No'
        self.sales = SalesManager()

    def work(self):
        print("Proxy checking for Sales Manager availability")
        if self.sales.busy == 'No':
            time.sleep(2)
            self.sales.talk()
        else:
            time.sleep(2)
            print("Sales Manager is busy")

    def talk(self):
        pass


p = ReceptionProxy()
p.work()