# coding=utf-8
import time
import unittest
from urllib import request
from bs4 import BeautifulSoup
import re
from uiautomation.framework.logger import Logger
from uiautomation.framework.browser_engine import BrowserEngine
from uiautomation.framework.browser_method import Browser_method

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
        method.screen_sysrq("专题图片")
        time.sleep(3)
        logger.info("log in success.")


    def test2(self):
        method = Browser_method(self.driver)
        method.back()
        btn1 = self.driver.find_element_by_xpath("//*[@id='main-slide']/div[4]/i[1]")
        method.mouse_hover(btn1)
        method.screen_sysrq("第一张")
        btn2 = self.driver.find_element_by_xpath("//*[@id='main-slide']/div[4]/i[2]")
        method.mouse_hover(btn2)
        method.screen_sysrq("第二张")
        btn3 = self.driver.find_element_by_xpath("//*[@id='main-slide']/div[4]/i[3]")
        method.mouse_hover(btn3)
        method.screen_sysrq("第三张")
        method.set_scrollTop("10000")
        method.screen_sysrq("首页底部")
        time.sleep(2)
        method.set_scrollTop("0")
    def test3(self):
        method = Browser_method(self.driver)
        self.driver.find_element_by_xpath("//*[text()='少女映画']").click()
        time.sleep(3)
        method.is_alert_present()



if __name__ == '__main__':
    unittest.main()