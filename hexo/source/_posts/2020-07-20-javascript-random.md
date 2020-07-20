---
title: Javascript 创建随机字符串的方法
date: 2020-07-20 18:16:37
tags: [javascript]
---

这里使用 JavaScript 自带的几种数学函数

<!-- more -->
<!-- toc -->

- `Math.random()` 随机返回区间 [0, 1) 内的小数
- `Math.round(num)` 取 num 四舍五入后的整数
- `Math.ceil(num)` 将 num 向上取整
- `Math.floor(num)` 将 num 向下取整

我们利用 `Math.random()` 和 `Math.floor()` 两个函数来构建函数。

```javascript
var chars = [
    '0','1','2','3','4','5','6','7','8','9',
    'A','B','C','D','E','F','G','H','I','J',
    'K','L','M','N','O','P','Q','R','S','T',
    'U','V','W','X','Y','Z'
];

// 生成随机数
function randomString(n) {
    var res = "";
    for(var i = 0; i < n ; i ++) {
        var id = Math.floor(Math.random() * chars.length);
        res += chars[id];
    }
    return res;
}

console.log(randomString(10))

```
