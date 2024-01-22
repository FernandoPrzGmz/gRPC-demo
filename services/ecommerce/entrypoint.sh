#!/bin/sh

echo "Waiting for database connection..."
while ! nc -z ecommerce_database 3306; do
  sleep 0.1
done
echo "Database started"

# Removes all data from database
python manage.py flush --no-input

# Make migrations
python manage.py migrate

if [ -n "$DJANGO_SUPERUSER_EMAIL" ] && [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ]; then
    (python manage.py createsuperuser --no-input)
fi

exec "$@"