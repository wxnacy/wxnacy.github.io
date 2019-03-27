---
title: Python 访问中文文档
date: 2019-03-27 14:42:32
tags: [python]
---

今天使用中文 Google 时，以外发现了 Python 的中文文档，地址： https://docs.python.org/zh-cn

<!-- more -->

它会默认跳转到 Python 3.7 的文档

![python](https://wxnacy-img.oss-cn-beijing.aliyuncs.com/blog/python-doc-zh_1411_705.png)

有意思的是，如果使用地址：https://docs.python.org 打开文档，左上角是看不到 `zh-cn` 选项的，大概是官方认为还没到直接开发的地步，因为确实很多东西还没做好。

比如搜索功能，现在还是只能搜索英文，如何的中文信息都搜索不到。

很多文档也还保留了大量的英文内容。

不过这不影响，一些基础模块的查看，毕竟有和没有是两个概念，这对很多初学者也是很重要的。

<!-- 现在文档有 `2.7` `3.5` `3.6` `3.7` `3.8` 多个版本 -->

文档左侧可以跳转其他版本，但是有个坑，直接点过去依然进入的是英文页面，我们需要
修改下地址，比如：

```bash
https://docs.python.org/3.6/
```

```bash
https://docs.python.org/zh-cn/3.6/
```

但是 `3.5` 版本修改后是 404，说明官方还完全没有开始这个版本的翻译工作，这里也是希望官方可以尽快完善。
