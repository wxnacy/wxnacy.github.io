#!/usr/bin/env bash

local_env=$1

if [ ! ${local_env} ]
then
    local_env=local
fi

export PYTHONPATH=`pwd` # 项目跟目录
export FLASK_CONFIG=${local_env} # 当前环境 可选 local product dev test
export NODE_PATH=`pwd`/nodejs
