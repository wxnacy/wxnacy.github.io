Array.prototype.extend = function(lists){
  var thisArr = this;
  Array.prototype.forEach.call(arguments, function(arg){
    Array.prototype.forEach.call(arg, function(obj){
      thisArr.push(obj)
    })
  });
};


var WebTools = (function(){

  function getArgsValue(key){
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
  };

  function isEmpty(val){
    if (val == '' || val == null || val == undefined || val == "undefined") {
      return true;
    }
    return false;
  };

  function isNotEmpty(val){
    return !isEmpty(val)
  };

  function setCookie(cname,cvalue,exdays) {
    var d = new Date();
    d.setTime(d.getTime()+(exdays*24*60*60*1000));
    var expires = "expires="+d.toGMTString();
    document.cookie = cname + "=" + cvalue + "; " + expires;
  };

  function getCookie(cname){
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for(var i=0; i<ca.length; i++)
    {
      var c = ca[i].trim();
      if (c.indexOf(name)==0) return c.substring(name.length,c.length);
    }
    return "";
  };

  var DIGITS = [
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
  var LETTER = [
    'a', 'b',
    'c', 'd', 'e', 'f', 'g', 'h',
    'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z',
  ];
  var CAPITAL = [
    'A', 'B',
    'C', 'D', 'E', 'F', 'G', 'H',
    'I', 'J', 'K', 'L', 'M', 'N',
    'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z',
  ];
  var SPECIAL = [
    '!', '@', '#', '$', '%', '^',
    '&','*'
  ];

  // DIGITS.push(LETTER)
  // DIGITS.push(CAPITAL)
  // DIGITS.push(NUM)
  // DIGITS.push(SPECIAL)
  // console.log(DIGITS);

  function getRandom(len){
    var array = new Array(len);
    array[0] = LETTER[parseInt(Math.random() * LETTER.length)];
    array[1] = CAPITAL[parseInt(Math.random() * CAPITAL.length)];
    array[2] = SPECIAL[parseInt(Math.random() * SPECIAL.length)];
    array[3] = NUM[parseInt(Math.random() * NUM.length)];
    for(var i = 4; i < len; i++){
      array[i] = DIGITS[parseInt(Math.random() * DIGITS.length)];
    }
    var res = array.join('');
    return array.join('');
  };

  function customizeLog(){
    var old = console.log;
    var logger = document.getElementById('console');
    console.log = function (message) {
      if (typeof message == 'object') {
        logger.innerHTML += (JSON && JSON.stringify ? JSON.stringify(message) : message) + '<br />';
      } else {
        logger.innerHTML += message + '<br />';
      }
    }
  }


  return {
    getArgsValue: getArgsValue,
    isEmpty: isEmpty,
    isNotEmpty: isNotEmpty,
    setCookie: setCookie,
    getCookie: getCookie,
    getRandom: getRandom,
  }
})();

function filterJson(json, include, exclude){
  console.log(json, include, exclude);
  if( isNotEmpty(include) ){


  }
}

var WebFetch = (function(){
  function get(url) {
    return request(url, 'GET')
  };
  function post(url, params) {
    return request(url, 'POST', params)
  };
  function request(url, method, params, headers) {
    var headers = {
      // "authorization": getCookie('authorization')
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
        reject(e)
        // 需要统一的处理错误方式，避免每次都catch
      })
    })
  };

  return {
    get: get,
  }
})();


// if( require.main === module  ){
  // // var d = { name: "wxnacy" }
  // // filterJson(d)
  // //
  // res = WebFetch.get(':4001/api/v1/wapi/test')
  // console.log(res);
// }
