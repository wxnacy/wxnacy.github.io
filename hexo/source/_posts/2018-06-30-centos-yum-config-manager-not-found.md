---
title: CentOS yum-config-manager command not found
date: 2018-06-30 18:25:02
tags: [linux]
---

`yum-config-manager` 命令是在 `yum-utils` 软件包中的。

<!-- more --><!-- toc -->
某些发行版本中默认是不安装的，此时判断没有 `yum-config-manager` 命令，手动安装下就行了。

```bash
if [ $SYS == 'centos' ];then
    path=`command -v yum-config-manager`
    if [ $path ];then
        echo -e "yum-utils\tinstall on $path"
    else
        sudo yum install -y yum-utils
    fi
fi
```
