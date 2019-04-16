#!/usr/bin/env bash

ENV=$1

if [ ! ${ENV} ]
then
    ENV=local
fi

export PYTHONPATH=`pwd` # 项目跟目录
export FLASK_CONFIG=${ENV} # 当前环境 可选 local product dev test
export NODE_PATH=`pwd`/nodejs
