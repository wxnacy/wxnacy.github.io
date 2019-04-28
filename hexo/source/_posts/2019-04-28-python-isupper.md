---
title: Python 判断字符串是否为大写及 is 方法延伸
tags:
  - python
date: 2019-04-28 21:16:02
---


Python 判断字符串是否为大写及延伸

<!-- more -->
<!-- toc -->

以下方法仅判断字符，数字和符号不影响结果

**isupper()** 判断是否都为大写

```python
>>> '1a!'.isupper()
False
>>> '1A!'.isupper()
True
```

**islower()** 判断是否都为小写

```python
>>> '1As!'.islower()
False
>>> '1s!'.islower()
True
```

**istitle()** 判断所有的单词首字符都是大写

```python
>>> 'This Is Upper'.istitle()
True
>>> 'This Is upper1'.istitle()
False
```

**isspace()** 判断所有的字符都是空格

```python
>>> 'This Is upper1'.isspace()
False
>>> ' '.isspace()
True
```

**isalnum()** 判断所有的字符都是数字或字母

```python
>>> '1a!'.isalnum()
False
>>> '1a'.isalnum()
True
>>> 'aa'.isalnum()
True
>>> '11'.isalnum()
True
```

**isalpha()** 判断所有的字符都是字母

```python
>>> '11'.isalpha()
False
>>> '1a'.isalpha()
False
>>> 'aa'.isalpha()
True
```

**isdigit()** 判断所有的字符都是数字

```python
>>> 'aa'.isdigit()
False
>>> '11'.isdigit()
True
>>> '1a'.isdigit()
False
```

还有两个类似的方法 **isdecimal()** 和 **isnumeric()**

