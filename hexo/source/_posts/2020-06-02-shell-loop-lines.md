---
title: Shell 对行进行循环处理
date: 2020-06-02 16:50:22
tags: [shell]
---

在编写脚本时经常需要目标结果进行按行处理，但是正常使用 `for` 循环会把结果按照单词来循环输出，并不是我想要的效果。

<!-- more -->
<!-- toc -->

使用管道加 `while` 的形式即可实现目的

```bash
ll | while read line
do
    echo $line
done
```
