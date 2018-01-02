const CryptoJS = require("crypto-js");
const SECRET_KEY = '5f71fbb6f071d5dc2a4221bb1f891492'

function create_sign(data, ts, rs) {
    data = sortDict(data);
    params = "";
    for(var k in data){
        params = params + `${k}=${data[k]}&`;
    }
    params = params + `ts=${ts}&`;
    params = params + `rs=${rs}`;
    sign = CryptoJS.HmacSHA1(params, SECRET_KEY).toString().toUpperCase();
    return sign;
};

function encryptParams(data) {
    var ts = new Date().getTime();
    var rs = 'ssd8wifhsd8fhf';
    var sign = create_sign(data, ts, rs);
    data['ts'] = ts;
    data['rs'] = rs;
    data['sign'] = sign;
    return data;
}

function check_sign(data) {
    var sign = data.sign;
    var ts = data.ts;
    var rs = data.rs;

    delete data.sign;
    delete data.ts;
    delete data.rs;

    var thisSign = create_sign(data, ts, rs);
    if( thisSign == sign ){
        return true;
    } else {
        return false;
    }
}

function sortDict(dict, isReverse=false) {
    keys = Object.keys(dict);
    keys.sort();
    newDict = {};
    keys.forEach(function(d, i){
        newDict[d] = dict[d];
    })
    return newDict;
};

module.exports.check_sign = check_sign;


// var res = sortDict({"w": 3, "a": 1, "z": 10})
// console.log(res);
// console.log(delete res.w);
// console.log(res);
// var params = {"w": 3, "a": 1, "z": 10};
// var data = encryptParams(params)
// params['ts'] = 1513691726035
// params['rs'] = "ssd8wifhsd8fhf"
// params['sign'] = "7D8A9EEADD7FE35A8BF309B554ACFAC00B016F49"
// console.log(check_sign(params));
// create_sign({"w": 3, "a": 1, "z": 10}, new Date().getTime(), 'sd7f92fh23hf')
