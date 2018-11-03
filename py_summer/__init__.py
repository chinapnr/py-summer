import os
from flask import *
from py_summer.config import DevelopmentConfig, TestingConfig
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class Summer(Flask):
    """
    申明一个Summer类，目前继承自Flask
    :param:
       无
    :returns:
       无
    """

    @staticmethod
    def load_conf(application):
        """
        加载自定义配置到当前的application对象中
        :param:
            * application(object): application 对象
        :return:
           无
        """
        server_env = os.environ.get('SERVER_ENV', default='development')
        if server_env == 'development':
            application.config.from_object(DevelopmentConfig)
        elif server_env == 'testing':
            application.config.from_object(TestingConfig)

    def create_server(self, test_config=None):
        """
        根据application对象创建serverr
        :param:
            * test_config(dict): application 对象
        :return:
           * application(object) application 对象
        """

        application = Flask(__name__, instance_relative_config=True)
        application.config.from_mapping(
            SECRET_KEY='secret_key_only_test'
        )

        if test_config is None:
            # 尝试从 config.py 中读入配置文件
            self.load_conf(application)
        else:
            # 如果传入 test 配置，则使用
            application.config.update(test_config)
        return application


# Summer 提供默认的app对象、db对象、同时维护套默认配置对象
app = Summer(__name__, instance_relative_config=True).create_server()

Base = declarative_base()
engine = create_engine(app.config.get('SQLALCHEMY_DATABASE_URI'))
Session = sessionmaker(bind=engine)
db = Session()


__version__ = '1.0.0'
