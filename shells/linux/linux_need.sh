#!/usr/bin/bash

PKG=''

check_system(){
    OS=`uname -s`
    if [ ${OS} == "Darwin"  ];then
        PKG='brew'
    elif [ ${OS} == "Linux"  ];then
        source /etc/os-release
        case $ID in
            debian|ubuntu|devuan)
                PKG='apt-get'
                ;;
            centos|fedora|rhel)
                PKG="yum"
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

check_system
echo $PKG
