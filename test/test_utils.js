
function getValue(key) {
    var name = key + "=";
    // var str = window.location.search;
    var str = 'http://localhost/www?v=dddddd&n=d3d';
    var beginIndex = str.indexOf("?" + name);
    if (beginIndex == -1) {
        beginIndex = str.indexOf("&" + name);
    }
    if (beginIndex != -1) {
        var pos_start = beginIndex + name.length + 1;
        var pos_end = str.indexOf("&", pos_start);
        if (pos_end == -1) {
            return decodeURIComponent(str.substring(pos_start));
        } else {
            return decodeURIComponent(str.substring(pos_start, pos_end));
        }
    }
}

Date.prototype.format=function(fmt) {
    var o = {
        "M+" : this.getMonth()+1, //月份
        "d+" : this.getDate(), //日
        "h+" : this.getHours()%12 == 0 ? 12 : this.getHours()%12, //小时
        "H+" : this.getHours(), //小时
        "m+" : this.getMinutes(), //分
        "s+" : this.getSeconds(), //秒
        "q+" : Math.floor((this.getMonth()+3)/3), //季度
        "S" : this.getMilliseconds() //毫秒
        };
    var week = {
        "0" : "/u65e5",
        "1" : "/u4e00",
        "2" : "/u4e8c",
        "3" : "/u4e09",
        "4" : "/u56db",
        "5" : "/u4e94",
        "6" : "/u516d"
        };
    if(/(y+)/.test(fmt)){
            fmt=fmt.replace(RegExp.$1, (this.getFullYear()+"").substr(4 - RegExp.$1.length));
        }
    if(/(E+)/.test(fmt)){
            fmt=fmt.replace(RegExp.$1, ((RegExp.$1.length>1) ? (RegExp.$1.length>2 ? "/u661f/u671f" : "/u5468") : "")+week[this.getDay()+""]);
        }
    for(var k in o){
            if(new RegExp("("+ k +")").test(fmt)){
                        fmt = fmt.replace(RegExp.$1, (RegExp.$1.length==1) ? (o[k]) : (("00"+ o[k]).substr((""+ o[k]).length)));
                    }
        }
    return fmt;
};

fetch('http://ip-api.com/json')
    .then(function(response){
        return response.json();
    }).then(function(data){
        console.log(data.query);
    })
