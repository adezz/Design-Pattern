from abc import ABCMeta, abstractmethod


# 内容：将一个复杂对象的构建与它的表示分离，使得同样的构建过程可以创建不同的表示。
# 角色：
#   1.抽象建造者（Builder）
#   2.具体建造者（Concrete Builder）
#   3.指挥者（Director）
#   4.产品（Product）
#
# 建造者模式与抽象工厂模式相似，也用来创建复杂对象。主要区别是建造者模式着重一步步构造一个复杂对象，而抽象工厂模式着重于多个系列的产品对象。
# 优点：
#   1.隐藏了一个产品的内部结构和装配过程
#   2.将构造代码与表示代码分开
#   3.可以对构造过程进行更精细的控制


# 一个角色的模型
class player():
    def __init__(self, face=None, body=None, arm=None, leg=None):
        self.face = face
        self.body = body
        self.arm = arm
        self.leg = leg

    def __str__(self):
        return "%s %s %s %s" % (self.face, self.body, self.arm, self.leg)


# 构建具体角色的接口
class playerBuider(metaclass=ABCMeta):

    @abstractmethod
    def create_face(self):
        pass

    @abstractmethod
    def create_body(self):
        pass

    @abstractmethod
    def create_arm(self):
        pass

    @abstractmethod
    def create_leg(self):
        pass


class GirlBuider(playerBuider):
    def __init__(self):
        self.player = player()

    def create_face(self):
        self.player.face = "漂亮脸蛋"

    def create_body(self):
        self.player.body = "苗条"

    def create_arm(self):
        self.player.arm = "漂亮胳膊"

    def create_leg(self):
        self.player.leg = "大长腿"


# 指挥者 实现注重"组装过程"
class PlayerDirector():

    def build_player(self, builder):
        # 这里的组装顺序完全由PlayerDirector来进行控制
        builder.create_body()
        builder.create_face()
        builder.create_arm()
        builder.create_leg()
        # 最后再返回组装完成的对象
        return builder.player


real = PlayerDirector().build_player(GirlBuider())
print(real)



