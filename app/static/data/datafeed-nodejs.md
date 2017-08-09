# datafeed-nodejs

## 本地测试方法
### 步骤
```
1. npm install -g aws-lambda-local
2. 在跟目录下执行 lambda-local -f handler -e test/data/watch -t 6 命令
```
### 参数说明
```
-f functionName     | --function=functionName       required       Path to Lambda function main file
-e eventPath        | --event=eventPath             optional       Path to .json file contains event object
-c contextPath      | --context=contextPath         optional       Path to .json file contains context object
-t seconds          | --timeout=seconds
```
### 批量测试
```
1. 项目根目录执行./lambda-test.sh {eventDirPath}
eventDirPath    测试json数据目录地址    如果不传默认test/data
```
## 部署文档
### 部署步骤
#### 使用serverless部署
```
1. 确认部署环境安装了serverless
2. 进入根目录,使用 npm install命令下载工具包
3. 执行 sls deploy命令即可部署
```


##	接口文档
### 测试地址
```
https://im1k8q4i0d.execute-api.us-west-2.amazonaws.com/prod/parser
```
### 头参数
名称 | 值
--- | ---
Content-Type | application/json
x-api-key | DUz8r2LmsCaSaV8bi81N87IaKqIbGNBm2t79lwTJ

### 测试curl地址
```
curl -X POST -H "x-api-key: DUz8r2LmsCaSaV8bi81N87IaKqIbGNBm2t79lwTJ" -H "Content-Type: application/json" -d '{"url":"https://www.youtube.com/watch?v=1GvUG1EbA6E"}' "https://im1k8q4i0d.execute-api.us-west-2.amazonaws.com/prod/parser"

curl -X POST -H "x-api-key: DUz8r2LmsCaSaV8bi81N87IaKqIbGNBm2t79lwTJ" -H "Content-Type: application/json" -d '{"url":"https://www.youtube.com/watch?v=1GvUG1EbA6E","filter":["快"],duration:300,page:1}' "https://im1k8q4i0d.execute-api.us-west-2.amazonaws.com/prod/parser"
```
### 参数JSON结构

名称 | 必传 | 类型 | 描述
----- | ------------- | ------ | --------
url | 是 | String | url地址
filters | 否 | array | 过滤title信息，当结果包含filters其中值得时候，该数据不返还
duration | 否 | int | 单位秒,过滤视频时长,当<=300时,会过滤掉大于该值的视频
page | 否 | int | 搜索页,如果page=3,则同时将2,3页的地址返回

### 返回
名称 | 必返 | 类型 | 描述
----- | ------------- | ------ | --------
status | 是 | int | 接口状态，详情见状态码
error_code | 否 | int | 当status！=200时，返回的错误状态码
error_msg | 否 | String | 当status ！=200时，返回的错误信息
params | 否 | hash | 当status！=200时，返回原参数
results | 否 | hash | 当status==200时，返回正确数据

### results中的item
名称 | 必返 | 类型 | 描述
----- | ------------- | ------ | --------
url | 是 | String | id,level=playlist时,为playlistId,level=video \|details时,为videoId
feedSource | 是 | String | 来源
level | 是 | String | (video\|details\|playlist)
pubdate | 否 | String | 上传时间，格式样例：2016-06-24
disLikeCount | 否 | String | 不喜欢视频的数量
likeCount | 否 | String | 喜欢数量
category | 否 | String | 分类
viewCount | 否 | String | 观看数
uploader | 否 | String | 上传人
duration | 否 | String | 时长，秒
title | 否 | String | 标题
channel | 否 | String | 频道id
image | 否 | String | 封面地址
regionsAllowed | 否 | String | 允许播放地区
tags | 否 | array | 视频标签集合
unavailable | 否 | boolean | 视频是否不可用，true为不可用
items | 否 | array | 视频id集合,当level=playlist是有效,如果有值则需要再次调用lambda

### 状态码
status | errorCode | 描述
------------- | ------ | --------
200 |  | 成功
400 | 1001 | 参数有误
500 | 1002 | url请求超时
400 | 1003 | 无法识别url
500 | 1004 | 内部错误,空指针
500 | 1005 | 内部错误,程序无法识别的错误

## 解析逻辑
### youtube
- /playlist
```
1. level=playlist
2. 返回playlist的url,image,title,items
3. url为playlist的id,需要调用者自行拼接地址
4. items为playlist的视频id集合(过滤掉 删除\下线 的视频)
```

