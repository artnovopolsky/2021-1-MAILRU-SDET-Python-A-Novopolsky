import pytest
from api_client import ApiClient


def pytest_addoption(parser):
    parser.addoption('--url', default='https://target.my.com/')


@pytest.fixture(scope='session')
def config(request):
    url = request.config.getoption('--url')
    return {'url': url}


@pytest.fixture(scope='function')
def api_client(config):
    return ApiClient(config['url'], email='artemnvp@rambler.ru', password='1artemnvp@rambler.ru')
