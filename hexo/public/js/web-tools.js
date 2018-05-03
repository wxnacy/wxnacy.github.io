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

// if( require.main === module  ){
  // console.log(WebTools.getRandom(1));
  // console.log(WebTools.getRandom(7));
  // var a = [1, 2]
  // a.extend(['a', 'b'], [8, 9], [4, 5])
  // console.log(a);
// }
