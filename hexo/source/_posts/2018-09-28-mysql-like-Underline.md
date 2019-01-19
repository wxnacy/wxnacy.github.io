---
title: Mysql 模糊搜索不识别下划线的问题
date: 2018-09-28 17:02:23
tags: [mysql]
---

使用 Mysql 进行模糊查询，使用下划线作为关键词，结果检索出了全部内容。

<!-- more --><!-- toc -->

```mysql
> select * from user where name like '%_%'
```

我很自然的想到了**转义**，然后试了下常用的转义字符 `\`

```mysql
> select * from user where name like '%\_%';
```

生效，所以如果碰见特殊字符不工作时，可以试试转义，比如 `%\%%`
