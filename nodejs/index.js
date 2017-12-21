const Koa = require('koa');
const kbp = require('koa-bodyparser');
const cors = require('koa-cors');
const app = new Koa();
const router = require('koa-router')();
// const ss = require('./src/screenshot.js');
const json = require('./src/json');
const mysql = require('./src/mysql-util.js');
const utils = require('./src/utils.js');
const Q = require('q');
const CryptoJS = require("crypto-js");

router.post('jsonParser','/json/parser',(ctx,next) => {
    const body = ctx.request.body;
    let data = body.data;
    let res = json.parser(data);
    ctx.response.body = {
        data: res,
        status: 200,
        message: ""
    };
    // const defer = Q.defer();
    // console.log(file_name)
    // console.log(url)
    // ss.createScreenShot(file_name,url, width, height).then(res => {
        // console.log(res)
        // ctx.response.body = {
            // data: {
                // file_name: res,
                // url: `http://tmdmenuimg.gochinatv.com/screen_shot/${res}`

            // },
            // status: 200,
            // message: ""
        // };
        // defer.resolve();

    // })
    // return defer.promise;


});

router.post('batch_screen_shot','/batch_screen_shot',(ctx,next) => {
    const body = ctx.request.body;
    let items = [];
    const defer = Q.defer();
    console.log(body.length);
    body.forEach(d =>{
        const url = d.url;
        const file_name = d.file_name;
        const width = d['width'];
        const height = d['height'];
        console.log(url);
        ss.createScreenShot(file_name,url, width, height, 2000).then(res => {
            console.log("get result");
            let item = {
                file_name: res,
                url: `http://tmdmenuimg.gochinatv.com/screen_shot/${res}`

            }
            items.push(item);
            if(items.length == body.length){
                ctx.response.body = {
                    data: items,
                    status: 200,
                    message: ""

                }
                defer.resolve();

            }

        });

    });

    return defer.promise;


});

router.put('put_page_view','/api/blog/page_view',(ctx,next) => {
    ctx.response.header['Content-Type']= 'application/json;charset=utf8';
    let body = ctx.request.body;
    let headers = ctx.request.headers;
    console.log(body);
    console.log(headers);

    // const defer = Q.defer();
    // mysql.query(sql, []).then(res => {
        // ctx.response.body = {
            // "headers": headers,
            // "status": 200
        // }
        // defer.resolve();
    // })
    // return defer.promise;
    return 'Hello World '
})

router.post('crypto','/api/crypto',(ctx,next) => {
    ctx.response.header['Content-Type']= 'application/json;charset=utf8';
    let body = ctx.request.body;
    let flag = utils.check_sign(body);
    if( !flag ){

        ctx.response.body = {
            "status": 403,
            "message": "error request"
        }
        return;
    }
    let content = body.content;
    let key = body.key;
    let type = body.type;
    let res = {};
    console.log(body);
    if( type == 'hmac' ){
        res = {
            "md5": CryptoJS.HmacMD5(content, key).toString(),
            "sha1": CryptoJS.HmacSHA1(content, key).toString(),
            "sha256": CryptoJS.HmacSHA256(content, key).toString(),
            "sha512": CryptoJS.HmacSHA512(content, key).toString(),
        }

    } else if( type == 'aes_encrypt' ){
        res['result'] = CryptoJS.AES.encrypt(content, key).toString()
    } else if( type == 'aes_decrypt' ){
        res['result'] = CryptoJS.AES.decrypt(content, key)
            .toString(CryptoJS.enc.Utf8);
    } else if( type == 'des_encrypt' ){
        res['result'] = CryptoJS.DES.encrypt(content, key).toString()
    } else if( type == 'des_decrypt' ){
        res['result'] = CryptoJS.DES.decrypt(content, key)
            .toString(CryptoJS.enc.Utf8);
    } else if( type == 'tdes_encrypt' ){
        res['result'] = CryptoJS.TripleDES.encrypt(content, key).toString()
    } else if( type == 'tdes_decrypt' ){
        res['result'] = CryptoJS.TripleDES.decrypt(content, key)
            .toString(CryptoJS.enc.Utf8);
    } else if( type == 'rabbit_encrypt' ){
        res['result'] = CryptoJS.Rabbit.encrypt(content, key).toString()
    } else if( type == 'rabbit_decrypt' ){
        res['result'] = CryptoJS.Rabbit.decrypt(content, key)
            .toString(CryptoJS.enc.Utf8);
    }else {
        res = {
            "md5": CryptoJS.MD5(content).toString(),
            "sha1": CryptoJS.SHA1(content).toString(),
            "sha256": CryptoJS.SHA256(content).toString(),
            "sha512": CryptoJS.SHA512(content).toString(),
        }
    }
    ctx.response.body = {
        "data": res,
        "status": 200,
        "message": ""
    }
})

router.get('test','/api/visit',(ctx,next) => {
    ctx.response.header['Content-Type']= 'application/json;charset=utf8';
    ctx.response.body = ctx.request.query;
    let sql = 'select * from visit_log order by id desc limit 5;'
    const defer = Q.defer();
    mysql.query(sql, []).then(res => {
        ctx.response.body = {
            query: ctx.request.query,
            bodys: ctx.request.body,
            "name": res
        }
        defer.resolve();
    })
    return defer.promise;
})

router.get('test','/api',(ctx,next) => {
    ctx.response.header['Content-Type']= 'application/json;charset=utf8';
    ctx.response.body = ctx.request.query;
    ctx.response.body = {
        query: ctx.request.query,
        bodys: ctx.request.body,
        "name": "wxnacy"
    }
})

app
    .use(kbp())
    .use(cors())
    .use(router.routes())
    .use(router.allowedMethods());
app.listen(5000,() => {
    console.log('listen to 0.0.0.0:5000');
});

