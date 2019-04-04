---
title: Zsh 加载速度优化
tags:
  - zsh
date: 2019-04-04 13:59:45
---


用 Zsh 也有几年的时间，期间各种添加配置，导致了每次启动都巨慢无比。我也换了 [fish](https://fishshell.com/) 用过几天，虽然速度很快，补全功能超爽，但是它最大的问题是不兼容 bash，那还玩个毛，我的开发环境极度依赖 bash 脚本，没办法了，Zsh 还是要接着用的，但是优化速度成了一个大问题。

<!-- more --><!-- toc -->

通过 `time` 分析 `zsh` 加载速度

```bash
$ time zsh -i -c exit
5.52 real         3.56 user         2.09 sys
```

这里的 `real` 代表的是执行 `zsh` 时真实的加载速度，好家伙，这个时间真是够受的。

我们再来看下无配置加载速度

```bash
$ time zsh --no-rcs -i -c exit
0.00 real         0.00 user         0.00 sys
```

我们当然不可能优化到这个速度，但这是我们的目标。

网上优化的方法，通常是使用懒加载，这是很优雅的解决方式，也很有效，但还是那句话，***好的东西也并不一定适用于所有人***。

关于懒加载，大家可以看看这篇文章 [zshrc 启动速度分析和优化](https://best33.com/283.moe)，里面梳理了怎样分析 `zshrc` 中每条语句的加载速度，从而我们可以针对性的优化。

如果懒加载可以解决你的问题，那现在已经可以关闭网页，然后优化你的配置了。

下面我先来说说懒加载的缺点，比如 `nvm` 的配置就很浪费时间

```bash
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh"  ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion"  ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
```

我们进行懒加载配置

```bash
nvm() {
    export NVM_DIR="$HOME/.nvm"
    [ -s "$NVM_DIR/nvm.sh"  ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
    [ -s "$NVM_DIR/bash_completion"  ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
    nvm "$@"
}
```

这样再次执行测速会发现优化了很多，是不是很兴奋呢？先别着急。

懒加载配置后，启动 `zsh` 时虽然提升了速度，但是想要使用 `node` 命令，需要先执行 `nvm` 实时加载上述的配置，这似乎没什么，不使用不加载，这不挺好吗？

先来说说我的环境，我的开发环境极度依赖脚本，如果使用了懒加载，那每个启动脚本前都要先套上一个无用的 `nvm` 命令，这多少有点不伦不类，并且这对于我来说好像并没有起到加速的效果。

并且有些功能懒加载并不正常，比如：

```bash
if [ -d "${HOME}/.pyenv" ]; then
    # https://github.com/pyenv/pyenv#basic-github-checkout
    export PYENV_ROOT="$HOME/.pyenv"
    export PATH="${PYENV_ROOT}/bin:${PATH}"
    # config for vim plugin YouComplateMe
    export PYENV_VIRTUALENV_DISABLE_PROMPT=1
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)";
fi
```

`pyenv` 用懒加载并不能正常使用，可能是我用的不对，但我也不想在纠结这个件事，我在想是不是可以换一条路。

我在 [Zsh 配置文件加载顺序](/2018/10/08/zsh-startup-files/)一文中介绍了 Zsh 配置文件的生命周期。

当打开新的 Terminal 时，配置加载顺序为 `~/.zshenv` `~/.zprofile` `~/.zshrc` `~/.zlogin`

执行 `zsh` 时，配置加载顺序为 `~/.zshenv` `~/.zshrc`

除了 `~/.zshrc` 我们发现了一个有意思的配置 `~/.zprofile`，它只在启动 Terminal 时才会加载，那我把不常变动并且耗时长的配置写在这里面不就行了。

这样不管是执行 `zsh`，还是 `source ~/.zshrc` 速度都得到了改善，这个看似自欺欺人的变动，却恰好能满足我的要求。

我使用 tmux 来管理窗口，每次开机后恢复一次 tmux 缓存窗口即可，知道下次重启电脑，我可能都不会在新建 Terminal 了，这样对于我来说就已经大大的优化的 `zsh` 速度。

最后我过滤了现在的配置文件，去掉了些无用的配置后，速度如下

```bash
> time zsh -i -c exit
0.23 real         0.13 user         0.08 sys
```

OK！终于可以愉快的使用 Zsh 了。

- [Zsh 配置文件加载顺序](https://wxnacy.com/2018/10/08/zsh-startup-files/)
- [Profiling zsh shell scripts](http://blog.xebia.com/profiling-zsh-shell-scripts/)
- [Speed up initial zsh startup with lazy-loading](https://frederic-hemberger.de/articles/speed-up-initial-zsh-startup-with-lazy-loading/)
