# <div align="center">analytics-api-microsservice</div>

<div align="center">

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python\&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.132.0-009688?logo=fastapi\&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-2.x-E92063?logo=pydantic\&logoColor=white)
![SQLModel](https://img.shields.io/badge/SQLModel-0.0.37-4B8BBE)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker\&logoColor=white)
![Gunicorn](https://img.shields.io/badge/Gunicorn-25.1.0-499848)
![Uvicorn](https://img.shields.io/badge/Uvicorn-0.41.0-222222)

</div>

---

## Overview

**analytics-api-microsservice** is a production-ready **FastAPI-based analytics microservice** designed to ingest structured data and return analytical insights.

The project is containerized with Docker and structured for scalability, clean routing separation, and data validation using modern Python tooling.

---


## 🏗 Project Structure

```
.
├── compose.yaml
├── Dockerfile
├── requirements.txt
├── notebooks/
│   └── notebook.ipynb
└── src/
    ├── main.py
    └── api/
        └── events/
            ├── __init__.py
            └── routing.py
```

* **compose.yaml** → Development orchestration with Docker Compose
* **Dockerfile** → Production-ready container image
* **notebooks/** → Analytics experimentation environment
* **src/main.py** → FastAPI application entry point
* **src/api/events/routing.py** → API routing & validation logic

---

## Tech Stack

* **FastAPI** — High-performance async API framework
* **Pydantic v2** — Data validation & serialization
* **SQLModel / SQLAlchemy 2.0** — ORM layer
* **TimescaleDB (planned support)** — Time-series optimized analytics
* **Gunicorn + Uvicorn** — Production ASGI server
* **Docker & Docker Compose** — Containerization & development workflow

---

## ⚙️ Development Setup

### 1️⃣ Build & Run with Docker Compose

```bash
docker compose up --build
```

API will be available at:

```
http://localhost:8000
```

---

### 2️⃣ Local Python Development (Optional)

Create virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run with Uvicorn:

```bash
uvicorn src.main:app --reload
```
---

## API Design

The API follows a modular architecture:

```
src/
 └── api/
      └── events/
           └── routing.py
```

* Separation of concerns
* Scalable routing structure
* Pydantic-powered request validation
* Ready for expansion (analytics modules, aggregation layers, DB integrations)

---

## Working on features:

* [ ] Database integration (PostgreSQL / TimescaleDB)
* [ ] Event ingestion pipeline
* [ ] Analytics aggregation endpoints
* [ ] Authentication & Authorization
* [ ] Observability (logging + metrics)
* [ ] CI/CD integration
* [ ] OpenAPI versioning strategy

---

## Production Considerations

* Gunicorn worker tuning
* Environment variable configuration
* Health checks & readiness endpoints
* Reverse proxy support (NGINX / Traefik)
* Horizontal scaling support

---

## Notebooks

The `notebooks/` directory is intended for:

* Exploratory data analysis
* Query prototyping
* Algorithm experimentation
* Performance validation before production integration

---
