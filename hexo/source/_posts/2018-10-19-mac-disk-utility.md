---
title: Mac 上“磁盘工具”中可用的文件系统格式
date: 2018-10-19 21:09:57
tags: [mac]
---


Mac 上的“磁盘工具”支持多种文件系统格式：

- Apple 文件系统 (APFS)：macOS 10.13 或后续版本使用的文件系统。
- Mac OS 扩展：macOS 10.12 或之前版本使用的文件系统。
- MS-DOS (FAT) 和 ExFAT： 与 Windows 兼容的文件系统。

<!-- more -->

## Apple 文件系统 (APFS)

Apple 文件系统 (APFS) 是运行 macOS 10.13 或后续版本的 Mac 电脑所使用的默认文件系统，它具有强加密、空间共享、磁盘快照、快速目录大小统计等特性，以及改进的文件系统基础。虽然 APFS 最适合于新款 Mac 电脑中所用的闪存/SSD 储存，它也可以与使用传统硬盘驱动器 (HDD) 和外置直连储存设备的低版本系统配合使用。macOS 10.13 或后续版本支持 APFS 用于可引导启动的宗卷和数据宗卷。

APFS 按照需求分配容器中的磁盘空间。磁盘的可用空间会共享，并且可按需分配到容器中任意单独的宗卷。如果需要，您可以指定每个宗卷的保留大小和配额大小。每个宗卷仅使用整体容器的一部分，这样一来，可用空间即容器的总大小减去该容器中所有宗卷的大小。

为运行 macOS 10.13 或后续版本的 Mac 电脑选取以下其中一种 APFS 文件系统格式。

- APFS：使用 APFS 格式。
- APFS（加密）：使用 APFS 格式且加密宗卷。
- APFS（区分大小写）：使用 APFS 格式并区分文件和文件夹名称的大小写。例如，名称为“Homework”和“HOMEWORK”的文件夹是两个不同的文件夹。
- APFS（区分大小写，加密）：使用 APFS 格式，区分文件和文件夹名称的大小写且加密宗卷。例如，名称为“Homework”和“HOMEWORK”的文件夹是两个不同的文件夹。

您可以轻松[将宗卷添加到 APFS 容器](https://support.apple.com/zh-cn/guide/disk-utility/dskutl14027/18.0/mac/10.14)。APFS 容器中的每个宗卷都可以拥有其 APFS 格式：APFS、APFS（加密）、APFS（区分大小写）或 APFS（区分大小写，加密）。

## Mac OS 扩展

为兼容运行 macOS 10.12 或之前版本的 Mac 电脑选取以下其中一种 Mac OS 扩展文件系统格式。

- Mac OS 扩展（日志式）：使用 Mac 格式（日志式 HFS Plus）来保护分层文件系统的完整性。
- Mac OS 扩展（日志式，加密）：使用 Mac 格式，要求密码，并加密分区。
- Mac OS 扩展（区分大小写，日志式）：使用 Mac 格式并区分文件夹名称的大小写。例如，名称为“Homework”和“HOMEWORK”的文件夹是两个不同的文件夹。
- Mac OS 扩展（区分大小写，日志式，加密）：使用 Mac 格式，区分文件夹名称的大小写，要求密码，并加密分区。

## Windows 兼容格式

如果格式化磁盘以配合 Windows 使用，请选取以下其中一种兼容 Windows 的文件系统格式。

- MS-DOS (FAT)：用于 Windows 宗卷且大小为 32 GB 或不足 32 GB。

- ExFAT：用于 Windows 宗卷且大小超过 32 GB。

[Mac 上“磁盘工具”中可用的文件系统格式](https://support.apple.com/zh-cn/guide/disk-utility/dsku19ed921c/mac)

