# encoding=utf-8

from abc import ABCMeta, abstractmethod


class FemaleA():
    def __init__(self, name):
        self.name = name


class Male(metaclass=ABCMeta):
    @abstractmethod
    def send_flower(self):
        pass

    @abstractmethod
    def send_chocolate(self):
        pass

    @abstractmethod
    def send_book(self):
        pass


class MaleA(Male):
    def __init__(self, name, love_female):
        self.name = name
        self.love_female = FemaleA(love_female)

    def send_flower(self):
        print('%s送花给%s' % (self.name, self.love_female.name))

    def send_chocolate(self):
        print('%s送巧克力给%s' % (self.name, self.love_female.name))

    def send_book(self):
        print('%s送书给%s' % (self.name, self.love_female.name))


# 这里是一个男B作为代理 促成 一个男A的和另外一个女A的，所以代理一般具有男A的所有功能，代替男A的进行需要进行的事情
class Proxy(Male):
    def __init__(self, name, proxyed_name, love_female):
        self.name = name
        self.proxyed = MaleA(proxyed_name, love_female)

    def send_flower(self):
        self.proxyed.send_flower()

    def send_chocolate(self):
        self.proxyed.send_chocolate()

    def send_book(self):
        self.proxyed.send_book()


if __name__ == '__main__':
    p = Proxy('男B', '男A', '女A')
    p.send_book()
    p.send_chocolate()
    p.send_flower()