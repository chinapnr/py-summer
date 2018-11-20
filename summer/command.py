import os
import sys
import click
import shutil
import json
from summer import app

if __name__ == '__main__':
    sys.path.insert(0, os.path.abspath(os.curdir))


@click.group()
def cli():
    """
    Summer Server 启动命令行管理工具
    """


@cli.command('start')
@click.option('--reload', default=False, type=click.BOOL, help='是否自动重新加载服务')
@click.option('--ip', default='127.0.0.1', type=click.STRING, help='IP地址', prompt='ip地址', required=False)
@click.option('--port', default='8080', type=click.STRING, help='端口号', prompt='端口号', required=False)
def start_server(reload):
    """
    启动 Server
    :param:
        * 无
    :return:
        * 无
    """
    click.echo(click.style('server start', fg='blue'))
    app.run(use_reloader=reload, host='127.0.0.1', port=app.config['IP_PORT'])


@cli.command('create')
@click.option('--name', '-n', default='py_summer_demo', type=click.STRING, help='项目名称', prompt='项目名称',
              required=True)
@click.option('--path', '-d', default='./', type=click.STRING, help='项目路径', prompt='项目路径', required=True)
def create(name, path):
    """
    创建新项目
    :param:
        * name(str): 项目路径
        * path(str): 项目名称
    :return:
        无
    """
    project_full_path = os.path.join(path, name)
    if os.path.exists(project_full_path):
        shutil.rmtree(project_full_path)
    os.makedirs(project_full_path)

    with open(os.path.join(os.path.dirname(__file__), 'tpl', 'config.json'), "r") as f:
        config = json.load(f)
    structure = config.get('structure')
    _load_config(structure, project_full_path)


def _load_config(structure, project_full_path):
    """
    加载生成代码的配置
    :param:
        * structure(str): 配置文件
        * project_full_path(str): 项目路径
    :return:
        无
    """
    for item in structure:
        name = item.get('name')
        is_folder = item.get('is_folder')
        child = item.get('child')
        current_path = os.path.join(project_full_path, name)

        if is_folder:
            _create_folder(current_path)
            _load_config(child, current_path)
        else:
            tpl = item.get('content')
            _create_file(current_path, tpl)


def _create_folder(folder_path):
    """
    创建文件夹
    :param:
        * folder_path(str): 文件夹地址
    :return:
        * 无
    """
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
    else:
        os.makedirs(folder_path)


def _create_file(file_path, tpl_name):
    """
    根据模版，生成文件
    :param:
        * file_path(str): 文件地址
        * tpl_name(str): 模版名称
    :return:
        * 无
    """
    tpl_file_path = os.path.join(os.path.dirname(__file__), 'tpl', tpl_name)
    _buffer = open(tpl_file_path, 'rb')
    with open(file_path, 'wb') as f:
        f.write(_buffer.read())
    _buffer.close()


# server 主要执行过程
if __name__ == '__main__':
    cli.add_command(start_server)
    cli.add_command(create)
    cli()
