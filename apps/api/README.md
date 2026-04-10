# Kastau API (Backend)

REST API untuk platform kebijakan daerah Kabupaten Jayapura, dibangun menggunakan FastAPI dan PostgreSQL.

## Prasyarat

- Python 3.11+
- [uv](https://docs.astral.sh/uv/) (Python package manager tercepat)
- Docker & Docker Compose (Opsional, untuk PostgreSQL)

## Setup Lokal

### 1. Menggunakan Docker

Paling mudah untuk menjalankan API beserta database-nya secara otomatis:
```bash
pnpm docker:up
```

### 2. Manual (Tanpa Docker)

Jika Anda ingin menjalankan server di luar container secara manual:

```bash
git clone https://github.com/papuaopensource/kastau
cd kastau/apps/api
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt  # Atau gunakan 'uv sync'
cp .env.example .env
alembic upgrade head
uvicorn app.main:app --reload
```

API tersedia di: `http://localhost:8000`

## Dokumentasi Endpoint

Akses dokumentasi interaktif di:

- **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
- **Redoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)

## Perintah Penting

| Perintah | Deskripsi |
|----------|-----------|
| `pnpm docker:up` | Menjalankan API & Postgres di Docker |
| `pnpm docker:seed` | Mengisi data dummy ke database Docker |
| `pnpm docker:migration` | Menjalankan migrasi database di Docker |
| `pnpm docker:migration:create` | Membuat file migrasi baru di Docker |
| `pnpm db:seed` | Mengisi data dummy ke database lokal |
| `pnpm db:exec` | Masuk ke terminal psql database |
| `pnpm docker:rm` | Menghapus container dan volume database |
