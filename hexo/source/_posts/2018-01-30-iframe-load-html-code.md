---
title: iframe 直接加载 html 代码的几种方法
tags:
  - javascript
date: 2018-01-30 09:53:46
---


iframe 除了加载普通 html 地址外，还有很多方式可以加载一段 html 代码

<!-- more --><!-- toc -->
比如我想加载一段代码
```html
<html><body>foo</body></html>
```
## data url
第一种可以使用 data url 格式，将 html 做 urlencode 编码处理后，作如下操作
```java
<iframe src="data:text/html;charset=utf-8,%3Chtml%3E%3Cbody%3Efoo%3C/body%3E%3C/html%3E" />
```

## 使用 js
另一种方式是利用 javascript 动态加载
```java
<iframe id="foo" />
<script>
var iframe = document.getElementById('foo'),
iframedoc = iframe.contentDocument || iframe.contentWindow.document;
iframedoc.body.innerHTML = 'Hello world';
</script>
```
## js 脚本
这个方法在大部分浏览器中都可以使用
```javascript
<iframe src="javascript: '<html><body>Hello, <b>world</b>.</body></html>'"></iframe>
```
## srcdoc
在 html5 中有一个新属性 srcdoc，它可以直接载入 html 代码
```java
<iframe srcdoc="<html><body>Hello, <b>world</b>.</body></html>"></iframe>
```

## 参考
- [Html code as IFRAME source rather than a URL](https://stackoverflow.com/questions/6102636/html-code-as-iframe-source-rather-than-a-url)
- [srcdoc polyfill](https://github.com/jugglinmike/srcdoc-polyfill)
