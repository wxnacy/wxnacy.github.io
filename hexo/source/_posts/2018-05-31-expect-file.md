---
title: Expect file 相关操作
date: 2018-05-31 14:55:14
tags: [expect]
---

本章将介绍 Expect 语法中 `file` 的相关操作。

<!-- more --><!-- toc -->

## 判断

**exists**

```bash
puts [file exists /usr/local/etc]             # 1
puts [file exists /usr/local/test]            # 0
```

**type**

`file type name` 可以获取文件类型共 `file, directory, characterSpecial, blockSpecial, fifo, link, socket` 几种类型

```bash
puts [file type /usr/local/etc]             # directory
puts [file type /usr/local/etc/redis.conf]  # file
```

**isdirectory**

```bash
puts [file isdirectory /usr/local/etc]                 # 1
puts [file isdirectory /usr/local/etc/redis.conf]      # 0
```

**isfile**

这里有一点需要注意，除了 `type == file` 全都会返回 0

```bash
puts [file isfile /usr/local/etc/redis.conf]    # 1
```

**判断**

```bash
if {[file isdirectory $f]} {
    puts yes
} else {
    puts no
}
```


## 操作

**link**

使用 `file link -link_type link_name target_file`

`-link_type` 有两种参数软连接 `-symbolic` 和硬链接 `-hard`，当 `link_name` 已经存在或者 `target_file` 不存在时就会报错

软连接

```bash
sh> ln -s target_file link_name
expect> file link link_name target_file     # 默认为软链接
```

硬链接

```bash
sh> ln target_file link_name
expect> file link -hard link_name target_file
```

查看软连接的连接对象

```bash
file readlink link_name
```

**join**

使用当前系统的路径分隔符将一个或多个相对目录文件名连接起来，如果有绝对路径，则前边的参数将会被舍弃掉

```bash
puts [file join a b c]      # a/b/c
puts [file join a /b c]     # /b/c
```

**delete**

```bash
file delete /usr/local/test/redis.conf
file delete -force /usr/local/test      # -force 参数可以删除非空目录
```

**copy**

用法 `file copy -force source target`

如果复制的是软连接文件，那么复制的也只是链接文件，而不是原文件

```bash
sh> ll
-rw-r--r--  1 wxnacy  wheel     0B May 31 16:24 a
lrwxr-xr-x  1 wxnacy  wheel     1B May 31 16:24 b -> a

expect> file copy b c

sh> ll
-rw-r--r--  1 wxnacy  wheel     0B May 31 16:24 a
lrwxr-xr-x  1 wxnacy  wheel     1B May 31 16:24 b -> a
lrwxr-xr-x  1 wxnacy  wheel     1B May 31 16:28 c -> a
```

覆盖目标

```bash
file copy -force file1 file2
```

复制多个文件目录中

```bash
file copy file1 file2 dir1
```

复制目录

```bash
file copy dir1 dir2
```

这里需要注意的是，如果 `dir2` 已经存在，那么 `dir1` 将会复制到 `dir2` 目录中，而在此执行则会报错，应该 `dir2` 中已经包含 `dir1`，此时即使有 `-force` 参数也不行

**rename**

相当于 `sh` 中的 `mv`，用法

```bash
file rename ?-force? ?--? source target
file rename ?-force? ?--? source ?source ...? targetDir
```

使用

```bash
sh> ll
-rw-r--r--  1 wxnacy  wheel   279B Aug 24  2017 host1
-rw-r--r--  1 wxnacy  wheel     0B Aug 24  2017 host2

expect> file rename host1 host3

sh> ll
-rw-r--r--  1 wxnacy  wheel   279B Aug 24  2017 host1
-rw-r--r--  1 wxnacy  wheel     0B Aug 24  2017 host2
-rw-r--r--  1 wxnacy  wheel   279B Aug 24  2017 host3
```

覆盖

```bash
sh> ll
-rw-r--r--  1 wxnacy  wheel   279B Aug 24  2017 host1
-rw-r--r--  1 wxnacy  wheel     0B Aug 24  2017 host2

expect> file rename -force host1 host2

sh> ll
-rw-r--r--  1 wxnacy  wheel   279B Aug 24  2017 host1
-rw-r--r--  1 wxnacy  wheel   279B Aug 24  2017 host2
```

移动到目录 `dir1`

```bash
file rename host1 host2 dir1
```


## 查看

**dirname**

获取最后一个路径分隔符以前的路径

```bash
puts [file dirname ~/data/test]     # ~/data
puts [file dirname ~/data]          # ~/
puts [file dirname ~]               # /Users
```

**tail**

获取最后一个路径分隔符以后的路径

```bash
puts [file dirname ~/data/test]     # test
```

**rootname**

查看文件名，去掉后缀

```bash
puts [file rootname do.sh]      # do
```

**extension**

获取文件名后缀，带有 `.`

```bash
puts [file extension do.sh]      # .sh
```

**separator**

获取系统分隔符

```bash
put [file separator]        # /
put [file separator ~/data] # /
```

**split**

分割路径

```bash
puts [file split ~/data]    # ~ data
```

**size**

获取文件大小，单位 Bytes

```bash
puts [file size host1]  # 279
```

**atime**

查看文件最后查看时间的时间戳

```bash
puts [file atime host1]     # 1527757243
```

**mtime**

查看文件最后修改时间的时间戳

```bash
puts [file mtime host1]     # 1527757243
```



- [file](http://wiki.tcl.tk/1041)
- [man file](https://www.tcl.tk/man/tcl/TclCmd/file.htm)
