---
title: Markdown 如何插入表格
date: 2018-08-08 15:16:10
tags: [markdown]
---

用 Markdown 写博客这么久，好像还没好好了解过，表格的输入。

<!-- more --><!-- toc -->

```
|title|long title|title|
|------|------|------|
|short content|short content|a long piece of content|
|a long piece of content|short content|short content|
```

通过一些 `|, -` 来组合即可显示如下的效果

|title|long title|title|
|------|------|------|
|short content|short content|a long piece of content|
|a long piece of content|short content|short content|

可以看到它在写法上比较张扬，但不影响美观的显示效果，不过为了美观，我通常这样写

```
| title                   | long title    | title                   |
| ----------------------- | ------------- | ----------------------- |
| short content           | short content | a long piece of content |
| a long piece of content | short content | short content           |

```

多余出来的空格和 `-` 并不影响最后的输出效果，`-` 至少有一个即可，以上只是一个强迫症的习惯。

在对齐方式上，默认标题居中对齐，内容居左对齐，通过 `:` 可以调整表格列的对齐方式

```
| title                   | long title    | title                   |
| :---------------------- | :-----------: | ----------------------: |
| short content           | short content | a long piece of content |
| a long piece of content | short content | short content           |
```

`:-` 为左对齐，`:-:` 为居中对齐、`-:` 为右对齐

| title                   | long title    | title                   |
| :---------------------- | :-----------: | ----------------------: |
| short content           | short content | a long piece of content |
| a long piece of content | short content | short content           |

