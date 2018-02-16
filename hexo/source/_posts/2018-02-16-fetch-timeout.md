---
title: Javascript 给 Fetch 加上 Timeout
tags:
  - javascript
date: 2018-02-16 19:34:53
---


使用 `setTimeout()` 函数给 Fetch Api 加上 timeout 效果
<!-- more -->
```javascript
const fetchRequest = (url, params={}, timeout=10000) => {
    let isTimeout = false;
    return new Promise(function(resolve, reject) {
        const TO = setTimeout(function() {
            isTimeout = true;
            reject(new Error('Fetch timeout'));
        }, timeout);

        fetch(url, params)
            .then(res => {
                clearTimeout(TO)
                if(!isTimeout) {
                    resolve(res)
                }
            }).catch(e => {
                if( isTimeout ){
                    return
                }
                reject(e)
            })
    })
}

fetchRequest('https://ipapi.co/json', null).then(res => {
    console.log(res);
})
fetchRequest('http://localhost:8010/test', null, 1000).catch(e => {
    console.log(e)
})
```
原理很简单，首先在 `fetch()` 函数外包一层 `Promise`，然后关键点在于 `setTimeout()`
```javascript
const TO = setTimeout(function() {
    isTimeout = true;
    reject(new Error('Fetch timeout'));
}, timeout);
```
在执行 `setTimeout()` 中的函数时，抛出异常，强行中断 `fetch` 动作，也就达到了 timeout 的效果，另外在 `Promise` 外面在封装一层，使方法调用起来更加方便。

- [JavaScript fetch with Timeout](https://davidwalsh.name/fetch-timeout)
