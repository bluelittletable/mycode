from time import sleep
import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
from testcases.common.myunit import MyTest
from testcases.pages.indexPage import IndexPage
from testcases.pages.loginPage import LoginPage
from testcases.pages.addcompanyPage import AddCompanyPage

class AddCompany(MyTest):
    '''添加测试单位'''
    def login(self):
        po = LoginPage(self.driver)
        po.openHomePage()
        po.login_action('superadmin','123456')
        sleep(2)
        self.addCompanytbutton()

    def addCompanytbutton(self):
        po2 = IndexPage(self.driver)
        po2.addAccount_action()
        sleep(2)
        po3 = AddCompanyPage(self.driver)
        company_text = po3.company_text_title()
        # print('company_text....',company_text)
        self.assertEqual(company_text,u'测试单位')
        self.addcompany()

    def addcompany(self):
        po4 = AddCompanyPage(self.driver)
        code = u'0100'
        name = u'北京文化'
        person = u'王大大'
        phone = u'1234567'
        goal = u'测试'
        content = u'测试测试'
        po4.add_company_action(code,name,person,phone,goal,content)
        sleep(10)
        text_button = po4.modify_button()
        self.assertEqual(text_button,u'修改')




if __name__ == '__main__':
    # unittest.main()
    suit = unittest.TestSuite()
    suit.addTest(AddCompany('test_login'))
    runner = unittest.TextTestRunner()
    runner.run(suit)

