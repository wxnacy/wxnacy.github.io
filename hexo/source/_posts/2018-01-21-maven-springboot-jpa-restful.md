---
title: 使用 Maven 构建 SpringBoot：JPA 和 RESTful
tags:
  - maven
  - springboot
date: 2018-01-21 16:50:24
---


昨天介绍了如何使用 StringBoot，今天讲讲怎么使用 [JPA](https://en.wikipedia.org/wiki/Java_Persistence_API) 操作数据库，并完成简单的 RESTful 风格接口。

<!-- more --><!-- toc -->
本章代码的 DEMO 地址：https://github.com/wxnacy/study/tree/master/java/SpringBoot-JPA

JPA 说白了就是我们常说的 ORM ，为了避免写繁琐的 SQL 语句，这些框架进行了不断的封装，就是为了让我们更加方便的开发，把精力更多的集中在业务逻辑上。

看本文前如果你还不了解 StringBoot，建议你先看下这篇文章[使用 Maven 构建 StringBoot：Hello World](/2018/01/20/maven-spring-boot-hello-world/)，因为我将不再讲项目结构。

## 创建数据库
新建一个 `study` 库，并新建 `user` 表
```mysql
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `name` varchar(32) NOT NULL DEFAULT '' COMMENT '用户名',
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=163 DEFAULT CHARSET=utf8mb4 COMMENT='用户表';
```

## 配置 pom.xml
```bash
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-jpa</artifactId>
</dependency>
<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
</dependency>
```
添加 JPA 和 Mysql 的依赖包

## 配置数据源
创建配置文件 `src/main/resources/application.properties`
```bash
spring.datasource.url=jdbc:mysql://localhost:3306/study
spring.datasource.username=root
spring.datasource.password=wxnacy
spring.datasource.driver-class-name=com.mysql.jdbc.Driver
```
创建 application.properties 文件，项目启动时会自动读取该文件中的数据，不需要配置路径，框架已经封装好了。

## 创建数据映射类
创建 `src/main/java/com/wxnacy/spring/User.java`
```java
package com.wxnacy.spring;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

@Entity
public class User{
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Integer id;
    private String name;


    public void setName(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public User() {
    }

    public User(Integer id, String name) {
        this.id = id;
        this.name = name;
    }
    public User(String name) {
        this.name = name;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public Integer getId() {
        return id;
    }
}
```
使用 `@Entity` 注解让 Spring 明白，这是个映射类，并直接映射到 user 表。`@Id` 告诉框架哪个是主键 id。`@GeneratedValue(strategy = GenerationType.AUTO)` 声明主键 id 的生成规则，`GenerationType.AUTO` 是把生成规则交给数据库引擎来操作，在本 Demo 中就是自增规则，这个值是缺省值，也可以直接用 `@GeneratedValue()` 来进行注解。`GenerationType` 的其他值，见[文档](https://docs.oracle.com/javaee/6/api/javax/persistence/GenerationType.html)

## 创建数据访问接口
创建 `src/main/com/wxnacy/spring/UserReopsitory.java`
```java
package com.wxnacy.spring;

import java.util.List;
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserRepository extends JpaRepository<User, Integer> {
    List<User> findByName(String name);
    User findById(Integer id);
}
```
这个类是关键，通过集成 `JapRepository` 接口，集成封装好的方法 `save(), findAll(), delete()` 等方法，也可以自定义方法。

它有一个非常令人兴奋的功能，就是可以根据名称来智能生成方法，比如 `findByName`，如果你使用驼峰命名法，将名称跟在后面，就可以根据字段 `name` 来查询数据，这给我们无限的可用性。

更多用法，见[文档](https://docs.spring.io/spring-data/data-jpa/docs/current/api/)

## 创建控制器
`src/main/com/wxnacy/spring/UserController.java`
```java
package com.wxnacy.spring;

import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class UserController {

    @Autowired
    private UserRepository userRepository;

	@PostMapping("/user")
    public User create(
        @RequestBody Map<String, String> body
            ) {
        User user = new User(body.get("name"));
        User item = userRepository.save(user);
        return item;
	}

	@GetMapping("/user")
    public List<User> users(
        @RequestParam(required=false, defaultValue="wxnacy") String name
            ) {
        List<User> res = userRepository.findByName(name);
        return res;
	}

	@GetMapping("/user/{id}")
    public User user(
        @PathVariable Integer id
            ) {
        User user = userRepository.findById(id);
        return user;
	}

}
```
使用 RESTful 风格，分别创建三个接口，创建用户，根据名称查询用户列表，以及查询单个用户。

## 运行
```bash
$ mvn spring-boot:run
```
创建用户
```bash
$ curl -X POST localhost:8080/user -H "Content-Type:application/json" -d '{"name":"wxnacy"}'
```
```bash
{"id":1,"name":"wxnacy"}
```
成功后重复创建几次

查询单个用户
```bash
$ curl localhost:8080/user/1
```
```bash
{"id":167,"name":"wxnacy"}
```

根据用户名查询用户列表
```bash
$ curl localhost:8080/user
```
```bash
[{"id":1,"name":"wxnacy"},{"id":2,"name":"wxnacy"}]
```


## 参考
- [Accessing data with MySQL](https://spring.io/guides/gs/accessing-data-mysql/)
- [Spring Boot中使用Spring-data-jpa让数据访问更简单、更优雅](http://blog.didispace.com/springbootdata2/)
- [Annotation Type RequestParam](https://docs.spring.io/spring/docs/current/javadoc-api/org/springframework/web/bind/annotation/RequestParam.html)
