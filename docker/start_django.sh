#!/bin/bash

echo "Creating .env file"
cp ./todo/.env.template ./todo/.env

echo "Running django migrations..."

python manage.py migrate

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Creating Admin Account..."
python manage.py createsuperuser  --noinput

echo "Starting Django DevServer"
python manage.py runserver 0.0.0.0:8000
# gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 2