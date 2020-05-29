
# 单例模式（Singleton Pattern）是一种常用的软件设计模式，该模式的主要目的是确保某一个类只有一个实例存在。当你希望在整个系统中，某个类只能出现一个实例时，单例对象就能派上用场。

# 内容：保证一个类只有一个实例，并提供一个访问它的全局访问点。
# 角色：
#   1.单例（Singleton）
# 优点：
#   1.对唯一实例的受控访问
#   2.单例相当于全局变量，但防止了命名空间被污染
import threading


# 单例模式的第一种方式
class Singleton(object):
    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            with Singleton._instance_lock:
                cls._instance = super().__new__(cls)
        return cls._instance


class Myclass(Singleton):
    def __init__(self, a):
        self.a = a


a = Myclass(10)
b = Myclass(20)

print(id(a))
print(id(b))














