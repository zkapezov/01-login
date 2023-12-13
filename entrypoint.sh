#!/usr/bin/env bash
python manage.py migrate
python manage.py initadmin
gunicorn webappexample.wsgi:application --bind "0.0.0.0:8081" --daemon
nginx -g 'daemon off;'