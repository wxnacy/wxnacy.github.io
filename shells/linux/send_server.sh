#!/usr/bin/env bash

IP=`curl ifconfig.io`
ETCTIP=$1
curl -X PUT http://${ETCTIP}:2379/v2/keys/upstreams/api/${IP}:8888?ttl=20 \
    -d value="{\"server\": \"${IP}:8888\", \"weight\": 5}"
