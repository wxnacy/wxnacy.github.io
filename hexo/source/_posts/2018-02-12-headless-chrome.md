---
title: Headless Chrome
tags:
  - 工具
date: 2018-02-12 17:05:43
---


> Headless Chrome is shipping in Chrome 59. It's a way to run the Chrome browser in a headless environment. Essentially, running Chrome without chrome! It brings all modern web platform features provided by Chromium and the Blink rendering engine to the command line.

<!-- more --><!-- toc -->
Headless Chrome 是在无头环境中运行 Chrome 的一种方式，即在没有 chrome 的情况下运行 Chrome。恩？没有 chrome 还怎么运行，这里有点绕，没有 chrome 是指不用真的打开一个浏览器，而是在命令行中运行命令，并模拟 Chrome 加载网页。这种方式在开发中很是方便。

## 版本要求
Chrome 59 版本以上才支持这个功能，如果你不知道当前客户端的版本，打开一个浏览器并打开 `chrome://version` 即可，如果版本过低，先升级下吧。

## 运行命令
在电脑中安装的 Chrome 客户端是并没有在环境变量中的，修改 `~/.bash_profile`
```bash
alias chrome="/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome"
alias chrome-canary="/Applications/Google\ Chrome\ Canary.app/Contents/MacOS/Google\ Chrome\ Canary"
alias chromium="/Applications/Chromium.app/Contents/MacOS/Chromium"
```
随后执行 `source ~/.bash_profile` 使变量生效，并在终端中输入 `chrome` 可以打开一个浏览器，这样环境变量就生效了。

## 使用 headless
### 打印 Dom
参数 `--dump-dom` 可以将 `document.body.innerHTML` 打印到标准输出中
```bash
chrome --headless --disable-gpu --dump-dom https://wxnacy.com
```
- `--headless` 即为使用 headless 模式打开 chrome
- `--disable-gpu` 如果在 Windows 中需要使用该参数

### 输出 PDF
将网页输出到名为 `output.pdf` 的文件中
```bash
chrome --headless --disable-gpu --print-to-pdf https://wxnacy.com
```

### 截图
将网页截图并命名为 `screenshot.png` 保存到当前目录中
```bash
chrome --headless --disable-gpu --screenshot https://wxnacy.com
```
设定打开多大的模拟浏览器在加载页面
```bash
chrome --headless --disable-gpu --screenshot --window-size=1280,1696 https://wxnacy.com
```

### REPL 模式 (read-eval-print loop)
该模式会进入一个 Javascript 环境，并可以通过输入 Javascript 指令来分析 Dom 元素
```bash
wxnacy@bogon ~/Documents> chrome --headless --disable-gpu --repl https://wxnacy.com
location.hre[0212/160208.469737:INFO:headless_shell.cc(398)] Type a Javascript expression to evaluate or "quit" to exit.
>>> document.title
{"result":{"type":"string","value":"wxnacy 博客"}}
```

- [Getting Started with Headless Chrome](https://developers.google.com/web/updates/2017/04/headless-chrome)


