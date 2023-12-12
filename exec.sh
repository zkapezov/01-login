#!/usr/bin/env bash
docker build -t auth0-django-01-login .
docker run --env-file .env -p 8081:8081 -it auth0-django-01-login