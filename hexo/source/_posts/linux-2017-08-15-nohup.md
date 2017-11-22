---
title: Linux 使用nohup在后台不挂断执行命令
date: 2017-08-15
tags: [linux]
---

> nohup 搭配 & 来不挂断地运行某条命令达到后台执行的效果，默认会在根目录生成一个
nohup.out 文件用来记录所有的 log 信息，也可以重定向到其他位置。

```bash
$ nohup gunicorn run:app &
```
## 重定向日志到制定文件
```bash
$ nohup gunicorn run:app >nohup.log 2>&1 &
```
