---
title: 如何获取指定位数随机数
date: 2017-12-06 18:00:59
tags: [算法, 工具, python, java, javascript]
---

点击按钮获取一个 16 位的包含 `[0-9][a-z][A-Z][!@#$%^&*]` 的密码
<button onClick="getRandom(16)">获取</button>: <span id="out"></span>
<!-- more -->
在实际开发中经常会用到随机数，这里介绍各种语言的实现方法
## Python
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

STR = [
    '0', '1', '2', '3', '4', '5',
    '6', '7', '8', '9', 'a', 'b',
    'c', 'd', 'e', 'f', 'g', 'h',
    'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z'
]
def get_random_str(str_len):
    """
    获取随机字符串
    :param str_len: 需要获取的长度
    :return:
    """
    def _create():
        return str(STR[int(random.uniform(0, len(STR)))])
    res = [_create() for x in range(0, str_len)]
    return ''.join(res)
```

## Java
```java
import java.util.Random;

private final static char[] digits = {
    '0', '1', '2', '3', '4', '5',
    '6', '7', '8', '9', 'a', 'b',
    'c', 'd', 'e', 'f', 'g', 'h',
    'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z'

};
public static String getRandom(int len){
    char[] result = new char[len];
    Random r = new Random();
    for(int i = 0; i < len; i++){
        result[i] = digits[Math.abs(r.nextInt(digits.length))];
    }
    return new String(result);
}
```

## Javascript
```javascript
var digits = [
    '0', '1', '2', '3', '4', '5',
    '6', '7', '8', '9', 'a', 'b',
    'c', 'd', 'e', 'f', 'g', 'h',
    'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z'

];
function getRandom(len){
    var array = new Array(len);
    for(var i = 0; i < len; i++){
        array[i] = digits[parseInt(Math.random() * digits.length)];
    }
    return array.join('');
}
```
