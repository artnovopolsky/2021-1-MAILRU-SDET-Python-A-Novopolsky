import pytest
import allure
from api.fixtures import api_client, login_api, fake_api
from mysql.builder import MySQLBuilder


@allure.feature('Тесты на API')
class TestAPI:

    def test_add_user(self, login_api, fake_api):
        """
        Тест проверяет добавление пользователя через API.
        Через ORM осуществляется проверка, что пользователь добавлен в БД.
        Ожидаемый результат: username при отправлении запроса совпадает с username в БД.
        """
        login_api.post_add_user(username=fake_api['username'],
                                password=fake_api['password'],
                                email=fake_api['email'])
        assert MySQLBuilder().select_by_username(fake_api['username']).username == fake_api['username']

    def test_add_existent_user(self, login_api, fake_data):
        """
        Тест проверяет добавление существующего пользователя через API.
        Ожидаемый результат: код ответа 304 (сущность существует/не изменилась).
        """
        login_api.post_add_user(username=fake_data['username'], password=fake_data['password'],
                                email=fake_data['email'], expected_status=304)

    def test_add_invalid_user(self, login_api, fake_api):
        """
        Тест на добавление пользователя c невалидными данными через API.
        Отправление POST-запроса на '/api/add_user'.
        Ожидаемый результат: код ответа 400 (плохой запрос).
        """
        login_api.post_add_user(username='cat', password='123', email='dog',
                                expected_status=400)

    def test_delete_user(self, login_api, fake_api):
        """
        Тест проверяет удаление пользователя через API.
        Через ORM происходит добавление пользователя в БД и проверка, что пользователь успешно удален.
        Ожидаемый результат: после удаления username в БД не найден.
        """
        MySQLBuilder().add_user(username=fake_api['username'],
                                password=fake_api['password'],
                                email=fake_api['email'])
        login_api.get_delete_user(username=fake_api['username'])
        assert MySQLBuilder().select_by_username(fake_api['username']) is None

    def test_block_user(self, login_api, fake_api):
        """
        Тест проверяет блокировку пользователя через API.
        Через ORM осуществляется добавление пользователя в БД, затем проверка, что поля access.
        Ожидаемый результат: поле access = 0.
        """
        MySQLBuilder().add_user(username=fake_api['username'],
                                password=fake_api['password'],
                                email=fake_api['email'])
        login_api.get_block_user(username=fake_api['username'])
        assert MySQLBuilder().select_by_username(fake_api['username']).access == 0

    def test_unblock_user(self, login_api, fake_api):
        """
        Тест проверяет разблокировку пользователя через API.
        Через ORM осуществляется добавление пользователя в БД с полем access=0.
        Затем проверка, что поле access изменилось.
        Ожидаемый результат: поле access стало равно 1.
        """
        MySQLBuilder().add_user(username=fake_api['username'], password=fake_api['password'],
                                email=fake_api['email'], access=0)
        login_api.get_unblock_user(username=fake_api['username'])
        assert MySQLBuilder().select_by_username(fake_api['username']).access == 1

    def test_delete_not_existent_user(self, login_api):
        """
        Тест проверяет удаление несуществующего пользователя через API.
        Ожидаемый результат: код ответа 404 (сущности не существует).
        """
        login_api.get_delete_user(username='testusername', expected_status=404)

    def test_login_not_existent_user(self, api_client):
        """
        Тест проверяет авторизацию несуществующего пользователя через API.
        Ожидаемый результат: код ответа 401 (пользователь не авторизован).
        """
        api_client.post_login(username='korovamoloko', password='123', expected_status=401)

    def test_find_me_error(self, login_api):
        """
        Тест на 'Find me error'.
        Отправление GET-запроса на '/static/scripts/findMeError.js'
        Ожидаемый результат: код ответа 200 (действие выполнено).
        """
        login_api._request(method='GET', location='/static/scripts/findMeError.js',
                           expected_status=200)

    def test_myapp_status(self, api_client):
        """
        Тест проверки статуса приложения через API.
        Отправление GET-запроса на '/status'.
        Ожидаемый результат: код ответа 200 (действие выполнено) и статус ответа 'ok'.
        """
        response = api_client.get_status().json()
        assert response['status'] == 'ok'
