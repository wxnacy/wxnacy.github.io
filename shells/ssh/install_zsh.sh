#!/usr/bin/env bash

# wget https://raw.githubusercontent.com/wxnacy/wxnacy.github.io/master/shells/ssh/install_zsh.sh && chmod +x install_zsh.sh && ./install_zsh.sh

sysOS=`uname -s`

update_zshrc(){
    sudo mv ~/.zshrc ~/.zshrc_old

    sudo echo 'source ~/.bash_profile' >> $1
    sudo echo 'source $ZSH/oh-my-zsh.sh' >> $1
    sudo echo 'export ZSH=${HOME}/.oh-my-zsh' >> $1
    sudo echo '' >> $1
    sudo echo 'ZSH_THEME="fishy"' >> $1
    sudo echo 'plugins=(git python sublime)' >> $1
    sudo echo '' >> $1
    sudo echo 'alias zshc="vim ~/.zshrc"' >> $1
    sudo echo 'alias zshs="source ~/.zshrc"' >> $1
    sudo echo 'alias vimc="vim ~/.vimrc"' >> $1
    sudo echo 'alias bp="vim ~/.bash_profile"' >> $1
    sudo echo 'alias bps="source ~/.bash_profile"' >> $1
    sudo echo 'alias sshc="vim ~/.ssh/config"' >> $1
    sudo echo 'alias c="clear"' >> $1
    sudo echo 'alias h="history"' >> $1

    source ~/.zshrc
}

install_ubuntu(){
    echo 'I am ubuntu'
    echo 'begin apt-get update'
    sudo apt-get update
    echo 'begin install git'
    sudo apt-get -y install git
    echo 'begin install zsh'
    sudo apt-get -y install zsh
    chsh -s /bin/zsh
    sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
    update_zshrc ~/.zshrc
    zsh
}
main(){
    if [ $sysOS == "Darwin"  ];then
        echo "I'm MacOS"
        update_zshrc ~/.wxnacy/test/find.txt
    elif [ $sysOS == "Linux"  ];then
        echo "I'm Linux"
        source /etc/os-release
        case $ID in
            debian|ubuntu|devuan)
                install_ubuntu
                ;;
            centos|fedora|rhel)
                yumdnf="yum"
                if test "$(echo "$VERSION_ID >= 22" | bc)" -ne 0;
                then
                    yumdnf="dnf"
                fi
                sudo $yumdnf install -y
                redhat-lsb-core
                ;;
            *)
                exit 1
                ;;
        esac
    else
        echo "Other OS: $sysOS"
    fi
}
main
