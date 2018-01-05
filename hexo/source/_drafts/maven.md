---
title: Maven 教程
tags: [java]
---

## 下载
Ubuntu
```bash
$ apt install maven
```
MacOS
```bash
$ brew install maven
```

```bash
mvn -v
mvn compile
mvn package
mvn install
mvn clean

mvn archetype:generate
-DgroupId=test.maven
-DartifactId=quick
-DarchetypeArtifactId=maven-archetype-quickstart
-DinteractiveMode=false

mvn archetype:generate -DgroupId=com.wxnacy.jar -DartifactId=ProjectJar -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
mvn archetype:generate -DgroupId=com.wxnacy.web -DartifactId=ProjectWar -DarchetypeArtifactId=maven-archetype-webapp -DinteractiveMode=false

```
