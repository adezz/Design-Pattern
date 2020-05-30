
from abc import ABCMeta, abstractmethod

# 通过组合来进行实现


class Manager(metaclass=ABCMeta):
    @abstractmethod
    def allow_rest(self, day):
        pass


class ChairManager(Manager):
    def allow_rest(self, day):
        if day < 10:
            print("ChairManager allow_rest %s day" % day)
        else:
            print("you are fired")


class GeneralManager(Manager):
    def __init__(self):
        self.top = ChairManager()

    def allow_rest(self, day):
        if day < 5:
            print("GeneralManager allow_rest %s day" % day)
        else:
            self.top.allow_rest(day)


class DeptManager(Manager):
    def __init__(self):
        self.top = GeneralManager()

    def allow_rest(self, day):
        if day < 2:
            print("DeptManager allow_rest %s day" % day)
        else:
            self.top.allow_rest(day)


deptmanager = DeptManager()

deptmanager.allow_rest(4)



