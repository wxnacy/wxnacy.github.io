const utils = require('./utils.js')

module.exports.requestLog = async (ctx, next) => {
    try {
        let req = ctx.request
        let header = req.header
        let prefix = `[${new Date()}][${req.method} ${req.url}]`
        for(let k in header){
            console.log(`${prefix} header ${k}: ${header[k]}`);
        }
        let begin = Date.now()
        await next();
        let cased = Date.now() - begin
        let res = ctx.response
        console.log(`${prefix} return ${res.status} ${res.message}`);
        console.log(`${prefix} end time cased ${cased}`);
    } catch( e ){
        s = e.status || 500
        ctx.body = {
            status: s,
            message: e.message
        }
        ctx.status = s
    }
}

module.exports.checkSign = async (ctx, next) => {
    let body = ctx.request.body
    console.log(body);
    if( ctx.request.method == 'GET' ){
        await next()
        return
    }
    let flag = utils.check_sign(body)
    if( !flag ){
        ctx.body = {
            status: 403,
            message: "error request"
        }
        ctx.status = 403
    }
    await next()
}
