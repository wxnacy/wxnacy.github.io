#!/usr/bin/env bash
sysOS=`uname -s`

update_zshrc(){
    echo 'source ~/.bash_profile' >> $1
    echo 'source $ZSH/oh-my-zsh.sh' >> $1
    echo 'export ZSH=${HOME}/.oh-my-zsh' >> $1
    echo '' >> $1
    echo 'ZSH_THEME="fishy"' >> $1
    echo 'plugins=(git python sublime)' >> $1
    echo '' >> $1
    echo 'alias zshc="vim ~/.zshrc"' >> $1
    echo 'alias zshs="source ~/.zshrc"' >> $1
    echo 'alias vimc="vim ~/.vimrc"' >> $1
    echo 'alias bp="vim ~/.bash_profile"' >> $1
    echo 'alias bps="source ~/.bash_profile"' >> $1
    echo 'alias sshc="vim ~/.ssh/config"' >> $1
    echo 'alias c="clear"' >> $1
    echo 'alias h="history"' >> $1
    source ~/.zshrc
}

install_ubuntu(){
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
ZSHRC='
source ~/.bash_profile
export ZSH=${HOME}/.oh-my-zsh


ZSH_THEME="fishy"

plugins=(git python sublime)
source $ZSH/oh-my-zsh.sh

alias zshc="vim ~/.zshrc"
alias zshs="source ~/.zshrc"
alias vimc="vim ~/.vimrc"
alias bp="vim ~/.bash_profile"
alias bps="source ~/.bash_profile"
alias sshc="vim ~/.ssh/config"

alias c="clear"
alias h="history"
'
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
