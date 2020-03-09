---
title: Node 从管道输入参数
date: 2020-03-06 11:45:51
tags: [node]
---

记录 Node 从管道输入参数的方式

<!-- more -->
<!-- toc -->

```javascript
const stdin = process.stdin;
let data = '';

stdin.setEncoding('utf8');

stdin.on('data', function (chunk) {
  data += chunk;
});

stdin.on('end', function () {
  console.log("Hello " + data);
});

stdin.on('error', console.error);
```

调用方式

```javascript
$ echo "1 2" | node test.js
```

改为同步调用方式

```javascript
/**
 *  * Author: wxnacy(wxnacy@gmail.com)
 *   * Description:
 *    */

const stdin = process.stdin;

function pipeInput() {
  return new Promise((resolve, reject) => {
    let data = '';

    stdin.setEncoding('utf8');

    stdin.on('data', function (chunk) {
      data += chunk;
    });

    stdin.on('end', function () {
      resolve(data)
    });

    stdin.on('error', reject);

  })
}

(async()=>{

  try {

    let data = await pipeInput()
    console.log(`参数为：${data}`);
  } catch (e) {
    console.error(e)
  }
})();
```
