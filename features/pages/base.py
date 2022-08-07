import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from time import sleep

class BasePage():

    BASE_URL = "http://localhost:8081/"
    DEBUG_STOP_MARKER = True

    def __init__(self):
        self.service = Service("F:/webdriver/chromedriver.exe")
        self.browser = webdriver.Chrome(service=self.service)

    def set_browser_settings(self):
        self.browser.maximize_window()

    def open_url(self):
        self.browser.get(self.BASE_URL)
        self.browser.implicitly_wait(1)

    def click_on_button_by_css(self,selector):
        Btn = self.browser.find_element(By.CSS_SELECTOR, selector)
        Btn.click()
        self.browser.implicitly_wait(1)

    def after_handle(self):
        if(self.DEBUG_STOP_MARKER):
            # time.sleep(0.25)
            time.sleep(1)

    def click_on_button_by_xpath(self, xpath):
        Btn = self.browser.find_element(By.XPATH, xpath)
        Btn.click()
        self.browser.implicitly_wait(1)

    def find_element_by_xpath(self, xpath):
        elem = self.browser.find_element(By.XPATH, xpath)
        if(elem):
            return elem
        else:
            return False