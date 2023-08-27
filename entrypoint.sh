#!/bin/bash

# Perform setup tasks, environment configuration, etc.

# Run Django migrations and collect static files
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput

# Start Gunicorn
gunicorn yacht_shop.wsgi:application --bind 0.0.0.0:8080

# Start the main application process
exec "$@"