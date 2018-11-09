---
title: Openresty 安装报错 ngx_postgres addon was unable to detect version of the libpq library
date: 2018-07-22 13:32:18
tags: [openresty]
---

手动编译安装 openresty 时报了个错

> ngx_postgres addon was unable to detect version of the libpq library

```bash
./configure --prefix=/opt/openresty \
            --with-luajit \
            --without-http_redis2_module \
            --with-http_iconv_module \
            --with-http_postgres_module
```

这明明是官方提供的命令行，但是它本身又不提供 postgresql-devel 只能自己手动安装

```bash
$ sudo yum install -y postgresql-devel
```

手动编译安装最好提前安装这几个包

```bash
$ sudo yum install -y pcre-devel openssl-devel gcc postgresql-devel
```
