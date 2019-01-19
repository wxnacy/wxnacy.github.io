---
title: Shell 判断字符串包含关系
tags:
  - shell
date: 2018-05-29 15:22:34
---


在 shell 脚本中有几种可以判断字符串包含的关系。

<!-- more --><!-- toc -->

**利用 grep**

```bash
strA="long string"
strB="string"
result=$(echo $strA | grep "${strB}")
if [[ "$result" != "" ]]
then
    echo "包含"
else
    echo "不包含"
fi
```

**利用运算符**

```bash
strA="helloworld"
strB="low"
if [[ $strA =~ $strB ]]
then
    echo "包含"
else
    echo "不包含"
fi
```

**利用通配符**

```bash
A="helloworld"
B="low"
if [[ $A == *$B* ]]
then
    echo "包含"
else
    echo "不包含"
fi
```

- [Shell判断字符串包含关系的几种方法](https://blog.csdn.net/iamlihongwei/article/details/59484029)
