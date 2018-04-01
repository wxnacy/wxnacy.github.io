#!/usr/bin/env bash

# 分割 nginx 日志

LOG_DIR=/usr/local/opt/openresty/nginx/logs
LOG_FILE=${LOG_DIR}/access.log
DT=`date "+%Y%m%d%H%M%S"`
test -f ${LOG_FILE} || mv ${LOG_FILE} ${LOG_FILE}.${DT}
openresty -s reopen
