---
title: Linux 报错 no acceptable C compiler found in $PATH
date: 2017-11-22 10:35:21
tags: [linux]
---

最近在使用 Linux 系统上安装 pyenv 时，报了 no acceptable C compiler found in
$PATH 的错误，字面意思是环境变量中没有可用的 c 编译器，查过资料后使用各自平台的
安装器安装即可

<!-- more -->

### Centos
```bash
$ yum -y install gcc
```

### Ubuntu
```bash
$ apt-get -y install gcc
```

