import pytest
import json
from mock.flask_mock import APP_DATA


class TestPostRequests:

    def test_create_user(self, connect):
        test_user = {'name': 'Peter', 'age': 16}
        resp = connect.post('/create_user', test_user)
        assert resp['status_code'] == 201

        body = json.loads(resp['body'])
        assert body['name'] == test_user['name']
        assert body['age'] == test_user['age']

    def test_create_existent_user(self, connect):
        existent_user = {'name': 'Danila', 'age': APP_DATA['Danila']}
        resp = connect.post('/create_user', existent_user)
        assert resp['status_code'] == 400


class TestGetRequests:

    def test_get_age(self, connect):
        resp = connect.get(f'/get_age/Artyom')
        assert resp['status_code'] == 200

        body = json.loads(resp['body'])
        assert body['age'] == APP_DATA['Artyom']

    def test_get_age_of_non_existent_user(self, connect):
        resp = connect.get(f'/get_age/Mikhail')
        assert resp['status_code'] == 404


class TestDeleteRequests:

    def test_delete_user(self, connect):
        existent_user = {'name': 'Mark'}
        resp = connect.delete('/delete_user', existent_user)
        assert resp['status_code'] == 200

    def test_delete_non_existent_user(self, connect):
        non_existent_user = {'name': 'Vasily'}
        resp = connect.delete('/delete_user', non_existent_user)
        assert resp['status_code'] == 404


class TestPutRequests:

    def test_change_age(self, connect):
        test_user = {'name': 'Artyom', 'new_age': 20}
        resp = connect.put('/change_age', test_user)
        assert resp['status_code'] == 201

        body = json.loads(resp['body'])
        assert body['age'] == test_user['new_age']

    def test_change_age_of_non_existent_user(self, connect):
        non_existent_user = {'name': 'Pavel', 'new_age': 24}
        resp = connect.put('/change_age', non_existent_user)
        assert resp['status_code'] == 404
