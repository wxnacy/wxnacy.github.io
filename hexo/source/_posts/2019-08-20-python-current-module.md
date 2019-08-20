---
title: Python 获取当前文件的模块对象
date: 2019-08-20 14:26:10
tags: [python]
---

根据[官方](https://www.python.org/dev/peps/pep-3130/)文档可以得到这样的用法

<!-- more -->
<!-- toc -->

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

import sys
mod = sys.modules[__name__]
```

这个特性可以应用在什么场景呢？当模块中的方法有什么共同特性时，我们可以配合 `getattr` 方法来进行动态调用，而不必编写复杂的判断语句。

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

def format_size(size: int):
    '''格式化大小'''
    unit = {
        0: 'B',
        1: 'K',
        2: 'M',
        3: 'G',
        4: 'T',
    }

    for i in range(6):
        if 1024 ** i <= size < 1024 ** ( i + 1 ):
            if i > 0:
                size = size / 1024 ** i
            return '{:0.1f}{}'.format( size, unit[i])
    return '{}B'.format(size)


if __name__ == "__main__":
    import sys
    module = sys.modules[__name__]
    args = sys.argv[1:]
    func_name = args[0]
    func = getattr(module, func_name)
    res = func(int(args[1]))
    print(res)

    # 调用方法
    # $ python utils.py format_size 1024
```
