#!/bin/sh
gunicorn app:app -w 2 --threads 3 -b 0.0.0.0:80