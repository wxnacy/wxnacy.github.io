---
title: Javascript input 输入限制
tags:
  - javascript
date: 2018-01-14 10:55:45
---


平常开发后台需要限制 input 域输入内容，如只允许数字，这里简单介绍几种常见限制。

<!-- more --><!-- toc -->
## 纯数字
```java
<input onkeyup="value=this.value.replace(/\D+/g,'')" >
```
输入内容试试：<input onkeyup="value=this.value.replace(/\D+/g,'')" >
```java
function onlyNum() {
    if(!(event.keyCode==46)&&!(event.keyCode==8)&&!(event.keyCode==37)&&!(event.keyCode==39))
    if(!((event.keyCode>=48&&event.keyCode<=57)||(event.keyCode>=96&&event.keyCode<=105)))
    event.returnValue=false;
}
<input onkeyup="onlyNum();" style="ime-mode:Disabled">
```
输入内容试试：<input onkeydown="onlyNum();" style="ime-mode:Disabled">
## 允许数字和小数点
```java
<input onKeypress="return (/[\d.]/.test(String.fromCharCode(event.keyCode)))" >
```
输入内容试试：<input onKeypress="return (/[\d.]/.test(String.fromCharCode(event.keyCode)))" >
## 只允许汉字
```java
<input  onkeyup="value=value.replace(/[^\u4E00-\u9FA5]/g,'')">
```
输入内容试试：<input  onkeyup="value=value.replace(/[^\u4E00-\u9FA5]/g,'')">
## 只允许字母、数字和@&=
```java
<input  onkeyup="value=value.replace(/[^\w=@&]|_/ig,'')">
```
<input  onkeyup="value=value.replace(/[^\w=@&]|_/ig,'')">
