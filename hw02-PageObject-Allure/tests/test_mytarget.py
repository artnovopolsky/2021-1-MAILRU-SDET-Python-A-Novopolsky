import pytest
import allure
from selenium.common.exceptions import TimeoutException
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
        campaign_name = campaign_page.create_campaign_name()
        campaign_page.create_campaign(campaign_name)

        created_campaign_name = campaign_page.find(campaign_page.locators.NEW_CAMPAIGN_IN_TABLE_LOCATOR).text
        assert created_campaign_name == campaign_name


@allure.feature('Тесты на UI')
@allure.story('Тесты на работу с сегментами')
class TestSegment(BaseCase):

    @pytest.mark.UI
    def test_create_segment(self, login):
        """ Тест на создание сегмента. """

        segment_page = self.authorized_page.go_to_segment_page()
        segment_name = segment_page.create_segment_name()
        segment_page.create_segment(segment_name)

        creating_segment_name = segment_page.find(segment_page.locators.SEGMENT_IN_TABLE_LOCATOR).text
        assert creating_segment_name == segment_name

    @pytest.mark.UI
    def test_delete_segment(self, login):
        """ Тест на удаление сегмента. """

        segment_page = self.authorized_page.go_to_segment_page()
        segment_page.create_segment(name=segment_page.create_segment_name())
        created_segment_name = segment_page.find(segment_page.locators.SEGMENT_IN_TABLE_LOCATOR).text

        segment_page.delete_segment(name=created_segment_name)

        with allure.step('Поиск первого сегмента в таблице для сравнения названий с удалённым сегментом.'):
            try:
                existing_segment_name = segment_page.find(segment_page.locators.SEGMENT_IN_TABLE_LOCATOR).text
            except TimeoutException:
                assert 'С чего начать?' in segment_page.driver.page_source
            else:
                assert existing_segment_name != created_segment_name
