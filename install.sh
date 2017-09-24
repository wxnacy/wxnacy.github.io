#!/usr/bin/env bash

# echo $(dirname $0)
# echo `pwd`
# if [ !  ${WXNACY} ]
# then
    # echo 'wxnacy'
    # echo 'export WXNACY=`pwd`' >> ~/.bash_profile
    # source ~/.bash_profile
# fi
# echo $WXNACY
export WXNACY_HOME=`pwd`
# ln -sf `pwd` ~/.wxnacy
ln -sf ${WXNACY_HOME}/shells/vim ~/.vim
ln -sf ${WXNACY_HOME}/shells/vim/vimrc.pathogen ~/.vimrc
ln -sf ${WXNACY_HOME}/shells/vim/ctags ~/.ctags
ln -sf ${WXNACY_HOME}/shells/tmux/tmux.conf ~/.tmux.conf
