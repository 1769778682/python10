# 需求：定义一个加法计算函数，并对该函数进行测试
# 定义一个加法函数
# 导包
import unittest


def add_func(x, y):
    """加法函数"""
    return x + y


class TestAdd(unittest.TestCase):
    """加法测试类"""

    def test_add(self):
        result = add_func(2, 7)
        print(f'测试1结果为{result}')

    def test_add2(self):
        result = add_func(6, 9)
        print(f'测试2结果为{result}')


if __name__ == '__main__':
    unittest.main()
