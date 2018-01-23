---
title: spring-data-jparepository
tags: [spring, jpa]
---

```java
public interface JpaRepository<T, ID extends Serializable> extends PagingAndSortingRepository<T, ID>, QueryByExampleExecutor<T> {
    List<T> findAll();

    List<T> findAll(Sort var1);

    List<T> findAll(Iterable<ID> var1);

    <S extends T> List<S> save(Iterable<S> var1);

    void flush();

    <S extends T> S saveAndFlush(S var1);

    void deleteInBatch(Iterable<T> var1);

    void deleteAllInBatch();

    T getOne(ID var1);

    <S extends T> List<S> findAll(Example<S> var1);

    <S extends T> List<S> findAll(Example<S> var1, Sort var2);

}
```

- [Spring Data JPA 2.0.2.RELEASE API](https://docs.spring.io/spring-data/data-jpa/docs/current/api/)
- [Interface JpaRepository](https://docs.spring.io/spring-data/data-jpa/docs/current/api/)
