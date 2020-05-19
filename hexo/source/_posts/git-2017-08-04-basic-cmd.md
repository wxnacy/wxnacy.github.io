---
title: Git 常用命令
date: 2017-08-04
tags: [git]
---
> 有这些命令就够了

<!-- more -->

<!-- toc -->
## ssh-key

```bash
ssh-keygen -t rsa -C "$your_email"          # 获取 sshkey
cat ~/.ssh/id_rsa.pub                       # 查看 sshkey
```

## 首次使用 git

客户端首次使用 git 提交时需要将 `id_rsa.pub` 内容提交到 github 上不然每次都会提示输入用户名密码

然后输入必要的配置

```bash
git config --global user.name wxnacy            # 配置用户名
git config --global user.email xxx@qq.com       # 配置邮件
git config --global push.default simple
git push -u origin master
```


## 初始化项目
```bash
cd project_root                             # 进入项目目录
git init                                    # 初始化git仓库
git add .                                   # 添加文件到仓库
git commit -m 'init commit'                 # 提交代码到本地仓库
git remote add origin ${repository_path}    # 将项目关联到git server
git pull origin master                      # 同步代码
git push origin master                      # push代码到远程仓库
git clone ${repository_path}                # 新的位置clone项目
```

## 删除文件
```bash
rm -r file_path
git rm -r ${file_path}
git commit -m 'remove'
git pull origin master
git push origin master
```
## 用户信息
```bash
git config --global user.name wxnacy            # 配置用户名
git config --global user.email xxx@qq.com       # 配置邮件

$ git config user.name      # 查看登录名
$ git config user.email     # 查看登录邮箱
```

## 记住密码
在服务器上 `clone` 代码第一次通常会提示输入密码，为了下次不再提示，可以在 `clone` 后做如下操作
```bash
git config credential.helper store
```
## 撤销操作
### 重新提交
提交后如果发现遗漏可以使用 `git commit --amend` 重新提交
```bash
git commit -m 'initial commit'
git add forgotten_file
git commit --amend
```
### 撤销提交文件
```bash
git checkout -- <file>              # 取消对文件的修改。还原到最近的版本，废弃本地做的修改。
git reset HEAD <file>...            # 取消已经暂存的文件。即，撤销先前"git add"的操作
git reset HEAD^                     # 回退所有内容到上一个版本
git reset HEAD^ a.py                # 回退a.py这个文件的版本到上一个版本
git reset –soft HEAD~3              # 向前回退到第3个版本
git reset –hard origin/master       # 将本地的状态回退到和远程的一样
git reset 057d                      # 回退到某个版本
git revert HEAD                     # 回退到上一次提交的状态，按照某一次的commit完全反向的进行一次commit.(代码回滚到上个版本，并提交git)
git merge --abort                   # 撤销所有合并操作
```
或者
```bash
git -c core.quotepath=false rm --cached -f -- env.sh
git -c core.quotepath=false checkout HEAD -- env.sh
```
## 修改remote url
```bash
git remote set-url origin ${new_repository_path}
```

## 分支

```bash
git checkout -b ${new_branch} master    # 从master创建新分支
git checkout ${branch_name}             # 定位分支
git checkout -b {local-branch-name} origin/{remote-branch-name} # 从远程分支创建新分支
git merge --no-off ${branch_name}       # 将其他分支合并到master
git rebase origin master # master分支合并到当前分支
git pull origin {branch-name}           # 拉取远程分支
```

## 标签

```bash
git tag ${tag_name} master              # 创建新分支
git push origin ${tag_name}             # 将标签推到远程仓库
git branch -D ${branch_tag_name}        # 删除本地分支或标签
git push origin :${branch_tag_name}     # 删除远程分支或分支
```

## 提交检查

在代码提前前或查看提交记录详情时可能会用到下面几组命令

### status
```bash
git status          # 查看当前版本状态（是否修改）
```

### log

```bash
git log             # 显示提交日志
git log -1          # 显示1行日志 -n为n行
git log --stat      # 显示提交日志及相关变动文件
git log -p -m       # 显示提交日志及变动的详细情况
git log v2.0        # 显示v2.0的日志
```

### show
```bash
git show dfb02e6e4f2f7b573         # 显示某个提交的详细内容
git show dfb02                     # 可只用commitid的前几位
git show HEAD                      # 显示HEAD提交日志
git show HEAD^                     # 显示HEAD的父（上一个版本）的提交日志 ^^为上两个版本 ^5为上5个版本
git show v2.0                      # 显示v2.0的日志及详细内容
```

### diff
```bash
git diff                                  # 显示所有未添加至index的变更
git diff --cached                         # 显示所有已添加index但还未commit的变更
git diff HEAD^                            # 比较与上一个版本的差异
git diff HEAD -- ./lib                    # 比较与HEAD版本lib目录的差异
git diff origin/master..master            # 比较远程分支master上有本地分支master上没有的
git diff origin/master..master --stat     # 只显示差异的文件，不显示具体内容
```

## 参考资料
- [常用 Git 命令清单](http://www.ruanyifeng.com/blog/2015/12/git-cheat-sheet.html)
- [Pro Git](https://git-scm.com/book/zh/v2)




