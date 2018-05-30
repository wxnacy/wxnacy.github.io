#!/usr/bin/env bash
TAG_NAME=$1
./push_tag.sh $TAG_NAME $2
ansible-playbook deploy_remote_api.yml -e "tag_name=$TAG_NAME"
