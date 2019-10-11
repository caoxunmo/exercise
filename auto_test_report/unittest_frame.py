# -*- encoding:utf-8 -*-

#unittest测试框架
import unittest
import os
from HtmlTestRunner import HTMLTestRunner


class Test(unittest.TestCase):
    #用于测试用例执行前的初始化工作
    def setUp(self):
        print("test start")

    def test_bbb(self):
        print("test bbb")

    def test_aaa(self):
        print("test aaa")

    #用于测试用例执行之后的善后工作
    def tearDown(self):
        print("test end")


if __name__ == '__main__':

    suite = unittest.TestSuite()
    suite.addTest(Test("test_bbb"))
    suite.addTest(Test("test_aaa"))
#    now = time.strftime("%Y-%m-%d %H_%M_%S")

#定义报告存放路径：
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(cur_dir, "report.html")

#定义测试报告：
    with open(file_path, "wb") as fp:
        runner = HTMLTestRunner(stream=fp,
                                descriptions=u"测试情况：")
#                                report_title="测试主题"
#标题编码格式有问题

        runner.run(suite)
