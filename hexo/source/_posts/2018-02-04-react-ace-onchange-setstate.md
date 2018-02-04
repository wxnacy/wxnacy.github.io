---
title: React-Ace 解决 onChange 中 setState 问题
tags:
  - react
date: 2018-02-04 21:32:01
---


React-Ace 解决 onChange 中 setState 的问题
<!-- more -->

我在正常使用 ace 的功能时碰见一个大问题就是在 `onChange` 的时候，`setState` 会出现问题。
```java
- onChange={this.onChange.bind(this)}
+ onChange={(newValue) => this.onChange(newValue)}
```
通常方法的调用使用第一种，但是在这里需要换成第二种方式

这时候可以成功的保存数据到 `state` 中，但是 ace 的输入功能会出现问题，变的无法正常输入，说白了是组件没有在改变 `state` 后及时更新，此时需要对 `shouldComponentUpdate`组件做出如下操作
```javascript
shouldComponentUpdate(nextProps, nextState) {
    if (this.state.aceValue !== nextState.aceValue) {
        return false
    } else {
        return true;
    }
}
```
也就是判断 `this.state.aceValue` 有变动后修改组件状态

或者简单点，直接让组件继承 `PureComponent`，它自动完成了 `shouldComponentUpdate` 的浅比较

完整调用如下
```javascript
onChange(newValue) {
    this.setState({aceValue: newValue})
}
shouldComponentUpdate(nextProps, nextState) {
    if (this.state.aceValue !== nextState.aceValue) {
        return false
    } else {
        return true;
    }
}
...
<AceEditor
onChange={(newValue) => this.onChange(newValue, mode)}
value={this.state.aceValue}/>
...
```


- [setState in onChange will block the editor](https://github.com/securingsincity/react-ace/issues/181)
- [谈一谈创建React Component的几种方式](https://segmentfault.com/a/1190000008402834)
