---
title: HTML import 加载模块
date: 2018-04-28 16:03:55
tags: [html, javascript]
---

在写静态页面的时候动态加载模块一直是个问题，以前只能用 `iframe, ajax` 等动态加载，这样整体的加载效果很差，最近才发现 HTML 中可以使用 `import` 导入。

<!-- more --><!-- toc -->
## 使用

```html
<head>
  <link rel="import" href="/path/to/imports/stuff.html">
</head>
```

`link` 中 `href` 中的导入地址必须允许跨域。

> 浏览器的网络协议栈(network stack)会对访问相同 URL 的请求自动去重。这意味着从同一个 URL 导入的内容只会被获取一次。无论这个地址被导入多少次，最终它将只执行一次。

## 检查是否可用

```java
function supportsImports() {
  return 'import' in document.createElement('link');
}

if (supportsImports()) {
  // 支持导入!
} else {
  // 使用其他的库来加载文件。
}
```

## link.import

若想访问导入的内容，需要使用 link 元素的 import 属性：

```java
var content = document.querySelector('link[rel="import"]').import;
```

在下面几种情况下，link.import 值为 null ：
- 浏览器不支持 HTML 导入。
- <link> 没有 rel="import"。
- <link> 没有被加入到 DOM 中。
- <link> 从 DOM 中被移除。
- 资源没有开启 CORS。

### 实例

假设 warnings.html 包含如下内容：

```html
<div class="warning">
  <style scoped>
    h3 {
      color: red;
    }
  </style>
  <h3>Warning!</h3>
  <p>This page is under construction</p>
</div>

<div class="outdated">
  <h3>Heads up!</h3>
  <p>This content may be out of date</p>
</div>
```

导入页面中

```html
<head>
  <link rel="import" href="warnings.html">
</head>
<body>
  ...
  <script>
    var link = document.querySelector('link[rel="import"]');
    var content = link.import;

    // 从 warning.html 的文档中获取 DOM。
    var el = content.querySelector('.warning');

    document.body.appendChild(el.cloneNode(true));
  </script>
</body>
```

## 包含模板

HTML Template 元素是 HTML 导入的好搭档。<template> 特别适合于为需要导入的应用搭建必要的标记。将内容包裹在一个 <template> 元素中还为你提供了延迟加载内容的好处。也就是说，在 template 元素加入到 DOM 之前，它包含的脚本不会执行。

**import.html**

```html
<template>
  <h1>Hello World!</h1>
  <img src="world.png"> <!-- 只有当模板生效后才会去请求图片 -->
  <script>alert("Executed when the template is activated.");</script>
</template>
```

**index.html**

```html
<head>
  <link rel="import" href="import.html">
</head>
<body>
  <div id="container"></div>
  <script>
    var link = document.querySelector('link[rel="import"]');

    // 从导入中复制 <template>。
    var template = link.import.querySelector('template');
    var content = template.content.cloneNode(true)

    document.querySelector('#container').appendChild(content);
  </script>
</body>
```

- [HTML imports](https://www.html5rocks.com/zh/tutorials/webcomponents/imports/)
