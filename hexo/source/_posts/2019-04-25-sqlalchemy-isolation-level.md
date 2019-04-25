---
title: SQLAlchemy 解决其他连接修改数据后，查询不到的问题
tags:
  - sqlalchemy
date: 2019-04-25 09:35:51
---


使用 SQLAlchemy 做数据库的读写分离，创建了主从两个 DB，结果发现使用主 DB 写入的数据，从 DB 无法实时查询，必须要重启服务才可以查到。

<!-- more -->
<!-- toc -->

做了各种尝试发现都得不到解决，突然想起以前碰见过类似的问题，但是当时通过其他方式绕了过去，果然不是不报，时候未到。这次必须得正面解决了。

经过 Google 后发现，这是事务的问题，在多个实例进行链接数据库时，如果不执行 `commit`，就得不到最新的数据。

我们可以使用 `session.commit()` 来单个解决，或者可以在创建引擎时通过调整隔离级别参数来永久解决。

```python
engine = create_engine('db_url', isolation_level = 'READ COMMITTED')
```

`isolation_level` 的值包含了：
- READ COMMITTED
- READ UNCOMMITTED
- REPEATABLE READ
- SERIALIZABLE
- AUTOCOMMIT

因为我使用只读，所以 `READ COMMITTED` 就可以满足要求，如果你是读写公用的 DB，直接使用 `AUTOCOMMIT` 就无脑解决了。

如果你使用 `flask_sqlalchemy`，在 `app.config` 中加入如下参数即可

```python
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
```

通过源码可以发现，当该参数设置为 `True` 时，它会自动进行 `commit` 操作

```python
@app.teardown_appcontext
def shutdown_session(response_or_exc):
    if app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']:
        if response_or_exc is None:
            self.session.commit()

    self.session.remove()
    return response_or_exc
```

- [Engine Creation API](https://docs.sqlalchemy.org/en/13/core/engines.html#engine-creation-api)
- [Mysql Transaction Isolation Level](https://docs.sqlalchemy.org/en/13/dialects/mysql.html#transaction-isolation-level)
