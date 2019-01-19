---
title: Python 安装 PyCrypto 报错
date: 2018-08-25 18:10:32
tags: [python]
---

Python 中很多加密操作都需要依赖包 PyCrypto，但是在新环境下运行它经常会报莫名其妙的错误，总结起来都是一个类型的错误格式。

<!-- more --><!-- toc -->

```bash
     from Crypto.XXX import XXX
ImportError: cannot import name 'XXX'
```

原因在于在现在的新老模块的冲突问题。

```bash
$ pip3 uninstall pycrypto
$ pip3 uninstall pycryptodome
$ pip3 install pycryptodome
```

卸载掉 Python3 自带的 `pycrypto` 模块，重新安装 `pycryptodome` 即可
