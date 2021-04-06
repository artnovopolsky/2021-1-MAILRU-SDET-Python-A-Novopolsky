import os
import pytest
import allure

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function')
def driver(config):
    manager = ChromeDriverManager(version='89.0.4389.23')
    browser = webdriver.Chrome(executable_path=manager.install())
    url = config['url']
    browser.get(url)
    browser.maximize_window()

    yield browser

    browser.quit()


@pytest.fixture
def base_page(driver):
    pass


@pytest.fixture
def main_page(driver):
    pass


@pytest.fixture
def search_page(driver):
    pass


@pytest.fixture(scope='function', autouse=True)
def ui_report(driver, request, test_dir):
    failed_tests_count = request.session.testsfailed

    yield

    if request.session.testsfailed > failed_tests_count:

        screenshot_file = os.path.join(test_dir, 'fail.png')
        driver.get_screenshot_as_file(screenshot_file)
        allure.attach.file(screenshot_file, 'fail.png',
                           attachment_type=allure.attachment_type.PNG)
        browser_logfile = os.path.join(test_dir, 'browser.log')

        with open(browser_logfile, 'w') as logfile:
            for i in driver.get_log('browser'):
                logfile.write(f"{i['level']} - {i['source']}\n{i['message']}\n\n")

        with open(browser_logfile, 'r') as logfile:
            allure.attach(logfile.read(), 'browser.log',
                          attachment_type=allure.attachment_type.TEXT)
