---
title: 如何在终端使用代理
tags:
  - 工具
date: 2018-02-28 09:50:19
---


如何在终端使用代理
<!-- more -->
我使用的翻墙环境使用 VPS 服务器搭建的，使用 [ShadowsocksX-NG](https://github.com/shadowsocks/ShadowsocksX-NG/releases) 客户端来完成代理操作，但是在终端环境中，仍然不能翻墙，这样很多依赖翻墙的开发就不能进行，这时候需要手动设置下环境变量。

我们需要写一个脚本来完成这件事，编辑 `~/.bash_profile`
```bash
...

function proxyoff(){
    unset http_proxy
    unset https_proxy
    echo -e "已关闭代理"
}
function proxyon() {
    export no_proxy="baidu.com,github.com,wxnacy.com"
    export http_proxy="http://127.0.0.1:1080"
    export https_proxy=$http_proxy
    echo -e "已开启代理"
}
...
```
在 `proxyon()` 函数中，`http_proxy, https_proxy` 的值是本机的代理地址，这个地址的端口号 ShadowsocksX-NG 已经帮我们完成了，`no_proxy` 是不需要走代理的地址列表，这样可以保证在访问国内时网速可以得到保证。

然后执行 `source ~/.bash_profile` 使函数生效，以后想在终端使用代理，运行 `proxyon` 即可
