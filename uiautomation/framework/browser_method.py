# 浏览器常用操作方法
import time
import os.path
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from uiautomation.framework.logger import Logger

logger = Logger(logger="browser_method").getlog()

class Browser_method(object):

    def __init__(self,driver):
        self.driver=driver

    # 返回上一页
    def back(self):
        self.driver.back()
        logger.info("后退")

    # 前进
    def forward(self):
        self.driver.forward
        logger.info("前进")

    # 刷新
    def refresh(self):
        self.driver.refresh()
        logger.info("刷新页面")



    # 进入iframe
    def go_iframe(self,frame):
        self.driver.switch_to.frame(frame)
        logger.info("进入frame %s" %frame)

    # 退出iframe
    def exit_iframe(self):
        self.driver.switch_to.default_content()
        logger.info("退出iframe")

    # 打开一个新的tab
    def new_tab(self):
        self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL+'t') #  触发ctrl + t
        logger.info("新建tab")

    # 获取当前页面的title
    def get_title(self):
        logger.info(self.driver.title)
        '''t = self.driver.title
        return t
'''

    # 获取浏览器版本号
    def get_version(self):
        logger.info(self.driver.capabilities['version'])
    # 截图
    def screen_sysrq(self,name):
        file_path = os.path.dirname(os.getcwd()) + '/Screenshots/'
        # rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        # screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(file_path+name+'.png')
            logger.info(u"开始截图并保存")

        except Exception as e:
            logger.error(u"出现异常", format(e))

    # alert弹出窗监控
    @property
    def alert_monit(self):
        try:
            alert = self.driver.switch_to.alert
            logger.info(alert.text)
        except Exception as e:
            print(format(e))


# 鼠标方法
    #     右击context_click()
    def mouse_rightclick(self,name1):
        ActionChains(self.driver).context_click(name1).perform()
        logger.info("鼠标右击")
    #     双击double_click()
    def mouse_doubleclick(self,name2):
        ActionChains(self.driver).double_click(name2).perform()
        logger.info("鼠标双击")
    #     拖动drag_and_drop()
    def mouse_drag_and_drop(self,name3):
        ActionChains(self.driver).drag_and_drop(name3).perform()
        logger.info("鼠标拖动")
    #     鼠标悬停move_to_element()
    def mouse_hover(self,name4):
        ActionChains(self.driver).move_to_element(name4).perform()
        logger.info("鼠标悬停")

# 操作cookie
    #获取cookie
    def get_cookie(self):
        cookie = self.driver.get_cookies()
        logger.info(cookie)
        return cookie
