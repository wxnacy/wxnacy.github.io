---
title: 修改 HTMLTestRunner.py 可以在 Python3 运行
tags:
  - python
date: 2018-03-20 18:46:14
---


原版的 [HTMLTestRunner](http://tungwaiyip.info/software/HTMLTestRunner.html) 只支持 python2 环境，为了使用我做了适配 python3 的改动，并记录在此

<!-- more --><!-- toc -->
## No module named StringIO
```python
self.outputBuffer = StringIO.StringIO()
```
py3 中 `StringIO` 由 `io` 代替，所以导入模块时需要加上如下操作
```python
try:
    import StringIO
except ImportError:
    import io as StringIO
```

## AttributeError: 'dict' object has no attribute 'has_key'
py3 中去掉了 `has_key()` 方法，判断是否包含 key 使用 `in` 操作符
```python
if not rmap.has_key(cls):
# ==>
if not cls in rmap:
```
## 'str' object has no attribute 'decode'
同样的 py3 中去掉了 `decode`
```python
ue = e.decode('latin-1')
# ==>
ue = e

uo = o.decode('latin-1')
# ==>
uo = o
```
## TypeError: unsupported operand type(s) for >>: 'builtin_function_or_method' and '_io.TextIOWrapper'
`print` 是 py3 与 py2 最不可调和的矛盾
```python
print >> sys.stderr, '\nTime Elapsed: %s' % (self.stopTime-self.startTime)
# ==>
print(sys.stderr, '\nTime Elapsed: %s' % (self.stopTime-self.startTime))
```

修改后完整代码地址： https://github.com/wxnacy/study/blob/master/python/unittest_demo/HTMLTestRunner.py

测试
```bash
$ wget https://raw.githubusercontent.com/wxnacy/study/master/python/unittest_demo/HTMLTestRunner.py
$ wget https://raw.githubusercontent.com/wxnacy/study/master/python/unittest_demo/to_html.py
$ python to_html.py
$ open my_report.html
```
打开网页的效果如下

![/images/htmltestrunner.png](/images/htmltestrunner.png)
