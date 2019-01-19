---
title: ansible入门案例1 远程部署项目
date: 2018-07-01 10:11:35
tags: [ansible]
---

专辑：[ansible学习笔记](/2017/08/14/ansible-2017-08-14-album-study-notes/)

<!-- more --><!-- toc -->

> 根据前几章讲到的内容，我们已经可以完成一些简单的功能。本章带领大家写一个通过git打tag包远程部署python项目。

**首先创建一个myproject目录，并进入其中创建如下文件：**

- `push_tag.sh`
- `deploy.sh`
- `ansible_hosts`
- `deploy_remote.yml`
- `deploy_remote.sh`

**文件内容分别如下：**

**push_tag.sh**

该脚本的功能在于传入 `tag_name` 和提交 msg ，并提交打包推到远程仓库中

```bash
#!/usr/bin/env bash

TAG_NAME=$1
PUSH_MSG=$2

main(){
    git pull origin master
    git add .
    git commit -m ${PUSH_MSG}
    git push origin master
    git tag ${TAG_NAME}
    git push origin ${TAG_NAME}
}

if [ ! ${TAG_NAME} ]
then
    echo 'UAGE: ./push_tag.sh <regex:tag_name>'
else
    main
fi
```

**deploy.sh**

该脚本需要在远程服务器执行，通过传入 `tag_name` 从 git 获取相应版本代码，并通过 supervisor 来重启项目

```bash
#!/usr/bin/env bash
# 部署指定tag 的api程序
# __author__ = "wenxiaoning(wenxiaoning@gochinatv.com)"
# __copyright__ = "Copyright of GoChinaTV (2017)."

TAG_NAME=$1

deploy_tag(){
    echo '******************************'
    echo '********开始部署tag：' ${TAG_NAME}
    echo '******************************'
    git fetch
    git checkout ${TAG_NAME}
    sudo /usr/local/bin/supervisorctl  -c /etc/supervisord/supervisord.conf restart tmd
    echo '******************************'
    echo '********部署成功'
    echo '******************************'
}

main(){
    if [ ! ${TAG_NAME} ]
    then
        echo 'UAGE: 需要传入想要部署的tag名称'
    else
        deploy_tag
    fi
}

main

```

**ansible_hosts**

该文件配置远程服务器信息，并通过sshkey进行连接

```bash
[api_prod]
prod.server.org ansible_ssh_user=root ansible_ssh_private_key_file=~/.ssh/sshkey.pem
```

**deploy_remote.yml**

改yml完成远程命令为，进入tmd目录，并执行 `./deploy_api.sh` 脚本部署项目

```bash
- hosts: api_prod
  tasks:
    - name: deploy
      shell: ./deploy_api.sh '{{tag_name}}'
      args:
      chdir: ~/tmd
```

**deploy_remote.sh**

改脚本作为一个桥梁连接完成本地提交代码和执行远程部署两项工作

```bash
#!/usr/bin/env bash
TAG_NAME=$1
MSG=$2

deploy(){
    echo '******************************'
    echo '********开始远程部署tag：' ${TAG_NAME}
    echo '******************************'
    ./push_tag.sh ${TAG_NAME} ${MSG}
    ansible-playbook deploy_remote_api.yml --extra-vars "tag_name=${TAG_NAME}" --inventory-file=ansible_hosts
    echo '******************************'
    echo '********部署成功'
    echo '******************************'
}

if [ ! ${TAG_NAME} ]
then
    echo 'UAGE: ./git_push.sh <regex:tag_name>'
else
    deploy
fi
```

**运行**

```bash
./deploy_remote.sh 1.0.0 '我的第一个版本'
```

