#!/usr/bin/env bash
CATEGORY=$1
NAME=$2
TITLE=$3




main(){
    python make_file.py "$CATEGORY"  "$NAME"  "${TITLE}"
}

main