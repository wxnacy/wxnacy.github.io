---
title: 如何获取 IP 、经纬度、时区一系列信息
date: 2017-11-30 17:43:09
tags: [开发]
---

在开发电视端产品时发现，并不能像手机端一样通过 GPS 等手段获取用户的经纬度，产品上添加的天气预报非常依赖这项数据，经 Google 发现，通过 IP 可以使用一些开发接口获取到这些信息，通过一系列接口调用可以形成一个闭环，现在记录下来。

<!-- more -->
## IP
获取 IP 的手段很多，最方便的是从后台获取接口请求的 IP 地址，也有开发 API 可以实现，比如 [ip-api](http://ip-api.com/) ，它提供了免费 API 可以使用
```bash
$ curl http://ip-api.com/json
```
```json
{
    "as": "AS22552 eSited Solutions",
    "city": "Orlando",
    "country": "United States",
    "countryCode": "US",
    "isp": "eSited Solutions",
    "lat": 28.5106,
    "lon": -81.1976,
    "org": "eSited Solutions",
    "query": "104.222.246.242",
    "region": "FL",
    "regionName": "Florida",
    "status": "success",
    "timezone": "America/New_York",
    "zip": "32825"

}
```
结果除了 IP 还有经纬度和时区，如果只需要这些信息，那已经足够了。但是会发现时区显示的是名字，在库里经常会保存小时偏移量 `8, -8` 等，所以还需要其他手段来获取。

## 时区
timezone [时刻表](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)
### Google API
Google API 提供了通过经纬度来获取时区的接口 [Time Zone API](https://developers.google.com/maps/documentation/timezone/intro?hl=zh-cn)
```bash
$ https://maps.googleapis.com/maps/api/timezone/json?location=39.6034810,-119.6822510&timestamp=1331161200&key=YOUR_API_KEY
```
```json
{
    "dstOffset" : 0,
    "rawOffset" : -28800,
    "status" : "OK",
    "timeZoneId" : "America/Los_Angeles",
    "timeZoneName" : "Pacific Standard Time"

}
```
返回的接口 `rawOffset` 字段就是时区的小时偏移量，单位秒

### timezonedb
如果你不想调用很多接口，还可以使用专门提供时区数据的服务 [timezonedb](https://timezonedb.com) 在[这里](https://timezonedb.com/download)可以直接下载 timezone 的数据库 SQL 文件或 CSV 文件，不过他们也提供 API
```bash
$ curl http://api.timezonedb.com/v2/get-time-zone?key=your_key&format=json&by=zone&zone=America/Chicago
```
```json
{
    "status": "OK",
    "message": "",
    "countryCode": "US",
    "countryName": "United States",
    "zoneName": "America/Chicago",
    "abbreviation": "CST",
    "gmtOffset": -21600,
    "dst": "0",
    "dstStart": 1509865200,
    "dstEnd": 1520755199,
    "nextAbbreviation": "CDT",
    "timestamp": 1512013032,
    "formatted": "2017-11-30 03:37:12"

}
```
结果中 `gmtOffset` 即为小时偏移量
