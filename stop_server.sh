#!/bin/sh

# uWSGI
kill -QUIT `cat logs/app.pid`
