/* by wxnacy */
var digits = [
    '0', '1', '2', '3', '4', '5',
    '6', '7', '8', '9',
    'a', 'b',
    'c', 'd', 'e', 'f', 'g', 'h',
    'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B',
    'C', 'D', 'E', 'F', 'G', 'H',
    'I', 'J', 'K', 'L', 'M', 'N',
    'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z',
    '!', '@', '#', '$', '%', '^',
    '&','*'
];
var NUM = [
    '0', '1', '2', '3', '4', '5',
    '6', '7', '8', '9',
];
var letter = [
    'a', 'b',
    'c', 'd', 'e', 'f', 'g', 'h',
    'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z',
];
var LETTER = [
    'A', 'B',
    'C', 'D', 'E', 'F', 'G', 'H',
    'I', 'J', 'K', 'L', 'M', 'N',
    'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z',
];
var special = [
    '!', '@', '#', '$', '%', '^',
    '&','*'
];
function getRandomFunc(len){
    var array = new Array(len);
    array[0] = LETTER[parseInt(Math.random() * LETTER.length)];
    array[1] = letter[parseInt(Math.random() * letter.length)];
    array[2] = special[parseInt(Math.random() * special.length)];
    array[3] = NUM[parseInt(Math.random() * NUM.length)];
    for(var i = 4; i < len; i++){
        array[i] = digits[parseInt(Math.random() * digits.length)];
    }
    var res = array.join('');
    return array.join('');
};
function getRandom(len){
    var res = getRandomFunc(len);
    document.getElementById('out').innerHTML = res;
};
var SECRET_KEY = '5f71fbb6f071d5dc2a4221bb1f891492'
function sortDict(dict) {
    keys = Object.keys(dict);
    keys.sort();
    newDict = {};
    keys.forEach(function(d, i){
        newDict[d] = dict[d];
    })
    return newDict;
};
function create_sign(data, ts, rs) {
    data = sortDict(data);
    params = "";
    for(var k in data){
        params = params + k + "=" + data[k] + '&';
    }
    params = params + "ts=" + ts + "&";
    params = params + "rs=" + rs;
    sign = CryptoJS.HmacSHA1(params, SECRET_KEY).toString().toUpperCase();
    return sign;
};
function encryptParams(data) {
    var ts = new Date().getTime();
    var rs = getRandomFunc(10);
    var sign = create_sign(data, ts, rs);
    data['ts'] = ts;
    data['rs'] = rs;
    data['sign'] = sign;
    return data;
};
function get_page_pv() {
    var pv =  document.getElementById('busuanzi_value_page_pv').innerHTML;
    return pv;
}
function create_visit(){
    var pv = get_page_pv();
    if( pv != '' && pv != 'undefined' ){
        clearInterval(pagePvTimer);
        var params = encryptParams({
            route: window.location.pathname,
            page_view: pv
        });
        fetch('/api/blog/page_view', {
            method: "PUT",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(params)
        }).then(function(res){
            return res.json()
        }).then(function(data){
        })
    }
};
function create_crypto(type) {
    var content = document.getElementById("msg").value;
    var key = document.getElementById("key").value;
    fetch('/api/crypto', {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(encryptParams({
            content: content,
            type: type,
            key: key
        }))
    }).then(function(res){
        return res.json();
    }).then(function(data){
        body = data.data;
        if( type == 'default' || type == 'hmac'){
            document.getElementById("crypto").style.display = 'none';
            document.getElementById("hash").style.display = 'block';
            document.getElementById("md5").innerHTML = body.md5;
            document.getElementById("sha1").innerHTML = body.sha1;
            document.getElementById("sha256").innerHTML = body.sha256;
            document.getElementById("sha512").innerHTML = body.sha512;
        } else {
            document.getElementById('hash').style.display = 'none';
            document.getElementById('crypto').style.display = 'block';
            document.getElementById("result").innerHTML = body.result;
        }
    });
};
var getAccessToken = function(){
    var us = Cookies.get('_US')
    if( us != null && us != undefined && us != '' && us != 'null' ){
        console.log('cookies', us);
        return Promise.resolve(us)
    }
    return new Promise(function(resolve, reject) {
        fetch('/api/access_token')
            .then(function(res){
                return res.json()
            }).then(function(data){
                console.log('fetch;', data);
                var us = data.data
                Cookies.set('_US', us)
                resolve(us)
            }).catch(function(e){
                console.log(e);
                reject(e)
            })
    })
}
/**
 * 搜索
 */
function doSearchByGoogle() {
    var value = document.getElementById('w-search').value
    if( value == '' ){
        return
    }
    value = 'site:https://wxnacy.com ' + value
    value = encodeURIComponent(value)
    var url = 'https://www.google.com/search?q=' + value
    window.open(url,'_blank');
}
/**
 * 回车搜索
 */
function doEnterSearch() {
    var e = window.event
    if( e.key == 'Enter' ){
        doSearchByGoogle()
    }
}

function doUrlencode(type) {
    var plain = document.getElementById('plain')
    var value = plain.value
    if( type == 'encode' ){
        value = encodeURIComponent(value)
        plain.value = value
    } else if( type == 'decode' ){
        value = decodeURIComponent(value)
        plain.value = value
    }

}

/**
 * 转换单位
 */
function doConvertSize() {
    var e = window.event
    var dom = e.path[0]
    var id = dom.id
    var value = dom.value
    if( isNaN(value) ){
        dom.value = value.replace(/\D+/g, '')
    }
    value = dom.value
    if( value == ''){
        return
    }
    value = parseFloat(value)
    var DOMS = ['bytes', 'kb', 'mb', 'gb', 'tb']
    var bytes = 0
    if( id == 'bit' ){
        bytes = value / 8
    } else if( id == 'bytes' ){
        bytes = value
    } else if( id == 'kb' ){
        bytes = value * Math.pow(1024, 1)
    } else if( id == 'mb' ){
        bytes = value * Math.pow(1024, 2)
    } else if( id == 'gb' ){
        bytes = value * Math.pow(1024, 3)
    } else if( id == 'tb' ){
        bytes = value * Math.pow(1024, 4)
    }
    var bit = bytes * 8
    document.getElementById('bit').value = bit
    for(var i = 0; i < DOMS.length; i++){
        document.getElementById(DOMS[i]).value = bytes / Math.pow(1024, i)
    }
}
function onlyNum() {
    if(!(event.keyCode==46)&&!(event.keyCode==8)&&!(event.keyCode==37)&&!(event.keyCode==39))
    if(!((event.keyCode>=48&&event.keyCode<=57)||(event.keyCode>=96&&event.keyCode<=105)))
    event.returnValue=false;
}
function checkNaN(){
    var value = window.event.path[0].value
    console.log(value);
    if( isNaN(value) ){
        event.returnValue = false;
    }
}
function isEmpty(val){
  if (val == '' || val == null || val == undefined || val == "undefined") {
    return true;
  }
  return false;
}
function getValue(key) {
  var name = key + "=";
  var str = window.location.search;
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
function visitor(){

    fetchGet('https://ipapi.co/json/').then(function(data){
        params = {
            ip: data.ip,
            url: window.location.href,
            referrer: document.referrer,
            ext_property: data
        }
        fetchPost('https://api.wxnacy.com/api/v1/visitor_log',params).then(function(data){
        })
    })
}
function setCookie(cname,cvalue,exdays) {
  var d = new Date();
  d.setTime(d.getTime()+(exdays*24*60*60*1000));
  var expires = "expires="+d.toGMTString();
  document.cookie = cname + "=" + cvalue + "; " + expires;
}

function getCookie(cname){
  var name = cname + "=";
  var ca = document.cookie.split(';');
  for(var i=0; i<ca.length; i++)
  {
    var c = ca[i].trim();
    if (c.indexOf(name)==0) return c.substring(name.length,c.length);
  }
  return "";
}
function fetchGet(url) {
    return fetchRequest(url, 'GET')
}
function fetchPost(url, params) {
    return fetchRequest(url, 'POST', params)
}
function fetchRequest(url, method, params) {
    var headers = {
        "authorization": getCookie('authorization')
    }
    if( method.toLowerCase() == 'post' ){
        headers['Content-Type']= 'application/json'
    }
    return new Promise(function(resolve, reject) {
        fetch(url, {
            method: method,
            headers: headers,
            body: JSON.stringify(params)
        }).then(function(res){
            return res.json()
        }).then(function(data){
            resolve(data)
        }).catch(function(e){
            console.log(e);
            reject(e)
            // 需要统一的处理错误方式，避免每次都catch
        })
    })
}

visitor()

// var pagePvTimer;
// pagePvTimer = setInterval(create_visit, 1000);
// getAccessToken().then(function(res){
    // console.log("access", res);
// })


// create_crypto();
// create_visit();
// console.log(get_page_pv());
// var params = {"w": 3, "a": 1, "z": 10};
// var data = encryptParams(params)
// console.log(data);
