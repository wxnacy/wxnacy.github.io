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
    console.log(params);
    console.log(sign);
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
function create_visit(){
    console.log(window.location.search);
    console.log(document.getElementById('busuanzi_value_page_pv').value);
    fetch('/api/visit', {
        "method": "POST"
    }).then(function(res){
        return res.json()
    }).then(function(data){
        console.log(data);
    })
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
        console.log(data);
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
// create_crypto();
// create_visit();
var params = {"w": 3, "a": 1, "z": 10};
var data = encryptParams(params)
console.log(data);
