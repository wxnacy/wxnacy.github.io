---
title: Excel 实现类似 Mysql GROUP BY 的功能
tags:
  - excel
date: 2020-08-06 11:03:31
---


Excel 用的越多就会越明白它上 G 的安装文件里面都是啥。

<!-- more -->
<!-- toc -->

![auRcTg.png](https://s1.ax1x.com/2020/07/30/auRcTg.png)

比如上图的数据，我想要实现类似 sql 语句 `select count(0) from user group by age` 的执行结果。如下图

![auRD6P.png](https://s1.ax1x.com/2020/07/30/auRD6P.png)

实现该结果的关键函数为 `COUNTIF()`

具体步骤如下：

先将想要 `group by` 的数据复制一份出来，然后选择该区域，通过“数据”，“删除重复性”来刷选出无重复数据。

[![auRRYj.png](https://s1.ax1x.com/2020/07/30/auRRYj.png)](https://imgchr.com/i/auRRYj)

[![auRrOf.png](https://s1.ax1x.com/2020/07/30/auRrOf.png)](https://imgchr.com/i/auRrOf)

在年龄后面使用函数 `=COUNTIF(B2:B6,G2)`，它的意思是在区域 `B2, B6` 中计算等于 `G2` 值的个数

[![auR60S.png](https://s1.ax1x.com/2020/07/30/auR60S.png)](https://imgchr.com/i/auR60S)

最后选中 `H2:H3`，按下 `CTRL-D` 既可快速填充所有数据

[![auRym8.png](https://s1.ax1x.com/2020/07/30/auRym8.png)](https://imgchr.com/i/auRym8)
