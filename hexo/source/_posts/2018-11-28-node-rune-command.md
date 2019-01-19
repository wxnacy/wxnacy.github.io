---
title: Node 运行 Linux 命令
date: 2018-11-28 17:54:47
tags: [node]
---

在 Node 中可以使用 [child_process.exec](https://nodejs.org/docs/v8.1.4/api/child_process.html#child_process_child_process_exec_command_options_callback) 方法来实现

<!-- more --><!-- toc -->

```javascript
const { exec } = require('child_process');
exec('ls', (err, stdout, stderr) => {
  if (err) {
    // node couldn't execute the command
    return;
  }

  // the *entire* stdout and stderr (buffered)
  console.log(`stdout: ${stdout}`);
  console.log(`stderr: ${stderr}`);
});
```
