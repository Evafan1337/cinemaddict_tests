from features.pages.base import BasePage

# def before_scenario(context, scenario):
#     context.browserWindow = BasePage()
#     context.browserWindow.open_url()

def before_all(context):
    print("before all")
    context.browserWindow = BasePage()
    context.browserWindow.open_url()
    context.browserWindow.set_browser_settings()

def after_all(context):
    context.browserWindow.browser.quit()

def after_step(context, step):

    #print(context.browserWindow)
    #print(context.scenario_name)
    #context.step
    #print(context.scenario.name + " " + context.step.name)
    #print(context.browserWindow.get_scenario_name())
    context.browserWindow.after_handle()