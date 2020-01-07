from testframe.Tools.HTMLTestRunner import HTMLTestRunner
import unittest
import time

pattern = "test_*.py"
test_dir = "G:/PycharmProjects/pyjiaoben/testframe/TestCase"
discover = unittest.defaultTestLoader.discover(test_dir, pattern=pattern)
now = time.strftime('%Y-%m-%d_%H_%M_%S_')
filename = "G:/PycharmProjects/pyjiaoben/testframe/Report" + '/' + now + 'result.html'
fp = open(filename, 'wb')
html_test_runner = HTMLTestRunner(stream=fp, title=u'测试报告', description=u'用例执行情况：')
runner = html_test_runner
runner.run(discover)
# 注意：调用函数一定要加括号
fp.close()


