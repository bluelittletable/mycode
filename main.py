import unittest
from HTMLTestRunner import HTMLTestRunner
import time,sys,os,BeautifulReport
from testcases.testcase.login_case1 import loginTest
from testcases.testcase.addaccount_case import AddAccount

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,BASE_PATH)


if __name__ == '__main__':
    # now_time =  time.strftime("%Y_%m_%d_%H_%M_%S")
    # fp = open(now_time+"result.html",'wb')
    # runner = HTMLTestRunner(fp,
    #                        title="IVR测试报告",
    #                        description="运行环境：Windows 7, Chrome")
    #    discover = unittest.defaultTestLoader.discover("./testcases", pattern='*_case.py')
    #
    # runner.run(discover)
    # fp.close()

    suite = unittest.TestSuite()
    all_cases = unittest.defaultTestLoader.discover('./testcases','*_case.py')
    [suite.addTests(case) for case in all_cases]
    report_obj = BeautifulReport.BeautifulReport(suite)
    report_obj.report(filename='test',description='测试报告',log_path='./report')



# if __name__ == '__main__':
#     test_app = "./mail_app" #定义测试应用
#     now_time =  time.strftime("%Y_%m_%d_%H_%M_%S")
#     fp = open(test_app+"/report/"+now_time+"result.html",'wb')
#     runner = HTMLTestRunner(fp,
#                            title="xxx测试报告",
#                            description="运行环境：windows 10, firefox")
#     discover = unittest.defaultTestLoader.discover(test_app+"/test_case", pattern='*_case.py')
#     runner.run(discover)
#     fp.close()

# def run():
#     g = GetCase()
#     g.create_py()
#     suite = unittest.TestSuite()
#     all_cases = unittest.defaultTestLoader.discover(PY_PATH,'Test*.py')
#     [suite.addTests(case) for case in all_cases]
#     report_obj = BeautifulReport.BeautifulReport(suite)
#     report_obj.report(filename='utp',log_path=REPORT_PATH,description='测试报告')


