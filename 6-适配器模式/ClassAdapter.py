from abc import ABCMeta, abstractmethod

# 内容：将一个类的接口转换成客户希望的另一个接口。适配器模式使得原本由于接口不兼容而不能一起工作的那些类可以一起工作。
# 两种实现方式：
#   1.类适配器：使用多继承
#   2.对象适配器：使用组合
#
# 角色：
#   1.目标接口（Target）
#   2.待适配的类（Adaptee）
#   3.适配器（Adapter）
# 适用场景：
#   1.想使用一个已经存在的类，而它的接口不符合你的要求
#   2.（对象适配器）想使用一些已经存在的子类，但不可能对每一个都进行子类化以匹配它们的接口。对象适配器可以适配它的父类接口。

class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass


class AliPay(Payment):
    def pay(self, money):
        print("支付宝支付了%s元." % money)


class WechatPay(Payment):
    def pay(self, money):
        print("微信支付了%s元." % money)


# Adaptee
class BankPay(object):
    def cost(self, money):
        print("银行支付了%s元." % money)


# Adaptee
class ApplePay(object):
    def cost(self, money):
        print("苹果支付了%s元." % money)


# 类适配Adapter器实现
class PaymentAdapter(Payment, BankPay):
    def pay(self, money):
        self.cost(money)


c = PaymentAdapter()
c.pay(300)



