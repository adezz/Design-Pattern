
from abc import ABCMeta, abstractmethod

# 内容：定义对象间的一种一对多的依赖关系,当一个对象的状态发生改变时, 所有依赖于它的对象都得到通知并被自动更新。观察者模式又称“发布-订阅”模式

# 角色：
#   1.抽象主题（Subject）
#   2.具体主题（ConcreteSubject）——发布者
#   3.抽象观察者（Observer）
#   4.具体观察者（ConcreteObserver）——订阅者

# 适用场景：
#   1.当一个抽象模型有两方面，其中一个方面依赖于另一个方面。将这两者封装在独立对象中以使它们可以各自独立地改变和复用。
#   2.当对一个对象的改变需要同时改变其它对象，而不知道具体有多少对象有待改变。
#   3.当一个对象必须通知其它对象，而它又不能假定其它对象是谁。换言之，你不希望这些对象是紧密耦合的。

# 优点：
#   1.目标和观察者之间的抽象耦合最小
#   2.支持广播通信

# 抽象订阅者

class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, notice):
        pass

    def attach(self, notice):
        pass

    def detach(self):
        pass


# 具体订阅者
class ObserverPeople(Observer):
    def __init__(self, company_info=None):
        self.company_info = company_info

    def update(self, notice):
        self.company_info = notice.company_info


# 抽象公众号
class Notice(object):
    def __init__(self):
        self.observerpeoples = []

    def nodify(self):
        for i in self.observerpeoples:
            i.update(self)

    def attach(self, observerpeople):
        self.observerpeoples.append(observerpeople)

    def detach(self, observerpeople):
        self.observerpeoples.remove(observerpeople)


# 具体公众号
class NoticeCompany(Notice):
    def __init__(self, company_info):
        super().__init__()
        self.__company_info = company_info

    @property
    def company_info(self):
        return self.__company_info

    @company_info.setter
    def company_info(self, company_info):
        self.__company_info = company_info
        self.nodify()


s1 = ObserverPeople()
s2 = ObserverPeople()
nc = NoticeCompany("浙江阿德博彩有限公司")
nc.attach(s1)
nc.attach(s2)
nc.company_info = "今天公司每天送一张pop卡"
print(s1.company_info)
print(s2.company_info)

nc.detach(s2)
nc.company_info = "今天公司每天送一张bob卡"

print(s1.company_info)
print(s2.company_info)



