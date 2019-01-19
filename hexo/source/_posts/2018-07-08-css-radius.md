---
title: CSS3 div 添加圆角边框
date: 2018-07-08 14:09:53
tags: [css]
---

在 CSS3 中使用 `border-radius` 属性来实现圆角功能。

<!-- more --><!-- toc -->

以像素大小来定义，数值越大，弧度越大

```css
div {
    border: 1px solid;
    border-radius: 25px;
}
```

也可以用百分比来定义

```css
div {
    border: 1px solid;
    witdh: 100px;
    height: 100px;
    border-radius: 20%;
}
```

Javascript 动态设置该属性

```javascript
object.style.borderRadius="5px"
```
