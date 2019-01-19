---
title: Linux 判断是否安装某个软件
date: 2018-06-27 18:15:26
tags: [linux]
---

Linux 中如果想要判断某个软件是否安装过，可以使用 `command` 命令

<!-- more --><!-- toc -->

**使用**

```bash
$ command -pvV command [arg ...]
```

**实例**

```bash
$ command -v java
/usr/bin/java

$ command -V java
java is /usr/bin/java

$ command -p java

Usage: java [-options] class [args...]
           (to execute a class)
   or  java [-options] -jar jarfile [args...]
           (to execute a jar file)
where options include:
    -d32          use a 32-bit data model if available
    -d64          use a 64-bit data model if available
    -server       to select the "server" VM
    -zero         to select the "zero" VM
    -dcevm        to select the "dcevm" VM
                  The default VM is server.

    -cp <class search path of directories and zip/jar files>
    -classpath <class search path of directories and zip/jar files>
...
```

**判断是否安装**

```bash
if [ `command -v java` ];then
    echo 'java 已经安装'
fi
```
