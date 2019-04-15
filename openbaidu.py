from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.get("http://www.baidu.com")
browser.find_element_by_id("kw").send_keys("远鉴")
browser.find_element_by_id("su").click()
time.sleep(10)
browser.quit()

