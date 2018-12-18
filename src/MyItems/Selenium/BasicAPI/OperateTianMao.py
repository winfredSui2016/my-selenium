# coding:utf-8
import unittest
import os
import time
import Getbrowser
import sys
from selenium.webdriver.support.ui import WebDriverWait #Need to import package WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains #引入ActionChains鼠标操作类
reload(sys)
sys.setdefaultencoding('utf-8')

tianmao_account = u'质馆旗舰店:小质'
tianmao_password = 'essence888666'
sina_account = u'seewd8@sina.cn'
sina_password = 'Suiyue447329961'

class OperateTianMao(unittest.TestCase): #13
    def setUp(self):
        self.driver = Getbrowser.Chrome()
        
    def testOperateDialog(self): 
        driver = self.driver
        URL = 'https://login.taobao.com/member/login.jhtml'
        driver.get(URL)
        try:
            driver.find_element_by_class_name('J_Quick2Static').click()
        except Exception as e:
            time.sleep(2)
        driver.find_element_by_class_name('weibo-login').click()
        driver.find_element_by_css_selector('input[type=text]').send_keys(sina_account) #The username box which showed on a new dialog below on 'tang-content'
        time.sleep(2)
    
        driver.find_element_by_css_selector('input[type=password]').send_keys(sina_password) #The password box which showed on a new dialog below on 'tang-content'
        time.sleep(2)

        for index in range(500):
            try:

                ActionChains(driver).drag_and_drop_by_offset(driver.find_element_by_id('nc_1_n1t').find_element_by_id('nc_1_n1z'), 500, 0).perform()  # 平行移动鼠标，此处直接设一个超出范围的值，这样拉到头后会报错从而结束这个动作
            except Exception as e:
                break
        time.sleep(2)  # 等待停顿时间

        # ActionChains(driver).click_and_hold(driver.find_element_by_id('nc_1_n1t').find_element_by_id('nc_1_n1z')).perform()
        # for index in range(200):
        #     try:
        #         ActionChains(driver).move_by_offset(10, 0).perform()  # 平行移动鼠标
        #     except Exception:
        #         break
        #     ActionChains(driver).reset_actions()
        #     time.sleep(0.1)  # 等待停顿时间
        # time.sleep(20)

        # while True:
        #     try:
        #         ActionChains(driver).drag_and_drop_by_offset(
        #             driver.find_element_by_id('nc_1_n1t').find_element_by_id('nc_1_n1z'), 400, 0).perform()
        #         time.sleep(5)
        #         text = driver.find_element_by_xpath("//div[@class='errloading']/span")
        #         if text.text.startswith(u'哎呀'):
        #             driver.find_element_by_xpath("//div[@class='errloading']/span/a").click()
        #             time.sleep(5)
        #         else:
        #             continue
        #     except Exception as e:
        #         # 这里定位失败后的刷新按钮，重新加载滑块模块
        #         # driver.find_element_by_xpath("//div[@class='errloading']/span/a").click()
        #         print(e)

        driver.find_element_by_css_selector('a[node-type=submitBtn]').click() #The login button which showed on a new dialog below on 'tang-content'
        time.sleep(100)

        cookies = driver.get_cookies()  # get_cookies() to get cookies from current page
        for cookie in cookies:
            print(
            "%s -> %s" % (cookie['name'], cookie['value']))  # To get all 'name' and 'value' cookies on current page
        print("==================================================")
        print(cookies)


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
