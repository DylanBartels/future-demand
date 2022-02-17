#/bin/sh -e

# Run migrations
alembic upgrade head

# Start server
exec uvicorn app:app --host 0.0.0.0 --port ${PORT:-3000}