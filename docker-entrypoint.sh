#!/bin/sh

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

echo "Waiting for DB to restart"
sleep 5

# Seed initial data
echo "Seed initial data"
python manage.py seed_data

# Start server
echo "Starting server"
gunicorn --bind 0.0.0.0:8000 config.wsgi