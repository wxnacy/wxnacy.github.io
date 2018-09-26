---
title: MySql 报错 Column count doesn't match value count at row 6540
date: 2018-09-26 11:16:29
tags: [mysql]
---

> Column count doesn't match value count at row 1

<!-- more --><!-- toc -->
该错误是在插入语句时报的，在 6540 行会看到在处理数据时，该条目的 values 数据与需要插入的列数目不同，这也是该问题的原因，将插入数据改变后，插入正常。
