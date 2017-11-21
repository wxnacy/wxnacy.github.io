#!/usr/bin/env bash
wget -N --no-check-certificate https://raw.githubusercontent.com/ToyoDAdoubi/doubi/master/ssr.sh && chmod +x ssr.sh
wget --no-check-certificate https://github.com/teddysun/across/raw/master/bbr.sh && chmod +x bbr.sh
yum -y install expect
wget --no-check-certificate https://raw.githubusercontent.com/wxnacy/wxnacy.github.io/master/shells/ssr/install_ssr && chmod +x install_ssr
./install_ssr

# wget --no-check-certificate https://raw.githubusercontent.com/wxnacy/wxnacy.github.io/master/shells/ssr/download_ssr.sh && chmod +x download_ssr.sh && ./download_ssr.sh
