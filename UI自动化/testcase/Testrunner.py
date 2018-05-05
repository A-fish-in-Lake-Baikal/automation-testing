# Testrunner方法
import unittest
import time
import os.path
import HTMLTestRunner


'''case = unittest.TestSuite()
case.addTest(Search('test_search1'))
case.addTest(Search('test_search2'))
case.addTest(MasterStation('test_log_in'))
case.addTest(MasterStation('test_home_page_assert'))
case.addTest(MasterStation('test_home_page_search'))
'''

# 设置报告文件保存路径  
report_path=os.path.dirname(os.path.abspath('.'))+'/test_report/'
# 获取系统当前时间  
now=time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
# 设置报告名称格式  
HtmlFile=report_path+now+"HTMLtemplate.html"
fp =open(HtmlFile,"wb")

# discover方法

suite = unittest.TestLoader().discover("testcase")

if __name__=='__main__':
    #执行用例  
    # runner=unittest.TextTestRunner()
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title = u"RC2.3.3搜索功能测试报告",description = u"用例测试情况")
    runner.run(suite)
