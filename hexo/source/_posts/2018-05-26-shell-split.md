---
title: Shell 语言如何 split 字符串
date: 2018-05-26 08:52:10
tags: [shell]
---

shell 语言本身不支持 `split` 语法，但是我们可以通过一些变通的方法来实现。

<!-- more --><!-- toc -->

```bash
str="aaa bbb ccc ddd"
arr=(${str})
echo $arr           # aaa
echo ${arr[@]}      # aaa bbb ccc ddd
echo ${!arr[@]}     # 0 1 2 3
echo ${arr[0]}      # aaa
```

```bash
str="aaa,bbb,ccc,ddd"
arr=(${str//,/ })   # 将 , 替换为空格
arr=(${str})
echo $arr           # aaa
echo ${arr[@]}      # aaa bbb ccc ddd
echo ${!arr[@]}     # 0 1 2 3
echo ${arr[0]}      # aaa
```
