import pytest
from base import logged_in_page, logged_out_page, change_profile_page
from base import FIO_LOCATOR, PHONE_LOCATOR, CHANGE_EMAIL_LOCATOR


@pytest.mark.UI
def test_login(logged_in_page):
    assert logged_in_page.current_url == 'https://target.my.com/dashboard'


@pytest.mark.UI
def test_logout(logged_out_page):
    assert 'Войти' in logged_out_page.page_source


@pytest.mark.UI
def test_edit_profile(change_profile_page):
    fio = ['ПитоновЗмейГорыныч', 'Питонов-Змей-Горыныч', 'Питонов Змей Горыныч']
    phone = ['273839', '+72736373839', '27-38-39']
    email = ['gorynych45@gm.ru', 'snake@555.ua', 'snakepythonov@gov.com']

    for i in range(len(fio) if len(fio) == len(phone) == len(email) else 0):
        modified_profile_page = change_profile_page(fio[i], phone[i], email[i])

        assert fio[i] == modified_profile_page.find_element_by_xpath(FIO_LOCATOR).get_attribute('value') and \
               phone[i] == modified_profile_page.find_element_by_xpath(PHONE_LOCATOR).get_attribute('value') and \
               email[i] == modified_profile_page.find_element_by_xpath(CHANGE_EMAIL_LOCATOR).get_attribute('value')


@pytest.mark.parametrize('locator, url', [
    pytest.param(
        "//a[contains(@class, 'center-module-statistics')]", "https://target.my.com/statistics/summary",
        id='statistics-button',
    ),
    pytest.param(
        "//a[contains(@class, 'center-module-pro')]", "https://target.my.com/pro",
        id='pro-button',
    ),
])
@pytest.mark.UI
def test_transition_to_pages(logged_in_page, locator, url):
    button = logged_in_page.find_element_by_xpath(locator)
    button.click()
    assert logged_in_page.current_url == url
