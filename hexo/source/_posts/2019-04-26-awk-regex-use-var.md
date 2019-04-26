---
title: awk 正则表达式中使用参数
tags:
  - linux
  - awk
date: 2019-04-26 08:08:55
---


awk 使用正则表达式过滤文本时可以使用可变参数，我本认为这应该是很普遍的需求，然而网上找了一圈也没看到一个比较全面的教程，不过东拼西凑也总算是满足了需求，今天来总结下。

<!-- more -->
<!-- toc -->

首先将当前文件列表导入到一份文本文件 [text](https://raw.githubusercontent.com/wxnacy/file/master/common/text) 中，作为测试使用

```bash
$ ll > text
```

![1](https://raw.githubusercontent.com/wxnacy/image/master/blog/awk1_548.png)

## 命令行传参

首先我们打算过滤文件列表的最后修改时间为 `10` 点的数据

```bash
$ awk '/10/ {print $0}' text
-rw-r--r--  1 wxnacy  staff    1052 Mar 13 22:50 awktest
-rw-r--r--  1 wxnacy  staff     100 Mar 25 22:53 b.py
-rw-r--r--  1 wxnacy  staff     121 Mar 14 10:19 test.go
-rw-r--r--  1 wxnacy  staff     106 Mar 13 10:53 test.js
```

这样得到的结果并准确，我们应该精确的对第 8 行进行正则匹配

```bash
$ awk '$8 ~ /10/ {print $0}' text
-rw-r--r--  1 wxnacy  staff     121 Mar 14 10:19 test.go
-rw-r--r--  1 wxnacy  staff     106 Mar 13 10:53 test.js
```

现在问题来了，我希望对 `10` 进行参数化，该怎么做呢？

awk 命令行模式可以直接使用 shell 参数，不过比较麻烦一点

```bash
$ hour=10
$ echo $hour
10
$ awk '$8 ~ /'"$hour"'/ {print $0}' text
```

`$hour` 还需要使用 `'""'` 包裹起来才行

好在 awk 也有办法传递参数，使用 `-v` 即可

```bash
$ awk -v hour=10 '$8 ~ hour {print $0}' text
```

如果使用参数的话，正则内容就不用 `//` 包裹了，直接使用参数即可。


只是这种情况下，如果我们想增加额外的符号，需要使用字符串包裹起来，比如想要查找时间以 `18` 为结尾的文件

```bash
$ awk -v hour=18 '$8 ~ hour"$" {print $0}' text
-rw-r--r--  1 wxnacy  staff     861 Apr 17 18:18 test
```

也可以使用 `if` 条件语句

```bash
$ awk -v hour=18 '{ if ($8 ~ hour"$") {print $0} }' text
```

很明显，命令行中使用 `if` 条件语句显得很乱，这主要还是要引出脚本化来。

## 脚本中传参

我们先将单引号中的条件脚本化

```bash
$ touch split.awk
$ chmod +x split.awk
$ vim split.awk
```

```bash
#!/usr/bin/env awk -f

{
    if ($8 ~ hour"$"){
        print $0
    }
}
```

执行

```bash
$ ./split.awk -v hour=18 text
-rw-r--r--  1 wxnacy  staff     861 Apr 17 18:18 test
```

这只是一个很简单的例子，真实的开发中，判断条件往往更加复杂的多，所以使用脚本是很明智的办法。

最后提一句，使用 `match()` 可以使脚本的可读性更好一些。

```bash
#!/usr/bin/env awk -f

{
    if (match($8 , hour"$")){
        print $0
    }
}
```

- [How to use awk variables in regular expressions?](https://stackoverflow.com/questions/11534173/how-to-use-awk-variables-in-regular-expressions)
