---
title: Javascript onkeydown onkeypress onkeyup 区别
tags:
  - javascript
date: 2018-03-04 21:17:18
---


onkeydown onkeypress onkeyup 区别

<!-- more --><!-- toc -->
```javascript
<input id="input" value="default" type="text" />
<script>
var input = document.getElementById('input');
input.onkeydown = function() {
    console.log('onkeydown ' + this.value);
}
input.onkeypress = function() {
    console.log('onkeypress ' + this.value);
}
input.onkeyup = function() {
    console.log('onkeyup ' + this.value);
}
</script>
```
现在运行这个例子，在 `input` 中输入 s 键，日志打印
```javascript
onkeydown
onkeypress
onkeyup s
```
与此可见，他们的运行顺序为 `onkeydown > onkeypress > onkeyup`，而 `onkeyup` 是在内容输入完毕后才会触发，这样如果需要拦截输入操作，就要在 `onkeydown, onkeypress` 时进行判断。

`onkeypress` 跟其他两者的区别在于
- 不识别中文输入法
- 无法响应功能键（如，delete，backspace，shift等）
