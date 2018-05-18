#!/usr/bin/env bash

PROD=$1

main() {
    cp local_config.py ${PROD}/app/local_config.py
    cd ${PROD}
    gunicorn -c gunicorn_config.py run:app
}

if [ ! ${PROD} ]
then
    echo 'Uage: ./run_gunicorn_in_docker.sh <prod-name[wxnacyapi]>'
else
    main
fi

