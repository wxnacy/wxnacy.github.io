---
title: Ansible Debug 调试
tags:
  - ansible
date: 2020-06-04 09:37:07
---


使用 Ansible 最痛苦的就是远程命令没有生效，但又看不到报错信息，Debug 就是为了解决这个烦恼。

<!-- more -->
<!-- toc -->

先来看个简单的例子，获取当前目录

```yml
- hosts: wxnacytest
  remote_user: root
  tasks:
  - name: Get path
    shell: |
        pwd
    register: result
  - name: Get debug info
    debug: var=result verbosity=0
```

输出结果为

<!-- ![tdMeXT.png](https://s1.ax1x.com/2020/06/03/tdMeXT.png) -->
[![tdMeXT.md.png](https://s1.ax1x.com/2020/06/03/tdMeXT.md.png)](https://imgchr.com/i/tdMeXT)

如图，远程执行命令的结果非常详细

`result.cmd` 运行的命令
`result.stdout` 运行的结果

`debug` 的参数如下

```bash
msg：调试输出的消息
var：将某个任务执行的输出作为变量传递给debug模块，debug会直接将其打印输出
verbosity：debug的级别（默认是0级，全部显示）
```


如果不想输出这么多信息，可以指定某个信息，比如 `stdout`

```yml
- hosts: wxnacytest
  remote_user: root
  tasks:
  - name: Get path
    shell: |
        pwd
    register: result
  - name: Get debug info
    debug: var=result.stdout verbosity=0
```

![td3UxI.png](https://s1.ax1x.com/2020/06/03/td3UxI.png)
