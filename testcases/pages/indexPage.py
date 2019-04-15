from selenium.webdriver.common.by import By
from testcases.pages.basePage import Page

class IndexPage(Page):

    homepage_menu_loc = (By.CSS_SELECTOR,'.treeview>a>span')
    accountmanage_menu_loc = (By.XPATH,'html/body/app-root/div/app-home/div/app-menu/aside/section/ul/li[4]/a/span')
    addaccount_button_loc = (By.XPATH,'html/body/app-root/div/app-home/div/app-content/div/app-test-account-statistics/section[2]/h4/a[1]')

    def login_success_user(self):
        print('进入首页了吗',self.find_element(*self.homepage_menu_loc).text)
        return self.find_element(*self.homepage_menu_loc).text

    def goAccountManage(self):
        print('找到测试账号管理了吗', self.find_element(*self.accountmanage_menu_loc).text)
        self.find_element(*self.accountmanage_menu_loc).click()

    def addCount(self):
        print('找到添加了吗', self.find_element(*self.addaccount_button_loc).text)
        self.find_element(*self.addaccount_button_loc).click()

    def addAccount_action(self):
        self.goAccountManage()
        self.addCount()



