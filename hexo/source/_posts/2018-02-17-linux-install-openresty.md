---
title: Linux 安装 openresty
tags:
  - linux
date: 2018-02-17 21:19:33
---


Linux 系统在安装 openresty 时，无法直接用 `yum, apt` 等安装包工具，需要手动添加 openresty 的仓库。

<!-- more --><!-- toc -->
## Ubuntu
### 安装
```bash
# 导入我们的 GPG 密钥：
wget -qO - https://openresty.org/package/pubkey.gpg | sudo apt-key add -

# 安装 add-apt-repository 命令
# （之后你可以删除这个包以及对应的关联包）
sudo apt-get -y install software-properties-common

# 添加我们官方 official APT 仓库：
sudo add-apt-repository -y "deb http://openresty.org/package/ubuntu $(lsb_release -sc) main"

# 更新 APT 索引：
sudo apt-get update
# 然后就可以像下面这样安装软件包，比如 openresty：
sudo apt-get install openresty
```
### 自启动
修改 `/etc/rc.local` 文件，在 `exit 0` 之前加入
```bash
/usr/bin/supervisord
```
保存退出，并修改权限
```bash
chmod +x /etc/rc.local
```
## CentOS
### 安装
```bash
# 添加仓库
sudo yum install yum-utils
sudo yum-config-manager --add-repo https://openresty.org/package/centos/openresty.repo

# 然后就可以像下面这样安装软件包，比如 openresty：
sudo yum install openresty
```
### 自启动
适用 CentOS >= 7 的版本
新建 `/usr/lib/systemd/system/openresty.service` 文件
```bash
[Unit]
Description=openresty daemon

[Service]
Type=forking
PIDFile=/usr/local/openresty/nginx/logs/nginx.pid
ExecStartPre=/usr/local/openresty/nginx/sbin/nginx -t
ExecStart=/usr/local/openresty/nginx/sbin/nginx
ExecReload=/bin/kill -s HUP $MAINPID
ExecStop=/bin/kill -s QUIT $MAINPID
PrivateTmp=true

[Install]
WantedBy=multi-user.target
```
开启自启动
```bash
systemctl enable openresty
```
查看启动状态
```bash
systemctl status openresty
```

## 手动编译
如果服务器重度依赖 Nginx 来做请求判断，那最好还是用编译的方式，`yum, apt` 安装的方式模块依赖非常有限，并不方便更改。

安装依赖
```bash
yum -y install pcre pcre-devel openssl openssl-devel
```
从 [download](https://openresty.org/cn/download.html) 页面找到最新版，或者你想要的版本
```bash
$ wget https://openresty.org/download/openresty-1.13.6.1.tar.gz
$ tar -zxvf openresty-1.13.6.1.tar.gz
$ cd openresty-1.13.6.1
$ ./configure --user=nginx --group=nginx \
    --with-http_ssl_module \
    --with-http_realip_module \
    --with-http_addition_module \
    --with-http_sub_module \
    --with-http_dav_module \
    --with-http_flv_module \
    --with-http_mp4_module \
    --with-http_gunzip_module \
    --with-http_gzip_static_module \
    --with-http_random_index_module \
    --with-http_secure_link_module \
    --with-http_stub_status_module \
    --with-mail \
    --with-mail_ssl_module \
    --with-file-aio

$ gmake && gmake install
```

- [OpenResty® Linux 包](https://openresty.org/cn/linux-packages.html)
