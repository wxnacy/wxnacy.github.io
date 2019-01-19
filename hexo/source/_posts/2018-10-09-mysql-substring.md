---
title: Mysql 截取字符串的函数
date: 2018-10-09 17:06:04
tags: [mysql]
---

MySQL 字符串截取函数：left(), right(), substring(), substring_index()

<!-- more --><!-- toc -->

## left()

截取字符串左侧部分

```mysql
> select left("wxnacy.com", 6);
wxnacy
```

## right()

截取字符串右侧部分

```mysql
> select right("wxnacy.com", 4);
.com
```

## substring()

从第 4 个字符开始截取

```mysql
> select substring("wxnacy.com", 4);
acy.com
```

从第 4 个字符开始截取 3 个字符

```mysql
> select substring("wxnacy.com", 4, 3);
acy
```


从倒数第 4 个字符开始截取

```mysql
> select substring("wxnacy.com", -4);
.com
```

从第 3 个字符开始截取 2 个字符

```mysql
> select substring("wxnacy.com", -3, 2);
co
```

## substring_index()

截取到第一个 `.` 符号的位置

```mysql
> select substring_index("www.wxnacy.com", ".", 1);
www
```

截取倒数第一个 `.` 符号之后的部分

```mysql
> select substring_index("www.wxnacy.com", ".", -1);
com
```

如果好不到指定的字符，返回整个字符串
