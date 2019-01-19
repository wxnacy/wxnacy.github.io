---
title: Javascript 页面刷新的几种方式
date: 2018-08-06 09:59:54
tags: [html, javascript]
---

页面刷新有几种方式

<!-- more --><!-- toc -->
## reload

```java
location.reload
```

## replace

```java
location.replace(location.href)
```

## meta-refresh

五秒钟定时刷新

```html
<meta http-equiv="refresh" content="5">
```

五秒后跳转指定页面

```html
<meta http-equiv="refresh" content="5;url=https://wxnacy.com">
```

## js 定时刷新

```java
<script language="JavaScript">
function myrefresh()
{
   window.location.reload();
}
setTimeout('myrefresh()',1000); //指定1秒刷新一次
</script>
```

- [js 刷新当前页面](https://www.jianshu.com/p/d8176460efc4)
