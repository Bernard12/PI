set WORKER_COUNT=16
gunicorn -w %WORKER_COUNT% main:app
