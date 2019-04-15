from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from testcases.pages.basePage import Page

class LoginPage(Page):

    #先定位
    username_input =(By.NAME,'username')
    password_input = (By.NAME,'password')
    submit_button = (By.CSS_SELECTOR,'.btn.btn-block.btn-login')
    login_error_hint = (By.XPATH,"html/body/app-root/div/app-login/div/div/div[2]/div/form/div[2]/div/span")


    #再操作

    def openHomePage(self):
        self.driver.get(self.base_url)

    def login_username(self,text):
        self.find_element(*self.username_input).send_keys(text)

    def login_password(self,text='123456'):
        self.find_element(*self.password_input).send_keys(text)

    def login_button(self):
        self.find_element(*self.submit_button).click()

    def login_action(self,username,password):
        self.login_username(username)
        self.login_password(password)
        self.login_button()

    def error_hint(self):
        # print('11111111',self.find_element(*self.login_error_hint).text)
        return self.find_element(*self.login_error_hint).text




