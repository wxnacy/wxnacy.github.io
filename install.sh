#!/usr/bin/env bash

export WXNACY_HOME=`pwd`
# ln -sf `pwd` ~/.wxnacy
ln -sf ${WXNACY_HOME}/shells/vim ~/.vim
ln -sf ${WXNACY_HOME}/shells/vim/vimrc.pathogen ~/.vimrc
ln -sf ${WXNACY_HOME}/shells/vim/ctags ~/.ctags
ln -sf ${WXNACY_HOME}/shells/tmux/tmux.conf ~/.tmux.conf
ln -sf ${WXNACY_HOME}/shells/vim/config/tern-config ~/.tern-config
ln -sf ${WXNACY_HOME}/shells/tmux ~/.tmux
