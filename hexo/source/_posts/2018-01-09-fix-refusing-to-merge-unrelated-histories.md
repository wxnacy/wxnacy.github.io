---
title: Git 解决 refusing to merge unrelated histories 错误
tags:
  - git
date: 2018-01-09 09:03:54
---


在昨天写 Maven 构建项目文章的时候，因为要把 demo 放到 GitHub 上，结果在 `pull` 代码的时候报错
<!-- more -->
```bash
fatal: refusing to merge unrelated histories
```
这个问题以前也碰到过，但因为懒，我通过一些讨巧的办法避开了这个问题，今天实在受不了了，赶紧 Google 了下，发现还是**正面面对问题**更简单。

> "git merge" used to allow merging two branches that have no common base by default, which led to a brand new history of an existing project created and then get pulled by an unsuspecting maintainer, which allowed an unnecessary parallel history merged into the existing project.  The command has been taught not to allow this by default, with an escape hatch "--allow-unrelated-histories" option to be used in a rare event that merges histories of two projects that started their lives independently.

在 Git 2.9.0 以后两个仓库的代码合并需要添加一个参数 `--allow-unrelated-histories`
```bash
$ git pull origin master --allow-unrelated-histories
```
完美解决

## 参考
- [Git 2.9 Release Notes](https://github.com/git/git/blob/master/Documentation/RelNotes/2.9.0.txt#L58-L68)
- [Git refusing to merge unrelated histories](https://stackoverflow.com/questions/37937984/git-refusing-to-merge-unrelated-histories)
