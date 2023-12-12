#!/usr/bin/env bash
docker build --no-cache -t auth0-django-01-login .
docker run --env-file .env -p 8080:8080 -it auth0-django-01-login