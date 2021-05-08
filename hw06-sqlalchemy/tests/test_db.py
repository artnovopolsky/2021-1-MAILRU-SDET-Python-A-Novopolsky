import pytest
import utils
from mysql.builder import MySQLBuilder
from mysql.models import RequestsCount, RequestTypeCount, MostFrequentRequest, Largest4xxRequest, UserWith5xxRequests


class BaseMySQL:

    def prepare(self):
        pass

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_client):
        self.client = mysql_client
        self.builder = MySQLBuilder(self.client)
        self.prepare()


class TestRequestsCount(BaseMySQL):

    def prepare(self):
        req_count = utils.count_requests()
        self.builder.create_requests_count(req_count)

    def test_requests_count(self):
        req_count = self.client.session.query(RequestsCount).all()
        assert len(req_count) == 1


class TestRequestTypesCount(BaseMySQL):

    def prepare(self):
        req_types_count = utils.count_request_types()
        for req_type in req_types_count:
            self.builder.create_request_type_count(req_type=req_type[0], count=req_type[1])

    def test_request_types_count(self):
        req_types_count = self.client.session.query(RequestTypeCount).all()
        assert len(req_types_count) == 5


class TestMostFrequentRequests(BaseMySQL):

    def prepare(self):
        most_freq_reqs = utils.most_frequent_requests()
        for most_freq_req in most_freq_reqs:
            self.builder.create_most_frequent_request(url=most_freq_req[0], count=most_freq_req[1])

    def test_most_frequent_requests(self):
        most_freq_reqs = self.client.session.query(MostFrequentRequest).all()
        assert len(most_freq_reqs) == 10


class TestLargest4xxRequests(BaseMySQL):

    def prepare(self):
        largest_4xx_reqs = utils.largest_4xx_requests()
        for req in largest_4xx_reqs:
            self.builder.create_largest_4xx_request(url=req[0], size=req[1], ip=req[2])

    def test_largest_4xx_requests(self):
        largest_4xx_reqs = self.client.session.query(Largest4xxRequest).all()
        assert len(largest_4xx_reqs) == 5


class TestUsersWith5xxRequests(BaseMySQL):

    def prepare(self):
        users_with_5xx_reqs = utils.users_with_5xx_requests()
        for user in users_with_5xx_reqs:
            self.builder.create_user_with_5xx_requests(ip=user[0], requests_number=user[1])

    def test_users_with_5xx_requests(self):
        users_with_5xx_reqs = self.client.session.query(UserWith5xxRequests).all()
        assert len(users_with_5xx_reqs) == 5
