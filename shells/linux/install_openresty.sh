#!/usr/bin/env bash

PKG=''
SYS=''

check_system(){
    OS=`uname -s`
    if [ ${OS} == "Darwin"  ];then
        PKG='brew'
        SYS='mac'
    elif [ ${OS} == "Linux"  ];then
        source /etc/os-release
        case $ID in
            debian|ubuntu|devuan)
                PKG='apt'
                SYS='ubuntu'
                ;;
            centos|fedora|rhel)
                PKG="yum"
                SYS="centos"
                # if test "$(echo "$VERSION_ID >= 22" | bc)" -ne 0;
                # then
                    # PKG="dnf"
                # fi
                ;;
            *)
                exit 1
                ;;
        esac
    else
        echo "Other OS: ${OS}"
    fi
}

install(){
    if [ ${SYS} == 'ubuntu' ]
    then

        wget -qO - https://openresty.org/package/pubkey.gpg | sudo apt-key add -
        sudo apt-get -y install software-properties-common
        sudo add-apt-repository -y "deb http://openresty.org/package/ubuntu $(lsb_release -sc) main"
        sudo apt-get -y update
        sudo apt-get -y install openresty

    elif [ ${SYS} == 'centos' ]
    then
        sudo ${PKG} -y install gcc-c++ aclocal
        sudo ${PKG} -y install pcre pcre-devel openssl openssl-devel # nginx
        sudo ${PKG} -y install epel-release htop # htop need
        sudo ${PKG} -y install install zlib zlib-devel  # GeoIp need

        sudo ${PKG} -y install readline readline-devel readline-static openssl-static sqlite-devel bzip2-devel bzip2-libs
    elif [ ${SYS} == 'mac' ]
    then
        echo ${SYS}

    fi
}

check_system
install
