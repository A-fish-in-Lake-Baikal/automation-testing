# coding=utf-8
import time
import unittest
from selenium.webdriver.common.action_chains import ActionChains
from framework.logger import Logger
from framework.browser_engine import BrowserEngine
from framework.browser_method import Browser_method

logger = Logger(logger="master station page").getlog()


class MasterStation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

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
        self.driver.find_element_by_xpath("//*[text()='动漫图片']").click()
        time.sleep(2)
        method.screen_sysrq("专题内容")
        time.sleep(3)
        logger.info("log in success.")


    '''def test2(self):
        method = Browser_method(self.driver)
        record = self.driver.find_element_by_xpath("//*[@class='png-icon p-history-icon']")
        actions = ActionChains(self.driver)
        actions.move_to_element(method)
        time.sleep(3)
        method.screen_sysrq("播放记录截图")'''



if __name__ == '__main__':
    unittest.main()