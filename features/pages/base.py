import time
from random import randint

from selenium import webdriver
from selenium.webdriver.common.by import By
from features.utils.env_const import EnvConst
import os

from time import sleep

class BasePage():

    BASE_URL = EnvConst.BASE_URL
    DEBUG_STOP_MARKER = EnvConst.DEBUG_STOP_MARKER
    MAKE_SCREENSHOT = EnvConst.MAKE_SCREENSHOT
    BETWEEN_STEPS_WAIT = EnvConst.BETWEEN_STEPS_WAIT

    #set by default
    BROWSER_NAME = EnvConst.BROWSER_NAME
    BROWSER_VERSION = EnvConst.BROWSER_VERSION
    #BROWSER_NAME = os.environ

    feature_name = "feature_name"
    scenario_name = "scenario_name"

    def __init__(self):
        #self.browser = webdriver.Chrome()

        self.install_env_settings()

        capabilities = {
            "browserName": self.BROWSER_NAME,
            "browserVersion": self.BROWSER_VERSION,
            "screenResolution": "1920x1080x24",
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": True,
            }
        }

        #http://localhost:4444/wd/hub
        #http://127.0.0.1:4444/wd/hub
        #http://0.0.0.0:4444/wd/hub
        self.browser = webdriver.Remote(
            command_executor="http://0.0.0.0:4444/wd/hub",
            desired_capabilities=capabilities)

        #self.browser.get(self.BASE_URL)

    def install_env_settings(self):
        print("install_env_settings")
        # if not os.environ["BROWSER"]:
        #     raise ("Env variable BROWSER is not set!")
        #
        # if not os.environ["VERSION"]:
        #     raise ("Env variable VERSION is not set!")

        self.BROWSER_NAME = os.environ["BROWSER"]
        self.BROWSER_VERSION = os.environ["VERSION"]

        print(self.BROWSER_NAME)
        print(self.BROWSER_VERSION)

    def get_browser(self):
        return self.browser

    def set_scenario_name(self, value):
        self.scenario_name = value

    def get_scenario_name(self):
        return str(self.scenario_name)

    def set_feature_name(self, value):
        self.feature_name = value

    def set_browser_settings(self):
        self.browser.maximize_window()

    def open_url(self):
        print(self.BASE_URL)
        self.browser.get(self.BASE_URL)
        self.browser.implicitly_wait(1)

    def click_on_button_by_css(self,selector):
        Btn = self.browser.find_element(By.CSS_SELECTOR, selector)
        Btn.click()
        self.browser.implicitly_wait(1)

    def after_handle(self):
        time.sleep(self.BETWEEN_STEPS_WAIT)

        if(self.MAKE_SCREENSHOT):
            print("make scr")

            sub_str = self.get_scenario_name().split('"')[1].split('"')[0]

            #print(self.get_scenario_name())
            #print(sub_str)

            # file = open("./output_data/output.txt", "a")
            # file.write("1 index.py \n")
            # file.close()

            filename = sub_str +"_"+ str(randint(100,1000))+".png"
            print(filename)
            self.browser.save_screenshot("output_data/scroots/"+filename)

        #if(self.DEBUG_STOP_MARKER):
            # time.sleep(0.25)
            #time.sleep(0.5)

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

    def is_enabled_element_by_xpath(self, xpath):
        return self.browser.find_element(By.XPATH, xpath).is_enabled()

    def find_element_by_css(self, css):
        elem = self.browser.find_element(By.CSS_SELECTOR, css)
        if(elem):
            return elem
        else:
            return False