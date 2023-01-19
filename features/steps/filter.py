from behave import *
from features.pages.base import BasePage

# Temp
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from features.utils.selectors import Selectors
from features.utils.env_const import EnvConst

import time

@given("website is open and all movies parameter set")
def open(context):

    #Check for opened website
    try:
        element_present = EC.presence_of_element_located((By.XPATH, Selectors.film_list_xpath))
        WebDriverWait(context.browserWindow.get_browser(), EnvConst.TIMEOUT_WAIT).until(element_present)
    except NoSuchElementException:
        print("Timed out waiting for page to load")

    #main-navigation__item main-navigation__item--active
    all_movies_btn_classes = context.browserWindow.get_browser().find_element(By.XPATH, Selectors.all_movies_btn_xpath).get_attribute("class")
    assert Selectors.main_btn_active_class.replace(".","") in all_movies_btn_classes

@when("we click on {btn_value} filter button")
def step(context, btn_value):
    #context.browserWindow.click_on_button_by_xpath("/html/body/main/nav/div/a[2]")
    context.browserWindow.click_on_button_by_xpath(Selectors.filtration_btn_xpath.get(btn_value))

    #context.browserWindow.after_handle()

@then("count films on clicked filter parameter and count all films")
def step(context):
    context.browserWindow.click_on_button_by_xpath("/html/body/main/ul/li[1]/a")
    context.browserWindow.after_handle()

    show_more_btn_exist_flag = True
    while show_more_btn_exist_flag:
        try:
            show_more_btn_exist_flag = context.browserWindow.find_element_by_xpath(
                "/html/body/main/section[1]/section[1]/button")

            if show_more_btn_exist_flag:
                context.browserWindow.click_on_button_by_xpath("/html/body/main/section[1]/section[1]/button")
                context.browserWindow.after_handle()
        except NoSuchElementException:
            show_more_btn_exist_flag = False
            # hardcode
            time.sleep(0.10)

    films_founded = context.browserWindow.browser.find_elements(By.CSS_SELECTOR, ".film-card")
    films_count = len(films_founded)

    films_count_menu = context.browserWindow.browser.find_element(By.CSS_SELECTOR, ".main-navigation__item--active").text

    if films_count == films_count_menu:
        pass

@then("return on all movies view")
def step(context):
    context.browserWindow.click_on_button_by_xpath("/html/body/main/nav/div/a[1]")
    #context.browserWindow.after_handle()
