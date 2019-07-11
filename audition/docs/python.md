# Python 相关

## 语法

- 如何判断一个对象的类型

```python
>>> isinstance(1, int)
True
```

- [有几种单例实现方式](/2019/02/18/python-signletion/)
- 什么时候传值什么时候传址
- [如何进行内存管理](/2019/06/16/python-memory-management/)
- [`list` 的交集和差集](/2019/03/12/python-list-diff-inter/)

## 代码输出

- 输出 `[x * x for x in range(1, 10)]` 的结果

考察的列表解析的使用

```python
>>> [x * x for x in range(1, 10)]
[1, 4, 9, 16, 25, 36, 49, 64, 81]
```
