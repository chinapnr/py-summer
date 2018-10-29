from fishbase import fish_file as fff
import os


class Config(object):
    DEBUG = False
    TESTING = False


# 生成 sqlite 数据库的 uri 字符串
def get_db_sqlite_uri(db_name):
    db_sqlite_uri = 'sqlite:///' + fff.get_abs_filename_with_sub_path('db', db_name)[1]
    return db_sqlite_uri


class DevelopmentConfig(Config):
    """
    开发环境配置
    """
    TESTING = False
    DEBUG = True
    SQLITE_NAME = os.environ.get('SQLITE_NAME', default='dev.sqlite')
    SQLALCHEMY_DATABASE_URI = get_db_sqlite_uri(SQLITE_NAME)
    PORT = 8080
    IP = '0.0.0.0'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_TEARDOWN = True


class TestingConfig(Config):
    TESTING = True
    PORT = 8080
    IP = '0.0.0.0'
