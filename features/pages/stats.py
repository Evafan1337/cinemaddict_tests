from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from base import BasePage

class StatsPage(BasePage):

    BASE_URL = "http://localhost:8081/"

    def setBrowserSettings(self):
        self.browser.maximize_window()

    def openUrl(self):
        self.browser.get(self.BASE_URL)
        self.browser.implicitly_wait(1)