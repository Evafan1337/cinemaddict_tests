from behave import *

# Temp
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

@given("website is open, all movies parameter set, sort is default")
def step(context):
    context.browserWindow.click_on_button_by_xpath("/ html / body / main / nav / div / a[1]")
    context.browserWindow.click_on_button_by_xpath("/html/body/main/ul/li[1]/a")

@when("we click on sort by date")
def step(context):
    context.browserWindow.click_on_button_by_xpath("/html/body/main/ul/li[2]/a")

@then("compare all films and check this release date")
def step(context):
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
    films_date = []
    for film in films_founded:
        films_date.append(film.find_element(By.CSS_SELECTOR, ".film-card__year").text)

    #make helper
    flag = 0
    test_list1 = films_date[:]
    test_list1.sort(reverse = True)
    if(test_list1 == films_date):
        flag = 1
    if(flag):
        pass