from selenium import webdriver
from testcases.pages.basePage import Page
from selenium.webdriver.common.by import By
from time import sleep

class AddCompanyPage(Page):

    add_company_text_loc = (By.CSS_SELECTOR,'.y-co-blue.y-mb20')
    company_code_loc = (By.XPATH,'html/body/app-root/div/app-home/div/app-content/div/app-test-account/section[1]/div/div/form/div[1]/div[1]/input')
    company_name_loc = (By.XPATH,'html/body/app-root/div/app-home/div/app-content/div/app-test-account/section[1]/div/div/form/div[1]/div[2]/input')
    contact_person_loc = (By.XPATH,'html/body/app-root/div/app-home/div/app-content/div/app-test-account/section[1]/div/div/form/div[1]/div[3]/input')
    company_phone_loc = (By.XPATH,'html/body/app-root/div/app-home/div/app-content/div/app-test-account/section[1]/div/div/form/div[2]/div/input')
    goal_testing_loc = (By.XPATH,'html/body/app-root/div/app-home/div/app-content/div/app-test-account/section[1]/div/div/form/div[3]/div/input')
    content_testing_loc = (By.XPATH,'html/body/app-root/div/app-home/div/app-content/div/app-test-account/section[1]/div/div/form/div[4]/div/input')
    add_button_loc = (By.XPATH,'html/body/app-root/div/app-home/div/app-content/div/app-test-account/section[1]/div/div/div/button')
    modify_button_loc = (By.XPATH,'html/body/app-root/div/app-home/div/app-content/div/app-test-account/section[1]/div/div/div/button')
    add_testing_account_loc = (By.XPATH,'html/body/app-root/div/app-home/div/app-content/div/app-test-account/section[2]/h4/button')




    def company_text_title(self):
        print('找到测试单位了吗',self.find_element(*self.add_company_text_loc).text)
        return self.find_element(*self.add_company_text_loc).text

    def company_code(self,text):
        self.find_element(*self.company_code_loc).send_keys(text)

    def company_name(self,text):
        self.find_element(*self.company_name_loc).send_keys(text)

    def contact_person(self, text):
        self.find_element(*self.contact_person_loc).send_keys(text)

    def company_phone(self, text):
        self.find_element(*self.company_phone_loc).send_keys(text)

    def goal_testing(self, text):
        self.find_element(*self.goal_testing_loc).send_keys(text)

    def content_testing(self, text):
        self.find_element(*self.content_testing_loc).send_keys(text)

    def add_button(self):
        self.find_element(*self.add_button_loc).click()

    def modify_button(self):
        return self.find_element(*self.modify_button_loc).text

    def add_testing_account(self):
        print('找到按钮啦',self.find_element(*self.add_testing_account_loc).text)
        self.find_element(*self.add_testing_account_loc).click()

    def add_company_action(self,code,name,person,phone,goal,content):
        self.company_code(code)
        self.company_name(name)
        self.contact_person(person)
        self.company_phone(phone)
        self.goal_testing(goal)
        self.content_testing(content)
        self.add_button()
        sleep(3)
        self.add_testing_account()



