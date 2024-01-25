#!/bin/sh

echo "Waiting for database connection..."
while ! nc -z inventory_database 3306; do
  sleep 0.1
done
echo "Database started"

# Run migrations
npm run migrate

exec "$@"