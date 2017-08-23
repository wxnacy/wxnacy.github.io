#!/usr/bin/env bash

TAG_NAME=$1


main(){
    for tag in `git tag -l ${TAG_NAME}`
    do
        git tag -d ${tag}
        git push origin :${tag}
    done
}

if [ ! ${TAG_NAME} ]
then
    echo 'UAGE: ./delete_git_tag.sh <regex:tag_name>'
else
    main
fi
