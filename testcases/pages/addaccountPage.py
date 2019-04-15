from selenium import webdriver
from testcases.pages.basePage import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class AddAccountPage(Page):

    entry_div_loc = (By.XPATH,'html/body/dialog-holder/dialog-wrapper/div/app-modal-add')
    entry_title_loc = (By.XPATH,'html/body/dialog-holder/dialog-wrapper/div/app-modal-add/div/div/div[1]/h4')
    test_account_loc = (By.XPATH,'html/body/dialog-holder/dialog-wrapper/div/app-modal-add/div/div/div[2]/form/div[1]/div/input')
    password_loc = (By.XPATH,'html/body/dialog-holder/dialog-wrapper/div/app-modal-add/div/div/div[2]/form/div[2]/div/input')
    input_period_loc = (By.XPATH,".//*[@id='testTimeRange']")
    phonelist_loc = (By.XPATH,'html/body/dialog-holder/dialog-wrapper/div/app-modal-add/div/div/div[2]/form/div[4]/div/select')
    confirm_button_loc = (By.XPATH,'html/body/dialog-holder/dialog-wrapper/div/app-modal-add/div/div/div[3]/button[1]')
    testing_accout_list_loc = (By.XPATH,'html/body/app-root/div/app-home/div/app-content/div/app-test-account/section[2]/div/table/tbody/tr[2]/td[3]')


    def entry_div(self):
        self.find_element(*self.entry_div_loc)
        print('找到入口啦',self.find_element(*self.entry_title_loc).text)


    def test_account(self,text):
        self.find_element(*self.test_account_loc).send_keys(text)

    def test_password(self,text):
        self.find_element(*self.password_loc).send_keys(text)

    def test_period(self,text):
        self.find_element(*self.input_period_loc).clear()
        self.find_element(*self.input_period_loc).send_keys(text)
        # self.find_element(*self.input_period_loc).send_keys(Keys.ENTER)

    def test_time_control(self):
        self.find_element(*self.time_control)

    def choose_start_period(self):
        self.find_element(*self.start_period_loc)

    def choose_end_period(self):
        self.find_element(*self.end_period_loc)

    def confirm_period(self):
        self.find_element(*self.confirm_period_loc)

    def test_phone(self):
        return self.find_element(*self.phonelist_loc)

    def confirm_button(self):
        return self.find_element(*self.confirm_button_loc).click()



    def add_account_action(self,account,password,period,tel):
        self.entry_div()
        self.test_account(account)
        self.test_password(password)
        js = 'document.getElementById("testTimeRange").value='+'"'+period+'"'+';'
        self.driver.execute_script(js)
        a = self.test_phone()
        s = Select(a)
        s.select_by_index(tel)
        self.confirm_button()

    def verify_added_result(self):
        print('看看加上了吗',self.find_element(*self.testing_accout_list_loc).text)
        return self.find_element(*self.testing_accout_list_loc).text

