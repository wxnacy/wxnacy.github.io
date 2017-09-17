kill -9 `ps aux | grep hexo| awk '{print $2}'`
nohup hexo server &
