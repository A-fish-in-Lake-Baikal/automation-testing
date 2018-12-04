# coding=utf-8
import time
import unittest
from uiautomation.framework.logger import Logger
from uiautomation.framework.browser_engine import BrowserEngine
from uiautomation.framework.browser_method import Browser_method

logger = Logger(logger="testing").getlog()
class MasterStation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)
        logger.info("Now, Open the browser.")

    @classmethod
    def tearDownClass(cls):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        logger.info("Now, Close and quit the browser.")
        cls.driver.quit()

        # 登录
    def test1(self):
        method = Browser_method(self.driver)
        self.driver.find_element_by_xpath("//*[text()='新闻']").click()
        time.sleep(3)
        logger.info("成功打开新闻页面.")
        time.sleep(2)


if __name__ == '__main__':
    unittest.main()