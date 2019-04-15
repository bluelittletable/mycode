from time import sleep
import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
from testcases.common.myunit import MyTest
from testcases.pages.indexPage import IndexPage
from testcases.pages.loginPage import LoginPage
from testcases.pages.addcompanyPage import AddCompanyPage
from testcases.pages.addaccountPage import AddAccountPage

class accountManage(MyTest):
    '''进入测试账号管理页面，准备添加测试账号'''
    def add_account(self):
        po = LoginPage(self.driver)
        po.openHomePage()
        po.login_action('superadmin','123456')
        sleep(2)
        self.addAccountbutton()

    def addAccountbutton(self):
        po2 = IndexPage(self.driver)
        po2.addAccount_action()
        sleep(2)
        po3 = AddAccountPage(self.driver)
        company_text = po3.company_text_title()
        # print('company_text....',company_text)
        self.assertEqual(company_text,u'测试单位')


if __name__ == '__main__':
    # unittest.main()
    suit = unittest.TestSuite()
    suit.addTest(accountManage('test_add_account'))
    runner = unittest.TextTestRunner()
    runner.run(suit)

