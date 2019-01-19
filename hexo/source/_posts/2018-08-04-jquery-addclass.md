---
title: jQuery addClass removeClass 方法
date: 2018-08-04 11:42:56
tags: [jquery]
---

使用 jquery 操作 class 样式非常方便，使用 `addClass, removeClass` 即可进行增加和删除

<!-- more --><!-- toc -->

**addClass**

```java
$("div").addClass("red")
$("div").addClass("red blue")
```

**removeClass**

```java
$("div").removeClass("red")
$("div").removeClass("red blue")
```

该方法不止可以接受字符串，还可以接受一个方法，方法返回样式字符串即可

```javascript
// index 当前 element 索引
// currentClass 当前 element class
$("div").addClass(function(index, currentClass) {
    if( currentClass != 'red' ){
        return 'blue';
    }
    return '';
})
```

[试一试](/run/?id=68719513754)

- [addClass()](https://api.jquery.com/addclass/)
