---
title: Hexo 写文章展示 Jupyter Notebook ipynb 后缀文件
date: 2020-06-13 23:58:29
tags: [hexo, jupyter]
---

使用 Hexo 展示 `ipynb` 文件是文章和代码笔记分开管理的最好方式，效果如下

<!-- more -->
<!-- toc -->

<script src="http://code.jquery.com/jquery-2.0.0.js"></script>
{% asset_jupyter /Users/wxnacy/.pyenv/shims/python ../../notebook/faker/locales.ipynb %}

这需要 [hexo-jupyter-notebook](https://github.com/qiliux/hexo-jupyter-notebook) 插件的支持

**安装**

```bash
$ npm install hexo-jupyter-notebook --save
```

**安装依赖**

```bash
$ brew install pandoc
$ pip install nbconvert
```

**修改配置**

打开 hexo 的配置文件 `_config.yml`，修改 `post_asset_folder` 为true

文章目录结构保持为

```bash
.
├── _posts
│   └── 2020-06-13-hexo-use-jupyter-notebook.md
└── notebook
    └── locals.jpynb
```

**文章嵌入**

```markdown
<script src="https://code.jquery.com/jquery-2.0.0.js"></script>
{% asset_jupyter /Users/wxnacy/.pyenv/shims/python ../../notebook/locales.ipynb %}
```

其中

`/Users/wxnacy/.pyenv/shims/python` 是当前环境 Python 脚本的路径
`../../notebook/locales.ipynb` 是 `*.ipynb` 文件和当前文章的相对路径，**这里必须是相对路径**

现在预览文章即可看到效果


参考

- [在hexo中写的文章支持jupyter-notebook显示](http://huanyouchen.github.io/2018/05/30/hexo-support-jupyter-notebook-in-blog/)



