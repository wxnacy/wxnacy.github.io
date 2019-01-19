---
title: Nginx 命令行参数
tags:
  - nginx
date: 2018-04-05 10:40:59
---


简单介绍下 Nginx 的命令行参数

<!-- more --><!-- toc -->
通过 `nginx -h` 我们可以得到如下参数信息
```bash
Options:
  -?,-h         : this help
  -v            : show version and exit
  -V            : show version and configure options then exit
  -t            : test configuration and exit
  -T            : test configuration, dump it and exit
  -q            : suppress non-error messages during configuration testing
  -s signal     : send signal to a master process: stop, quit, reopen, reload
  -p prefix     : set prefix path (default: /usr/local/Cellar/nginx/1.12.0_1/)
  -c filename   : set configuration file (default: /usr/local/etc/nginx/nginx.conf)
  -g directives : set global directives out of configuration file
```
其中我们常用到的命令如下
查看版本
```bash
$ nginx -V

nginx version: nginx/1.12.0
built by clang 8.0.0 (clang-800.0.42.1)
built with OpenSSL 1.1.0e  16 Feb 2017 (running with OpenSSL 1.1.0f  25 May 2017)
TLS SNI support enabled
configure arguments: --prefix=/usr/local/Cellar/nginx/1.12.0_1 --with-http_ssl_module --with-pcre --sbin-path=/usr/local/Cellar/nginx/1.12.0_1/bin/nginx --with-cc-opt='-I/usr/local/opt/pcre/include -I/usr/local/opt/openssl@1.1/include' --with-ld-opt='-L/usr/local/opt/pcre/lib -L/usr/local/opt/openssl@1.1/lib' --conf-path=/usr/local/etc/nginx/nginx.conf --pid-path=/usr/local/var/run/nginx.pid --lock-path=/usr/local/var/run/nginx.lock --http-client-body-temp-path=/usr/local/var/run/nginx/client_body_temp --http-proxy-temp-path=/usr/local/var/run/nginx/proxy_temp --http-fastcgi-temp-path=/usr/local/var/run/nginx/fastcgi_temp --http-uwsgi-temp-path=/usr/local/var/run/nginx/uwsgi_temp --http-scgi-temp-path=/usr/local/var/run/nginx/scgi_temp --http-log-path=/usr/local/var/log/nginx/access.log --error-log-path=/usr/local/var/log/nginx/error.log --with-http_gzip_static_module --with-http_v2_module
```
修改 `nginx.conf` 文件后测试是否通过
```bash
$ nginx -t

nginx: the configuration file /usr/local/etc/nginx/nginx.conf syntax is ok
nginx: configuration file /usr/local/etc/nginx/nginx.conf test is successful
```
运行 Nginx 时指定配置文件
```bash
$ nginx -c /www/nginx.conf
```
`-s` 的使用
快速关闭 Nginx
```bash
$ nginx -s stop
```
优雅的关闭 Nginx
```bash
$ nginx -s quit
```
优雅地关闭 Nginx，这是说 Nginx 主进程会等待 worker 进程完成当前用户请求的处理。需要启动时的用户身份来执行

重新打开日志文件
```bash
$ nginx -s reopen
```
可用于[分割日志](/2018/04/02/nginx-split-log/)后，重新打开一个新的日志文件，

重新加载配置
```bash
$ nginx -s reload
```
当主进程接收到 reload 信号，它会检查配置文件的语法，然后尝试应用该配置。如果成功，主进程启动新的 worker 进程，并发送消息给原来的 worker 进程要求他们关闭。如果加载配置失败，主进程会对改动进行回滚，继续以原来的配置进行工作。当原来的 worker 进程接收到消息要他们关闭，他们会停止接收新的连接，并继续处理当前的请求直到完成。完成之后，原来的 worker 进程将会退出。

