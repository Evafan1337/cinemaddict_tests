from behave import *
from features.pages.base import BasePage

# @when ("we open website")
# def step(context):
#     context.browserWindow = BasePage()
#     context.browserWindow.openUrl()

# @then ("website is open")
# def step(context):
#     context.browserWindow.title = "Cinemaddict"
#     pass

@when ("we click on stats button")
def step(context):
    context.browserWindow.clickOnButtonByCSS(".main-navigation__additional")

@when("we can see stats page")
def step(context):
    pass