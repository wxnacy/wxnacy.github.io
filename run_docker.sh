#!/usr/bin/env bash

ENV=$2
PROD=$1

main() {
    sudo docker pull wxnacy/wxnacy:latest
    sudo docker container stop ${PROD}
    sudo docker run \
        -it \
        --restart on-failure:10 \
        -d \
        --name ${PROD} \
        -v "$PWD":/wxnacy/${PROD} \
        -w /wxnacy \
        -p 4010:4100 \
        --env FLASK_CONFIG=${ENV} \
        --env PYTHONPATH=./ \
        wxnacy/wxnacy:latest \
        ./${PROD}/run_gunicorn_in_docker.sh ${PROD}
        # ls -l
}

if [ ! ${PROD} ] || [ ! ${ENV} ]
then
    echo 'Uage: ./run_docker.sh <prod-name[wxnacyapi]> <env[local[product]]>'
else
    main
fi

