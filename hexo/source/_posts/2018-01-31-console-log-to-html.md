---
title: Javascript 将 console.log 日志打印到 html 页面中
tags:
  - javascript
date: 2018-01-31 14:23:39
---


如何将 `console.log()` 打印的日志输出到 html 页面中
<!-- more -->
```javascript
(function () {
	var old = console.log;
	var logger = document.getElementById('log');
	console.log = function (message) {
		if (typeof message == 'object') {
			logger.innerHTML += (JSON && JSON.stringify ? JSON.stringify(message) : message) + '<br />';
		} else {
			logger.innerHTML += message + '<br />';
		}
	}
})();
```

## 参考
- [Javascript: console.log to html](https://stackoverflow.com/questions/20256760/javascript-console-log-to-html)
