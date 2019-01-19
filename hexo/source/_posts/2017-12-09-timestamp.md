---
title: 获取时间戳及世界时间转换
date: 2017-12-09 19:30:07
tags: [算法, 工具, javascript]
---
<link rel='stylesheet' type='text/css' href='/css/ts.css'></link>
现在的 Unix 时间戳: <span id="ts"></span> <button onClick="doBegin()" style="width: 50;">开始</button> <button onClick="doEnd()" style="width: 50;">停止</button>
现在的北京时间: <span id="bj"></span>
现在的 UTC 时间: <span id="utc"></span>
时间戳 <input id='yts' style="width: 110px;" value="1512823433"> 秒 <button onClick="doTsTrans()" style="width: 110;">转为北京时间</button> <span id='tbj' ></span>
北京时间(YYYY/MM/dd HH:mm:ss) <input id='ybj' style="width: 185px;" value="2017-12-09 21:23:52"> 秒 <button onClick="doBjToTs1()" style="width: 110;">转为时间戳</button> <span id='tts' ></span>
北京时间 <input id='y' style="width: 50px;" value="2017"> 年 <input id='M' class='m' value="12"> 月 <input id='d' class='m' value="9"> 日 <input id='h' class='m' value="21"> 时 <input id='m' class='m' value="23"> 分 <input id='s' class='m' value="52"> 秒 <button onClick="doBjToTs2()" style="width: 110;">转为时间戳</button> <span id='tts2' ></span>

<script async type="text/javascript" src="/js/ts.min.js"></script>
<!-- more -->
最近在做时间相关的功能，涉及到换算各个时区，干脆写了一个时间戳和北京时间转换的一个小工具，如上。顺便总结下几种语言在时间方面的操作

<!-- toc -->
## 获取时间戳
### Javascript
```javascript
var timestamp = Date.parse(new Date());     // ==> 1512825782000
var timestamp = (new Date()).valueOf();     // ==> 1512825782232
var timestamp=new Date().getTime();         // ==> 1512825782232
```
三个方法都可以获取时间戳，不同的地方在于第一种方法精确到秒，毫秒为用 0 补全，剩下两种方法结果是一致的

### Java
```java
import java.util.Date;
import java.util.Calendar;


System.currentTimeMillis()              // 1 ==> 1512896121862
new Date().getTime()                    // 2 ==> 1512896121862
Calendar.getInstance().getTimeInMillis()// 3 ==> 1512896121862
```
三个方法返回的结果是一致的，都精确到毫秒数。效率方面方法 1 最快，因为是直接获取机器的时间。方法 3 最慢，因为需要处理时区的问题。

## 时间戳转系统时间
### Javascript
```javascript
new Date(timestamp * 1000);
```
这样获取到的时间是当前系统时区的时间，想要获取 UTC 时间需要手动算下偏移量
```javascript
var offset = new Date().getTimezoneOffset()     // ==> -480 分钟
```
这个方法返回当前时区和 UTC 时间的偏移量，`-480分钟` 代表当前时区减去 480 分钟，即为 UTC 时间
```javascript
new Date((ts + offset * 60) * 1000)             // ==> UTC 时间
```
Javascript 没有时间格式化方法，需要自己扩展，这个方法是从网上找的，相对其他方法是比较好的，推荐使用。
```javascript
Date.prototype.format=function(fmt) {
    var o = {
        "M+" : this.getMonth()+1, //月份
        "d+" : this.getDate(), //日
        "h+" : this.getHours()%12 == 0 ? 12 : this.getHours()%12, //小时
        "H+" : this.getHours(), //小时
        "m+" : this.getMinutes(), //分
        "s+" : this.getSeconds(), //秒
        "q+" : Math.floor((this.getMonth()+3)/3), //季度
        "S" : this.getMilliseconds() //毫秒
        };
    var week = {
        "0" : "/u65e5",
        "1" : "/u4e00",
        "2" : "/u4e8c",
        "3" : "/u4e09",
        "4" : "/u56db",
        "5" : "/u4e94",
        "6" : "/u516d"
        };
    if(/(y+)/.test(fmt)){
            fmt=fmt.replace(RegExp.$1, (this.getFullYear()+"").substr(4 - RegExp.$1.length));
        }
    if(/(E+)/.test(fmt)){
            fmt=fmt.replace(RegExp.$1, ((RegExp.$1.length>1) ? (RegExp.$1.length>2 ? "/u661f/u671f" : "/u5468") : "")+week[this.getDay()+""]);
        }
    for(var k in o){
            if(new RegExp("("+ k +")").test(fmt)){
                        fmt = fmt.replace(RegExp.$1, (RegExp.$1.length==1) ? (o[k]) : (("00"+ o[k]).substr((""+ o[k]).length)));
                    }
        }
    return fmt;
};
```

## 系统时间转时间戳
### Javascript
```java
Math.round(new Date('2017-12-10 10:21:12').getTime()/1000)
Math.round(new Date('2017/12/10 10:21:12').getTime()/1000)
```
## 其他语言
- [Python](/2017/12/10/python-datetime/)

## 参考
- [Unix时间戳转换工具](http://tool.chinaz.com/Tools/unixtime.aspx)
- [世界时区查询](https://time.artjoey.com/cn/)
- [世界协调时间](http://zh.thetimenow.com/utc/coordinated_universal_time)
