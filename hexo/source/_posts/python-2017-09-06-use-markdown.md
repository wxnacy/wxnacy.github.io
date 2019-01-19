---
title: Python 使用 Markdown
date: 2017-09-06 21:15
tags: [python, markdown]
---
> wxnacy 博客第一版 markdown 处理方案

<!-- more -->

<!-- toc -->
## mistune

[github](https://github.com/lepture/mistune)

### 安装
```bash
$ pip install mistune
```

### 使用
```python
import mistune

res = mistune.Markdown('# title')
print(res)

md = mistune.Markdown()
content = '# title'
print(md(content))
```

### 更多

[更多用法](https://github.com/lepture/mistune#options)

## markdown

[github](https://github.com/Python-Markdown/markdown)

### 安装
```bash
$ pip install markdown
```

### 使用

```python
import markdown

md = markdown.Markdown()
res = md.convert('# title')
print(res)
```

### TOC

```python
import markdown

EXT = ['markdown.extensions.toc']
md = markdown.Markdown(extensions=EXT)
res = md.convert('# title \n[TOC]\n## h2')
print(res)

```

### 更多
[ 官方文档 ](https://pythonhosted.org/Markdown/)
[更多extensions值](https://pythonhosted.org/Markdown/extensions/index.html)

## markdown2

[github](https://github.com/trentm/python-markdown2)

### 下载

```bash
$ pip install markdown2
```

### 使用

```python
import markdown2

md = markdown2.Markdown()
res = md.convert('# title')
print(res)
```

### TOC

```python
import markdown2

md = markdown2.Markdown(extras=["toc","header-ids"])
res = md.convert('# title \n[TOC]\n## h2')
print(res.toc_html)     # 这样只能得到单独生成的目录，不能生成到md文章中

```

### 更多
[更多extras值](https://github.com/trentm/python-markdown2/wiki/Extras)

