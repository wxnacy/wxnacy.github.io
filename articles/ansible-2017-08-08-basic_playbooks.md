# ansible入门笔记2 Playbooks

专辑：[ansible学习笔记](/?p=/doc/shell/ansible/study_notes.md)

> Playbooks 是 Ansible的配置,部署,编排语言.他们可以被描述为一个需要希望远程主机执行命令的方案,或者一组IT程序运行的命令集合.

一个playbook就是一个YAML文件，所以playbook文件一般都以.yml结尾，一个playbook文件由一个或多个play组成，每个play定义了在一个或多个远程主机上执行的一系列的task，其中每个task一般就是调用一个ansible的模块，如调用copy模块复制文件到远程主机或调用shell模块执行命令。

## 简单的配置
配置deploy.yml完成进入远程服务器的某个目录并执行git pull操作
```bash
- hosts: wxnacy # 它会默认使用/etc/ansible/hosts 中配置的服务器组名 也可以单独设置hosts地址
  tasks:
  - name: cd path and git pull # 命令名称
    shell: git pull # 执行命令
    args:
      chdir: ~/workdir # 进入目录
```
运行
```bash
$ ansible-playbook deploy.yml

PLAY [wxnacy] **********************************************************************************************************************************************************************************************

TASK [cd path and git pull] *************************************************************************************************************************************************************************************
ok: [wxnacy.server.org]


PLAY RECAP *************************************************************************************************************************************************************************************************
wxnacy.server.org             : ok=2    changed=1    unreachable=0    failed=0
```
执行完运行命令ansible会在webservers组中依次执行tasks，返回以上样式结果极为成功，结果通过红黄绿三种颜色标明了不同的执行结果，红色表示有task执行失败，黄色表示改变了远程主机状态。

- 上一节：[ansible入门笔记1 Get Started](/?p=/doc/shell/ansible/basic_get_started.md)
- 下一节：[ansible入门笔记3 Playbooks 简单扩展](/?p=/doc/shell/ansible/basic_playbooks_ext.md)


