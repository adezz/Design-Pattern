from abc import ABCMeta, abstractmethod


# 内容：定义一个用于创建对象的接口（工厂接口），让子类决定实例化哪一个产品类。
# 角色：
#   1.抽象工厂角色（Creator）
#   2.具体工厂角色（Concrete Creator）
#   3.抽象产品角色（Product）
#   4.具体产品角色（Concrete Product）
#   5.客户端（client）


# 优点：
#   1.每个具体产品都对应一个具体工厂类 所以实现'单一原则' 不需要修改工厂类代码所以实现'开闭原则'
#   2.隐藏了对象创建的实现细节
# 缺点：
#   3.每增加一个具体产品类，就必须增加一个相应的具体工厂类，导致代码繁琐


# 抽象产品类
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        raise NotImplementedError


# 具体产品类
class Alipay(Payment):
    def pay(self, money):
        print("支付宝支付了%s元." % money)


# 具体产品类
class WechatPay(Payment):
    def pay(self, money):
        print("微信支付了%s元." % money)


# 具体产品类
class HuabeiPay(Payment):
    def pay(self, money):
        print("花呗支付了%s元." % money)


# 抽象工厂类
class Factory(metaclass=ABCMeta):
    @staticmethod
    def createpayment(self):
        pass


# 具体工厂类
class AlipayFactory(object):
    def createpayment(self):
            return Alipay()


class WechatPayFactory(object):
    def createpayment(self):
            return Alipay()


class HuabeiPayFactory(object):
    def createpayment(self):
            return Alipay()


# client客户端
pf = AlipayFactory()
alipay = pf.createpayment()
alipay.pay(100)
