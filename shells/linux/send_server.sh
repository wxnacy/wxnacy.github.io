#!/usr/bin/env bash

IP=`curl ifconfig.io`
ETCTIP=$1
PORT=$2

if [ ! ${PORT} ]
then
    PORT=8888
fi

curl -X PUT http://${ETCTIP}:2379/v2/keys/upstreams/api/${IP}:${PORT}?ttl=65 \
    -d value="{\"server\": \"${IP}:${PORT}\", \"weight\": 5}"
