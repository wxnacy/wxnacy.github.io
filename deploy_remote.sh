#!/usr/bin/env bash
./push_tag.sh $1 $2
ansible-playbook deploy_remote.yml