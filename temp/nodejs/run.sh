kill -9 `ps aux | grep index.js | awk '{print $2}'`
nohup node index.js &
