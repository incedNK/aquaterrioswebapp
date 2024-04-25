#!/bin/sh

alembic upgrade head

gunicorn -w 4 -k uvicorn.workers.UviconWorker main:app --bind 0.0.0.0:8000