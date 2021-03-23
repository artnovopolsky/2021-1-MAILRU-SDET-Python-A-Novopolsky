import pytest
from selenium import webdriver

EXEC_PATH = '/home/artnovopolsky/mailru-course/chromedriver'
URL = 'https://target.my.com/'


@pytest.fixture()
def driver():
    browser = webdriver.Chrome(executable_path=EXEC_PATH)
    browser.implicitly_wait(5)
    browser.get(URL)
    browser.maximize_window()
    yield browser
    browser.quit()
