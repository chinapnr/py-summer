from py_summer import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import config as config_center


def load_conf(application):
    """
    将配置载入app中
    :param application: application实例
    :return: 载入配置的application实例
    """
    server_env = os.environ.get('SERVER_ENV', default='Development')
    config_obj_name = ''.join([server_env, 'Config'])
    config_obj = getattr(config_center, config_obj_name)
    application.config.from_object(config_obj)
    return application


# 实例化获得app对象
app = Summer(__name__, instance_relative_config=True).create_server()
# 载入配置
app = load_conf(app)

# 获得db对象
Base = declarative_base()
engine = create_engine(app.config.get('SQLALCHEMY_DATABASE_URI'))
Session = sessionmaker(bind=engine)
db = Session()

