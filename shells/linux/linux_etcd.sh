#!/usr/bin/env bash

PKG=''
SYS=''

wget https://github.com/coreos/etcd/releases/download/v3.3.5/etcd-v3.3.5-linux-amd64.tar.gz
tar -zxvf etcd-v3.3.5-linux-amd64.tar.gz
sudo cp etcd-v3.3.5-linux-amd64/etcd* /usr/bin/


sudo cp etcd.conf /etc/sysconfig/etcd.conf
sudo cp etcd.yml /etc/etcd.yml
sudo cp etcd. /etc/etcd.yml

cat <<EOF | sudo tee /etc/sysconfig/etcd.conf
ETCD_LOG_DIR=/var/log/etcd
ETCD_CONFIG=/etc/etcd.yml
EOF


cat <<EOF | sudo tee /etc/etcd.yml
name: "api"
data-dir: /var/lib/etcd
listen-client-urls: http://0.0.0.0:2379
EOF

test -d /var/lib/etcd || sudo mkdir /var/lib/etcd


