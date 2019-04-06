---
title: Python 操作剪切板
tags:
  - python
date: 2019-04-06 17:59:15
---


Python 操作剪切板，需要调用系统的 C 动态库，或者使用自带的命令行。

<!-- more --><!-- toc -->

Windows 系统可以动态调用 `ctypes` 库，具体操作步骤可以看看这篇文章：https://www.jianshu.com/p/430f4af2cb06

下面我们主要来说下 Mac 系统的操作方式。

## 使用 pbcopy 和 pbpaste

在 Mac 系统中可以使用 `pbcopy` 和 `pbpaste` 来实现复制粘贴操作，这两个命令都是系统自带的。

`pbcopy` 接收管道输入的文字，并复制到剪切板。`pbpaste` 直接输出剪切板的内容

```bash
$ echo '我爱你中国' | pbcopy
$ pbpaste
我爱你中国
```

使用起来还是很方便的，接下来是 Python 中如何调用。

使用 `subprocess` 模块下的 `Popen` 方法，可以很方便的操作管道的输入输出信息。

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 在 Mac 系统中使用剪切板

import subprocess

def set_clipboard(data: str):
    p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
    p.stdin.write(data.encode("utf-8"))
    p.stdin.close()
    p.communicate()

def get_from_clipboard():
    p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
    p.wait()
    byte_data = p.stdout.read()
    p.stdout.close()
    return byte_data.decode('utf-8')

if __name__ == "__main__":
    set_clipboard('我爱你中国')
    print(get_from_clipboard())

# python clipboard.py
# 我爱你中国
```

## 使用 pyperclip 模块

如果你的系统需要适应各个平台，并且需要比较高的稳定性，那还是直接使用第三方模块 [pyperclip](https://github.com/asweigart/pyperclip) 比较方便。

它的源码地址为：https://github.com/asweigart/pyperclip/blob/master/src/pyperclip/__init__.py

其实他就是整合了上述的方法，只是应该了这么多人的使用，已经非常稳定，使用方法也更简单。

```python
>>> import pyperclip
>>> pyperclip.copy('The text to be copied to the clipboard.')
>>> pyperclip.paste()
'The text to be copied to the clipboard.'
```

`Windows` 和 `Mac` 平台可以直接使用。

`Linux` 需要 `xclip` `xsel` `gtk` `PyQt4` 依赖包，可以根据平台通过 `apt` 或 `yum` 进行安装。
