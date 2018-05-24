#!/usr/bin/env bash

PKG=''
SYS=''

wget https://github.com/coreos/etcd/releases/download/v3.3.5/etcd-v3.3.5-linux-amd64.tar.gz
tar -zxvf etcd-v3.3.5-linux-amd64.tar.gz
sudo cp etcd-v3.3.5-linux-amd64/etcd* /usr/local/bin
