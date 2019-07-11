const env_config = require('./local_config.json').local;
const bunyan = require('bunyan')
const bfmt = require('bunyan-format')
const CryptoJS = require("crypto-js");

const fmtOut = bfmt({outputMode: "long"} , process.stdout)
const log = bunyan.createLogger({
    name: 'wxnacy',
    level: "debug",
    serializers: bunyan.stdSerializers,
    streams: [{
        type: 'rotating-file',
        path: `${process.env.NODE_PATH}/logs/api.log`,
        period: '1d',   // daily rotation
        count: 10        // keep 3 back copies
    }, {
        stream: fmtOut
    }]
});

const BaseResponse = function() {
    this.status= 200
    this.message= "ok"
    this.data= {}
}

BaseResponse.prototype.ok = function(ctx, data) {
    this.status = 200
    this.data = data
    this.message = 'ok'
    ctx.body = this
}

BaseResponse.prototype.failed = function(ctx, status, message) {
    this.status = status
    this.data = {}
    this.message = message
    ctx.body = this
    ctx.status = status
}

BaseResponse.prototype.toJSON = function() {
    return {
        status: this.status,
        data: this.data,
        message: this.message
    }
}

const UserSecret = function(opts={}) {
    this.ip = opts.ip
    this.ua = opts.ua
    this.ts = parseInt(Date.now() / 1000)
    this.key = 'd67673f506f955d7c61821867a3a41dc'
}

UserSecret.prototype.encrypt = function() {
    let data = JSON.stringify(this)
    let res = CryptoJS.AES.encrypt(data, this.key).toString()
    let plain = CryptoJS.AES.decrypt(res, this.key).toString(CryptoJS.enc.Utf8)
    return res
}

UserSecret.prototype.decrypt = function(secret) {
    let plain = CryptoJS.AES.decrypt(secret, this.key)
        .toString(CryptoJS.enc.Utf8)
    if( plain ){
        try {
            let res = JSON.parse(plain)
            return res
        } catch(e){
            log.error(e)
            return null
        }
    }
    return null
}


module.exports.env_config = env_config;
module.exports.log = log;
module.exports.BaseResponse = BaseResponse;
module.exports.UserSecret = UserSecret;

