from features.pages.base import BasePage

# def before_scenario(context, scenario):
#     context.browserWindow = BasePage()
#     context.browserWindow.open_url()

def before_all(context):
    context.browserWindow = BasePage()
    context.browserWindow.open_url()
    context.browserWindow.set_browser_settings()

def after_all(context):
    context.browserWindow.browser.quit()