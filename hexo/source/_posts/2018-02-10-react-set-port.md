---
title: React 启动自定义 Port 端口号
tags:
  - react
date: 2018-02-10 11:39:28
---


React 启动时自定义端口号
<!-- more -->
修改 `package.json` 中 `start` 一行
## Linux or MacOS
```bash
"start": "PORT=4003 react-scripts start",
```
或者
```bash
"start": "export PORT=3006 react-scripts start"
```

## Windows
```bash
"start": "set PORT=3006 && react-scripts start"
```

- [How to specify a port to run a create-react-app based project?](https://stackoverflow.com/questions/40714583/how-to-specify-a-port-to-run-a-create-react-app-based-project)

