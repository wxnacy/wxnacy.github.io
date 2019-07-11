var CryptoJS = require("crypto-js");

var hash = CryptoJS.MD5('message');
console.log(hash.toString());
var hash = CryptoJS.SHA1('message');
console.log(hash.toString());

var data = [{id: 1}, {id: 2}]

var ciphertext = CryptoJS.DES.encrypt(JSON.stringify(data), 'secret key 123');
console.log(ciphertext.toString());

var bytes  = CryptoJS.DES.decrypt(ciphertext.toString(), 'secret key 123');
var decryptedData = JSON.parse(bytes.toString(CryptoJS.enc.Utf8));

console.log(decryptedData);
