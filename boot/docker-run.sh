#!/bin/bash

source /opt/venv/bin/activate

cd /code

RUN_PORT=${PORT:-8000}
RUN_HOST=${HOST:-0.0.0.0}

exec gunicorn src.main:app \
    -k uvicorn.workers.UvicornWorker \
    --bind ${RUN_HOST}:${RUN_PORT} \
    --workers 2