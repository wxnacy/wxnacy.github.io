---
title: JavaScript 自定义监听事件 Event
date: 2018-05-08 15:31:12
tags: [javascript]
---

这个需求的由来是在做[点击或拖拽获取文件信息](/run/?id=68719489588)时，获取文件这一步操作不希望每次都写，而是封装起来，同时希望可以自定义一个监听事件，以后我只需要监听 Element 的该监听事件就可以拿到需要上传的文件。

<!-- more --><!-- toc -->

首先来看如何定义一个监听事件

**语法**

```javascript
event = new Event(typeArg, eventInit);
```

**参数**

- typeArg 是DOMString 类型，表示所创建事件的名称
- eventInit 可选 是 EventInit 类型的字典，接受以下字段:
  - "bubbles"，可选，Boolean类型，默认值为 false，表示该事件是否冒泡。
  - "cancelable"，可选，Boolean类型，默认值为 false， 表示该事件能否被取消。
  - "composed"，可选，Boolean类型，默认值为 false，指示事件是否会在影子DOM根节点之外触发侦听器。

以前也有 [Document.createEvent()](https://developer.mozilla.org/zh-CN/docs/Web/API/Document/createEvent) 创建方法，但是已经被废弃。

**使用**

```javascript
// 定义事件类型
var evt = new Event('upload', {"bubbles":true, "cancelable":true})
// 在元素上监听事件
var obj = document.getElementById('file');
obj.addEventListener('upload', function(e){
    console.log('upload 事件触发了');
}, false);

obj.dispatchEvent(evt)  // 调用监听事件
// upload 事件触发了
```

以上模拟了事件创建和触发的过程。

在获取文件信息的例子中完成使用详见[自定义监听事件](/run/?id=68719489633)

- [Event](https://developer.mozilla.org/zh-CN/docs/Web/API/Event/Event)
- [创建和触发 events](https://developer.mozilla.org/zh-CN/docs/Web/Guide/Events/Creating_and_triggering_events)
- [JavaScript event对象：当前事件](http://www.itxueyuan.org/view/6340.html)
- [JavaScript 自定义事件](https://juejin.im/entry/57a4a7427db2a2005a98bcf0)
