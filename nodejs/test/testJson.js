const json = require('../src/json');
const bunyan = require('bunyan')
// const config = require('../bunyan_config.json')
var log = bunyan.createLogger({
    name: 'myapp',
    level: "debug",
    serializers: bunyan.stdSerializers,
    streams: [{
        type: 'rotating-file',
        path: `${process.env.NODE_PATH}/logs/api.log`,
        period: '1d',   // daily rotation
        count: 10        // keep 3 back copies
    }, {
        stream: process.stdout
    }]
});
log.info('hi');

// let res = json.parser('{"name":"age"}')
// console.log(" res", res);
