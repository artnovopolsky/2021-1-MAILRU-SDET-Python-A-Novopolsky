import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    chrome_driver = webdriver.Chrome(executable_path='/home/artnovopolsky/mailru-course/chromedriver')
    chrome_driver.implicitly_wait(5)
    chrome_driver.get('https://target.my.com/')
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()
