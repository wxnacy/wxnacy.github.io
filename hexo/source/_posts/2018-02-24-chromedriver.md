---
title: Chrome Driver 下载
tags:
  - python
  - 工具
date: 2018-02-24 09:16:32
---


在使用 Splinter 等 web 测试工具时，机器需要安装对应浏览器的 WebDriver 才能运行，在这总结下 Chrome Driver 在几种环境下的安装方式

<!-- more --><!-- toc -->

## MacOS
苹果最简单，使用 [Homebrew](/2017/09/07/mac-2017-09-07-homebrew/) 轻松搞定
```bash
$ brew install chromedriver
```

## Linux
Linux 就麻烦些，两种方式
### 从官网下载
- 首先访问 https://sites.google.com/a/chromium.org/chromedriver/downloads 查找最新的包
- `wget https://chromedriver.storage.googleapis.com/2.35/chromedriver_linux64.zip`
- `unzip chromedriver_linux64.zip`
- `mv chromedriver /usr/local/bin`
这种方式需要翻墙，不然下载不下来

### npm 安装
```bash
$ sudo npm -g install chromedriver
$ ln -sf /usr/lib/node_modules/chromedriver/lib/chromedriver/chromedriver /usr/local/bin/chromedriver
```

