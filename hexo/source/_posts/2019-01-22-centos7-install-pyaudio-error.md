---
title: CentOS 7 安装 PyAudio 出错
date: 2019-01-22 16:19:08
tags: [python]
---

CentOS 7 系统下安装 PyAudio 总是报错，关键信息如下

<!-- more --><!-- toc -->

```bash
...
#include "portaudio.h"
...
error: Setup script exited with error: command 'gcc' failed with exit status 1
```

错误原因在于缺少 `portaudio.h` 头文件，安装 portaudio 即可

访问下载页面 http://portaudio.com/download.html 下载 `pa_stable_v190600_20161030.tgz` 或更高版本，并解压安装

```bash
$ wget http://portaudio.com/archives/pa_stable_v190600_20161030.tgz
$ var -xvf pa_stable_v190600_20161030.tgz
$ cd portaudio
$ ./configure
$ sudo make && sudo make install
```

随后再次下载 PyAudio 即可

```bash
$ sudo pip install PyAudio
```

或者

```bash
$ sudo easy_install PyAudio
```
