---
title: ansible入门笔记3 Playbooks 简单扩展
date: 2017-08-08
tags: [ansible]
---

专辑：[ansible学习笔记](/2017/08/14/ansible-2017-08-14-album-study-notes/)

> Playbooks 在实际应用过程中，需要用到一些额外扩展功能，比如外部传参或指定hosts文件，本章节将着重介绍

<!-- more -->

## 外部传参

现在有一个playbook.yml文件，想要完成进入某个目录并完成部署任务，host和执行命令中的参数tag_name 需要外部传值
```bash
- hosts: '{{host}}'
  tasks:
  - name: deploy
    shell: ./deploy_api.sh '{{tag_name}}'
    args:
      chdir: ~/path

```

通过 `--extra-vars` 或简写 `-e` 进行传值,现在可以通过三种方式进行传值：
- key=value
```bash
ansible-playbook playbook.yml --extra-vars "host=xxx tag_name=xxx"
```
- json格式
```bash
ansible-playbook playbook.yml --extra-vars "{'host':'xxx','tag_name':'xxx'}"
```
- jaon文件
```bash
ansible-playbook playbook.yml --extra-vars "kwargs.json"
```

## 指定hosts文件

当多人协作开发项目的时候，都是全局/etc/ansible/hosts文件并不方便，我们可以通过传参 `--inventory-file` 或 `-i` 来制定当前playbook使用的hosts文件
```bash
ansible-playbook playbook.yml --inventory-file=~/ansible-hosts
```


