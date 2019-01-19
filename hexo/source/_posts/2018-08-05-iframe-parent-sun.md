---
title: Iframe 父子页面元素调用
date: 2018-08-05 11:08:52
tags: [javascript, jquery]
---

了解下 iframe 父子页面元素调用的几种方法。

<!-- more --><!-- toc -->

## 获取 iframe 内元素

- **Javascript**

```javascript
// 方法1
let text = document.getElementById("iframeId").contentWindow.document.getElementById("iframe 内元素 id").value;
// 方法2
let text = window.frames['frameName'].document.getElementById("iframe 内元素 id").value;
```

- **jquery**

```javascript
// 方法3
let text = $("#iframeId").contents().find("#iframe 内元素 id").val();
// 方法4
let text = $("#iframe 内元素 id", window.frames["frameName"].document).val();
```

## 获取 iframe 外元素


```javascript
// 方法1 javascript
let text = window.parent.document.getElementById('iframe 外元素 id').value;
// 方法2 jquery
let text = $('#iframe 外元素 id', parent.document).val();
```

## 调用 iframe 外方法

```java
parent.iframeOutFunc()
```
