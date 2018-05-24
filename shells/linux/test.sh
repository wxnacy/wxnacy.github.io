#!/usr/bin/env bash

# . check_system.sh

curl https://raw.githubusercontent.com/wxnacy/wxnacy.github.io/master/shells/linux/check_system.sh -o wxnacy_check.sh

. wxnacy_check.sh


echo $PKG

rm wxnacy_check.sh
