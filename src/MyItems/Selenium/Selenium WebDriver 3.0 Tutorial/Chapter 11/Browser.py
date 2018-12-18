import os
from selenium import webdriver

def IE():
    if os.name == 'nt':
        IEDriver = os.path.abspath(os.path.join(os.path.dirname("__file__"),os.path.pardir,os.path.pardir,'Drivers','IEDriverServer.exe'))
        #IEDriver = os.path.join(os.path.abspath('..'),'Drivers','IEDriverServer.exe')
        os.environ["webdriver.ie.driver"] = IEDriver
        driver = webdriver.Ie(IEDriver)
        driver.maximize_window()
    else:
        print ("IE cannot be ran on non-Windows system!")
    return driver

def Chrome():
    if os.name == 'nt':
        CDriver = os.path.abspath(os.path.join(os.path.dirname("__file__"),os.path.pardir,os.path.pardir,'Drivers','chromedriver.exe'))
        #CDriver = os.path.join(os.path.abspath('..'),'Drivers','chromedriver.exe')
    elif os.name == 'posix':
        CDriver = os.path.abspath(os.path.join(os.path.dirname("__file__"),os.path.pardir,os.path.pardir,'Drivers','chromedriver.exe'))
        #CDriver = os.path.join(os.path.abspath('..'),'Drivers','chromedriver.exe')
    os.environ["webdriver.chrome.driver"] = CDriver
    driver = webdriver.Chrome(CDriver)
    driver.maximize_window()
    return driver

def Firefox():
    if 'nt' in os.name:
        FFDriver = "C:\Program Files\Mozilla Firefox"
        os.environ["PATH"] = FFDriver
    elif 'posix' in os.name:
        FFDriver = os.path.abspath(os.path.join(os.path.dirname("__file__"),os.path.pardir,os.path.pardir,'Drivers','geckodriver'))
        #FFDriver = os.path.join(os.path.abspath('..'),'Drivers','geckodriver')
        os.environ["webdriver.gecko.driver"] = FFDriver
    driver = webdriver.Firefox()
    driver.maximize_window()
    return driver
