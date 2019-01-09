---
title: 重新学 Java 系列：简单解析 xml 文件的方式
date: 2019-01-09 14:19:07
tags: [java]
---

现在公认的最好的文本解析格式为 JSON，XML 已经是过时的标准，但是不可避免的一些历史悠久的项目还在用，比如微信的部分 api，比如 Maven 的 pom.xml 文件。
<!-- more --><!-- toc -->
Java 有很多解析 XML 格式的包，不过我想关注的是最简单的原生方式。

优先准备一个文件 `Stocks.xml`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<stocks>
       <stock>
              <symbol>Citibank</symbol>
              <price>100</price>
              <quantity>1000</quantity>
       </stock>
       <stock>
              <symbol>Axis bank</symbol>
              <price>90</price>
              <quantity>2000</quantity>
       </stock>
</stocks>
```

**必备包**

```java
import java.io.File;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;
```

**解析 DOM**

```java
File stocks = new File("Stocks.xml");
DocumentBuilderFactory dbFactory = DocumentBuilderFactory.newInstance();
DocumentBuilder dBuilder = dbFactory.newDocumentBuilder();
Document doc = dBuilder.parse(stocks);
doc.getDocumentElement().normalize();
```

**获取根节点名**

```java
doc.getDocumentElement().getNodeName();
```

**获取节点列表**

```java
NodeList nodes = doc.getElementsByTagName("stock");
```

**遍历节点**

```java
for (int i = 0; i < nodes.getLength(); i++) {
    Node node = nodes.item(i);
}
```

**获取原件内容**

```java
if (node.getNodeType() == Node.ELEMENT_NODE) {
    Element element = (Element) node;
    NodeList nodes = element.getElementsByTagName("symbol").item(0).getChildNodes();
    Node node = (Node) nodes.item(0);
    System.out.println(node.getNodeValue());
}
```

**完整代码**

```java
import java.io.File;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;

public class DOMExampleJava {

    public static void main(String args[]) {
        try {

            Document doc = parseXml("Stocks.xml")

                System.out.println("root of xml file " + doc.getDocumentElement().getNodeName());
            NodeList nodes = doc.getElementsByTagName("stock");
            System.out.println("==========================");

            for (int i = 0; i < nodes.getLength(); i++) {
                Node node = nodes.item(i);

                if (node.getNodeType() == Node.ELEMENT_NODE) {
                    Element element = (Element) node;
                    System.out.println("Stock Symbol: " + getValue("symbol", element));
                    System.out.println("Stock Price: " + getValue("price", element));
                    System.out.println("Stock Quantity: " + getValue("quantity", element));
                }
            }
        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }

    private static Document parseXml(String filePath) {
        File stocks = new File(filePath);
        DocumentBuilderFactory dbFactory = DocumentBuilderFactory.newInstance();
        DocumentBuilder dBuilder = dbFactory.newDocumentBuilder();
        Document doc = dBuilder.parse(stocks);
        doc.getDocumentElement().normalize();
        return doc;
    }

    private static String getValue(String tag, Element element) {
        NodeList nodes = element.getElementsByTagName(tag).item(0).getChildNodes();
        Node node = (Node) nodes.item(0);
        return node.getNodeValue();
    }
}
```
