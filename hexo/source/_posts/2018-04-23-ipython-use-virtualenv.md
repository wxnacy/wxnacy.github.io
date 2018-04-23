---
title: IPython 使用 virtualenv 环境
date: 2018-04-23 17:20:19
tags: [python]
---

IPython 默认是不会使用当前环境的虚拟环境的，不过可以变通一下通过先打开 python shell 交互界面，然后倒入 IPython 模块的形式在达到目的。
<!-- more -->

我们直接修改 shell 命令别称

```bash
alias ipy="python -c 'import IPython; IPython.terminal.ipapp.launch_new_instance()'"
```

- [Calling IPython from a virtualenv](https://stackoverflow.com/questions/20327621/calling-ipython-from-a-virtualenv)
