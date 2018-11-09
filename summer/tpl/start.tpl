#!/bin/bash

# 获取当前文件所在目录
basepath=$(cd `dirname $0`; pwd)
cd $basepath
cd ../

nohup /root/app/python362/bin/gunicorn -c gunicorn.conf -t 60 server:app
