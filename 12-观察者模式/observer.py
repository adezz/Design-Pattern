from abc import ABCMeta, abstractmethod


# 内容：定义对象间的一种一对多的依赖关系,当一个对象的状态发生改变时, 所有依赖于它的对象都得到通知并被自动更新。观察者模式又称“发布-订阅”模式

# 角色：
#   1.抽象主题（Subject）
#   2.具体主题（ConcreteSubject）——发布者
#   3.抽象观察者（Observer）
#   4.具体观察者（ConcreteObserver）——订阅者

# 抽象观察者
class Observer(metaclass=ABCMeta):  # 抽象订阅者
    @abstractmethod
    def update(self, notice):  # notice 是一个Notice类的对象，update方法用来更新发布者所发布的内容
        pass


# 具体观察者
class Staff(Observer):
    def __init__(self):
        self.company_info = None  # 存储所订阅的信息，类似可以作为公众号的名字

    def update(self, notice):
        self.company_info = notice.company_info


# 抽象发布者
class Notice:
    def __init__(self):
        self.observers = []

    def attach(self, obs):
        self.observers.append(obs)

    def detach(self, obs):
        self.observers.remove(obs)

    def notify(self):  # 推送
        for obs in self.observers:
            obs.update(self)


# 具体发布者
class StaffNotice(Notice):
    def __init__(self, company_info=None):
        super().__init__()
        self.__company_info = company_info

    @property
    def company_info(self):
        return self.__company_info

    @company_info.setter
    def company_info(self, info):
        self.__company_info = info
        self.notify()  # 推送：通过装饰器一步到位 实现双方都改变的作用


# Client
notice = StaffNotice("阿德赌博有限公司")
s1 = Staff()  # 订阅者
s2 = Staff()  # 订阅者
notice.attach(s1)
notice.attach(s2)
notice.company_info = "公司今年业绩非常好，给大家发奖金！！！"
print(s1.company_info)
print(s2.company_info)