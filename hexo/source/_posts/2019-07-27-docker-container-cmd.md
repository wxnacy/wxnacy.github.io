---
title: Docker 容器的一些操作
tags:
  - docker
date: 2019-07-27 21:22:38
---


整理自[操作 Docker 容器](https://yeasy.gitbooks.io/docker_practice/container/)，为了方便查看简化整理为一篇。

<!-- more -->
<!-- toc -->

## 启动容器

**新建并启动**

启动容器并执行命令后，如果命令进程退出，该容器也会立马终止

```bash
$ docker run ubuntu:bionic echo 'hello world'
hello world
```

在全部容器列表中可以查看

```bash
$ docker container ls -a
CONTAINER ID        IMAGE               COMMAND                CREATED             STATUS                     PORTS               NAMES
7c4a4cea19aa        ubuntu:bionic       "echo 'hello world'"   3 minutes ago       Exited (0) 7 seconds ago                       elegant_brahmagupta
```

使用 `-it` 参数可以进入交互模式

```bash
$ docker run -it ubuntu:bionic /bin/bash
root@82a4d9031d1c:/# ls
bin   dev  home  lib64  mnt  proc  run   srv  tmp  var
boot  etc  lib   media  opt  root  sbin  sys  usr
root@82a4d9031d1c:/# exit
exit
```

其中，-t 选项让Docker分配一个伪终端（pseudo-tty）并绑定到容器的标准输入上， -i 则让容器的标准输入保持打开。

当利用 docker run 来创建容器时，Docker 在后台运行的标准操作包括：

- 检查本地是否存在指定的镜像，不存在就从公有仓库下载
- 利用镜像创建并启动一个容器
- 分配一个文件系统，并在只读的镜像层外面挂载一层可读写层
- 从宿主主机配置的网桥接口中桥接一个虚拟接口到容器中去
- 从地址池配置一个 ip 地址给容器
- 执行用户指定的应用程序
- 执行完毕后容器被终止

**启动已终止容器**

```bash
$ docker container start <id|name>
```

以刚才的交互模式容器为例

```bash
$ docker container ls -a                    # 1
CONTAINER ID        IMAGE               COMMAND                CREATED              STATUS                          PORTS               NAMES
7c4a4cea19aa        ubuntu:bionic       "echo 'hello world'"   About a minute ago   Exited (0) About a minute ago                       elegant_brahmagupta
82a4d9031d1c        ubuntu:bionic       "/bin/bash"            2 minutes ago        Exited (0) About a minute ago                       tender_jennings

$ docker container start 82a4d9031d1c       # 2
82a4d9031d1c

$ docker container ls                       # 3
CONTAINER ID        IMAGE               COMMAND                CREATED             STATUS                          PORTS               NAMES
82a4d9031d1c        ubuntu:bionic       "/bin/bash"            3 minutes ago       Up 7 seconds                                        tender_jennings

$ docker exec -it 82a4d9031d1c /bin/bash    # 4
root@82a4d9031d1c:/# ps                     # 5
  PID TTY          TIME CMD
   25 pts/1    00:00:00 bash
   34 pts/1    00:00:00 ps
```

* `1` 查看所有转态的容器
* `2` 启动执行 `/bin/bash` 命令的容器
* `3` 查看当前运行的容器
* `4` 启动容器的交互模式
* `5` 查看容器中的进程

通过最后一步可以得知，容器的核心为所执行的应用程序，所需要的资源都是应用程序运行所必需的。除此之外，并没有其它的资源。这种特点使得 Docker 对资源的利用率极高，是货真价实的轻量级虚拟化。

**后台守护运行**

使用 `-d` 参数即可将容器在后台运行

```bash
$ docker run -d ubuntu:18.04 /bin/sh -c "while true; do echo hello world; sleep 1; done"
```

使用

```bash
$ docker logs -f <id|name>
```

或

```bash
$ docker container logs -f <id|name>
```

即可实时查看最新日志

## 进入容器

前面我们试过使用 `run` 命令配合 `-it` 参数来进入交互模式，进入容器的交互模式也是类似，不过这里需要 `exec` 命令。

```bash
$ docker exec -it ubuntu:bionic /bin/bash
root@82a4d9031d1c:/# exit
exit
```

使用完毕，使用 `exit` 退出即可，容器的运行状态不会影响。

还有一个命令也可以进入容器

```bash
$ docker attach <id|name>
```

但是该模式下使用 `exit` 退出时，容器也会跟着停止，所以并不实用，了解即可。

## 导出和导入

**导出**

```bash
$ docker container ls
CONTAINER ID        IMAGE               COMMAND                CREATED             STATUS                          PORTS               NAMES
82a4d9031d1c        ubuntu:bionic       "/bin/bash"            3 minutes ago       Up 7 seconds                                        tender_jennings
$ docker export 82a4d9031d1c > ubuntu.tar
```

将容器快照导出到本地

**导入容器镜像**

使用本地文件导入

```bash
$ cat ubuntu.tar | docker import demo/ubuntu:v1.0
```

使用网络地址导入

```bash
$ docker import http://example.com/exampleimage.tgz demo/ubuntu:v1.0
```

注：用户既可以使用 docker load 来导入镜像存储文件到本地镜像库，也可以使用 `docker import` 来导入一个容器快照到本地镜像库。这两者的区别在于容器快照文件将丢弃所有的历史记录和元数据信息（即仅保存容器当时的快照状态），而镜像存储文件将保存完整记录，体积也要大。此外，从容器快照文件导入时可以重新指定标签等元数据信息。


## 停止容器

```bash
$ docker container stop <id|name>       # 停止容器
$ docker container start <id|name>      # 启动容器
$ docker container restart <id|name>    # 重启容器
```

## 删除

```bash
# 关闭已经停止的容器
$ docker container rm <id:name>
```

```bash
# 如果要删除一个运行中的容器，可以添加 -f 参数。Docker 会发送 SIGKILL 信号给容器。
$ docker container rm -f <id:name>
```

```bash
# 关闭全部终止状态的容器
$ docker container prune
```

## 重启服务

```bash
$ sudo systemctl daemon-reload
$ sudo systemctl restart docker
```
