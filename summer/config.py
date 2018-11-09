from fishbase import fish_file as fff
import os


class Config(object):
    """
    配置文件类
    """
    DEBUG = False
    TESTING = False
    CURRENT_PATH = os.path.dirname('.')


def get_db_sqlite_uri(db_name, db_path=Config.CURRENT_PATH):
    """
    获取 sqlite 地址

    :param:
        * db_name(str): 数据库名称
    :return:
        * db_sqlite_uri(str): sqlite 链接地址
    """
    db_sqlite_uri = 'sqlite:///' + fff.get_abs_filename_with_sub_path(db_path, db_name)[1]
    return db_sqlite_uri


class DevelopmentConfig(Config):
    """
    开发环境配置类
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
    """
    测试环境配置类
    """
    TESTING = True
    PORT = 8080
    IP = '0.0.0.0'
