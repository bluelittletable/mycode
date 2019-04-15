class Page(object):
    '''页面基础类'''

    def __init__(self,driver,base_url = u'http://10.10.11.38:8081'):
        self.driver = driver
        self.base_url = base_url
        self.timeout = 30

    def open(self):
        self.driver.get(self.base_url)



    def find_element(self,*loc):
        return self.driver.find_element(*loc)

    def input_text(self,loc,text):
        self.find_element(*loc).send_keys(text)

    def click(self,loc):
        self.find_element(*loc).click()

    def get_title(self):
        return self.driver.title

    def script(self,src):
        return self.driver.execute_script(src)