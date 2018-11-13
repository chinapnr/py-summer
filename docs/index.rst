.. fish_base documentation master file, created by
   sphinx-quickstart on Wed Apr 18 15:20:36 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


|Build Status| |Coverage Status| |Documentation Status|

py-summer
---------

一个快速生成 Python Web
项目框架的工具，用户无需考虑后端框架（即支持多后端，目前支持 Flask
）。支持自定义生成项目层级结构、接口。内容包含演示代码、测试用例等。

Installing
----------

Install and update using pip:

.. code:: python

    pip install -U py-summer

A Simple Example
----------------

1. 生成一个新项目

   ::

       summer create -n test_project -d ./

2. 生成的项目层级结构

   ::

       │  .gitignore                            ignore 文件
       │  gunicorn.conf                         gunicorn 配置文件
       │  requirements.txt                      项目运行所需依赖包
       │  server.py                             项目入口文件
       ├─application                            application
       │  │  __init__.py
       │  │  router.py                          路由
       │  ├─controller
       │  │      hello_controller.py            controller
       │  ├─model
       │  │      hello_model.py                 model
       │  └─view
       │         hello_handler.py               handler
       ├─config
       │      config.py                         配置文件
       ├─docker                                 docker 文件夹
       │      docker-compose.yml
       │      start.sh
       ├─log                                    日志文件夹
       ├─test                                   测试用例
       │      conftest.py
       │      test_api.py
       │      test_db.py
       └─tools                                  辅助方法
               error.py

3. 运行项目

   .. code:: python

       python server.py

   默认监听所有地址， 端口为 8080。测试页可访问
   http://127.0.0.1:8080/api/test

Features
--------

1. 集成 Flask 常用功能模块

   目前计划集成功能点如下：
    -  启动方式
    -  路由处理
    -  数据库处理
    -  异常处理
    -  常用插件


2. 支持接口根据配置文件自动生成，进一步提高代码规范，开发效率。

.. |Build Status| image:: https://travis-ci.org/chinapnr/py-summer.svg?branch=master
   :target: https://travis-ci.org/chinapnr/py-summer
.. |Coverage Status| image:: https://coveralls.io/repos/github/chinapnr/py-summer/badge.svg?branch=master
   :target: https://coveralls.io/github/chinapnr/py-summer?branch=master
.. |Documentation Status| image:: https://readthedocs.org/projects/py-summer/badge/?version=latest
   :target: https://py-summer.readthedocs.io/zh/latest/?badge=latest




函数列表
-----------------------------

.. toctree::
   :maxdepth: 1

   change_log


可以到以下单元中查找具体的函数列表和使用说明。

.. toctree::
   :maxdepth: 2

   app
   config
   models




