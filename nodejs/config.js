const env_config = require('./local_config.json').local;
const bunyan = require('bunyan')
const bfmt = require('bunyan-format')
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


module.exports.env_config = env_config;
module.exports.log = log;
