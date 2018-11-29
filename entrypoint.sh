#!/usr/bin/env bash
WORK_DIR=$(dirname $(readlink -f $0))
cd ${WORK_DIR}

python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000
# exec gunicorn -b 0.0.0.0:8000 -w ${WORKER_NUMBER:-2} -k gevent send_msg.wsgi