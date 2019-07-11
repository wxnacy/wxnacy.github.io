const log = require('../config.js').log
const Promise = require('es6-promise').Promise;
log.info('hi');


const testPromise = (flag) => {
    return new Pormise((resolve, reject) => {
        if( flag == 1 ){
            resolve(11)
        } else {
            reject(22)
        }
    })
}

testPromise(1).then(res => {
    console.log(res);
})
