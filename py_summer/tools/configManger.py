import os
import importlib


class ConfigManager(object):
    config_map = {
        'development': 'DevelopmentConfig',
        'testing': 'TestingConfig'
    }

    def __init__(self, env_key, config_dir=None):
        config_dir = config_dir if config_dir else '.'.join(['py_summer', 'config'])
        self._content = dict()
        self.current_config_obj = None
        self.env_key = env_key
        self.env_value = os.getenv(self.env_key, 'development')  # 默认加载development配置
        self.read(config_dir)

    def __getitem__(self, item):
        config_item = hasattr(self._content[self.env_value], item)
        return getattr(self._content[self.env_value], item) if config_item else None

    def read(self, relative_path):
        try:
            config_package = importlib.import_module(relative_path)
        except ImportError:
            raise ImportError('Wrong relative path provided.')
        current_config_obj = getattr(config_package, ConfigManager.config_map.get(self.env_value))
        self.current_config_obj = self._content[self.env_value] = current_config_obj
        return self


if __name__ == '__main__':
    """
    根据环境去加载配置，实例化对象的时候的时候直接传入环境变量名称，默认配置路径为summer.config下
    例子：config['DEBUG'] 取用当前环境下的DEBUG的值，没有则返回None
    """
    config = ConfigManager('SERVER_ENV')
    print(config['DEBUG'])  # True
    print(config['xxx'])    # None
    print(config.current_config_obj)  # config object
