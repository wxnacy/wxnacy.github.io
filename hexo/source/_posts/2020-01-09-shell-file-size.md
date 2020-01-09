---
title: Shell 获取单个文件大小的几种方式
date: 2020-01-09 16:21:42
tags: [shell]
---

假设有文件 `wxnacy`

<!-- more -->
<!-- toc -->

## wc

```bash
$ echo $(wc -c < wxnacy)
$ echo $(cat wxnacy | wc -c)
$ wc -c wxnacy | awk '{print $1}'
```

## ls

```bash
$ ls -l wxnacy | awk '{print $5}'
```

## stat

```bash
$ stat wxnacy | awk '{print $8}'
```
