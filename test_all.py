import unittest,time,os,multiprocessing
# import HTMLTestRunner
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.maximize_window()
driver.implicitly_wait(10)

# 查找元素
# 关键字输入框
driver.find_element_by_css_selector('#kw').send_keys('selenium')
driver.find_element_by_css_selector('.bg s_btn').click()
time.sleep(2)

driver.quit()
