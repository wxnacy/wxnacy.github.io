# git 常用命令
## 初始化项目
```bash
进入项目目录: cd project_root
初始化git仓库: git init
添加文件到仓库: git add .
提交代码到本地仓库: git commit -m 'init commit'
将项目关联到git server: git remote add origin ${repository_path}
同步代码: git pull origin master
push代码到远程仓库: git push origin master
新的位置clone项目: git clone ${repository_path}
```

## 删除文件
```bash
rm -r file_path
git rm -r ${file_path}
git commit -m 'remove'
git pull origin master
git push origin master
```


## 记住密码
```bash
git config credential.helper store
```
## revert commit
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
git checkout -b ${new_branch} master # 从master创建新分支 
git checkout ${branch_name} # 定位分支 
git merge --no-off ${branch_name} # 将其他分支合并到master 
git rebase origin master # master分支合并到当前分支 
```

## 标签

```bash
git tag ${tag_name} master # 创建新分支 
git push origin ${tag_name} # 将标签推到远程仓库 
git branch -D ${branch_tag_name} # 删除本地分支或标签 
git push origin :${branch_tag_name} # 删除远程分支或分支
```







