# coding:utf-8
import unittest
import os
import time
import Getbrowser
import sys
from selenium.webdriver.support.ui import WebDriverWait #Need to import package WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains #引入ActionChains鼠标操作类


class OperateMeituan2(unittest.TestCase): #13

    def setUp(self):
        self.driver = Getbrowser.Chrome()
        
    def testOperateDialog(self): 
        driver = self.driver
        URL = 'http://e.waimai.meituan.com/?time=1544932839557#/v2/order/history'
        driver.get(URL)

        driver.add_cookie({'name': 'uuid', 'value': '56f309a2b7584333ab14.1540818721.1.0.0'})
        driver.add_cookie({'name': '_lxsdk_cuid', 'value': '166bffb6b5fc8-09facd9a4e80f3-346a7809-fa000-166bffb6b5fc8'})
        driver.add_cookie({'name': '_lxsdk', 'value': '166bffb6b5fc8-09facd9a4e80f3-346a7809-fa000-166bffb6b5fc8'})
        driver.add_cookie({'name': '_lxsdk_s', 'value': '167b58ea190-c0c-834-e45%7C%7C4'})
        driver.add_cookie({'name': 'device_uuid', 'value': '!6bd3ac40-df10-4d14-8a95-8502d87f979f'})
        driver.add_cookie({'name': 'uuid_update', 'value': 'true'})
        driver.add_cookie({'name': 'wpush_server_url', 'value': 'wss://wpush.meituan.com'})
        driver.add_cookie({'name': 'shopCategory', 'value': 'food'})
        driver.add_cookie({'name': 'JSESSIONID', 'value': '17d4694y5973ezcwow8yr4q5u'})
        driver.add_cookie({'name': '_ga', 'value': 'GA1.2.1699851629.1541557091'})
        driver.add_cookie({'name': 'pushToken', 'value': '0eH2luv8S8TizlUcTsM4NeTtHWIxeK4L4uTsSfOcyY5I*'})
        driver.add_cookie({'name': 'acctId', 'value': '22946079'})
        driver.add_cookie({'name': 'brandId', 'value': '-1'})
        driver.add_cookie({'name': 'wmPoiId', 'value': '-1'})
        driver.add_cookie({'name': 'isOfflineSelfOpen', 'value': '0'})
        driver.add_cookie({'name': 'isChain', 'value': '1'})
        driver.add_cookie({'name': 'existBrandPoi', 'value': 'true'})
        driver.add_cookie({'name': 'ignore_set_router_proxy', 'value': 'true'})
        driver.add_cookie({'name': 'token', 'value': '0sruiZYGctdTyDjyqHhiyYpoMeAKMLzDgjuK_GeQfhBo*'})
        driver.add_cookie({'name': 'set_info', 'value': '%7B%22wmPoiId%22%3A-1%2C%22ignoreSetRouterProxy%22%3Atrue%7D'})
        driver.add_cookie({'name': 'setPrivacyTime', 'value': '3_20181216'})
        time.sleep(5)
        driver.switch_to_frame('hashframe')

        print(driver.current_url) # "current_url" to get the page title URL address on current page
        print(driver.page_source) # "page_source" to get the page source on current page

        # driver.find_element_by_id('login').send_keys('zgkf1888') #The username box which showed on a new dialog below on 'tang-content'
        # time.sleep(2)
        #
        # driver.find_element_by_name('password').send_keys('zgkf123') #The password box which showed on a new dialog below on 'tang-content'
        # time.sleep(2)
        #
        # driver.find_element_by_css_selector('button[type=submit]').click() #The login button which showed on a new dialog below on 'tang-content'
        # time.sleep(2)
        #
        # # ActionChains(driver).drag_and_drop(driver.find_element_by_id('yodaBoxWrapper').find_element_by_id('yodaBox'), driver.find_element_by_id('yodaMoveingBar')).perform()
        # # ActionChains(driver).context_click(driver.find_element_by_id('yodaBoxWrapper').find_element_by_id('yodaBox')).perform()
        # ActionChains(driver).click_and_hold(driver.find_element_by_id('yodaBoxWrapper').find_element_by_id('yodaBox')).perform()
        # for index in range(200):
        #     try:
        #         ActionChains(driver).move_by_offset(10, 0).perform()  # 平行移动鼠标
        #     except Exception:
        #         break
        #     ActionChains(driver).reset_actions()
        #     time.sleep(0.1)  # 等待停顿时间
        # time.sleep(2)
        #
        # cookies = driver.get_cookies()  # get_cookies() to get cookies from current page
        # for cookie in cookies:
        #     print(
        #     "%s -> %s" % (cookie['name'], cookie['value']))  # To get all 'name' and 'value' cookies on current page
        # print("==================================================")
        # print(cookies)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
