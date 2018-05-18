#!/usr/bin/env bash

install_centos(){

    sudo yum install -y yum-utils device-mapper-persistent-data lvm2

    sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo

    sudo yum install -y docker-ce

    sudo systemctl start docker

    sudo systemctl enable docker
}


main(){

    install_centos

    echo '**********************************'
    echo '****        安装完成          ****'
    echo '**********************************'
}

main
