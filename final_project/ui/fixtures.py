import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():

    caps = {
        "browserName": "chrome",
        "version": "89.0",
        "sessionTimeout": "2m",
    }

    browser = webdriver.Remote(command_executor="http://127.0.0.1:4444/wd/hub",
                               desired_capabilities=caps)

    browser.get("http://final_project_myapp_1:9999")
    browser.maximize_window()
    yield browser
    browser.quit()
