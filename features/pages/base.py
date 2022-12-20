import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from features.utils.env_const import EnvConst

from time import sleep

class BasePage():

    BASE_URL = EnvConst.BASE_URL
    DEBUG_STOP_MARKER = EnvConst.DEBUG_STOP_MARKER

    def __init__(self):
        self.browser = webdriver.Chrome()

    def get_browser(self):
        return self.browser

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
            time.sleep(0.1)

    def click_on_button_by_xpath(self, xpath):
        Btn = self.browser.find_element(By.XPATH, xpath)
        Btn.click()
        self.browser.implicitly_wait(1)

    # click on elem and click on btn is same methods?
    def click_on_elem_by_xpath(self, xpath):
        elem = self.browser.find_element(By.XPATH, xpath)
        elem.click()
        self.browser.implicitly_wait(1)

    def click_on_child_elem(self, parent, child_css):
        elem = parent.find_element(By.CSS_SELECTOR, child_css)
        elem.click()
        self.browser.implicitly_wait(1)

    def find_element_by_xpath(self, xpath):
        elem = self.browser.find_element(By.XPATH, xpath)
        if(elem):
            return elem
        else:
            return False

    def is_visible_element_by_xpath(self, xpath):
        return self.browser.find_element(By.XPATH, xpath).is_displayed()

    def is_visible_element_by_css(self, css):
        return self.browser.find_element(By.CSS_SELECTOR, css).is_displayed()

    def find_element_by_css(self, css):
        elem = self.browser.find_element(By.CSS_SELECTOR, css)
        if(elem):
            return elem
        else:
            return False