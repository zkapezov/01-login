#!/usr/bin/env bash
docker build --no-cache -t auth0-django-01-login .
docker run --env-file .env -p 80:80 -it auth0-django-01-login