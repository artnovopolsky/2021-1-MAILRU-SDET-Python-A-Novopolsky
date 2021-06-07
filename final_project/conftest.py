import os
import shutil
import pytest
import faker


def pytest_addoption(parser):
    parser.addoption('--url', default='http://myapp:9999')
    parser.addoption('--debug_log', action='store_true')


def pytest_configure(config):
    base_test_dir = '/tmp/tests'
    if not hasattr(config, 'workerinput'):
        if os.path.exists(base_test_dir):
            shutil.rmtree(base_test_dir)
        os.makedirs(base_test_dir)

    config.base_test_dir = base_test_dir


@pytest.fixture(scope='session')
def config(request):
    url = request.config.getoption('--url')
    debug_log = request.config.getoption('--debug_log')
    return {'url': url, 'debug_log': debug_log}


@pytest.fixture(scope='function')
def test_dir(request):
    """ Создаёт директорию под каждый тест """

    test_name = request._pyfuncitem.nodeid.replace('/', '_').replace(':', '_')
    test_dir = os.path.join(request.config.base_test_dir, test_name)
    os.makedirs(test_dir)
    return test_dir


@pytest.fixture(scope='function')
def fake_data():
    fake = faker.Faker()
    return {
        'username': fake.user_name(),
        'email': fake.email(),
        'password': fake.password()
    }
