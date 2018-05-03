kill -9 `ps aux | grep hexo| awk '{print $2}'`
JS_HOME="themes/yilia/source/js"
uglifyjs ${JS_HOME}/wxnacy.js -o ${JS_HOME}/wxnacy.min.js -m
uglifyjs ${JS_HOME}/web-tools.js -o ${JS_HOME}/web-tools.min.js -m
# uglifyjs ${JS_HOME}/ts.js -o ${JS_HOME}/ts.min.js -m
nohup hexo server --draft &
