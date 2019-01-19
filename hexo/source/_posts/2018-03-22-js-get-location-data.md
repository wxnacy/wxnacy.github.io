---
title: JavaScript 获取地址相关信息
tags:
  - javascript
date: 2018-03-22 16:34:12
---


简单总结下 JavaScript 环境下获取当前地址相关信息

<!-- more --><!-- toc -->
## window.location
`window.location` 中包含了很丰富的地址信息
```javascript
console.log(window.location)
```
```json
{
　　　　"hash":"",
　　　　"host":"localhost:4001",
　　　　"href":"http://localhost:4001/2018/03/22/js-get-location-data/?query=s",
　　　　"port":"4001",
　　　　"origin":"http://localhost:4001",
　　　　"search":"?query=s",
　　　　"hostname":"localhost",
　　　　"pathname":"/2018/03/22/js-get-location-data/",
　　　　"protocol":"http:",
　　　　"ancestorOrigins":{}
}
```
一般常用到 `window.location.href` 来获取当前地址，`window.location.search` 来分析传入的参数

## referrer
referrer 是流量来源地址，非常有用，可以用它来做
- 登陆后跳回访问页面
- 网站数据统计
- 防盗链
获取非常简单
```java
console.log(document.referrer);
// https://www.google.com/
```
