import pytest

from base import logged_in, logged_out, change_profile_page

from locators import FIO_LOCATOR, PHONE_LOCATOR, CHANGE_EMAIL_LOCATOR  # For edit profile test
from locators import STATISTICS_LOCATOR, PRO_LOCATOR  # For transition to page test


@pytest.mark.UI
def test_login(driver):
    logged_in(driver)
    assert driver.current_url == 'https://target.my.com/dashboard'


@pytest.mark.UI
def test_logout(driver):
    logged_in(driver)
    logged_out(driver)
    assert 'Войти' in driver.page_source


@pytest.mark.UI
def test_edit_profile(driver):
    fio = 'Питонов Змей Горыныч'
    phone = '27-38-39'
    email = 'snakepythonov@gov.com'
    change_profile_page(driver, fio, phone, email)
    assert fio == driver.find_element(*FIO_LOCATOR).get_attribute('value') and \
           phone == driver.find_element(*PHONE_LOCATOR).get_attribute('value') and \
           email == driver.find_element(*CHANGE_EMAIL_LOCATOR).get_attribute('value')


@pytest.mark.parametrize('locator, url', [
    pytest.param(
        STATISTICS_LOCATOR, "https://target.my.com/statistics/summary",
        id='statistics',
    ),
    pytest.param(
        PRO_LOCATOR, "https://target.my.com/pro",
        id='pro',
    ),
])
@pytest.mark.UI
def test_transition_to_pages(driver, locator, url):
    logged_in(driver)
    button = driver.find_element(*locator)
    button.click()
    assert driver.current_url == url
