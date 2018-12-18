# coding:utf-8
import unittest
import os
import time
import Getbrowser
import sys
from selenium.webdriver.support.ui import WebDriverWait #Need to import package WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains #引入ActionChains鼠标操作类


class OperateMPKI(unittest.TestCase): #13

    def setUp(self):
        self.driver = Getbrowser.Chrome()
        
    def testOperateDialog(self): 
        driver = self.driver
        URL = 'https://mpki.trustasia.com/#/account/login'
        driver.get(URL)
        time.sleep(5)

        print(driver.current_url) # "current_url" to get the page title URL address on current page
        print(driver.page_source) # "page_source" to get the page source on current page

        driver.find_element_by_css_selector('input[type=text]').send_keys('winfred.sui') #The username box which showed on a new dialog below on 'tang-content'
        time.sleep(2)

        driver.find_element_by_css_selector('input[type=password]').send_keys('sui123') #The username box which showed on a new dialog below on 'tang-content'
        time.sleep(2)
    
        driver.find_element_by_css_selector('button[type=submit]').click() #The login button which showed on a new dialog below on 'tang-content'
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
