---
title: Javascript trim() 方法及兼容
tags:
  - javascript
date: 2018-02-13 17:37:43
---


`trim()` 方法会从一个字符串的两端删除空白字符。在这个上下文中的空白字符是所有的空白字符 (space, tab, no-break space 等) 以及所有行终止符字符（如 LF，CR）。

<!-- more --><!-- toc -->
## 使用
`trim()` 方法并不影响原字符串本身，它返回的是一个新的字符串。
```javascript
var orig = '   foo  ';
console.log(orig.trim()); // 'foo'
```

## 兼容
如果 trim() 不存在，可以在所有代码前执行下面代码
```java
if( !String.prototype.trim) {
    String.prototype.trim = function () {
        return this.replace(/^[\s\uFEFF\xA0]+|[\s\uFEFF\xA0]+$/g, '');
    };
}
```

- [原文](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/String/Trim)
