---
title: 使用 Maven 构建 StringBoot：Hello World
tags:
  - maven
  - springboot
date: 2018-01-20 20:18:36
---


其实在用了 Python、Ruby 等语言后，再也回不去 Java 的一个很大原因，就是它的配置太多了，在用最受欢迎的 Spring 来做一个简单的 Hello World 输出，也要成吨的配置，这让脱了裤子的我们顿时没了兴致，但是 StringBoot 解决了这个问题。

<!-- more --><!-- toc -->
Spring Boot 是一个轻量级框架，可以完成基于 Spring 的应用程序的大部分配置工作。其实说白了，它封装好了我们默认需要一些配置，我们只需要继承它就可以了。

本章将简单介绍如何使用 StringBoot 运行一个最简单的 Web 项目，来输出 Hello World ，Demo 地址：https://github.com/wxnacy/study/tree/master/java/SpringBoot-HelloWorld

## 工作环境
- JDK >= 8
- Maven 最新版本（我默认你已经学习了 Maven 的基础知识）
- Git
- 任意开发工具，比如 Vim

## 创建项目
```bash
mvn archetype:generate -DgroupId=com.wxnacy.spring -DartifactId=SpringBoot-HelloWorld -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
```
使用 `maven-archetype-quickstart` 模板快速创建一个简单的 jar 项目即可，

## 配置 pom.xml
```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.wxnacy.spring</groupId>
    <artifactId>SpringBoot-HelloWorld</artifactId>
    <packaging>jar</packaging>
    <version>1.0-SNAPSHOT</version>
    <name>SpringBoot-HelloWorld</name>
    <url>http://maven.apache.org</url>

    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>1.5.9.RELEASE</version>
    </parent>

    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
    </dependencies>
    <properties>
        <java.version>1.8</java.version>
    </properties>
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>
</project>
```
它做了这么几件事
- 继承 `spring-boot-starter-parent` 包完成配置
- 指定 `spring-boot-starter-web` 包明确该项目为 web 项目
- 使用 `spring-boot-maven-plugin` 来最终构建项目

## Controller
编辑 `src/main/java/com/wxnacy/spring/HelloController.java` 类
```java
package com.wxnacy.spring;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {

	@RequestMapping("/")
	public String index() {
		return "Hello World";
	}

}
```
`@RestController` 注解相当于集合了 `@Controller` 和 `@ResponseBody` 两个注解的功能，代表该类已经做好了使用 SpringMVC 框架来构建 web 请求的准备。

`@RequestMapping` 注解将地址 `/` 映射到 `index()` 方法上。

## 创建 Application
`src/main/java/com/wxnacy/spring/HelloController.java`
```java
package com.wxnacy.spring;

import java.util.Arrays;

import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
public class Application {

    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }

    @Bean
    public CommandLineRunner commandLineRunner(ApplicationContext ctx) {
        return args -> {

            System.out.println("Let's inspect the beans provided by Spring Boot:");

            String[] beanNames = ctx.getBeanDefinitionNames();
            Arrays.sort(beanNames);
            for (String beanName : beanNames) {
                System.out.println("beanName"+ beanName);
            }

        };
    }
}
```
`@SpringBootApplication` 将融合以下几种注解的功能
- `@Configuration` 标记类作为 Application 上下文 bean 的源
- `@EnableAutoConfiguration` 告诉Spring Boot开始添加基于classpath设置、其他bean和各种属性的设置。
- `@ComponentScan` 告诉 Spring 在当前包中查找其他组件、配置和服务，允许它找到控制器。

最后使用 `main()` 方法来启动一个 Application，全部配置就完成了。你可能注意到，这个项目没有一个 XML 配置，这就是 SpringBoot 要做的，完全用 Java 的注解来进行配置，它已经用足够好的默认值来配置一个 web 项目，比如以前必备的 `DispatcherServlet`

还有一个使用 `@Bean` 注解的 `commandLineRunner()` 方法，它并不是必备的，但是可以将项目启动所需要的 bean 都打印出来。

## 运行
```bash
$ mvn clean package && java -jar target/SpringBoot-HelloWorld-1.0-SNAPSHOT.jar
```
或
```bash
$ mvn spring-boot:run
```
```bash

  .   ____          _            __ _ _
 /\\ / ___'_ __ _ _(_)_ __  __ _ \ \ \ \
( ( )\___ | '_ | '_| | '_ \/ _` | \ \ \ \
 \\/  ___)| |_)| | | | | || (_| |  ) ) ) )
    '  |____| .__|_| |_|_| |_\__, | / / / /
 =========|_|==============|___/=/_/_/_/
 :: Spring Boot ::        (v1.5.9.RELEASE)

2018-01-20 20:12:10.121  INFO 87328 --- [           main] com.wxnacy.spring.Application            : Starting Application on bogon with PID 87328 (/Users/wxnacy/PycharmProjects/study/java/SpringBoot-HelloWorld/target/classes started by wxnacy in /Users/wxnacy/PycharmProjects/study/java/SpringBoot-HelloWorld)
2018-01-20 20:12:10.124  INFO 87328 --- [           main] com.wxnacy.spring.Application            : No active profile set, falling back to default profiles: default
2018-01-20 20:12:10.169  INFO 87328 --- [           main] ationConfigEmbeddedWebApplicationContext : Refreshing org.springframework.boot.context.embedded.AnnotationConfigEmbeddedWebApplicationContext@790736dd: startup date [Sat Jan 20 20:12:10 CST 2018]; root of context hierarchy
2018-01-20 20:12:11.072  INFO 87328 --- [           main] s.b.c.e.t.TomcatEmbeddedServletContainer : Tomcat initialized with port(s): 8080 (http)
2018-01-20 20:12:11.084  INFO 87328 --- [           main] o.apache.catalina.core.StandardService   : Starting service [Tomcat]
2018-01-20 20:12:11.086  INFO 87328 --- [           main] org.apache.catalina.core.StandardEngine  : Starting Servlet Engine: Apache Tomcat/8.5.23
2018-01-20 20:12:11.157  INFO 87328 --- [ost-startStop-1] o.a.c.c.C.[Tomcat].[localhost].[/]       : Initializing Spring embedded WebApplicationContext
2018-01-20 20:12:11.157  INFO 87328 --- [ost-startStop-1] o.s.web.context.ContextLoader            : Root WebApplicationContext: initialization completed in 991 ms
2018-01-20 20:12:11.258  INFO 87328 --- [ost-startStop-1] o.s.b.w.servlet.ServletRegistrationBean  : Mapping servlet: 'dispatcherServlet' to [/]
2018-01-20 20:12:11.261  INFO 87328 --- [ost-startStop-1] o.s.b.w.servlet.FilterRegistrationBean   : Mapping filter: 'characterEncodingFilter' to: [/*]
2018-01-20 20:12:11.261  INFO 87328 --- [ost-startStop-1] o.s.b.w.servlet.FilterRegistrationBean   : Mapping filter: 'hiddenHttpMethodFilter' to: [/*]
2018-01-20 20:12:11.261  INFO 87328 --- [ost-startStop-1] o.s.b.w.servlet.FilterRegistrationBean   : Mapping filter: 'httpPutFormContentFilter' to: [/*]
2018-01-20 20:12:11.261  INFO 87328 --- [ost-startStop-1] o.s.b.w.servlet.FilterRegistrationBean   : Mapping filter: 'requestContextFilter' to: [/*]
2018-01-20 20:12:11.470  INFO 87328 --- [           main] s.w.s.m.m.a.RequestMappingHandlerAdapter : Looking for @ControllerAdvice: org.springframework.boot.context.embedded.AnnotationConfigEmbeddedWebApplicationContext@790736dd: startup date [Sat Jan 20 20:12:10 CST 2018]; root of context hierarchy
2018-01-20 20:12:11.520  INFO 87328 --- [           main] s.w.s.m.m.a.RequestMappingHandlerMapping : Mapped "{[/]}" onto public java.lang.String com.wxnacy.spring.HelloController.index()
2018-01-20 20:12:11.523  INFO 87328 --- [           main] s.w.s.m.m.a.RequestMappingHandlerMapping : Mapped "{[/error]}" onto public org.springframework.http.ResponseEntity<java.util.Map<java.lang.String, java.lang.Object>> org.springframework.boot.autoconfigure.web.BasicErrorController.error(javax.servlet.http.HttpServletRequest)
2018-01-20 20:12:11.523  INFO 87328 --- [           main] s.w.s.m.m.a.RequestMappingHandlerMapping : Mapped "{[/error],produces=[text/html]}" onto public org.springframework.web.servlet.ModelAndView org.springframework.boot.autoconfigure.web.BasicErrorController.errorHtml(javax.servlet.http.HttpServletRequest,javax.servlet.http.HttpServletResponse)
2018-01-20 20:12:11.548  INFO 87328 --- [           main] o.s.w.s.handler.SimpleUrlHandlerMapping  : Mapped URL path [/webjars/**] onto handler of type [class org.springframework.web.servlet.resource.ResourceHttpRequestHandler]
2018-01-20 20:12:11.548  INFO 87328 --- [           main] o.s.w.s.handler.SimpleUrlHandlerMapping  : Mapped URL path [/**] onto handler of type [class org.springframework.web.servlet.resource.ResourceHttpRequestHandler]
2018-01-20 20:12:11.572  INFO 87328 --- [           main] o.s.w.s.handler.SimpleUrlHandlerMapping  : Mapped URL path [/**/favicon.ico] onto handler of type [class org.springframework.web.servlet.resource.ResourceHttpRequestHandler]
2018-01-20 20:12:11.676  INFO 87328 --- [           main] o.s.j.e.a.AnnotationMBeanExporter        : Registering beans for JMX exposure on startup
2018-01-20 20:12:11.718  INFO 87328 --- [           main] s.b.c.e.t.TomcatEmbeddedServletContainer : Tomcat started on port(s): 8080 (http)
Let's inspect the beans provided by Spring Boot:
application
basicErrorController
beanNameHandlerMapping
beanNameViewResolver
characterEncodingFilter
commandLineRunner
conventionErrorViewResolver
defaultServletHandlerMapping
defaultValidator
defaultViewResolver
dispatcherServlet
dispatcherServletRegistration
duplicateServerPropertiesDetector
embeddedServletContainerCustomizerBeanPostProcessor
error
errorAttributes
errorPageCustomizer
errorPageRegistrarBeanPostProcessor
faviconHandlerMapping
faviconRequestHandler
handlerExceptionResolver
helloController
hiddenHttpMethodFilter
httpPutFormContentFilter
httpRequestHandlerAdapter
jacksonObjectMapper
jacksonObjectMapperBuilder
jsonComponentModule
localeCharsetMappingsCustomizer
mappingJackson2HttpMessageConverter
mbeanExporter
mbeanServer
messageConverters
methodValidationPostProcessor
multipartConfigElement
multipartResolver
mvcContentNegotiationManager
mvcConversionService
mvcHandlerMappingIntrospector
mvcPathMatcher
mvcResourceUrlProvider
mvcUriComponentsContributor
mvcUrlPathHelper
mvcValidator
mvcViewResolver
objectNamingStrategy
org.springframework.boot.autoconfigure.AutoConfigurationPackages
org.springframework.boot.autoconfigure.condition.BeanTypeRegistry
org.springframework.boot.autoconfigure.context.ConfigurationPropertiesAutoConfiguration
org.springframework.boot.autoconfigure.context.PropertyPlaceholderAutoConfiguration
org.springframework.boot.autoconfigure.info.ProjectInfoAutoConfiguration
org.springframework.boot.autoconfigure.internalCachingMetadataReaderFactory
org.springframework.boot.autoconfigure.jackson.JacksonAutoConfiguration
org.springframework.boot.autoconfigure.jackson.JacksonAutoConfiguration$Jackson2ObjectMapperBuilderCustomizerConfiguration
org.springframework.boot.autoconfigure.jackson.JacksonAutoConfiguration$JacksonObjectMapperBuilderConfiguration
org.springframework.boot.autoconfigure.jackson.JacksonAutoConfiguration$JacksonObjectMapperConfiguration
org.springframework.boot.autoconfigure.jmx.JmxAutoConfiguration
org.springframework.boot.autoconfigure.validation.ValidationAutoConfiguration
org.springframework.boot.autoconfigure.web.DispatcherServletAutoConfiguration
org.springframework.boot.autoconfigure.web.DispatcherServletAutoConfiguration$DispatcherServletConfiguration
org.springframework.boot.autoconfigure.web.DispatcherServletAutoConfiguration$DispatcherServletRegistrationConfiguration
org.springframework.boot.autoconfigure.web.EmbeddedServletContainerAutoConfiguration
org.springframework.boot.autoconfigure.web.EmbeddedServletContainerAutoConfiguration$EmbeddedTomcat
org.springframework.boot.autoconfigure.web.ErrorMvcAutoConfiguration
org.springframework.boot.autoconfigure.web.ErrorMvcAutoConfiguration$DefaultErrorViewResolverConfiguration
org.springframework.boot.autoconfigure.web.ErrorMvcAutoConfiguration$WhitelabelErrorViewConfiguration
org.springframework.boot.autoconfigure.web.HttpEncodingAutoConfiguration
org.springframework.boot.autoconfigure.web.HttpMessageConvertersAutoConfiguration
org.springframework.boot.autoconfigure.web.HttpMessageConvertersAutoConfiguration$StringHttpMessageConverterConfiguration
org.springframework.boot.autoconfigure.web.JacksonHttpMessageConvertersConfiguration
org.springframework.boot.autoconfigure.web.JacksonHttpMessageConvertersConfiguration$MappingJackson2HttpMessageConverterConfiguration
org.springframework.boot.autoconfigure.web.MultipartAutoConfiguration
org.springframework.boot.autoconfigure.web.ServerPropertiesAutoConfiguration
org.springframework.boot.autoconfigure.web.WebClientAutoConfiguration
org.springframework.boot.autoconfigure.web.WebClientAutoConfiguration$RestTemplateConfiguration
org.springframework.boot.autoconfigure.web.WebMvcAutoConfiguration
org.springframework.boot.autoconfigure.web.WebMvcAutoConfiguration$EnableWebMvcConfiguration
org.springframework.boot.autoconfigure.web.WebMvcAutoConfiguration$WebMvcAutoConfigurationAdapter
org.springframework.boot.autoconfigure.web.WebMvcAutoConfiguration$WebMvcAutoConfigurationAdapter$FaviconConfiguration
org.springframework.boot.autoconfigure.websocket.WebSocketAutoConfiguration
org.springframework.boot.autoconfigure.websocket.WebSocketAutoConfiguration$TomcatWebSocketConfiguration
org.springframework.boot.context.properties.ConfigurationPropertiesBindingPostProcessor
org.springframework.boot.context.properties.ConfigurationPropertiesBindingPostProcessor.store
org.springframework.context.annotation.internalAutowiredAnnotationProcessor
org.springframework.context.annotation.internalCommonAnnotationProcessor
org.springframework.context.annotation.internalConfigurationAnnotationProcessor
org.springframework.context.annotation.internalRequiredAnnotationProcessor
org.springframework.context.event.internalEventListenerFactory
org.springframework.context.event.internalEventListenerProcessor
preserveErrorControllerTargetClassPostProcessor
propertySourcesPlaceholderConfigurer
requestContextFilter
requestMappingHandlerAdapter
requestMappingHandlerMapping
resourceHandlerMapping
restTemplateBuilder
serverProperties
simpleControllerHandlerAdapter
spring.http.encoding-org.springframework.boot.autoconfigure.web.HttpEncodingProperties
spring.http.multipart-org.springframework.boot.autoconfigure.web.MultipartProperties
spring.info-org.springframework.boot.autoconfigure.info.ProjectInfoProperties
spring.jackson-org.springframework.boot.autoconfigure.jackson.JacksonProperties
spring.mvc-org.springframework.boot.autoconfigure.web.WebMvcProperties
spring.resources-org.springframework.boot.autoconfigure.web.ResourceProperties
standardJacksonObjectMapperBuilderCustomizer
stringHttpMessageConverter
tomcatEmbeddedServletContainerFactory
viewControllerHandlerMapping
viewResolver
websocketContainerCustomizer
welcomePageHandlerMapping
2018-01-20 20:12:11.727  INFO 87328 --- [           main] com.wxnacy.spring.Application            : Started Application in 1.964 seconds (JVM running for 4.126)
```
当看到这样的信息就代表启动成功了，从`Let's inspect the beans provided by Spring Boot` 开始输出的信息，就是所有加载到的类

查看结果
```bash
$ curl http://localhost:8080
```
```bash
Hello World
```
## 参考
- [Building an Application with Spring Boot](https://spring.io/guides/gs/spring-boot/)
- [Spring Boot 基础](https://www.ibm.com/developerworks/cn/java/j-spring-boot-basics-perry/index.html)
