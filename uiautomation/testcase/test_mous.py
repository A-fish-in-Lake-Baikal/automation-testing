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
        url = method.get_url()
        page = request.Request(url)
        page_info = request.urlopen(page).read().decode('utf-8')
        soup = BeautifulSoup(page_info, 'html.parser')
        links = soup.find_all('img',src=re.compile(r'.jpg$'))
        for link in links:
            print(link)



if __name__ == '__main__':
    unittest.main()