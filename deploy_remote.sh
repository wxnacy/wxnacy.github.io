#!/usr/bin/env bash
./push.sh $1
ansible-playbook deploy_remote.yml