#!/usr/bin/env bash
TAG_NAME=$1
cd hexo
hexo clean
hexo generate
cd ..
./push_tag.sh $TAG_NAME $2
ansible-playbook deploy_remote.yml -e "tag_name=$TAG_NAME"
