#!/bin/bash
DJANGODIR=$(dirname $(cd `dirname $0` && pwd))
DJANGO_SETTINGS_MODULE=config.settings
cd $DJANGODIR
source .venv/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
exec python manage.py runserver 0:9000
