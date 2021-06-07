from mysql.models import TestUser
from mysql.client import MySQLClient


class MySQLBuilder:

    def __init__(self):
        self.client = MySQLClient()

    def add_user(self, username, password, email, access=1):
        test_user = TestUser(
            username=username,
            password=password,
            email=email,
            access=access
        )
        self.client.session.add(test_user)
        self.client.session.commit()
        return test_user

    def select_by_username(self, username):
        return self.client.session.query(TestUser).filter(TestUser.username == username).first()

    def drop_access_by_username(self, username):
        user = self.client.session.query(TestUser).filter(TestUser.username == username).first()
        user.access = 0
        self.client.session.commit()
