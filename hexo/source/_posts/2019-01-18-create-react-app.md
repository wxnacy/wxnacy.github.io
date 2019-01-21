---
title: React 通过入门项目 create-react-app 了解其语法
date: 2019-01-18 14:26:20
tags: [react]
---

[create-react-app](https://github.com/facebook/create-react-app) 是 React 的入门项目，通过它可以窥见 React 项目的简单构成和基本语法。

<!-- more --><!-- toc -->

## 安装

三种方法

```bash
$ npx create-react-app my-app
```

npx 来自 npm 5.2+ 或更高版本自带软件。

```bash
$ npm init react-app my-app
```

```bash
$ yarn create react-app my-app
```

**启动**

```bash
$ cd my-app
$ yarn start
```

随后会启动 `3000` 端口服务，并自动在浏览器中打开地址 `http://localhost:300`，如图

![react-app](https://wxnacy-img.oss-cn-beijing.aliyuncs.com/blog/react.png)

为什么使用 `yarn start` 命令可以启动，原因在于 `package.json` 中的关键代码

```json
"scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
}
```

不管是 `npm` 还是 `yarn`，相应的命令都会在 `scripts` 字段中转换为相应的 `react-scripts` 命令

## 启动流程

以下为 React 项目简单结构

```bash
my-app
├── README.md
├── node_modules
├── package.json
├── .gitignore
├── public
│   ├── favicon.ico
│   ├── index.html
│   └── manifest.json
└── src
    ├── App.css
    ├── App.js
    ├── App.test.js
    ├── index.css
    ├── index.js
    ├── logo.svg
    └── serviceWorker.js
```

通过项目结构，我们慢慢了解下，React 的启动流程。

**启动程序**

首先这是一个 Node 项目，所以默认的启动程序为 `src/index.js` 文件。

通过文件中的关键代码

```java
import App from './App';

ReactDOM.render(<App />, document.getElementById('root'));
```

可以看到，`ReactDOM` 将 `<App />` 渲染到 `document.getElementById('root')` 中，`root` 是从 `public/index.html` 获取的。

**渲染程序**

查看 `App.js` 文件

```java
import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            Edit <code>src/App.js</code> and save to reload.
          </p>
          <a
            className="App-link"
            href="https://reactjs.org"
            target="_blank"
            rel="noopener noreferrer"
          >
            Learn React
          </a>
        </header>
      </div>
    );
  }
}

export default App;
```

`class App` 是渲染页面组件，在类中可以通过各种内置或自己写的 JS 方法，对页面进行处理，并通过 `render()` 方法渲染页面，在这个方法内返回的是由 JSX 语法编写的代码，该语法我认为就是由 `js/html/css` 组合而成，所以 React 也是经常被认为是大逆不道将 三种语言写在同一个文件里。

## 构建静态页面

虽然是 Node 项目，但是作为前端页面，我们总要将它构建成静态页面，才能发布到服务中。

```bash
$ yarn build
```

运行后，会在根目录生成 `build` 文件夹，构建后的静态内容都在其中，结构如下

```bash
build
├── asset-manifest.json
├── favicon.ico
├── index.html
├── manifest.json
├── precache-manifest.3351d163fa29e67b0b41ea8c711c59df.js
├── service-worker.js
└── static
    ├── css
    │   ├── main.27a53a32.chunk.css
    │   └── main.27a53a32.chunk.css.map
    ├── js
    │   ├── 1.fa92c112.chunk.js
    │   ├── 1.fa92c112.chunk.js.map
    │   ├── main.881217d8.chunk.js
    │   ├── main.881217d8.chunk.js.map
    │   ├── runtime~main.229c360f.js
    │   └── runtime~main.229c360f.js.map
    └── media
        └── logo.5d5d9eef.svg

4 directories, 15 files
```

页面入口为 `index.html`，静态文件在 `static` 文件夹中。

不过整个文件夹为什么只有一个 `index.html`，如果有多个页面，它可以完成任务吗？

## 为什么入口只有 index.html

首先回答上面那个问题，React 项目只需要一个 `index.html` 就可以访问所有页面。

为什么呢？要回答这个问题需要看下源码。

上边我们说到 `index.js` 加载了 `App.js` 渲染的页面，那么我们可以写多个类似 `App.js` 的“页面”，而 `index.js` 中可以通过访问地址来决定渲染那个页面。

当然这需要借助其他依赖包，不在我们本次讨论返回内。
