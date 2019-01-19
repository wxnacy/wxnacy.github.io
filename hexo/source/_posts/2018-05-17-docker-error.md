---
title: AWS AMI 下载 Docker 报错
date: 2018-05-17 09:39:52
tags: [docker]
---

使用 AWS AMI 服务器安装 Docker 死活装不上。

<!-- more --><!-- toc -->

```bash
[ec2-user@ip-172-31-6-217 ~]$ sudo yum install -y docker-ce
Loaded plugins: priorities, update-motd, upgrade-helper
Resolving Dependencies
--> Running transaction check
---> Package docker-ce.x86_64 0:18.05.0.ce-3.el7.centos will be installed
--> Processing Dependency: container-selinux >= 2.9 for package: docker-ce-18.05.0.ce-3.el7.centos.x86_64
--> Processing Dependency: libseccomp >= 2.3 for package: docker-ce-18.05.0.ce-3.el7.centos.x86_64
--> Processing Dependency: libsystemd.so.0(LIBSYSTEMD_209)(64bit) for package: docker-ce-18.05.0.ce-3.el7.centos.x86_64
--> Processing Dependency: pigz for package: docker-ce-18.05.0.ce-3.el7.centos.x86_64
--> Processing Dependency: systemd-units for package: docker-ce-18.05.0.ce-3.el7.centos.x86_64
--> Processing Dependency: libseccomp.so.2()(64bit) for package: docker-ce-18.05.0.ce-3.el7.centos.x86_64
--> Processing Dependency: libsystemd.so.0()(64bit) for package: docker-ce-18.05.0.ce-3.el7.centos.x86_64
--> Processing Dependency: libltdl.so.7()(64bit) for package: docker-ce-18.05.0.ce-3.el7.centos.x86_64
--> Running transaction check
---> Package docker-ce.x86_64 0:18.05.0.ce-3.el7.centos will be installed
--> Processing Dependency: container-selinux >= 2.9 for package: docker-ce-18.05.0.ce-3.el7.centos.x86_64
--> Processing Dependency: libsystemd.so.0(LIBSYSTEMD_209)(64bit) for package: docker-ce-18.05.0.ce-3.el7.centos.x86_64
--> Processing Dependency: systemd-units for package: docker-ce-18.05.0.ce-3.el7.centos.x86_64
--> Processing Dependency: libsystemd.so.0()(64bit) for package: docker-ce-18.05.0.ce-3.el7.centos.x86_64
---> Package libseccomp.x86_64 0:2.3.1-2.4.amzn1 will be installed
---> Package libtool-ltdl.x86_64 0:2.4.2-20.4.8.5.32.amzn1 will be installed
---> Package pigz.x86_64 0:2.3.3-1.6.amzn1 will be installed
--> Finished Dependency Resolution
Error: Package: docker-ce-18.05.0.ce-3.el7.centos.x86_64 (docker-ce-edge)
           Requires: container-selinux >= 2.9
Error: Package: docker-ce-18.05.0.ce-3.el7.centos.x86_64 (docker-ce-edge)
           Requires: systemd-units
Error: Package: docker-ce-18.05.0.ce-3.el7.centos.x86_64 (docker-ce-edge)
           Requires: libsystemd.so.0()(64bit)
Error: Package: docker-ce-18.05.0.ce-3.el7.centos.x86_64 (docker-ce-edge)
           Requires: libsystemd.so.0(LIBSYSTEMD_209)(64bit)
 You could try using --skip-broken to work around the problem
 You could try running: rpm -Va --nofiles --nodigest
```

后来看到大神的指点 [issue](https://github.com/moby/moby/issues/33930#issuecomment-312782998) 使用

```bash
$ sudo yum install -y --setopt=obsoletes=0 \
    docker-ce-17.03.1.ce-1.el7.centos \
    docker-ce-selinux-17.03.1.ce-1.el7.centos
```

仍然不行，最后发现当前使用为

```bash
Amazon Linux AMI 2018.03.0 (HVM), SSD Volume Type - ami-e251209a
```

Docker 对内核要求比较高，换成比较新的

```bash
Amazon Linux 2 LTS Candidate 2 AMI (HVM), SSD Volume Type - ami-31394949
```

装新版 Docker 依然不行，但是执行上边的命令可以安装老版本

