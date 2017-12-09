---
title: 获取时间戳及世界时间转换
date: 2017-12-09 19:30:07
tags: [算法, 工具, javascript]
---
<link rel='stylesheet' type='text/css' href='/ts.css'></link>
现在的 Unix 时间戳: <span id="ts"></span>
现在的北京时间: <span id="bj"></span>
现在的 UTC 时间: <span id="utc"></span>
时间戳 <input id='yts' style="width: 110px;" value="1512823433"> 秒 <button onClick="doTsTrans()" style="width: 110;">转为北京时间</button> <span id='tbj' ></span>
北京时间(YYYY/MM/dd HH:mm:ss) <input id='ybj' style="width: 185px;" value="2017-12-09 21:23:52"> 秒 <button onClick="doBjToTs1()" style="width: 110;">转为时间戳</button> <span id='tts' ></span>
北京时间 <input id='y' style="width: 50px;" value="2017"> 年 <input id='M' class='m' value="12"> 月 <input id='d' class='m' value="9"> 日 <input id='h' class='m' value="21"> 时 <input id='m' class='m' value="23"> 分 <input id='s' class='m' value="52"> 秒 <button onClick="doBjToTs2()" style="width: 110;">转为时间戳</button> <span id='tts2' ></span>

<script async type="text/javascript" src="/ts.js"></script>
<!-- more -->
最近在做时间相关的功能，涉及到换算各个时区，干脆写了一个时间戳和北京时间转换的一个小工具，如上。顺便总结下几种语言在时间方面的操作
## 获取时间戳
### javascript
```javascript
var timestamp = Date.parse(new Date());     # ==> 1512825782000
var timestamp = (new Date()).valueOf();     # ==> 1512825782232
var timestamp=new Date().getTime();         # ==> 1512825782232
```
三个方法都可以获取时间戳，不同的地方在于第一种方法精确到秒，毫秒为用 0 补全，剩下两种方法结果是一致的

***未完待续***
## 参考
[Unix时间戳转换工具](http://tool.chinaz.com/Tools/unixtime.aspx)
