---
title: Linux 安装 Elasticsearch
tags:
  - elastic
date: 2018-07-04 09:40:23
---


在安装 Elasticsearch 时，推荐使用软件管理器方式安装

<!-- more --><!-- toc -->

## 安装 Java

我们只需要安装 `jre` 即可

```bash
# centos
$ sudo yum install java-1.8.0-openjdk.x86_64

# ubuntu
$ sudo apt install -y openjdk-8-jre

$ java -version

openjdk version "1.8.0_171"
OpenJDK Runtime Environment (build 1.8.0_171-b10)
OpenJDK 64-Bit Server VM (build 25.171-b10, mixed mode)
```

## 安装 Elasticsearch

### CentOS 7

两种方式

- **添加 YUM 仓库**

```bash
$ sudo rpm --import https://artifacts.elastic.co/GPG-KEY-elasticsearch

$ REPO=/etc/yum.repos.d/elastic.repo
$ echo "[elasticsearch-6.x]" | sudo tee -a ${REPO}
$ echo "name=Elasticsearch repository for 6.x packages" | sudo tee -a ${REPO}
$ echo "baseurl=https://artifacts.elastic.co/packages/6.x/yum" | sudo tee -a ${REPO}
$ echo "gpgcheck=1" | sudo tee -a ${REPO}
$ echo "gpgkey=https://artifacts.elastic.co/GPG-KEY-elasticsearch" | sudo tee -a ${REPO}
$ echo "enabled=1" | sudo tee -a ${REPO}
$ echo "autorefresh=1" | sudo tee -a ${REPO}
$ echo "type=rpm-md" | sudo tee -a ${REPO}

$ sudo yum install -y elasticsearch
```

- **rpm 安装**

```bash
$ wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.2.4.rpm
$ sudo rpm --install elasticsearch-6.2.4.rpm
```

### Ubuntu

也是两种方式

- **添加 APT 仓库**

```bash
$ wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -

$ echo "deb https://artifacts.elastic.co/packages/6.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-6.x.list

$ sudo apt-get update && sudo apt-get install elasticsearch
```

- **dpkg 安装**

```bash
$ wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.3.0.deb
$ sudo dpkg -i elasticsearch-6.3.0.deb
```

**安装完成设置启动配置**

设置开机自启

```bash
$ sudo systemctl daemon-reload
$ sudo systemctl enable elasticsearch.service
```

启动

```bash
$ sudo systemctl start elasticsearch.service
```

访问

```bash
$ curl localhost:9200

{
  "name" : "elasticsearch",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "pLrLT2D9QA6VM9-6cdi1vQ",
  "version" : {
    "number" : "6.2.4",
    "build_hash" : "ccec39f",
    "build_date" : "2018-04-12T20:37:28.497551Z",
    "build_snapshot" : false,
    "lucene_version" : "7.2.1",
    "minimum_wire_compatibility_version" : "5.6.0",
    "minimum_index_compatibility_version" : "5.0.0"
  },
  "tagline" : "You Know, for Search"
}
```


此时 Elasticsearch 在服务器外通过 ip 是无法访问的，需要修改 `network.host`

```bash
$ sudo vim /etc/elasticsearch/elasticsearch.yml
```

```bash
network.host: 0.0.0.0
```

然后重启

```bash
$ sudo systemctl start elasticsearch.service
```

此时通过 ip 访问即可

另外 `cluster.name, node.name` 等 Elasticsearch 启动配置都可以在这个文件修改

## 配置

通过 `rpm` 方式安装的软件目录如下

类型    | 描述                                                                                                   | 默认地址                         | 配置
----    | ----                                                                                                   | --------                         | ---
home    | Elasticsearch home directory or $ES_HOME                                                               | /usr/share/elasticsearch         |
bin     | 二进制运行脚本包含 `elasticsearch` 开启一个实例，`elasticsearch-plugin` 安装插件                       | /usr/share/elasticsearch/bin     |
conf    | 配置文件包含 elasticsearch.yml                                                                         | /etc/elasticsearch               | `ES_PATH_CONF`
conf    | 环境变量包括堆大小，文件描述符                                                                         | /etc/sysconfig/elasticsearch     |
data    | 在节点上分配的每个索引/分片的数据文件的位置。 可以容纳多个地点。                                       | /var/lib/elasticsearch           | `path.data`
logs    | 日志文件                                                                                               | /var/log/elasticsearch           | `path.logs`
plugins | 插件文件的位置。每个插件都将包含在一个子目录中。                                                       | /usr/share/elasticsearch/plugins |
repo    | 共享文件系统存储库位置。 可以容纳多个地点。 文件系统存储库可以放置在此处指定的任何目录的任何子目录中。 |                                  |


环境配置 `/etc/sysconfig/elasticsearch` 会包含如下信息

- `JAVA_HOME` Set a custom Java path to be used.

- `MAX_OPEN_FILES` 最大打开文件数，默认 65536.

- `MAX_LOCKED_MEMORY` 最大锁定的内存大小。 如果使用 elasticsearch.yml 中的 `bootstrap.memory_lock` 选项，则设置为无限制。

- `MAX_MAP_COUNT` 进程可能具有的最大内存映射区数量。如果您使用 mmapfs 作为索引存储类型，请确保将其设置为较高值。有关更多信息，请查看关于 `max_map_count` 的 linux 内核文档。 这是在启动 Elasticsearch 之前通过 sysctl 设置的。 默认为262144。

- `ES_PATH_CONF` 配置文件目录（需要包含 elasticsearch.yml，jvm.options 和 log4j2.properties 文件）; 默认为 `/etc/elasticsearch`。

- `ES_JAVA_OPTS` 你可能想要应用的任何其他JVM系统属性。

- `RESTART_ON_UPGRADE` 在软件包升级时配置重启，默认为false。 这意味着您必须在手动安装包后重新启动Elasticsearch实例。 其原因是为了确保集群中的升级不会导致连续的碎片重新分配，从而导致高网络流量并缩短集群的响应时间。


- [Install Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/6.x/install-elasticsearch.html)
- [How To Install and Configure Elasticsearch on CentOS 7](https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-elasticsearch-on-centos-7)
