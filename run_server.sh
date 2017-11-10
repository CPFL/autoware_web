#!/bin/sh

# uWSGI
kill -QUIT `cat logs/app.pid`
sleep 2
uwsgi --ini conf/app.ini
