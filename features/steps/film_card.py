from behave import *

# Temp
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

from features.utils.selectors import Selectors
from features.utils.env_const import EnvConst



@given("film_card.website is open")
def step(context):

    if(context.browserWindow.get_scenario_name() is not context.scenario):
        #context.scenario_name = context.scenario
        context.browserWindow.set_scenario_name(context.scenario)

    try:
        element_present = EC.presence_of_element_located((By.XPATH, Selectors.film_list_xpath))
        WebDriverWait(context.browserWindow.get_browser(), EnvConst.TIMEOUT_WAIT).until(element_present)
    except NoSuchElementException:
        print("Timed out waiting for page to load")

    context.browserWindow.click_on_button_by_xpath(Selectors.all_movies_btn_xpath)
    context.browserWindow.click_on_button_by_xpath(Selectors.sort_by_default_xpath)

    #context.browserWindow.after_handle()
    assert context.browserWindow.is_visible_element_by_xpath(Selectors.film_list_xpath) == True

# Can create one test method
# @when("we click on '{film_count}' film preview")
@when("we click on film {elem_to_locate} of film with number {film_count}")
def step(context, film_count, elem_to_locate):
    film_card_locator = Selectors.film_card_class.get(elem_to_locate)
    film_card_xpath = "// *[ @ id = " + film_count + "]"
    film_card_elem = context.browserWindow.find_element_by_xpath(film_card_xpath)
    context.browserWindow.click_on_child_elem(film_card_elem, film_card_locator)

    assert context.browserWindow.is_visible_element_by_css(Selectors.film_card_class.get("details")) == True
    #.browserWindow.after_handle()

@then("film card is {visible_status}")
def step(context, visible_status):
    if visible_status == "visible":
        assert context.browserWindow.is_visible_element_by_css(Selectors.film_card_class.get("details")) == True
    else:
        assert context.browserWindow.is_visible_element_by_css(Selectors.film_card_class.get("details")) == False

@then("we close it")
def step(context):
    context.browserWindow.click_on_button_by_xpath('/html/body/section/form/div[1]/div[1]/button')
    context.browserWindow.get_browser().implicitly_wait(0.25)

    element = WebDriverWait(context.browserWindow.get_browser(), 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/main/section[1]/section[1]/div"))
    )

    #ActionChains(context.browserWindow.get_browser()).send_keys(Keys.ESCAPE).perform()
    #context.browserWindow.after_handle()
