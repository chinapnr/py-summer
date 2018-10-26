import os
from flask import *
from py_summer.config import DevelopmentConfig, TestingConfig
from flask_sqlalchemy import SQLAlchemy


class Summer(Flask):

    @staticmethod
    def read_conf(application):
        server_env = os.environ.get('SERVER_ENV', default='development')
        # 根据 server 环境状态读入 flask config 对象
        if server_env == 'development':
            application.config.from_object(DevelopmentConfig)
        elif server_env == 'testing':
            application.config.from_object(TestingConfig)

    def create_server(self, test_config=None):
        """Create and configure an instance of the Flask application."""
        application = Flask(__name__, instance_relative_config=True)

        application.config.from_mapping(
            # a default secret that should be overridden by instance config
            SECRET_KEY='secret_key_only_test',
        )

        # 如果没有传入 config dict
        if test_config is None:
            # 尝试从 config.py 中读入配置文件
            # load the instance config, if it exists, when not testing
            self.read_conf(application)
        else:
            # 如果传入 test 配置，则使用
            application.config.update(test_config)

        # ensure the instance folder exists
        # try:
        #     os.makedirs(application.instance_path)
        # except OSError:
        #     pass

        return application


# Summer 提供默认的app对象、db对象、同时维护套默认配置对象
app = Summer(__name__, instance_relative_config=True).create_server()
db = SQLAlchemy(app)

__version__ = '1.0.0'
