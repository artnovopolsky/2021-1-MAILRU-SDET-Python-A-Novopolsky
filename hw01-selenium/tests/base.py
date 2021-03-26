import pytest
import time

# BASIC LOCATORS
# Locators for log in
SIGN_IN_LOCATOR = "//div[contains(@class, 'responseHead-module-button')]"
EMAIL_LOCATOR = "//input[@name='email']"
PASSWORD_LOCATOR = "//input[@name='password']"
ENTER_LOCATOR = "//div[contains(@class, 'authForm-module-button')]"

# Locators for log out
USER_INFO_LOCATOR = "//div[contains(@class, 'right-module-rightButton') or contains(@class, 'right-module-mail')]"
LOG_OUT_LOCATOR = "//a[@href='/logout']"

# Locators for transition to profile page
PROFILE_LOCATOR = "//a[@href='/profile']"

# Locators for change profile info
FIO_LOCATOR = "//div[@data-name='fio']/div/input"
PHONE_LOCATOR = "//div[@data-name='phone']/div/input"
CHANGE_EMAIL_LOCATOR = "//div[contains(@class, 'email')]/div/div/input"
SAVE_LOCATOR = "//div[contains(@class, 'button') and contains(text(), 'Сохранить')]"


@pytest.fixture
def logged_in_page(driver,
                   email='artemnvp@rambler.ru',
                   password='1artemnvp@rambler.ru'):
    sign_in_button = driver.find_element_by_xpath(SIGN_IN_LOCATOR)
    sign_in_button.click()

    email_field = driver.find_element_by_xpath(EMAIL_LOCATOR)
    email_field.clear()
    email_field.send_keys(email)

    password_field = driver.find_element_by_xpath(PASSWORD_LOCATOR)
    password_field.clear()
    password_field.send_keys(password)

    enter_button = driver.find_element_by_xpath(ENTER_LOCATOR)
    enter_button.click()

    time.sleep(2)  # Waiting for page generation
    yield driver


@pytest.fixture
def logged_out_page(logged_in_page):
    user_info_button = logged_in_page.find_element_by_xpath(USER_INFO_LOCATOR)
    user_info_button.click()

    log_out_button = logged_in_page.find_element_by_xpath(LOG_OUT_LOCATOR)
    log_out_button.click()

    time.sleep(2)  # Waiting for page generation
    yield logged_in_page


@pytest.fixture
def change_profile_page(logged_in_page):
    profile_button = logged_in_page.find_element_by_xpath(PROFILE_LOCATOR)
    profile_button.click()

    def _change_profile_page(fio='Иванов Иван Иванович',
                             phone='88005553535',
                             email='ivanivanov@gov.com'):

        fio_field = logged_in_page.find_element_by_xpath(FIO_LOCATOR)
        fio_field.clear()
        fio_field.send_keys(fio)

        phone_field = logged_in_page.find_element_by_xpath(PHONE_LOCATOR)
        phone_field.clear()
        phone_field.send_keys(phone)

        change_email_field = logged_in_page.find_element_by_xpath(CHANGE_EMAIL_LOCATOR)
        change_email_field.clear()
        change_email_field.send_keys(email)

        save_button = logged_in_page.find_element_by_xpath(SAVE_LOCATOR)
        save_button.click()

        logged_in_page.refresh()

        time.sleep(2)  # Waiting for page generation
        return logged_in_page

    yield _change_profile_page
