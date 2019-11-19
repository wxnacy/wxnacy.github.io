---
title: Linux Crontab 定时任务
tags:
  - linux
date: 2018-01-15 10:07:33
---

Linux 中使用 crontab 来定时执行命令或指定脚本。

<!-- more -->
<!-- toc -->

## Hello World

先什么都不要说，跟我一起 Hello World
首先修改 `~/.bash_profile`

```bash
export EDITOR=vim
```

然后执行 `source ~/.bash_profile` 使配置生效
随后新建一个定时任务

```bash
$ crontab -e
```

将下面的文字复制进去

```bash
* * * * * /bin/echo Hello World `date`\n >> ~/output
```

<!-- 然后执行 `:wq` 退出，会得到如下提示 -->

```bash
crontab: installing new crontab
```

这代表你已经创建一个定时任务，它的作用是，每分钟在 `~/output` 文件中添加一行带有时间标记的字符串 `Hello World`，如下

```bash
Hello World Sun Jan 14 20:14:01 CST 2018n
Hello World Sun Jan 14 20:15:01 CST 2018n
Hello World Sun Jan 14 20:16:01 CST 2018n
Hello World Sun Jan 14 20:17:01 CST 2018n
Hello World Sun Jan 14 20:18:01 CST 2018n
```

你使用 `tail -f ~/output` 命令就可以每隔一分钟看到一行输出。

## 使用说明
不管你有没有成功的实现刚才的效果，现在来跟我一起看看刚才就做了些什么吧
- **crontab -e** crontab 执行定时任务，需要配置任务列表，这条命令就是在编辑任务
- **export DEITOR=vim** 是为了指定编辑任务时，使用的编辑器，现在绝大多数 Linux 都是用 Vim
编辑生成的任务文件在目录 `/var/spoot/cron` 中（这是 CentOS 系统，如果是 Ubuntu 则是在 `/var/spoot/cron/crontabs` 目录中）有一个用户名命名的文件，比如 `root` ，剩下的操作刚才已经有所介绍，还有一些常用命令
### 查看任务列表
```bash
$ crontab -l
```
```bash
* * * * * /bin/echo Hello World `date`\n >> ~/output
```
### 删除任务
```bash
$ crontab -r
```
这样刚才生成的文件就会被删除掉
### 第二种方法
如果你不像文件生成在这个目录中，也可以做如下操作
```bash
$ vim ~/roottab         # 手动生成一个配置文件

* * * * * /bin/echo Hello World `date`\n >> ~/output

$ crontab ~/roottab     # 启动定时任务，并制定该文件
```
### 配置文件格式
下面来详细说说 crontab 文件格式
```bash
* * * * * /bin/echo Hello World `date`\n >> ~/output
|-|-|-|-|-|- 分钟 0 ~ 59
  |-|-|-|-|- 小时 0 ~ 23
    |-|-|-|- 日   1 ~ 31
      |-|-|- 月   1 ~ 12
        |-|- 周   0 ~ 7
          |- 需要执行的命令
```
### 更多使用实例
```bash
# 每分钟执行一次
* * * * * /bin/echo Hello World `date`\n >> ~/output
# 每小时执行一次
* */1 * * * /bin/echo Hello World `date`\n >> ~/output
# 每小时的第3和第15分钟执行
3,15 * * * * /bin/echo Hello World `date`\n >> ~/output
# 每隔两天的上午8点到11点的第3和第15分钟执行
3,15 8-11 */2 * * /bin/echo Hello World `date`\n >> ~/output
# 每周一上午8点到11点的第3和第15分钟执行
3,15 8-11 * * 1 /bin/echo Hello World `date`\n >> ~/output
```

## 按秒数间隔来执行

有点需要单说一下，crontab 最小单位是按照分钟来执行的，默认是不支持按照秒数来执行的，不过我们可以想一些变通的方法，利用**延时**。

```bash
* * * * * sleep 15; /bin/echo Hello World `date`\n >> ~/output
```

上面的语句代表了每分钟执行任务的时候，先睡眠 15 秒在执行。

```bash
* * * * * /bin/echo Hello World `date`\n >> ~/output
* * * * * sleep 15; /bin/echo Hello World `date`\n >> ~/output
```

这样写的话就代表了，每分钟执行一次，每分钟推后 15 秒在执行一次，在多写几个，我们就可以得到一个每隔 15 秒执行一次的定时任务了，比如

```bash
* * * * * /bin/echo Hello World `date`\n >> ~/output
* * * * * sleep 15; /bin/echo Hello World `date`\n >> ~/output
* * * * * sleep 30; /bin/echo Hello World `date`\n >> ~/output
* * * * * sleep 45; /bin/echo Hello World `date`\n >> ~/output
```

唯一的缺点就是第一次执行这个定时任务的时候，前 1 分钟是轮空的。

## 服务状态
Ubuntu
```bash
# 启动、重启，停止、重载、运行状态
$ service cron start|restart|stop|reload|status
```
CentOS < 7
```bash
# 启动、重启，停止、重载、运行状态
$ service crond start|restart|stop|reload|status

$ chkconfig sshd on     # 开机自启sshd
$ chkconfig sshd off    # 开机关闭自启sshd
$ chkconfig --list sshd # 查看每个运行级别类型中服务的当前状态
```
CentOS >= 7
```bash
$ systemctl enable crond.service     # 开机自启crond
$ systemctl disable crond.service    # 开机关闭自启crond
$ systemctl start crond.service      # 启动crond
$ systemctl restart crond.service    # 重启
$ systemctl stop crond.service       # 停止
$ systemctl reload crond.service     # 重新加载
$ systemctl status crond.service     # 查看启动状态
```
## 参考
- [crontab 定时任务](http://linuxtools-rst.readthedocs.io/zh_CN/latest/tool/crontab.html#)
