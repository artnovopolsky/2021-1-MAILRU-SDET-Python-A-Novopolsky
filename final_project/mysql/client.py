import sqlalchemy
from sqlalchemy.orm import sessionmaker


class MySQLClient:

    def __init__(self, user='root', password='admin',
                 db_name='DB_MYAPP', host='0.0.0.0', port='3306'):

        self.user = user
        self.password = password
        self.db_name = db_name
        self.host = host
        self.port = port

        self.connection = self.connect()
        self.session = sessionmaker(bind=self.connection)()

    def connect(self):
        engine = sqlalchemy.create_engine(
            f'mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{self.db_name}',
            encoding='utf8'
        )

        return engine.connect()
