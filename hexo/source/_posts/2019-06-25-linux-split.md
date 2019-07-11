---
title: Linux split 分割日志
date: 2019-06-25 14:43:11
tags: [linux]
---

split 命令用于将文件平均分割为多个小文件，多用于日志查看。

<!-- more -->
<!-- toc -->

先下载一个测试文件 [split_test](https://raw.githubusercontent.com/wxnacy/file/master/common/split_test)

```bash
$ split split_test
$ ll

-rw-r--r--  1 wxnacy  staff  216320 Jun 25 14:52 split_test
-rw-r--r--  1 wxnacy  staff   20000 Jun 25 14:54 xaa
-rw-r--r--  1 wxnacy  staff   20000 Jun 25 14:54 xab
-rw-r--r--  1 wxnacy  staff   20000 Jun 25 14:54 xac
-rw-r--r--  1 wxnacy  staff   20000 Jun 25 14:54 xad
-rw-r--r--  1 wxnacy  staff   20000 Jun 25 14:54 xae
-rw-r--r--  1 wxnacy  staff   20000 Jun 25 14:54 xaf
-rw-r--r--  1 wxnacy  staff   20000 Jun 25 14:54 xag
-rw-r--r--  1 wxnacy  staff   20000 Jun 25 14:54 xah
-rw-r--r--  1 wxnacy  staff   20000 Jun 25 14:54 xai
-rw-r--r--  1 wxnacy  staff   20000 Jun 25 14:54 xaj
-rw-r--r--  1 wxnacy  staff   16320 Jun 25 14:54 xak
```

默认 `split` 会将文件均匀的分割成多个小文件，文件名以 `x` 开头，剩余字符按字符表排序。

**语法**

```bash
$ split [OPTION]... [FILE [PREFIX]]
```

`split` 命令有多个参数可供调用

`-b` 指定输出文件的大小，单位为 byte。
`-d` 使用数字作为后缀。
`-l` 指定输出文件的行数
`-a` 指定后缀的长度

**分割出 100k 的文件**

`-b` 默认单位为 byte，可以指定分割单位，如 `K,M,G,T,P,E,Z,Y`

```bash
$ split -b 100k split_test
$ ll
total 856
-rw-r--r--  1 wxnacy  staff  216320 Jun 25 14:52 split_test
-rw-r--r--  1 wxnacy  staff  102400 Jun 25 14:59 xaa
-rw-r--r--  1 wxnacy  staff  102400 Jun 25 14:59 xab
-rw-r--r--  1 wxnacy  staff   11520 Jun 25 14:59 xac
```

**使用数字为后缀，并指定长度**

```bash
$ split -b 100k -d -a 4 split_test
$ ll
total 424
-rw-rw-r-- 1 vagrant vagrant 216320 Jun 25 07:12 split_test
-rw-rw-r-- 1 vagrant vagrant 102400 Jun 25 07:13 x0000
-rw-rw-r-- 1 vagrant vagrant 102400 Jun 25 07:13 x0001
-rw-rw-r-- 1 vagrant vagrant  11520 Jun 25 07:13 x0002
```

**指定文件前缀**

```bash
$ split -b 100k -d -a 4 split_test split.
$ ll
total 424
-rw-rw-r-- 1 vagrant vagrant 216320 Jun 25 07:12 split_test
-rw-rw-r-- 1 vagrant vagrant 102400 Jun 25 07:15 split.0000
-rw-rw-r-- 1 vagrant vagrant 102400 Jun 25 07:15 split.0001
-rw-rw-r-- 1 vagrant vagrant  11520 Jun 25 07:15 split.0002
```

**指定行数分割文件**

```bash
$ split -l 1000 split_test
$ ll
total 428
-rw-rw-r-- 1 vagrant vagrant 216320 Jun 25 07:12 split_test
-rw-rw-r-- 1 vagrant vagrant  20000 Jun 25 07:20 xaa
-rw-rw-r-- 1 vagrant vagrant  20000 Jun 25 07:20 xab
-rw-rw-r-- 1 vagrant vagrant  20000 Jun 25 07:20 xac
-rw-rw-r-- 1 vagrant vagrant  20000 Jun 25 07:20 xad
-rw-rw-r-- 1 vagrant vagrant  20000 Jun 25 07:20 xae
-rw-rw-r-- 1 vagrant vagrant  20000 Jun 25 07:20 xaf
-rw-rw-r-- 1 vagrant vagrant  20000 Jun 25 07:20 xag
-rw-rw-r-- 1 vagrant vagrant  20000 Jun 25 07:20 xah
-rw-rw-r-- 1 vagrant vagrant  20000 Jun 25 07:20 xai
-rw-rw-r-- 1 vagrant vagrant  20000 Jun 25 07:20 xaj
-rw-rw-r-- 1 vagrant vagrant  16320 Jun 25 07:20 xak

$ wc -l xaa
1000 xaa
```
