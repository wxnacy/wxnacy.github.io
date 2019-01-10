---
title: 重新学 Java 系列：获取 jar 包中类名列表
tags:
  - java
date: 2019-01-08 14:55:53
---

> 这个是一个系列阅读，关于为什么重新学习，我在文章 [重新学 Java 系列：新系列、新开始](/2018/12/29/java-renew-why/)(https://wxnacy.com/2018/12/29/java-renew-why/) 中有提到，这个系列是在有 Java 基础的情况下，重新学习讨论一下以前可能忽略掉，或者没理解的知识细节，我想要永远在学习的路上。

<!-- more --><!-- toc -->
最近想要自己写一下 Vim 中 Java 代码的自动补全，涉及到 `import` 部分的自动导入，记录下关键步骤。

想要做自动导入，首先需要知道依赖包中类名的列表，也就是需要反解出 jar 中 class 列表。

这里需要 `java.util.jar` 包中的几个类，直接上代码

```java
import java.util.ArrayList;
import java.util.Enumeration;
import java.util.List;
import java.util.jar.JarEntry;
import java.util.jar.JarFile;

/**
 * Created by wxnacy
 */
public class ClassList {

    public static void main(String args[]) {

        List<String> list = new ArrayList<String>();
        try {
            JarFile jarFile = new JarFile("/Users/wxnacy/.m2/repository/com/alibaba/fastjson/1.1.34/fastjson-1.1.34.jar");
            Enumeration enu = jarFile.entries();
            while (enu.hasMoreElements()) {
                JarEntry jarEntry = (JarEntry) enu.nextElement();
                String name = jarEntry.getName();
                // 过滤出 class 文件
                if (name.endsWith(".class") && name.indexOf("$") == -1 ) {
                    // 重新格式化文件名
                    name = name.substring(0, name.indexOf(".class"));
                    name = name.replaceAll("/", ".");
                    System.out.println(name);
                    list.add(name);
                }

            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        System.out.println("list length " + list.size());

    }


}
```



