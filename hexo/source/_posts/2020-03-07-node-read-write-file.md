---
title: Node 写入和读取文件
date: 2020-03-07 11:09:35
tags: [node]
---

记录 Node 写入和读取文件的简单方法

<!-- more -->
<!-- toc -->


```javascript
/**
 *  * Author: wxnacy(wxnacy@gmail.com)
 *   * Description:
 *    */
const fs = require('fs');

fs.writeFile('/tmp/test', 'Hello World', function(err, data) {
  if( err ){
    return console.log(err);
  }
  console.log(data);
})

fs.readFile('/tmp/test', 'utf8', (err, data) => {
  if( err ){
    return console.log(err);
  }
  console.log(data);
})
```

将读取改为同步调用方式

```javascript
/**
 *  * Author: wxnacy(wxnacy@gmail.com)
 *   * Description:
 *    */
const fs = require('fs');

const path = '/Users/wxnacy/Downloads/test.sh'

async function read() {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if( err ){
        reject(err)
      }
      resolve(data)
    })
  })
}

(async () => {

  try {

    let data = await read()
    console.log(data);
  } catch (e) {
    console.log(e);

  }

})();
```
