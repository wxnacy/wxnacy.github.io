---
title: js和css获取屏幕大小
date: 2017-08-05
tags: [javascript]
---

[原文：https://segmentfault.com/q/1010000004605042](https://segmentfault.com/q/1010000004605042)

<!-- more --><!-- toc -->
## js
```javascript
function getScreenInfo()
{
    var s = "";
    s = " 网页可见区域宽：" document.body.clientWidth;
    s = " 网页可见区域高：" document.body.clientHeight;
    s = " 网页可见区域宽：" document.body.offsetWidth " (包括边线和滚动条的宽)";
    s = " 网页可见区域高：" document.body.offsetHeight " (包括边线的宽)";
    s = " 网页正文全文宽：" document.body.scrollWidth;
    s = " 网页正文全文高：" document.body.scrollHeight;
    s = " 网页被卷去的高(ff)：" document.body.scrollTop;
    s = " 网页被卷去的高(ie)：" document.documentElement.scrollTop;
    s = " 网页被卷去的左：" document.body.scrollLeft;
    s = " 网页正文部分上：" window.screenTop;
    s = " 网页正文部分左：" window.screenLeft;
    s = " 屏幕分辨率的高：" window.screen.height;
    s = " 屏幕分辨率的宽：" window.screen.width;
    s = " 屏幕可用工作区高度：" window.screen.availHeight;
    s = " 屏幕可用工作区宽度：" window.screen.availWidth;
    s = " 你的屏幕设置是 " window.screen.colorDepth " 位彩色";
    s = " 你的屏幕设置 " window.screen.deviceXDPI " 像素/英寸";
}

```
## css判断
```css
/* 小屏幕（平板，大于等于 768px） */
@media (min-width: 768px) { ... }

/* 中等屏幕（桌面显示器，大于等于 992px） */
@media (min-width: 992px) { ... }

/* 大屏幕（大桌面显示器，大于等于 1200px） */
@media (min-width: 1200px) { ... }

```


