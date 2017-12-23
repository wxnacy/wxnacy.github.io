const Redis = require('ioredis');
// const client = new Redis({
    // host:"localhost",
    // port:"6379",
    // db: 0
// });
const client = new Redis();

// client.set('test', 11);
// let res = client.get("test")
let obj = {"name": "wxnacy"};
obj = "wxnacy";
// client.set('test', new Buffer(obj), 30).then(data => {
    // console.log(data);
    // client.disconnect();
// }).catch(e => {
    // console.log(e);
// })


const set = (name, value) =>{
    return client.set(name, value).then(res => {
        console.log(res);
        client.disconnect()
    }).catch(e => {
        console.log(e);
        client.disconnect()
    })
}

// client.get('test').then(data => {
    // console.log(data);
    // client.close();
// });
set('test', obj);
