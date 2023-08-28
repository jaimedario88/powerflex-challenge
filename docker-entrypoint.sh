#!/bin/sh

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Seed initial data
echo "Seed initial data"
python manage.py seed_data

export DJANGO_SUPERUSER_PASSWORD=admin
export DJANGO_SUPERUSER_EMAIL=admin@example.com
export DJANGO_SUPERUSER_USERNAME=admin

# Add a superuser / this is only done for the reviewers convenience, 
# I would never do this under __real, code-to-be-exposed to the internet__ conditions
if [ "$DJANGO_SUPERUSER_USERNAME" ]
then
    python manage.py createsuperuser \
        --noinput \
        --username $DJANGO_SUPERUSER_USERNAME \
        --email $DJANGO_SUPERUSER_EMAIL
    echo "Create superuser"
fi

# Start server
echo "Starting server"
gunicorn --bind 0.0.0.0:8000 config.wsgi