#!/bin/bash
echo "---------------------------"
echo " Starting Gunicorn"
echo "---------------------------"
gunicorn run:app -w 6 --bind :$BIND_PORT --log-file /var/log/gunicorn-log.log \
         --error-log /var/log/gunicorn-error.log --log-level "debug" \
         --capture-output  --enable-stdio-inheritance
