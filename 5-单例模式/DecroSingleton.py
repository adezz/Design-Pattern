# 通过装饰器来实现单例模式

import threading


def mySingleton(myclass):
    _instance = {}
    _instance_lock = threading.Lock()

    def _singleton(*args, **kargs):
        if myclass not in _instance:
            with _instance_lock:
                _instance[myclass] = myclass(*args, **kargs)  # 当前cls为第一次的一个类的实例化的对象进行保存
        return _instance[myclass]
    return _singleton


@mySingleton
class Myclass_1(object):
    def printmy(self):
        print("Myclass_1")

@mySingleton
class Myclass_2(object):
    def printmy(self):
        print("Myclass_2")


a = Myclass_1()
b = Myclass_1()

c = Myclass_2()
d = Myclass_2()


print(id(a), id(b))

print(id(c), id(d))
