#!/bin/sh


# Apply database migrations
echo "Applying database migrations..."
python manage.py makemigrations
python manage.py migrate

# Collect static files (if applicable)
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Start the Django application
echo "Starting Django server..."
exec "$@"
