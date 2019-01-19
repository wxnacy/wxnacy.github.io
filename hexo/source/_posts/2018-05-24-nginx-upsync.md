---
title: Openresty 使用 upsync 模块实现服务自动发现
date: 2018-05-24 09:25:33
tags: [nginx]
---

当业务量激增时，增减服务器是很频繁的事，每次手动修改配置文件的 `upstream` 并不是让人满意的做法，每次增加了服务器 nginx 可以自动刷新就好了，这时候需要使用到 upsync 模块。

<!-- more --><!-- toc -->

## 安装模块

openresty 版本为 1.11.2.2，通过动态加载的方式导入。

**下载并解压模块**

```bash
$ wget https://github.com/weibocom/nginx-upsync-module/archive/v2.0.0.tar.gz
$ tar -zxvf v2.0.0.tar.gz

drwxrwxr-x  5 ec2-user ec2-user     4096 Jul  2  2017 nginx-upsync-module-2.0.0
```

**下载 openresty**

```bash
$ wget https://openresty.org/download/openresty-1.11.2.2.tar.gz
$ tar -zxvf openresty-1.11.2.2.tar.gz

drwxrwxr-x  6 ec2-user ec2-user     4096 May 23 06:20 openresty-1.11.2.2
```

**编译安装**

```bash
$ ./configure --prefix=/usr/local/openresty --add-dynamic-module=../nginx-upsync-module-2.0.0
$ sudo gmake && sudo gmake install
```

然后在 `/usr/local/openresty/nginx/modules` 目录下会出现 `ngx_http_upsync_module.so` 模块文件，然后在 nginx.conf 中导入

```bash
load_module modules/ngx_http_upsync_module.so;

events {
    worker_connections  1024;
}
```


## etcd

upsync 模块支持 consul 和 etcd 两种服务发现服务，在这里我们使用 etcd，如果你不了解 etcd，请看[这里](/2018/05/23/etcd/)

我们添加两个服务到 `k/v` 储存中

```bash
$ etcdctl set upstreams/127.0.0.1:8001 '{"server": "127.0.0.1:8001"}'
$ etcdctl set upstreams/127.0.0.1:8002 '{"server": "127.0.0.1:8002"}'
```

查看文件夹 `upstreams/`

```bash
$ curl http://127.0.0.1:2379/v2/keys/upstreams/

{"action":"get","node":{"key":"/upstreams","dir":true,"nodes":[{"key":"/upstreams/127.0.0.1:8001","value":"{\"server\": \"127.0.0.1:8001\"}","modifiedIndex":4,"createdIndex":4},{"key":"/upstreams/127.0.0.1:8002","value":"{\"server\": \"120.0.0.1:8002\"}","modifiedIndex":5,"createdIndex":5}],"modifiedIndex":4,"createdIndex":4}}
```

## upstream 配置

upstream 配置如下：

```bash
upstream test {
    server localhost:8003 ;
    upsync 127.0.0.1:2379/v2/keys/upstreams/ upsync_timeout=6m upsync_interval=500ms upsync_type=etcd strong_dependency=off;
    upsync_dump_path /usr/local/openresty/nginx/conf/servers/servers_test.conf;
}

server {
    listen       80;
    server_name  localhost;

    location / {
        proxy_pass http://test;
    }

    location /upstream_list {
        upstream_show;
    }
}
```

参数 `upsync_dump_path` 的作用在于将 `upstreams/` 的内容备份到本地，并作为 `upstream` 列表使用，`servers_test.conf` 内容如下

```bash
server 127.0.0.1:8001 weight=1 max_fails=2 fail_timeout=10s;
server 127.0.0.1:8002 weight=1 max_fails=2 fail_timeout=10s;
```

当 `servers_test.conf` 成功下载后，配置 `server localhost:8003;` 将不再生效，它仅仅是为了不让 nginx 报错而存在的。

`upstream_show` 的作用是返回当前服务列表

```bash
$ curl localhost/upstream_list

Upstream name: test; Backend server count: 2
        server 127.0.0.1:8001 weight=1 max_fails=2 fail_timeout=10s;
        server 127.0.0.1:8002 weight=1 max_fails=2 fail_timeout=10s;
```

- [nginx-upsync-module](https://github.com/weibocom/nginx-upsync-module)
