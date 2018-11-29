#!/usr/bin/env bash
WORK_DIR=$(dirname $(readlink -f $0))
cd ${WORK_DIR}

python manage.py makemigrations
python manage.py migrate
exec python manage.py runserver 0.0.0.0:8000
# exec gunicorn -b 0.0.0.0:8000 -w ${WORKER_NUMBER:-2} -k gevent send_msg.wsgi
