from fishbase import fish_file as fff
import os


class Config(object):
    """
    开发环境、单元测试环境使用SQLite3
    测试环境、准生产环境、生产环境使用MySQL
    ORM框架使用SQLAlchemy
    """
    DEBUG = False

    @staticmethod
    def _get_sqlite_uri(db_name):
        """
        生成 sqlite 数据库的 uri 字符串
        :param db_name: 数据库名称
        :return: db url
        """
        db_sqlite_uri = 'sqlite:///' + fff.get_abs_filename_with_sub_path('db', db_name)[1]
        return db_sqlite_uri


class DevelopmentConfig(Config):
    """
    开发环境配置
    """
    DEBUG = True
    SQLITE_NAME = os.environ.get('SQLITE_NAME', default='dev.sqlite')
    DATABASE_URI = Config._get_sqlite_uri(SQLITE_NAME)
    PORT = 8080
    IP = '0.0.0.0'
    ROUTE_PREFIX = '/api'


class TestingConfig(Config):
    """
    测试环境配置
    """
    DEBUG = True
    SQLITE_NAME = os.environ.get('SQLITE_NAME', default='test.sqlite')
    DATABASE_URI = Config._get_sqlite_uri(SQLITE_NAME)
    PORT = 8080
    IP = '0.0.0.0'
    ROUTE_PREFIX = '/api'


class ProductConfig(Config):
    """
    生产环境配置
    """
    DEBUG = True
    DATABASE_URI = 'Mysql database address'
    PORT = 8080
    IP = '0.0.0.0'
    ROUTE_PREFIX = '/api'
