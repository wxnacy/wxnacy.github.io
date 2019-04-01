---
title: Pyenv 安装 Python3.7 报错：zlib not available
tags:
  - python
date: 2019-03-31 13:30:55
---


最近升级 Mac 系统，又手贱升级了 pyenv，结果安装 Python3.7 时报了错

<!-- more -->

```bash
pyenv install 3.7 zipimport.ZipImportError: can't decompress data; zlib not available
```

查询了下，发现是因为 Xcode 命令行工具没有安装需要的头，需要手动进行安装，运行如下命令可以解决这个问题

```bash
$ xcode-select --install
$ sudo installer -pkg /Library/Developer/CommandLineTools/Packages/macOS_SDK_headers_for_macOS_10.14.pkg -target /
```

我的环境是

- macOS Mojave 10.14.3
- pyenv 1.2.9
- 安装 3.7.2 版本

- [Install failed, "zlib not available" on macOS Mojave](https://github.com/pyenv/pyenv/issues/1219)
