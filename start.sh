#!/bin/bash
gunicorn app.run:app -w 2 -b 0.0.0.0:6661 -k gevent --keep-alive 60 -t 72000