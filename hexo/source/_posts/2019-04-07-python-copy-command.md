---
title: Python 复制文件的两种方式
tags:
  - python
date: 2019-04-07 18:48:45
---


Python 中实现文件复制，大概分为两种方式**复制函数**和**调用 shell**

<!-- more --><!-- toc -->

## 函数复制

`shutil` 模块中有几个可以实现复制的方法

其实 `copy()` 方法是最常用到的，它相当于 `cp -P` 命令，可以复制文件的内容和权限。

```python
import shutil
# shutil.copy(源文件, 目标文件) 目标文件可以是目录
shutil.copy('test.sh', 'test_copy.sh')
shutil.copy('test.sh', '/tmp')
```

```bash
-rwxr-xr-x  1 wxnacy  wheel     90 Apr  6 19:05 test.sh
-rwxr-xr-x  1 wxnacy  wheel     90 Apr  6 19:09 test_copy.sh
```

`copy()` 方法中调用了 `copyfile()` `copymode()` 两个方法。

- `copyfile()` 负责复制文件内容，但是目标文件不能是目录，并且必须可以写入
- `copymode()` 负责复制文件权限

`copyfile()` 方法中又调用了低级方法 `copyfileobj()`

`copyfileobj()` 方法可以假定了一个可选参数（缓冲区大小），你可以用来设置缓冲区长度。这是复制过程中保存在内存中的字节数。系统使用的默认大小是 16 KB。

还有个 `copy2()` 方法，它类似 `copy()`，但是它可以在复制数据时获取元数据中添加的访问和修改时间。

几个方法就功能而言 `copy2() > copy() > copyfile()`，相对应的功能和耗时是成正比的，所以我建议一般情况下可以使用 `copy()` 方法，如果大批量复制操作，并且没有特殊权限，比如图片，那么还是使用 `copyfile()` 更好一点。


## 调用 shell

还有一个万能的方式是直接调用 shell 命令。

现在使用 `subprocess` 模块代替其他调用 shell 的模块。

```python
import subprocess
import shlex

cmds = shlex.split("cp test.sh test_popen.sh")
p = subprocess.Popen(cmds)
p.communicate()
```

`Popen()` 方法的第一个参数为执行的命令，在 Unix 系统中，如果该参数为字符串，那它只能是一个可执行文件，如果想要传参，则必须以数组的形式传入，`shlex.split()` 方法可以将复杂的命令转换为数组的形式。

在 Windows 系统中可以使用字符串传入命令行，并且需要使用 `copy source_file target_file` 命令。

## 效率对比

最后对比下他们的速度，执行 100 次时间如下。

```bash
copy_file time    0.022215532000000003
copy time         0.059561121999999994
copy2 time        0.07728823600000001
popen time        0.37018151000000005
```

大概是 `subprocess` 模块会生成子进程的原因，速度慢了很多，在这种情况下，复制操作优选依然是 `copy()` `copyfile()` 方法。

- [How to Copy a File in Python – 9 Different Ways to do It!](https://www.techbeamers.com/python-copy-file/)
