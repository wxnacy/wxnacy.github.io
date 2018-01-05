const config = require('../local_config.json').local.twitter
console.log(config);
const Twitter = require('twitter-node-client').Twitter;
const twitter = new Twitter(config)
const TWITTER_BASE_URL = 'https://api.twitter.com/1.1';

const error = function (err, response, body) {
    console.log('ERROR [%s]', JSON.stringify(err, null, 2));

};

const success = function (data) {
    console.log('Data [%s]', data);
};

// twitter.doPost(`${TWITTER_BASE_URL}/direct_messages/new.json`, {
    // user_id: '2510838212',
    // text: 'This is easy.'
// }, error, success);

twitter.getUserTimeline({ screen_name: 'BoyCook', count: '10' }, error, success)
// twitter.doRequest(`${TWITTER_BASE_URL}/direct_messages/events/list.json`, error, success)
// twitter.getUser('2510838212', error, success)
// twitter.getSearch({'q':'#haiku','count': 10}, error, success);
