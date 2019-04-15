from time import sleep
import unittest,random,sys
from selenium.webdriver.common.by import By
from selenium import webdriver
from testcases.pages.loginPage import LoginPage
from testcases.common.myunit import MyTest
from testcases.pages.indexPage import IndexPage


class loginTest(MyTest):
    '''首页登录测试'''

    def test_login_user_pwd_null(self):
        '''用户名、密码同时为空或用户名为空，密码正确'''
        po = LoginPage(self.driver)
        po.openHomePage()
        po.login_action('','')
        sleep(2)
        error_msg = po.error_hint()
        self.assertEqual(error_msg,u'用户名称为空，登录失败！')

    def test_login_pwd_null(self):
        '''用户名正确，密码为空'''
        po = LoginPage(self.driver)
        po.open()
        po.login_action('superadmin','')
        sleep(2)
        error_msg = po.error_hint()
        self.assertEqual(error_msg,u'密码为空，登录失败！')

    def test_login_username_wrong(self):
        '''用户名不正确，密码正确'''
        po = LoginPage(self.driver)
        po.open()
        po.login_action('superadmin1','123456')
        sleep(2)
        error_msg = po.error_hint()
        self.assertEqual(error_msg,u'用户未注册，登录失败！')

    def test_login_pwd_wrong(self):
        '''用户名正确，密码不正确'''
        po = LoginPage(self.driver)
        po.open()
        po.login_action('superadmin','1234567')
        sleep(2)
        error_msg = po.error_hint()
        self.assertEqual(error_msg,u'密码错误，登录失败！')

    def test_login_username_pwd_correct(self):
        '''用户名和密码都正确'''
        po = LoginPage(self.driver)
        po.open()
        user = 'superadmin'
        po.login_action(user,'123456')
        sleep(2)
        po2 = IndexPage(self.driver)
        indexmenu = po2.login_success_user()
        self.assertEqual(indexmenu,u'主页')





if __name__ == '__main__':
    # unittest.main()
    suit = unittest.TestSuite()
    suit.addTest(loginTest('test_login_username_pwd_correct'))
    runner = unittest.TextTestRunner()
    runner.run(suit)
