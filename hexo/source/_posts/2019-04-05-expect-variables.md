---
title: Expect 设置变量和读取环境变量
tags:
  - expect
date: 2019-04-05 20:34:00
---


Expect 中设置变量跟 Bash 稍有不同

<!-- more -->

**Bash**

```bash
name=wxnacy
echo $name  # wxnacy
```

**Expect**

```bash
set name wxnacy
puts $name  # wxnacy
```

边境变量也是如此

**Bash**

```bash
echo $HOME      # /Users/wxnacy
```

**Expect**

```bash
puts $env(HOME) # /Users/wxnacy
```
