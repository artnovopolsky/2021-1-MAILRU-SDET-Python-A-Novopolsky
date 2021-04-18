import pytest
import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from base_case import BaseCase
from fixtures import *


@allure.feature('Тесты на UI')
@allure.story('Негативные тесты на логин')
class TestLoginFailure(BaseCase):

    @pytest.mark.UI
    def test_fake_credentials(self):
        """ Тест авторизации с валидными, но неподходящими данными. """

        self.unauthorized_page.login(email='korova@moloko.ru', password='12345')
        error_message_title = self.unauthorized_page.find(self.unauthorized_page.locators.ERROR_LOCATOR).text
        assert error_message_title == 'Error'

    @pytest.mark.UI
    def test_invalid_email(self):
        """ Тест авторизации с невалидным e-mail. """

        self.unauthorized_page.login(email='korovamoloko', password='12345')
        alert = self.unauthorized_page.find(self.unauthorized_page.locators.INVALID_EMAIL_LOCATOR)
        assert alert.get_attribute('textContent') == 'Введите email или телефон'


@allure.feature('Тесты на UI')
@allure.story('Тесты на создание рекламной кампании')
class TestCampaignCreation(BaseCase):

    @pytest.mark.UI
    def test_create_campaign(self, login):
        """ Тест на создание рекламной кампании. """

        campaign_page = self.authorized_page.go_to_campaign_page()
        campaign_name = campaign_page.create_campaign()
        campaign_page.find((By.XPATH, campaign_page.locators.CAMPAIGN_IN_TABLE_LOCATOR.format(campaign_name)))


@allure.feature('Тесты на UI')
@allure.story('Тесты на работу с сегментами')
class TestSegment(BaseCase):

    @pytest.mark.UI
    def test_create_segment(self, login):
        """ Тест на создание сегмента. """

        segment_page = self.authorized_page.go_to_segment_page()
        segment_name = segment_page.create_segment()
        segment_page.find((By.XPATH, segment_page.locators.SEGMENT_IN_TABLE_LOCATOR.format(segment_name)))

    @pytest.mark.UI
    def test_delete_segment(self, login):
        """ Тест на удаление сегмента. """

        segment_page = self.authorized_page.go_to_segment_page()
        segment_name = segment_page.create_segment()
        segment_page.delete_segment(segment_name)
        with pytest.raises(TimeoutException):
            segment_page.find((By.XPATH, segment_page.locators.SEGMENT_IN_TABLE_LOCATOR.format(segment_name)), timeout=2)
