---
title: MacOS /dev/urandom 报错 tr Illegal byte sequence
tags:
  - mac
date: 2018-03-07 10:06:33
---

> tr: Illegal byte sequence

<!-- more -->
在使用 MacOS 环境运行
```bash
tr -dc A-Za-z0-9_\!\@\#\$\%\^\&\*\(\)-+= < /dev/urandom | head -c 32 | xargs
```
来生成随机数时，会报非法字符的错误，主要是因为 MacOS 在处理 unicode 字符时跟 Linux 会不一样，此时需要指定一个语言环境才行，如：C
```bash
LC_CTYPE=C tr -dc A-Za-z0-9_\!\@\#\$\%\^\&\*\(\)-+= < /dev/urandom | head -c 32 | xargs
```
