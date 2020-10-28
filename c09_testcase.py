# 注意：在使用UnitTest框架过程中，
# 所有的文件名必须遵循标识符命名规范，否则有可能出现文件无法运行的问题
# 1.导包
import unittest


# 2.自定义测试类
# class Test(object):  # 普通类
# 自定义测试类：必须继承自 unittest.TestCase
class Test(unittest.TestCase):
    # 在测试类后侧运行代码，会执行测试类中所有的测试方法

    # 3.自定义测试方法
    # def demo(self):  # 普通方法定义
    # pass
    # 自定义测试方法：要求方法名必须以test作为前缀开头
    def test_add1(self):  # 注意：在测试方法后运行代码，会执行当前的方法
        print('测试方法1')

    def test_add2(self):
        print('测试方法2')


# 说明
# 1.正常情况下，我们定义的类和方法，必须经过调用方可执行
# 2.但在测试框架中，测试类和测试方法是不需要调用就可以执行的
if __name__ == '__main__':
    unittest.main()
