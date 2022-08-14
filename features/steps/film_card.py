from behave import *

# Temp
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time


@given("film_card.website is open")
def step(context):
    context.browserWindow.click_on_button_by_xpath("/ html / body / main / nav / div / a[1]")
    context.browserWindow.click_on_button_by_xpath("/html/body/main/ul/li[1]/a")
    context.browserWindow.after_handle()


# Can create one test method
# @when("we click on '{film_count}' film preview")
@when("we click on film preview of film with number {film_count}")
def step(context, film_count):
    film_card_xpath = "// *[ @ id = " + film_count + "]"
    film_card_elem = context.browserWindow.find_element_by_xpath(film_card_xpath)
    context.browserWindow.click_on_child_elem(film_card_elem, ".film-card__poster")
    context.browserWindow.after_handle()


@when("we click on film title of film with number {film_count}")
def step(context, film_count):
    film_card_xpath = "// *[ @ id = " + film_count + "]"
    film_card_elem = context.browserWindow.find_element_by_xpath(film_card_xpath)
    context.browserWindow.click_on_child_elem(film_card_elem, ".film-card__title")
    context.browserWindow.after_handle()


@when("we click on film comment count of film with number {film_count}")
def step(context, film_count):
    film_card_xpath = "// *[ @ id = " + film_count + "]"
    film_card_elem = context.browserWindow.find_element_by_xpath(film_card_xpath)
    context.browserWindow.click_on_child_elem(film_card_elem, ".film-card__comments")
    context.browserWindow.after_handle()


@when("we click on film release date of film with number {film_count}")
def step(context, film_count):
    film_card_xpath = "// *[ @ id = " + film_count + "]"
    film_card_elem = context.browserWindow.find_element_by_xpath(film_card_xpath)
    context.browserWindow.click_on_child_elem(film_card_elem, ".film-card__year")
    context.browserWindow.after_handle()


@when("we click on film genre of film with number {film_count}")
def step(context, film_count):
    film_card_xpath = "// *[ @ id = " + film_count + "]"
    film_card_elem = context.browserWindow.find_element_by_xpath(film_card_xpath)
    context.browserWindow.click_on_child_elem(film_card_elem, ".film-card__genre")
    context.browserWindow.after_handle()


@then("film card is opened")
def step(context):
    # film_card_exist_flag = True
    film_card_exist_flag = context.browserWindow.find_element_by_css(".film-details")
    if film_card_exist_flag:
        pass


@then("we close it")
def step(context):
    context.browserWindow.click_on_button_by_xpath('/html/body/section/form/div[1]/div[1]/button')
    context.browserWindow.after_handle()
