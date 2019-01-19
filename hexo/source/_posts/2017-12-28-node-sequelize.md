---
title: Node ORM 框架 Sequelize
tags:
  - node
date: 2017-12-28 16:40:44
---


我感觉使用任何一门语言作为后台开发都应该了解他的 [ORM（Object Relational Mapping）](https://zh.wikipedia.org/wiki/%E5%AF%B9%E8%B1%A1%E5%85%B3%E7%B3%BB%E6%98%A0%E5%B0%84) 框架，这是对开发效率的负责，省掉写 Sql 的时间，把它留给更有意义的地方。

<!-- more --><!-- toc -->
本篇以 Mysql 数据库为例，带大家了解 Node 中最多人用的 ORM 框架 [Sequelize](http://docs.sequelizejs.com/)
## 下载
npm
```bash
$ npm install sequelize --save
$ npm install mysql2 --save
```
yarn
```bash
$ yarn add sequelize
$ yarn add mysql2
```

## 创建连接
使用配置
```javascript
const Sequelize = require('sequelize');
const sequelize = new Sequelize('database', 'username', 'password', {
    host: 'localhost',
    dialect: 'mysql',
    pool: {
        max: 5,
        min: 0,
        acquire: 30000,
        idle: 10000
    },
});
```
使用连接URI
```javascript
const sequelize = new Sequelize('postgres://user:pass@example.com:5432/dbname');
```
Sequelize 更多用法见 [API](http://docs.sequelizejs.com/class/lib/sequelize.js~Sequelize.html)

## 创建 Model
首先使用执行下面的语句创建一个测试表 `test`
```mysql
CREATE TABLE `test` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `name` varchar(32) NOT NULL DEFAULT '',
    `create_ts` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COMMENT='test';
```
接下来创建 Model
```javascript
const Test = sequelize.define('test', {
    id: {
        type: Sequelize.INTEGER,
        primaryKey: true,
        autoIncrement: true,
    },
    name: {
        type: Sequelize.STRING
    },
    create_ts: {
        type: Sequelize.DATE
    }
},{
    timestamps: false,
    freezeTableName: true,
});
```
更多 [dataTypes](http://docs.sequelizejs.com/manual/tutorial/models-definition.html#data-types) 以字段检查 [validations](http://docs.sequelizejs.com/manual/tutorial/models-definition.html#validations)
`define` 方法的前两个参数比较好理解，第一个是表名，第二个定义了表中字段的映射关系，第三个比较有意思，待会儿我们在聊它的作用。

## 使用 Model
首先来创建一条数据，需要用到 `build(), save()` 两个方法
```java
Test.build({name: "wxnacy"}).save()
    .then(() => {sequelize.close()})
    .catch(() => {sequelize.close()})
```
`save()` 方法回来一个 Premise ，并且必须在结束时加上 `sequelize.close()` 方法关闭连接，目前我还没找到自动关闭的地方，如果你知道，一定要告诉我。
查询
```java
Test.findOne({where: {name: 'wxnacy'}}).then(test => {
    console.log(test.id, test.name)     // 1 wxnacy
    sequelize.close()
}).catch(e => {
    sequelize.close()
})
```
这种查询方式很简洁，写起来很爽，跟 `Rails` 很像，这时我们可以来说说前边创建 Model 时提到的 `timestamps, freezeTableName` 两个参数的作用，你去掉这两个参数在执行一次，它会报错，日志中给出的 Sql 语句是这样的
```mysql
SELECT `id`, `name`, `create_ts`, `createdAt`, `updatedAt` FROM `tests` AS `test` WHERE `test`.`name` = 'wxnacy' LIMIT 1;
```
两个奇怪的点，凭空多出了 `createAt, updateAt` 两个字段，原表名默认来 `tests`，Sequelize 很“贴心”，直接将表名加了个复数，也把我们表中最常用的两个字段也默认加了进去，BUT，表名我就不想加复数，我的创建时间修改时间也不打算叫这个名字，所以这里需要一些额外的控制
- **freezeTableName** 是否将表名默认使用 `define()` 的第一个参数，默认 false
- **tableName** 自定义表名
- **timestamps** 控制是否添加（createAt，updateAt）两个字段，默认 true
- **createdAt** 如果 `timestamps` 等于 true，可以设置这个参数，false 为不添加，或者可以为它设置别名，比如 `create_ts`
- **updatedAt** 同上
- **deletedAt** 同上
我知道你想说什么，如果每个 Model 都这样设置那是要累死的，所以他必须要有一个可以设置全局的地方，比如
```javascript
const sequelize = new Sequelize(db, user, pw, {
    define: {
        timestamps: false,
        freezeTableName: true,
    }
})
```
更多的 define 配置请见[文档](http://docs.sequelizejs.com/manual/tutorial/models-definition.html#configuration)
好了，我们来写一个完整的例子吧
```java
const Sequelize = require('sequelize');
const sequelize = new Sequelize('database', 'username', 'password', {
    host: 'localhost',
    dialect: 'mysql',
    pool: {
        max: 5,
        min: 0,
        acquire: 30000,
        idle: 10000
    },
});
const Test = sequelize.define('test', {
    id: {
        type: Sequelize.INTEGER,
        primaryKey: true,
        autoIncrement: true,
    },
    name: {
        type: Sequelize.STRING,
        allowNull: true,
        defaultValue: ''
    },
    create_ts: {
        type: Sequelize.DATE
    }
});
Test.build({name: "wxnacy"}).save()
    .then(() => {
        return Test.findById(1)
    }).then(item => {
        console.log(item.id, item.name);    // 1 wxnacy
        sequelize.close()
    }).catch(e => {
        console.log(e);
        sequelize.close()
    })
```
### 常用的方法
```java
Test.create({name: "wxnacy"})
Test.build({name: "wxnacy"}).save()
Test.findById(1).then(test => {console.log(test.toJSON());})
Test.findOne({name: "wxnacy"})
Test.findAll({where: {id: [1, 2, 3]}})
Test.findAll({
    where: {
        id: [1, 2, 3],
        name: "wxnacy",
        name: {
            [Op.like]: 'wxn'
        },
    },
    order: [
        ['id'],
        ['create_ts', 'DESC']
    ],
    limit: 10
})
Test.all()
Test.findById(1).then(item => {
    item.name = 'winn'
    item.save()
})
Test.findOrCreate({where: {name: "wxnacy"}, defaults: {}})
    .spread((blog, created) => {
        console.log(blog.get({plain: true}));
        console.log(created);
    })

```
Model 更多使用方法见[文档](http://docs.sequelizejs.com/manual/tutorial/models-usage.html)
