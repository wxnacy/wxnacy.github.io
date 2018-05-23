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
    sudo ${PKG} -y update
    sudo ${PKG} -y install gcc g++ make cmake
    sudo ${PKG} -y install git vim wget unzip
    if [ ${SYS} == 'ubuntu' ]
    then
        sudo ${PKG} -y install htop python-pip
        sudo pip install httpie
        sudo ${PKG} -y install patch zlib1g.dev libgdbm-dev libssl-dev libsqlite3-dev libbz2-dev libreadline-dev
        sudo ${PKG} -y install dnsutils     # dig
    elif [ ${SYS} == 'centos' ]
    then
        sudo ${PKG} -y install gcc-c++ aclocal
        sudo ${PKG} -y install pcre pcre-devel openssl openssl-devel # nginx
        sudo ${PKG} -y install epel-release htop # htop need
        sudo ${PKG} -y install install zlib zlib-devel  # GeoIp need
        sudo ${PKG} -y install install bind-utils       # dig

        sudo ${PKG} -y install readline readline-devel readline-static openssl-static sqlite-devel bzip2-devel bzip2-libs
    elif [ ${SYS} == 'mac' ]
    then
        echo ${SYS}

    fi
}

check_system
install
echo $PKG
