const Koa = require('koa');
const kbp = require('koa-bodyparser');
const cors = require('koa-cors');
const app = new Koa();
const router = require('koa-router')();
// const ss = require('./src/screenshot.js');
const json = require('./src/json');
const Q = require('q');

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

