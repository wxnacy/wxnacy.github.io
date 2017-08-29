#!/usr/bin/env bash
# 部署指定tag 的api程序
# __author__ = "wenxiaoning(wenxiaoning@gochinatv.com)"
# __copyright__ = "Copyright of GoChinaTV (2017)."


deploy_tag(){
    echo '******************************'
    echo '********开始部署api：'
    echo '******************************'
    kill -9 `ps aux | grep gunicorn_config.py | awk '{print $2}'`
#    git pull
    source env.sh
    nohup gunicorn -c gunicorn_config.py run:app &
    #nohup gunicorn -c gunicorn_config.py run:app >nohup-`date +%Y-%m-%d`.log 2>&1 &
#    gunicorn -w 2  -b 0.0.0.0:8002 run:app --log-file debug.log
#    --access-logfile access.log \

    echo '******************************'
    echo '********部署成功'
    echo '******************************'
}

main(){
    deploy_tag
}

main
