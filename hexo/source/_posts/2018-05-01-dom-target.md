---
title: HTML DOM target 属性
date: 2018-05-01 20:03:58
tags: [html]
---

DOM 中 target 共有四种属性
<!-- more -->
- `_blank` 在一个新的未命名的窗口载入文档
- `_self` 在相同的框架或窗口中载入目标文档
- `_parent` 把文档载入父窗口或包含了超链接引用的框架的框架集
- `_top` 把文档载入包含该超链接的窗口,取代任何当前正在窗口中显示的框架

[试一试](/run/?id=68719487583)

**动态设置**

```javascript
var target = document.getElementById('target');
target.href = "https://baidu.com"
target.target = '_blank'
```
