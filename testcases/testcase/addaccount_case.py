from time import sleep
import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
from testcases.common.myunit import MyTest
from testcases.pages.indexPage import IndexPage
from testcases.pages.loginPage import LoginPage
from testcases.pages.addcompanyPage import AddCompanyPage
from testcases.testcase.addcompany_c import AddCompany
from testcases.pages.addaccountPage import AddAccountPage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from testcases.common.db_mysql import Op_mysql


class AddAccount(MyTest):
    '''添加测试账号'''

    def test_login(self):
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
        code = u'0200'
        name = u'北京文化'
        person = u'王大大'
        phone = u'1234567'
        goal = u'测试'
        content = u'测试测试'
        po4.add_company_action(code,name,person,phone,goal,content)
        sleep(3)
        text_button = po4.modify_button()
        self.add_account()

    def add_account(self):
        po1 = AddAccountPage(self.driver)
        account = 'hello'
        password = 'hello'
        period = '2014-10-12 - 2014-10-13'
        tel = '1'
        po1.add_account_action(account,password,period,tel)
        result = po1.verify_added_result()
        self.assertEqual(result,u'hello')
        self.del_info()

    def del_info(self):
        delinfo = Op_mysql('10.10.11.38','fosafer','fosafer@com',db='ivr_new')
        result1 = delinfo.execute("delete from ivr_company where company_name = '北京文化' ;")
        result2 = delinfo.execute("delete from u_user where username = 'hello' ;")
        self.assertEqual(result1,u'OK')
        self.assertEqual(result2,u'OK')



if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(AddAccount('test_login'))
    runner = unittest.TextTestRunner()
    runner.run(suit)

