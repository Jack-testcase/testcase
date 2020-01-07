import unittest
from selenium import webdriver
import time
from testframe.Page.LoginPage import LoginPage


class test_login(unittest.TestCase):
    # 前置条件，打开网页，打开网站，并最大化
    def setUp(self):
        global a
        a = LoginPage()

        # 登录脚本

    def test_login(self):
        a.login()
        time.sleep(3)
        url = a.getCurrentUrl()
        assert url == 'null'
      #  a.getScreenshot('G:/PycharmProjects/pyjiaoben/testframe/Report')


        # 收尾

    def tearDown(self):
        a.quit()
    # a.driver
