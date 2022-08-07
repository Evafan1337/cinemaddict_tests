from behave import *
from features.pages.base import BasePage

# Temp
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

@given("website is open and all movies parameter set")
def open(context):
    # main - navigation__item - -active
    # create check for success click?
    allMoviesButton = context.browserWindow.click_on_button_by_xpath("/ html / body / main / nav / div / a[1]")

@when("we click on watchlist button")
def step(context):
    context.browserWindow.click_on_button_by_xpath("/html/body/main/nav/div/a[2]")
    context.browserWindow.after_handle()

@when("we click on history button")
def step(context):
    context.browserWindow.click_on_button_by_xpath("/html/body/main/nav/div/a[3]")
    context.browserWindow.after_handle()

@when("we click on favorites button")
def step(context):
    context.browserWindow.click_on_button_by_xpath("/html/body/main/nav/div/a[4]")
    context.browserWindow.after_handle()

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
            time.sleep(2)

    films_founded = context.browserWindow.browser.find_elements(By.CSS_SELECTOR, ".film-card")
    films_count = len(films_founded)

    films_count_menu = context.browserWindow.browser.find_element(By.CSS_SELECTOR, ".main-navigation__item--active").text

    if films_count == films_count_menu:
        pass

@then("return on all movies view")
def step(context):
    context.browserWindow.click_on_button_by_xpath("/html/body/main/nav/div/a[1]")
    context.browserWindow.after_handle()
