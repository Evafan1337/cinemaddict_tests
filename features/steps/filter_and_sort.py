from behave import *

# Temp
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

@given("filter_and_sort.website is open, all movies parameter set, sort is default")
def step(context):
    context.browserWindow.click_on_button_by_xpath("/ html / body / main / nav / div / a[1]")
    context.browserWindow.click_on_button_by_xpath("/html/body/main/ul/li[1]/a")