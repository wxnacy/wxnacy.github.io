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
showTime();
begin();
var timer;
function doBegin() {
    timer = setInterval(showTime, 1000);
};
function doEnd() {
    clearInterval(timer);
};
function begin() {
    timer = setInterval(showTime, 1000);
};
function doTsTrans(){
    console.log('do');
    var ts = document.getElementById('yts').value;
    console.log(ts);
    var bj = tstrans(ts);
    document.getElementById('tbj').innerHTML = bj;
};
function doBjToTs2(){
    // YYYY MM dd HH mm ss to ts
    var y = document.getElementById('y').value;
    var M = document.getElementById('M').value;
    var d = document.getElementById('d').value;
    var h = document.getElementById('h').value;
    var m = document.getElementById('m').value;
    var s = document.getElementById('s').value;
    var bj = y + '/' + M + '/' + d + ' ' + h + ':' + m + ':' + s;
    var now = new Date(bj);
    document.getElementById('tts2').innerHTML = Math.round(now.getTime()/1000);
};
function doBjToTs1(){
    // YYYY-MM-dd HH:mm:ss to ts
    var bj = document.getElementById('ybj').value;
    // var now = new Date(bj.replace(/-/g, '/'));
    var now = new Date(bj);
    document.getElementById('tts').innerHTML = Math.round(now.getTime()/1000);
};
function showTime() {
    var now = new Date();
    var ts=new Date().getTime()/1000;
    var offset = now.getTimezoneOffset() * 60;
    ts = Math.round(ts);
    // timestamp
    document.getElementById('ts').innerHTML = ts;
    var bj = tstrans(ts);
    // bj time
    document.getElementById('bj').innerHTML = bj;
    var utc = tstrans(ts + offset)
    // utc time
    document.getElementById('utc').innerHTML = utc;
};
function bjToTs(y, M, d, h, m, s){
    if( h >= 8 ){
        h = h - 8;
    } else {
        d = d - 1;
    }
    // bj time to ts
    var utc = new Date(Date.UTC(y, M - 1, d, h, m, s));
    var strtime = '2017-12-09 21:14:49';
    var utc = new Date(strtime.replace(/-/g, '/'));
    console.log(utc.getTime()/1000);
    return Math.round(utc.getTime()/1000);
};
function tstrans(ts){
    var date = new Date(ts * 1000);//如果date为13位不需要乘1000
    return date.format('yyyy-MM-dd HH:mm:ss');
};
function getUTCDate(){
    var date = new Date();
    var y = date.getFullYear();
    var M = date.getUTCMonth() + 1;
    var d = date.getUTCDate();
    var h = date.getUTCHours();
    var m = date.getUTCMinutes();
    var s = date.getUTCSeconds();

    M = M < 10 ? '0' + M : M;
    d = d < 10 ? '0' + d : d;
    h = h < 10 ? '0' + h : h;
    m = m < 10 ? '0' + m : m;
    s = s < 10 ? '0' + s : s;
    return y + '-' + M + '-' + d + ' ' + h + ':' + m + ':' + s;
};
// console.log((new Date()).format('YYYY-MM-dd HH:mm:ss'));
