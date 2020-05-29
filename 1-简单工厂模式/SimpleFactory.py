# coding=utf-8


# 内容：不直接向客户端暴露对象创建的实现细节，而是通过一个工厂类来负责创建产品类的实例。
# 角色：
#   1.工厂角色（Creator）
#   2.抽象产品角色（Product）
#   3.具体产品角色（Concrete Product）
#   4.客户端（client）

# 优点：
#   1.隐藏了对象创建的实现细节
#   2.客户端不需要修改代码
# 缺点：
#   1.违反了单一职责原则，将创建逻辑几种到一个工厂类里
#   2.当添加新产品时，需要修改工厂类代码，违反了开闭原则

from abc import ABCMeta, abstractmethod


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


# 工厂类
class Factory(object):
    def createpayment(self, pay_method):
        if pay_method == 'alipay':
            return Alipay()
        elif pay_method == 'wechatpay':
            return WechatPay()
        elif pay_method == 'huabeipay':
            return HuabeiPay()
        else:
            raise TypeError("not method %s" % pay_method)


# client客户端
factory = Factory()
alipay = factory.createpayment('alipay')
alipay.pay(100)

