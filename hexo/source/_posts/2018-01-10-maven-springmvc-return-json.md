---
title: 使用 Maven 构建 SpringMVC ：返回 JSON 格式数据
tags:
  - java
  - maven
  - spring
date: 2018-01-10 13:44:19
---


前两天使用 Maven 构建了 SpringMVC 最简单的功能，访问地址跳转到页面并显示 Hello World ，今天来介绍如何返回 JSON 格式数据。

<!-- more --><!-- toc -->
如果你还没有看过 [使用 Maven 构建 SpringMVC ：Hello World](/2018/01/08/maven-spring-hello-world/) 这篇文章，最好先看一下，因为今天不再赘述项目结构的内容。
## Controller
首先是 Controller，新建类 `JsonController.java`
```java
package com.wxnacy.spring.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import java.util.HashMap;
import java.util.Map;

@Controller
public class JsonController {

	@RequestMapping(value="/api")
    @ResponseBody
	public Map api() {
		Map map=new HashMap();
		map.put("status", "200");
		return map;
	}
}
```
这里用到注解 `@ResponseBody` ，它可以将对象作为 HTTP 响应正文返回，并调用适合 HttpMessageConverter 的 Adapter 转换对象，写入输出流。我们就以 Map 对象作为输出对象。

## 配置
servlet.xml
```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:context="http://www.springframework.org/schema/context"
    xmlns:mvc="http://www.springframework.org/schema/mvc"
    xsi:schemaLocation="http://www.springframework.org/schema/beans
    http://www.springframework.org/schema/beans/spring-beans-3.0.xsd
    http://www.springframework.org/schema/context
    http://www.springframework.org/schema/context/spring-context-3.2.xsd
    http://www.springframework.org/schema/mvc
    http://www.springframework.org/schema/mvc/spring-mvc-3.2.xsd ">

    <mvc:annotation-driven/>
    <context:component-scan base-package="com.wxnacy.spring.controller"/>
</beans>
```
HttpMessageConverter 接口需要在配置中开启 `<mvc:annotation-driven/>`，并且需要在文件的 beans 定义中需要声明 mvc 的 `xmlns:mvc` 和 `xsi:schemaLocation` 不然就会报错。

## Jackson 解析
Spring 默认是由 [Jackson](https://github.com/FasterXML/jackson-databind) 来解析 JSON 的，所以需要在 pom.xml 中引入对应包。
```xml
<properties>
    ...
    <!-- Use the latest version whenever possible. -->
    <jackson.version>2.9.0</jackson.version>
    ...
</properties>
<dependencies>
    ...
    <dependency>
        <groupId>com.fasterxml.jackson.core</groupId>
        <artifactId>jackson-databind</artifactId>
        <version>${jackson.version}</version>
    </dependency>
    ...
</dependencies>
```
然后启动项目，访问 `/api` 会得到 JSON 响应
![1](/images/springjson.png)

## Fastjson 解析
[Fastjson](https://github.com/alibaba/fastjson) 是号称解析速度最快的 JSON 转换工具，由 alibaba 团队开发完成的，给国人长脸啊。
使用也很简单，先引入包
Maven
```xml
<dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>fastjson</artifactId>
    <version>1.2.44</version>
</dependency>
```
servlet.xml 增加一些配置
```xml
<mvc:annotation-driven>
    <mvc:message-converters register-defaults="true">
        <bean class="com.alibaba.fastjson.support.spring.FastJsonHttpMessageConverter">
            <property name="supportedMediaTypes" value="application/json;charset=UTF-8"/>
            <property name="features">
                <array>
                    <!-- [>QuoteFieldNames———-输出key时是否使用双引号,默认为true<] -->
                    <!-- [>WriteMapNullValue——–是否输出值为null的字段,默认为false<] -->
                    <!-- [>WriteNullNumberAsZero—-数值字段如果为null,输出为0,而非null<] -->
                    <!-- [>WriteNullListAsEmpty—–List字段如果为null,输出为[],而非null<] -->
                    <!-- [>WriteNullStringAsEmpty—字符类型字段如果为null,输出为”“,而非null<] -->
                    <!-- [>WriteNullBooleanAsFalse–Boolean字段如果为null,输出为false,而非null<] -->
                    <!-- [>DisableCircularReferenceDetect 关闭循环引用<] -->
                    <value>WriteNullNumberAsZero</value>
                    <value>WriteNullListAsEmpty</value>
                    <value>WriteNullStringAsEmpty</value>
                    <value>WriteNullBooleanAsFalse</value>
                    <value>DisableCircularReferenceDetect</value>
                </array>
            </property>
        </bean>
    </mvc:message-converters>
</mvc:annotation-driven>
```
就这么简单，再次启动项目，即可看到效果。

demo 地址：https://github.com/wxnacy/study/tree/master/java/SpringMVC-ReturnJson
