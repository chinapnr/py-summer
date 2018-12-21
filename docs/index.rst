.. fish_base documentation master file, created by
   sphinx-quickstart on Wed Apr 18 15:20:36 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


|Build Status| |Coverage Status| |Documentation Status|

py-summer
---------

一个快速生成 Python Web 项目框架的工具，用户无需考虑后端框架（即支持多后端，目前支持 Flask）。支持自定义生成项目层级结构、接口。内容包含演示代码、测试用例等。


安装
----

Install and update using pip:

.. code::

    pip install -U py-summer

示例
----

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

   .. code::

       python server.py

   默认监听所有地址， 端口为 8080。测试页可访问
   http://127.0.0.1:8080/api/test


生成的项目模块说明
------------------
通过上面的示例，我们生成了一个简单的 http web 服务，下面将对生成的目录中各模块做一下介绍，简单的文件已经在目录结构中有说明，这里将不在赘述。

1. application

这里是 web 应用程序的总目录，里面包含 model/view/controller， 即 web 服务的 MVC 部分，router.py 这里是设置整个项目路由的地方。

2. config

config 目录是整个工程的配置目录，里面通过类的形式来进行各种环境的配置，通过 application 下的 __init__.py 来导入配置信息。

3. docker

docker 中是 docker-compose 的配置文件，用来配置项目的部署环境，start.sh 是 docker 容器启动的入口文件。

4. test

test 这里是项目的单元测试模块，里面有一个 conftest.py 文件来配置测试信息，test_xxx.py 文件是具体的单元测试文件，这里使用 pytest.fixture 打通 server/client 进行测试，测试时无需额外启动 server 即可测试 server 接口。



后续计划
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




