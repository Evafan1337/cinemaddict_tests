from selenium import webdriver
import os

BROWSER_NAME = "chrome"
BROWSER_VERSION = "107.0"
BASE_URL = "http://192.168.0.108:8081"

capabilities = {
    "browserName": BROWSER_NAME,
    "browserVersion": BROWSER_VERSION,
    "screenResolution": "1920x1080x24",
    "selenoid:options": {
        "enableVNC": True,
        "enableVideo": True,
    }
}

browser = webdriver.Remote(
    command_executor="http://0.0.0.0:4444/wd/hub",
    desired_capabilities=capabilities)

browser.get(BASE_URL)
browser.maximize_window()

print(browser.title)
print(os.environ["BROWSER"])


browser.quit()