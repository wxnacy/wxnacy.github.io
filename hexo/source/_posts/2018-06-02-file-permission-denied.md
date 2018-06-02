---
title: Linux 输出内容到文件权限不够
tags:
  - linux
date: 2018-06-02 10:29:59
---


`sudo echo 'Hello World' >> /var/log/test` 在执行语句时会出现权限不够的错误

<!-- more --><!-- toc -->

```bash
-bash: /var/log/test: Permission denied
```

原因是虽然 `echo` 加了 `sudo`，但是 `>>` 仍然没有 `sudo` 权限，需要将整个语句都加上 `sudo` 权限

```bash
$ sudo bash -c "echo 'Hello World' >> /var/log/test"
```

另一种方式是用 `tee` 命令

```bash
$ cat <<EOF | sudo tee -a /var/log/test
> Hello World
> EOF

```

输入 `EOF` 代表完成输入
