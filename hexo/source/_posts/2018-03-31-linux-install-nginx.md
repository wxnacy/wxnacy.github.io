---
title: CentOS 7 安装 Nginx
tags:
  - linux
  - nginx
date: 2018-03-31 16:16:47
---

这两天折腾 Nginx 使用 GeoIp 通过分析 ip 来区分用户来源，又学到了些东西，今天先来总结下 Nginx 的安装方式

<!-- more --><!-- toc -->
## RPM 包安装
RPM 包安装有两种方式，分别是添加 EPEL 库和添加 Nginx 库
### 安装 EPEL 库
安装 EPEL 库
```bash
$ sudo yum -y install epel-release
```
安装 Nginx
```bash
$ sudo yum -y install nginx
```
查看版本
```bash
$ nginx -V
nginx version: nginx/1.12.2
built by gcc 4.8.5 20150623 (Red Hat 4.8.5-16) (GCC)
built with OpenSSL 1.0.2k-fips  26 Jan 2017
TLS SNI support enabled
configure arguments: --prefix=/usr/share/nginx --sbin-path=/usr/sbin/nginx --modules-path=/usr/lib64/nginx/modules --conf-path=/etc/nginx/nginx.conf --error-log-path=/var/log/nginx/error.log --http-log-path=/var/log/nginx/access.log --http-client-body-temp-path=/var/lib/nginx/tmp/client_body --http-proxy-temp-path=/var/lib/nginx/tmp/proxy --http-fastcgi-temp-path=/var/lib/nginx/tmp/fastcgi --http-uwsgi-temp-path=/var/lib/nginx/tmp/uwsgi --http-scgi-temp-path=/var/lib/nginx/tmp/scgi --pid-path=/run/nginx.pid --lock-path=/run/lock/subsys/nginx --user=nginx --group=nginx --with-file-aio --with-ipv6 --with-http_auth_request_module --with-http_ssl_module --with-http_v2_module --with-http_realip_module --with-http_addition_module --with-http_xslt_module=dynamic --with-http_image_filter_module=dynamic --with-http_geoip_module=dynamic --with-http_sub_module --with-http_dav_module --with-http_flv_module --with-http_mp4_module --with-http_gunzip_module --with-http_gzip_static_module --with-http_random_index_module --with-http_secure_link_module --with-http_degradation_module --with-http_slice_module --with-http_stub_status_module --with-http_perl_module=dynamic --with-mail=dynamic --with-mail_ssl_module --with-pcre --with-pcre-jit --with-stream=dynamic --with-stream_ssl_module --with-google_perftools_module --with-debug --with-cc-opt='-O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1 -m64 -mtune=generic' --with-ld-opt='-Wl,-z,relro -specs=/usr/lib/rpm/redhat/redhat-hardened-ld -Wl,-E'
```
### 添加 Nginx 仓库
添加 Nginx 仓库
```bash
$ sudo rpm -Uvh http://nginx.org/packages/centos/7/noarch/RPMS/nginx-release-centos-7-0.el7.ngx.noarch.rpm
```
安装 Nginx
```bash
$ sudo yum -y install nginx
```
查看版本
```bash
$ nginx -V
nginx version: nginx/1.12.2
built by gcc 4.8.5 20150623 (Red Hat 4.8.5-16) (GCC)
built with OpenSSL 1.0.2k-fips  26 Jan 2017
TLS SNI support enabled
configure arguments: --prefix=/etc/nginx --sbin-path=/usr/sbin/nginx --modules-path=/usr/lib64/nginx/modules --conf-path=/etc/nginx/nginx.conf --error-log-path=/var/log/nginx/error.log --http-log-path=/var/log/nginx/access.log --pid-path=/var/run/nginx.pid --lock-path=/var/run/nginx.lock --http-client-body-temp-path=/var/cache/nginx/client_temp --http-proxy-temp-path=/var/cache/nginx/proxy_temp --http-fastcgi-temp-path=/var/cache/nginx/fastcgi_temp --http-uwsgi-temp-path=/var/cache/nginx/uwsgi_temp --http-scgi-temp-path=/var/cache/nginx/scgi_temp --user=nginx --group=nginx --with-compat --with-file-aio --with-threads --with-http_addition_module --with-http_auth_request_module --with-http_dav_module --with-http_flv_module --with-http_gunzip_module --with-http_gzip_static_module --with-http_mp4_module --with-http_random_index_module --with-http_realip_module --with-http_secure_link_module --with-http_slice_module --with-http_ssl_module --with-http_stub_status_module --with-http_sub_module --with-http_v2_module --with-mail --with-mail_ssl_module --with-stream --with-stream_realip_module --with-stream_ssl_module --with-stream_ssl_preread_module --with-cc-opt='-O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -m64 -mtune=generic -fPIC' --with-ld-opt='-Wl,-z,relro -Wl,-z,now -pie'
```
两种安装方式都很简洁，效果也差不多，但是通过 EPEL 库方式安装出来会发现，Nginx 的携带的模块要多一些，比如 `http_geoip_module` 而它恰恰是服务器安全和设置重要的模块之一，预期后期折腾的去安装模块，为什么不开始就装上呢

## 编译安装
包安装很方便，但是扩展性不够，比如添加额外的模块，还是要使用源码编译
首先安装依赖
```bash
$ yum -y install pcre pcre-devel openssl openssl-devel
```
从 [download](https://nginx.org/en/download.html) 下载当前文档版
```bash
$ wget https://nginx.org/download/nginx-1.12.2.tar.gz
```
创建相应用户
```bash
$ groupadd -f nginx
$ useradd -g nginx nginx
```
解压并安装
```bash
$ tar zxvf nginx-1.12.2.tar.gz
$ cd nginx-1.12.2
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
$ make && make install
```
默认的安装目录为 `/usr/local/nginx`
最后将命令脚本超链接到环境变量中
```bash
$ ln -sf /usr/local/nginx/sbin/nginx /usr/local/bin/nginx
```
## 使用
启动
```bash
$ nginx
```
停止
```bash
$ nginx -s [start, stop]
```
重新启动
```bash
$ nginx -s reopen
```
修改 `nginx.conf` 先进性测试是否没有语法错误
```bash
$ nginx -t
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
```
然后重新加载配置，使之生效
```bash
$ nginx -s reload
```
系统命令的方式来启动停止
```bash
$ sudo systemctl [start, stop, restart] nginx
```
设置或取消开机启动
```bash
$ sudo systemctl [enable, disable] nginx
```


