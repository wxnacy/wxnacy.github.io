---
title: Python 如何打印不换行进度条
date: 2019-04-12 22:36:10
tags: [python]
---

Python 中打印不换行进度条，可以说是简单透顶，使用内置方法 `print` 直接打印即可

<!-- more -->

先看下效果

![image](https://raw.githubusercontent.com/wxnacy/image/master/blog/python_progress.gif)

大部分时间我们使用 `print` 是不带多与参数的，但是它有个带有默认值的参数 `end`

```python
print('', end='\n')
```

默认情况下 `end='\n'`，表示打印完毕后进行换行。

`\r` 则表示将光标移动到行首

```python
print('', end='\r')     # 简而言之，这样就可以起到不换行的效果
```

完整代码请见 [single_line_progress.py](https://github.com/wxnacy/study/blob/master/python/simple/single_line_progress.py)
