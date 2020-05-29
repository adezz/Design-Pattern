

from abc import ABCMeta, abstractmethod

# 接口
# ========================
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self):
        raise NotImplementedError


class Alipay(Payment):
    def pay(self):
        print("Alipay")


class WechatPay(Payment):
    def pay(self):
        print("WechatPay")


pay = Alipay()
pay.pay()
# ========================

#接口隔离/单一职责原则


class LandAnimal(metaclass=ABCMeta):
    @abstractmethod
    def walk(self):
        pass


class WaterAnimal(metaclass=ABCMeta):
    @abstractmethod
    def swim(self):
        pass


class SkyAnimal(metaclass=ABCMeta):
    @abstractmethod
    def fly(self):
        pass


class Tiger(LandAnimal):
    def walk(self):
        print("tiget walk")


class Frog(WaterAnimal, LandAnimal):
    def walk(self):
        print("frog walk")

    def swim(self):
        print("frog swim")


tiger = Tiger()
tiger.walk()



