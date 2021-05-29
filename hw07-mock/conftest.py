import pytest
from mock import flask_mock
from client.socket_http_client import SocketClient


@pytest.fixture(scope='session')
def connect():
    flask_mock.run_mock(host='127.0.0.1', port=8888)
    client = SocketClient(host='127.0.0.1', port=8888)
    yield client
    client.get('/shutdown')
