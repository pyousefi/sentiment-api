#!/bin/bash

python scripts/import_data.py
gunicorn --timeout 100 --bind 0.0.0.0:${PORT} wsgi_app:app
