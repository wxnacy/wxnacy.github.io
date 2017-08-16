#!/usr/bin/env bash

./run.sh
#openresty -s stop
kill -9 `ps aux | grep nginx | awk '{print $2}'`
openresty  -p `pwd`/nginx -c `pwd`/nginx/conf/nginx.conf
