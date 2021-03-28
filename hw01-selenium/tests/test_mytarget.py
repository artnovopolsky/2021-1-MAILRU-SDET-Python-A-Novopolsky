import pytest

from base import logged_in, logged_out, change_profile_page

from locators import SIGN_IN_LOCATOR  # For logout test
from locators import FIO_LOCATOR, PHONE_LOCATOR, CHANGE_EMAIL_LOCATOR  # For edit profile test
from locators import STATISTICS_LOCATOR, PRO_LOCATOR  # For transition to page test


@pytest.mark.UI
def test_login(driver):
    logged_in(driver)
    assert driver.current_url == 'https://target.my.com/dashboard'


@pytest.mark.UI
def test_logout(driver):
    logged_out(driver)
    driver.find_element(*SIGN_IN_LOCATOR)


@pytest.mark.UI
def test_edit_profile(change_profile_page):
    """ Edits profile info several times in a row """

    fio = ['ЗмейГорыныч', 'Питонов-Змей', 'Питонов Змей Горыныч']
    phone = ['273839', '+72736373839', '27-38-39']
    email = ['gorynych45@gm.ru', 'snake@555.ua', 'snakepythonov@gov.com']

    for f, p, e in zip(fio, phone, email):
        modified_profile = change_profile_page(f, p, e)

        assert f == modified_profile.find_element(*FIO_LOCATOR).get_attribute('value') and \
               p == modified_profile.find_element(*PHONE_LOCATOR).get_attribute('value') and \
               e == modified_profile.find_element(*CHANGE_EMAIL_LOCATOR).get_attribute('value')


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
