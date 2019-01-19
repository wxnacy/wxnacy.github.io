---
title: Ubuntu 1604 版本安装 Chrome
tags:
  - linux
date: 2018-06-24 15:25:22
---


在使用 NodeJS 实现网页截图功能时，需要在 Ubuntu 上安装 Chrome 浏览器。

<!-- more --><!-- toc -->

## 安装

将下载源加入系统源列表

```bash
$ sudo wget http://www.linuxidc.com/files/repo/google-chrome.list -P /etc/apt/sources.list.d/
```

导入谷歌软件公钥

```bash
$ wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
```

安装

```bash
$ sudo apt update -y && sudo apt install -y  google-chrome-stable
```

## 使用

使用 `headless` 打印 DOM

```bash
$ google-chrome --headless --disable-gpu --dump-dom https://wxnacy.com
```

- [Ubuntu 16.04安装Chrome浏览器](https://blog.csdn.net/qq_30164225/article/details/54632634)
- [Headless Chrome](https://wxnacy.com/2018/02/12/headless-chrome/)
