---
title: Python f-strings 3.6 版本新增加的字符串格式化功能
tags:
  - python
date: 2018-01-16 13:50:15
---


差不多半个月前我介绍了 Python 最新的字符串格式化函数 [format()](/2018/01/03/python-format/)，今天来介绍下 3.6 版本增加的新功能 [formatted string literals](https://docs.python.org/3.6/reference/lexical_analysis.html#f-strings) ，简称 `f-strings`

<!-- more --><!-- toc -->
## 使用
这是一个让人兴奋的格式化字符串的方式，为什么这么说，先来看看效果
```python
>>> name = 'wxnacy'
>>> f'my name is {name}'
'my name is wxnacy'
>>> f'my name is {name} and length is {len(name)}'
'my name is wxnacy and length is 6'
```
之所以叫 `f-strings` ，就是要用 f 作为字符串的开头，就像 `b'', u''` 那样，然后用 `{}` 中使用变量，甚至可以使用函数方法，就可以完成格式化，如果你也接触 Node 开发，就知道现在在 Javascript 中字符串的格式化通常是这样的
```javascript
> name = 'wxnacy'
'wxnacy'
> `my name is ${name} and length is ${name.length}`
'my name is wxnacy and length is 6'
```
## 与 format() 对比
`f-strings` 与 `format()` 格式化的语法完全一致，**只是更加简洁**
```python
>>> f'{datetime.now():%Y-%m-%d %H:%M:%S.%s}'
'2018-01-16 11:37:18.1516073838'
>>> '{:%Y-%m-%d %H:%M:%S.%s}'.format(datetime.now())
'2018-01-16 11:44:34.1516074274'
```
从上面的例子可以看到，除了以 `f` 开头外，唯一的区别就在 `datetime.now()` 放在 `:` 的前面。这样关于数字、日期、对象等格式化的使用，只要看我这篇文章 [Python 格式化函数 format](/2018/01/03/python-format/) 即可。

可以想象如果你的项目版本全面提到 3.6 以后，`f-strings` 格式化方法一定是首选，因为它不但简洁，并且**快**，它的速度比 `format()` 快了一倍。

## 参考
- [Formatted string literals](https://docs.python.org/3.6/reference/lexical_analysis.html#f-strings)
- [The new f-strings in Python 3.6](https://cito.github.io/blog/f-strings/)
- [PEP 498 -- Literal String Interpolation](https://www.python.org/dev/peps/pep-0498/)
