from selenium import webdriver
import unittest
import os
from time import sleep


class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':

    class Test(MyTest):

        def test_case(self):
            self.driver.get("http://www.baidu.com")
            self.driver.find_element_by_id("kw").send_keys("unittest")
            self.driver.find_element_by_id("su").click()
            sleep(2)

    unittest.main()