# coding=utf-8
import time
import unittest
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
    def test_log_in(self):
        method = Browser_method(self.driver)
        method.alert_monit()
        self.driver.find_element_by_xpath("//*[@class='png-icon login-btn']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='login-username']").send_keys(r"admin")
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='login-password']").send_keys("00000")
        self.driver.find_element_by_xpath("//*[@id='login-btn']").click()
        method.screen_sysrq("登录成功")
        method.alert_monit()
        logger.info("log in success.")

    # 页面内容检查
    def test_home_page_assert(self):
        # 检查总站首页是否有总站按钮
        method = Browser_method(self.driver)
        try:
            logo = self.driver.find_element_by_xpath("//*[@class='png-icon master-icon toMasterPage']").is_displayed()
            logger.info("成功找到总站按钮")
        except Exception as e:
            logger.error("总站按钮不存在")
            method.screen_sysrq("总站按钮不存在")
        # 断言:最新推荐是否存在
        try:
            new_Recommended = self.driver.find_element_by_xpath("//*[text()='最新推荐']").is_displayed()
            self.driver.find_element_by_xpath("//*[text()='最新推荐']").click()
            logger.info("New Recommended pass")
        except Exception as e:
            logger.error("New Recommended not found!!", format(e))
            method.screen_sysrq("没有最新推荐")
        time.sleep(1)

        # 断言:最新公告是否存在
        try:
            latest_announcement = self.driver.find_element_by_xpath("//*[text()='最新公告']").is_displayed()
            self.driver.find_element_by_xpath("//*[text()='最新公告']").click()
            logger.info("latest announcement pass")
        except Exception as e:
            logger.error("latest announcement not found!!", format(e))
            method.screen_sysrq("没有最新公告")
        time.sleep(1)

        # 断言:应用与下载是否存在
        try:
            download_app = self.driver.find_element_by_xpath("//*[text()='应用与下载']").is_displayed()
            self.driver.find_element_by_xpath("//*[text()='应用与下载']").click()
            logger.info("download app pass")
        except Exception as e:
            logger.error("download app not found!!", format(e))
            method.screen_sysrq("没有应用与下载")
        time.sleep(1)

        # 断言:最新排行是否存在
        try:
            newest_ranking = self.driver.find_element_by_xpath("//*[text()='最新排行']").is_displayed()
            self.driver.find_element_by_xpath("//*[text()='最新排行']").click()
            logger.info("newest ranking pass")
        except Exception as e:
            logger.error("newest ranking not found!!", format(e))
            method.screen_sysrq("没有最新排行")
        time.sleep(1)

        # 断言:最新上传是否存在
        try:
            newest_upload = self.driver.find_element_by_xpath("//*[text()='最新上传']").is_displayed()
            self.driver.find_element_by_xpath("//*[text()='最新上传']").click()
            logger.info("newest upload pass")
        except Exception as e:
            logger.error("newest upload not found", format(e))
            method.screen_sysrq("没有最新上传")
        time.sleep(1)

        # 断言:好评排行是否存在
        try:
            ranking_list = self.driver.find_element_by_xpath("//*[text()='好评排行']").is_displayed()
            self.driver.find_element_by_xpath("//*[text()='好评排行']").click()
            logger.info("ranking list pass")
        except Exception as e:
            logger.error("ranking list not found", format(e))
            method.screen_sysrq("没有好评排行")
        time.sleep(1)

        # 断言:所有站点是否存在
        try:
            all_site = self.driver.find_element_by_xpath("//*[text()='所有站点']").is_displayed()
            self.driver.find_element_by_xpath("//*[text()='所有站点']").click()
            logger.info("all site pass")
        except Exception as e:
            logger.error("all site not found", format(e))
            method.screen_sysrq("没有所有站点")
        time.sleep(1)
        # 断言:数据统计是否存在
        try:
            data_statistics = self.driver.find_element_by_xpath("//*[text()='数据统计']").is_displayed()
            self.driver.find_element_by_xpath("//*[text()='数据统计']").click()
            logger.info("data statistics pass")
        except Exception as e:
            logger.error("data statistics not found", format(e))
            method.screen_sysrq("没有数据统计")
        time.sleep(1)

        logger.info("assert success.")

    # 搜索
    def test_home_page_search(self):
        method = Browser_method(self.driver)
        self.driver.find_element_by_xpath("//*[@class='form-control' and @id='search-input']").clear()
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@class='form-control' and @id='search-input']").send_keys("1")
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@class='btn png-icon search-icon']").click()
        method.alert_monit()
        time.sleep(2)
        method.back()
        method.alert_monit()
        logger.info("search success.")

if __name__ == '__main__':
    unittest.main()