import pytest
import time

# Basic locators
SIGN_IN_LOCATOR = "//div[contains(@class, 'responseHead-module-button')]"
EMAIL_LOCATOR = "//input[@name='email']"
PASSWORD_LOCATOR = "//input[@name='password']"
ENTER_LOCATOR = "//div[contains(@class, 'authForm-module-button')]"
USER_INFO_LOCATOR = "//div[contains(@class, 'right-module-rightButton') or contains(@class, 'right-module-mail')]"
LOG_OUT_LOCATOR = "//a[@href='/logout']"

# Personal data
EMAIL = 'artemnvp@rambler.ru'
PASSWORD = '1artemnvp@rambler.ru'


@pytest.fixture()
def logged_in_page(driver):
    sign_in_button = driver.find_element_by_xpath(SIGN_IN_LOCATOR)
    sign_in_button.click()

    email_field = driver.find_element_by_xpath(EMAIL_LOCATOR)
    email_field.clear()
    email_field.send_keys(EMAIL)

    password_field = driver.find_element_by_xpath(PASSWORD_LOCATOR)
    password_field.clear()
    password_field.send_keys(PASSWORD)

    enter_button = driver.find_element_by_xpath(ENTER_LOCATOR)
    enter_button.click()

    time.sleep(2) # ждём полную генерацию страницы
    yield driver


@pytest.fixture()
def logged_out_page(logged_in_page):
    user_info_button = logged_in_page.find_element_by_xpath(USER_INFO_LOCATOR)
    user_info_button.click()

    log_out_button = logged_in_page.find_element_by_xpath(LOG_OUT_LOCATOR)
    log_out_button.click()

    time.sleep(2) # ждём полную генерацию страницы
    yield logged_in_page
