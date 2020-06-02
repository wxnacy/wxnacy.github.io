#!/usr/bin/env bash
# TAG_NAME=`./next_version`
TAG_NAME=v$(date '+%Y.%m.%d.%H%M%S')
cd hexo
hexo clean
hexo generate
cd ../leetcode
mkdocs build
cd ..
./push_tag.sh $TAG_NAME $1
ansible-playbook deploy_remote.yml -e "tag_name=$TAG_NAME"
