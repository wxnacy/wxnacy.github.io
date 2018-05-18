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
                if test "$(echo "$VERSION_ID >= 22" | bc)" -ne 0;
                then
                    PKG="dnf"
                fi
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
    sudo ${PKG} update
    sudo ${PKG} -y install git gcc make vim wget htop python-pip
    sudo pip install httpie
    if [ ${SYS} == 'ubuntu' ]
    then
        # sudo ${PKG} -y install patch zlib1g.dev libgdbm-dev libssl-dev libsqlite3-dev libbz2-dev libreadline-dev
        echo ${SYS}
    elif [ ${SYS} == 'centos' ]
    then
        sudo ${PKG} -y install readline readline-devel readline-static openssl openssl-devel openssl-static sqlite-devel bzip2-devel bzip2-libs
    elif [ ${SYS} == 'mac' ]
    then
        echo ${SYS}

    fi
}

check_system
install
echo $PKG
