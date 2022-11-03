#!/usr/bin/env bash

# gunicorn core.asgi:application --bind 127.0.0.1:8010 -k uvicorn.workers.UvicornWorker
#gunicorn --config gunicorn-cfg.py core.wsgi

# gunicorn core.wsgi --user www-data --bind 0.0.0.0:8010 --workers
echo "Starting server....!"
nginx -g "daemon on;" && gunicorn core.asgi:application --user www-data --bind 127.0.0.1:8010 -k uvicorn.workers.UvicornWorker

echo "Started server....!"
