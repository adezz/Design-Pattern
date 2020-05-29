from abc import ABCMeta, abstractmethod


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


# 对象适配器,通过组合的方式进行实现，优点可以批量的进行适配
class PaymentAdapter(Payment):
    def __init__(self, payment):
        self.payment = payment

    def pay(self, money):
        self.payment.cost(money)


# a = AliPay()
# a.pay(100)
#
# b = WechatPay()
# b.pay(200)

b = BankPay()

adapter = PaymentAdapter(b)
adapter.pay(100)


