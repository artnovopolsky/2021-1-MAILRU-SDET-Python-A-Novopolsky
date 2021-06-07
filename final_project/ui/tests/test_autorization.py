import pytest
import allure
from ui.tests.base_case import BaseCase
from ui.fixtures import *
from mysql.builder import MySQLBuilder


@allure.feature('Тесты на UI')
@allure.story('Тесты на авторизацию')
class TestAuthorizationPage(BaseCase):

    def test_check_authorization_page(self, setup):
        """
        Тест успешного открытия страницы авторизации.
        Проверяет наличие приветственной строки в исходном коде страницы.
        Ожидаемый результат: строка присутствует.
        """
        assert 'Welcome to the TEST SERVER' in self.authorization_page.driver.page_source

    def test_fields_validation(self, setup):
        """
        Тест валидации полей в форме авторизации.
        Проверяет наличие атрибута required у полей.
        Ожидаемый результат: у полей присутствует валидация.
        """
        self.authorization_page.check_fields_validation()

    def test_fake_credentials(self, setup):
        """
        Негативный тест на авторизацию.
        Проверяет реакцию приложения на валидные, но неподходящие данные.
        Ожидаемый результат: сообщение об ошибке 'Invalid username or password'.
        """
        self.authorization_page.login(username='123123123', password='123')
        self.authorization_page.find(self.authorization_page.locators.INVALID_ERROR_MESSAGE)

    def test_invalid_username(self, setup):
        """
        Негативный тест на авторизацию.
        Проверяет реакцию приложения на невалидные данные (слишком короткий/длинный username).
        Ожидаемый результат: сообщение об ошибке 'Incorrect username length'.
        """
        self.authorization_page.login(username='123', password='123')
        self.authorization_page.find(self.authorization_page.locators.INCORRECT_ERROR_MESSAGE)

    def test_valid_credentials(self, setup, fake_data):
        """
        Позитивный тест на авторизацию.
        При помощи ORM пользователь добавляется в БД. Затем происходит попытка авторизации.
        Ожидаемый результат: найдена строка 'Logged as' на главной странице.
        """
        MySQLBuilder().add_user(username=fake_data['username'],
                                email=fake_data['email'],
                                password=fake_data['password'])
        self.authorization_page.login(username=fake_data['username'],
                                      password=fake_data['password'])
        self.main_page.find(self.main_page.locators.LOGGED_AS, 2)
