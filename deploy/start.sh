#!/usr/bin/env bash
gunicorn app.run:app -w 2 -b 0.0.0.0:6666 -k gevent --keep-alive 60 -t 72000