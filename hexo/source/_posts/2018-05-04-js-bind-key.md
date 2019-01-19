---
title: JavaScript 绑定组合键
tags:
  - javascript
date: 2018-05-04 15:13:25
---


在写[在线编辑](/run/)时需要使用 `ctrl+s` 组合键完成保存的功能，今天总结下用法。

<!-- more --><!-- toc -->

监听 `ctrl+s` 组合键，并自定义功能，其他键位正常使用
```javascript
document.onkeydown = function(e) {
  console.log(e);
  var keyCode = e.keyCode || e.which || e.charCode;
  var ctrlKey = e.ctrlKey || e.metaKey;
  if(ctrlKey && keyCode == 83) {
    e.preventDefault();
    alert('保存')
  }
  return true;
}
```

按下 `ctrl+l` 打印 `event` 会有如下结果

```java
altKey : false
bubbles : true
cancelBubble : false
cancelable : true
charCode : 0
code : "KeyL"
composed : true
ctrlKey : false
currentTarget : null
defaultPrevented : false
detail : 0
eventPhase : 0
isComposing : false
isTrusted : true
key : "l"
keyCode : 76
location : 0
metaKey : true
repeat : false
returnValue : true
shiftKey : false
srcElement : body
target : body
timeStamp : 87489.19999999634
type : "keydown"
which : 76
```

根据 `altKey, shiftKey, keyCode` 我们还可以完成 `alt, shift` 等组合键的判断。

如果考虑兼容问题，可以直接使用一个开放组件 [jQuery.Hotkeys](https://github.com/jeresig/jquery.hotkeys)

```javascript
$(document).on('keydown', null, 'ctrl+a', fn);
```
