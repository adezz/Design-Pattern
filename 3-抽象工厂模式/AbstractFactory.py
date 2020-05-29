from abc import ABCMeta, abstractmethod

# 内容：定义一个工厂类接口，让工厂子类来创建一系列相关或相互依赖的对象。
#   例：生产一部手机，需要手机壳、CPU、操作系统三类对象进行组装，其中每类对象都有不同的种类。对每个具体工厂，分别生产一部手机所需要的三个对象。
#
#   相比工厂方法模式，抽象工厂模式中的每个具体工厂都生产一套产品。
#
# 优点：
#   1.将客户端与类的具体实现相分离
#   2.每个工厂创建了一个完整的产品系列，使得易于交换产品系列
#   3.有利于产品的一致性（即产品之间的约束关系）
# 缺点：
#   1.难以支持新种类的（抽象）产品，比如没有共性就会难以支持，就比如突然需要一个摄像头配件，那么工厂类就需要加 就需要比较大的改动


# 抽象产品类
class PhoneShell(metaclass=ABCMeta):
    @abstractmethod
    def show_shell(self):
        pass


# 抽象产品类
class OS(metaclass=ABCMeta):
    @abstractmethod
    def show_os(self):
        pass


# 抽象产品类
class CPU(metaclass=ABCMeta):
    @abstractmethod
    def show_cpu(self):
        pass


# 具体产品类
class SmallShell(PhoneShell):
    def show_shell(self):
        print(" 普通手机小手机壳")


# 具体产品类
class BigShell(PhoneShell):
    def show_shell(self):
        print(" 普通手机大手机壳")


# 具体产品类
class AppleShell(PhoneShell):
    def show_shell(self):
        print(" 苹果手机壳")


# 具体产品类
class SnapDragonCPU(CPU):
    def show_cpu(self):
        print(" 骁龙CPU")


# 具体产品类
class MediaTekCPU(CPU):
    def show_cpu(self):
        print(" 联发科CPU")


# 具体产品类
class AppleCPU(CPU):
    def show_cpu(self):
        print(" 苹果CPU")


# 具体产品类
class Android(OS):
    def show_os(self):
        print(" Android系统")


# 具体产品类
class IOS(OS):
    def show_os(self):
        print(" iOS系统")


# 抽象工厂类
class Factory(metaclass=ABCMeta):

    @abstractmethod
    def create_phoneshell(self):
        pass

    @abstractmethod
    def create_os(self):
        pass

    @abstractmethod
    def create_cpu(self):
        pass


# 具体工厂类
class XiaoMiPhoneFactory(Factory):
    def create_cpu(self):
        return MediaTekCPU()

    def create_os(self):
        return Android()

    def create_phoneshell(self):
        return BigShell()


class Phone(object):
    def __init__(self, cpu, os, shell):
        self.cpu = cpu
        self.os = os
        self.shell = shell

    def show_info(self):
        print("手机信息为：")
        self.cpu.show_cpu()
        self.os.show_os()
        self.shell.show_shell()


def make_phone(factory):
    return Phone(factory.create_cpu(), factory.create_os(), factory.create_phoneshell())


phone = make_phone(XiaoMiPhoneFactory())
phone.show_info()



