#!/usr/bin/env bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
API_DIR="$(dirname "$SCRIPT_DIR")"

cd "$API_DIR"

# Check for --pg flag to enable PostgreSQL
if [[ "$*" == *"--pg"* ]]; then
    echo "Starting PostgreSQL via Docker..."
    docker compose -f docker/docker-compose.yml up -d db
    export DB_HOST=localhost
    echo "Using PostgreSQL on localhost:5432"
else
    echo "Using SQLite database..."
fi

uv sync
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
