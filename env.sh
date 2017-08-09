#!/usr/bin/env bash

ENV=$1

if [ ! ${ENV} ]
then
    ENV=local
fi

export PYTHONPATH=./
export FLASK_CONFIG=${ENV}