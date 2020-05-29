
# 内容：为子系统中的一组接口提供一个一致的界面，外观模式定义了一个高层接口，这个接口使得这一子系统更加容易使用
# 角色：
#   1.外观（facade）
#   2.子系统类（subsystem classes）

# 优点：
#   1.减少系统相互依赖
#   2.提高了灵活性
#   3.提高了安全性


class Cpu(object):
    def run(self):
        print("cpu run...")

    def stop(self):
        print("cpu stop...")


class Disk(object):
    def run(self):
        print("Disk run...")

    def stop(self):
        print("Disk stop...")


class Memory(object):
    def run(self):
        print("Memory run...")

    def stop(self):
        print("Memory stop...")


class Computer(object):
    def __init__(self):
        self.cpu = Cpu()
        self.disk = Disk()
        self.memory = Memory()

    def run(self):
        self.cpu.run()
        self.disk.run()
        self.memory.run()

    def stop(self):
        self.cpu.stop()
        self.disk.stop()
        self.memory.stop()


com = Computer()
com.run()
print("==================")
com.stop()