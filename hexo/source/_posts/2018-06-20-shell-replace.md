---
title: Shell 中的 Replace
tags:
  - shell
date: 2018-06-20 17:00:37
---


Shell 中没有没有 Replace 方法，但是有一些替换方案。

<!-- more --><!-- toc -->

**用法**

```bash
${parameter/pattern/string}
```

**使用**

```bash
$ a=/data/wxnacy/data/log/log.txt
$ echo ${a/data/User}           # 将第一个 data 替换为 User
/User/wxnacy/data/log/log.txt

$ echo ${a//data/User}           # 将全部 data 替换为 User
/User/wxnacy/User/log/log.txt

$ echo ${a/#\/data/\/User}           # 匹配开头 /data 替换为 /User（/ 需要转义）
/User/wxnacy/data/log/log.txt

$ echo ${a/%log.txt/User}           # 匹配结尾 log.txt 替换为 User
/data/wxnacy/data/log/User
```

其他方法

还有一种方法是利用 sed 来实现

```bash
$ echo $a | sed -e "s/data/User/g"
/User/wxnacy/User/log/log.txt
```

对比一下还是第一种方式简单

- [bash shell 中的扩展--参数和变量扩展](http://blog.51cto.com/xuke1668/868683)
- [Replace a string in shell script using a variable](https://stackoverflow.com/questions/3306007/replace-a-string-in-shell-script-using-a-variable)
