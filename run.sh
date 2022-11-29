#!/bin/sh
gunicorn -w 1 --threads 3 -b 0.0.0.0:80 app:app