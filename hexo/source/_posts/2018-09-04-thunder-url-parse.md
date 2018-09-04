---
title: 迅雷地址解析
date: 2018-09-04 16:55:40
tags: [算法]
---

平常用迅雷比较多，一直对 `thunder://` 开头的地址一直比较好奇，今天有时间来研究下它是怎么加密的。
<!-- more --><!-- toc -->

拿一个地址做例子

```bash
thunder://QUFodHRwczovL3d3dy53eG5hY3kuY29tWlo=
```

首先去掉 `thunder://` 只看后面的字符串，通过末尾的 `=` 号，我们很容易联想到这是一个 base64 编码的数据

我们试着将它解码为普通字符串得到如下结果

```bash
AAhttps://www.wxnacy.comZZ
```

很明显是一个 http 地址，只是开头结尾加上了 `AA, ZZ`，很简单，随便一个语言就可以很容易写出转换工具。

还有快车、QQ旋风等只要是类似的地址结果都是想通的逻辑，只是地址前后添加的符号各有不同而已，这里不再一一解析。