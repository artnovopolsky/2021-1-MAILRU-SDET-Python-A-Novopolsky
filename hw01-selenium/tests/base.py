import pytest
import time
import locators

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def logged_in(driver,
              email='artemnvp@rambler.ru',
              password='1artemnvp@rambler.ru'):
    sign_in_button = driver.find_element(*locators.SIGN_IN_LOCATOR)
    sign_in_button.click()

    email_field = driver.find_element(*locators.EMAIL_LOCATOR)
    email_field.clear()
    email_field.send_keys(email)

    password_field = driver.find_element(*locators.PASSWORD_LOCATOR)
    password_field.clear()
    password_field.send_keys(password)

    enter_button = driver.find_element(*locators.ENTER_LOCATOR)
    enter_button.click()

    time.sleep(2)  # Waiting for page generation
    return driver


def logged_out(logged_in_page):
    user_info_button = logged_in_page.find_element(*locators.USER_INFO_LOCATOR)
    user_info_button.click()

    log_out_button = WebDriverWait(logged_in_page, 20).until(EC.element_to_be_clickable(locators.LOG_OUT_LOCATOR))
    log_out_button.click()

    time.sleep(2)  # Waiting for page generation
    return logged_in_page


def change_profile_page(driver,
                        fio='Иванов Иван Иванович',
                        phone='88005553535',
                        email='ivanivanov@gov.com'):
    logged_in(driver)

    profile_button = driver.find_element(*locators.PROFILE_LOCATOR)
    profile_button.click()

    fio_field = driver.find_element(*locators.FIO_LOCATOR)
    fio_field.clear()
    fio_field.send_keys(fio)

    phone_field = driver.find_element(*locators.PHONE_LOCATOR)
    phone_field.clear()
    phone_field.send_keys(phone)

    change_email_field = driver.find_element(*locators.CHANGE_EMAIL_LOCATOR)
    change_email_field.clear()
    change_email_field.send_keys(email)

    save_button = driver.find_element(*locators.SAVE_LOCATOR)
    save_button.click()

    driver.refresh()

    time.sleep(2)  # Waiting for page generation
    return driver
