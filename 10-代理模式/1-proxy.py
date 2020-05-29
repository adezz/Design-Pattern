
from abc import ABCMeta, abstractmethod

# 内容：为其他对象提供一种代理以控制对这个对象的访问

# 应用场景：
#   1.远程代理：为远程的对象提供代理
#   2.虚代理：根据需要创建很大的对象
#   3.保护代理：控制对原始对象的访问，用于对象有不同访问权限时

# 角色：
#   1.抽象实体（Subject）
#   2.实体（RealSubject）
#   3.代理（Proxy）

# 优点：
#   1.远程代理：可以隐藏对象位于远程地址空间的事实
#   2.虚代理：可以进行优化，例如根据要求创建对象
#   3.保护代理：允许在访问一个对象时有一些附加的内务处理


# 抽象实体
class Proxy(metaclass=ABCMeta):
    @abstractmethod
    def get_content(self):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


# 实体 = 远程代理
class RemoteProxy(Proxy):
    def __init__(self, filename):
        self.filename = filename
        f = open('test.txt', 'r', encoding='utf-8')
        self.content = f.read()
        f.close()

    def get_content(self):
        return self.content

    def set_content(self, content):
        f = open('test.txt', 'w', encoding='utf-8')
        f.write(content)
        f.close()


# 实体 = 虚代理
class VirtualProxy(Proxy):
    def __init__(self, filename):
        self.filename = filename
        self.proxy = None

    def get_content(self):
        if not self.proxy:
            self.proxy = RemoteProxy(self.filename)
        return self.proxy.get_content()

    def set_content(self, content):
        if not self.proxy:
            self.proxy = RemoteProxy(self.filename)
        return self.proxy.set_content(content)


# 实体 = 保护代理
class ProtectedProxy(Proxy):
    def __init__(self, filename):
        self.proxy = RemoteProxy(filename)

    def get_content(self):
        return self.proxy.get_content()

    def set_content(self, content):
        raise PermissionError("无写入权限")

# remoteproxy = RemoteProxy('test.txt')
# print(remoteproxy.get_content())



# pp = ProtectedProxy('test.txt')
# print(pp.get_content())
# pp.set_content('123')





