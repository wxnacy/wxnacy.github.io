---
title: Linux 获取当前登录用户名
date: 2020-04-01 11:23:54
tags: [linux]
---

写脚本时发现需要自适应当前登录用户的名字，查询后记录下

<!-- more -->
<!-- toc -->

**USER**

```bash
$ echo $USER
wxnacy
```

**whoami**

```bash
$ echo $(whoami)
wxnacy
```

这里看着很别扭，注意三个单词中间不能有空格，不然就成了这样

```bash
$ echo $(who am i)
wxnacy ttys044 Apr 1 11:26
```

只用 `$(who)` 则可以获取更多信息

```bash
$ echo $(who)
wxnacy console Mar 31 15:40 wxnacy ttys000 Mar 31 15:44 wxnacy ttys067 Mar 31 15:48
```
