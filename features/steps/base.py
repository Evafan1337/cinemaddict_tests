from behave import *
from features.pages.base import BasePage

@when ("we open website")
def step(context):
    context.browserWindow = BasePage()
    context.browserWindow.openUrl()


@then ("website is open")
def step(context):
    context.browserWindow.title = "Cinemaddict"
    print('ok!')
    pass