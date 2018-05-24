#!/usr/bin/env bash

# . check_system.sh

curl https://raw.githubusercontent.com/wxnacy/wxnacy.github.io/master/shells/linux/check_system.sh -o wxnacy_check.sh

. wxnacy_check.sh


echo $PKG

rm wxnacy_check.sh

sudo yum install -y gcc g++ make cmake git vim wget unzip \
         gcc-c++ aclocal \
         pcre pcre-devel openssl openssl-devel \
         epel-release htop \
         install zlib zlib-devel  \
         install bind-utils      \ 
sudo yum install -y         readline readline-devel readline-static openssl-static sqlite-devel\
         bzip2-devel bzip2-libs
