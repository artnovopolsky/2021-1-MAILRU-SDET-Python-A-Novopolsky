import os
import pytest
import allure

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pages.base_page import BasePage
from pages.unauthorized_page import UnauthorizedPage
from pages.authorized_page import AuthorizedPage
from pages.campaign_page import CampaignPage
from pages.segment_page import SegmentPage


@pytest.fixture(scope='function')
def driver(config):
    manager = ChromeDriverManager(version='89.0.4389.23', log_level=0)
    browser = webdriver.Chrome(executable_path=manager.install())
    url = config['url']
    browser.get(url)
    browser.maximize_window()

    yield browser

    browser.quit()


@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture
def unauthorized_page(driver):
    return UnauthorizedPage(driver=driver)


@pytest.fixture
def authorized_page(driver):
    return AuthorizedPage(driver=driver)


@pytest.fixture
def campaign_page(driver):
    return CampaignPage(driver=driver)


@pytest.fixture
def segment_page(driver):
    return SegmentPage(driver=driver)


@pytest.fixture(scope='function')
def login(driver):
    return UnauthorizedPage(driver).login()


@pytest.fixture(scope='function', autouse=True)
def ui_report(driver, request, test_dir):
    """ Добавляет в отчёт скриншоты и логи браузера """
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
