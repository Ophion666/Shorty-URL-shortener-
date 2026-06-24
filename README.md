# Shorty - URL Shortener & Click Analytics API

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)

## Motivation

I built this project to deepen my understanding of HTTP request mechanics, REST API architecture, database relationships, and backend system design.

URL shorteners are a classic backend engineering challenge. Instead of creating a simple link minifier, I wanted to build a production-oriented service capable of generating unique short URLs, handling redirections reliably, and collecting real-time traffic analytics for every visit.

The project focuses on API design, database modeling, testing, and solving practical issues such as redirect caching and collision-safe key generation.

---

## Tech Stack

* **Language:** Python 3.11
* **Framework:** FastAPI
* **Database:** PostgreSQL
* **ORM:** SQLAlchemy
* **Database Migrations:** Alembic
* **Testing:** Pytest, HTTPX
* **Infrastructure:** Docker, Docker Compose

---

## Architectural Decisions & Challenges

### Accurate Analytics Through HTTP 307 Redirects

Most URL shorteners use `301 Moved Permanently` redirects. While efficient, browsers often cache these responses aggressively. After the first visit, subsequent clicks may bypass the backend entirely, causing analytics data to become inaccurate.

To guarantee that every click reaches the API and is recorded, I implemented `HTTP 307 Temporary Redirect`. This forces the browser to contact the server on every redirect request, ensuring reliable analytics and accurate click counts.

### Collision-Safe Short URL Generation

Short links are generated using random 6-character alphanumeric keys.

Random generation always introduces a possibility of collisions, which could cause database integrity errors. To eliminate this risk, I implemented a uniqueness verification loop that checks PostgreSQL before saving a newly generated key.

This guarantees that every short URL remains unique while keeping the implementation lightweight and performant.

### Relational Analytics Design

Traffic analytics are stored using a strict One-to-Many database relationship:

```text
Link
 └── Click
      ├── IP Address
      ├── User-Agent
      └── Timestamp
```

This structure allows efficient aggregation of analytics while preserving detailed click history for future reporting features.

---

## Key Features

* **URL Shortening Service:** Converts long URLs into compact 6-character shareable links.
* **Automatic Redirection:** Fast and reliable redirect handling through FastAPI.
* **Real-Time Analytics:** Records every visit, including visitor IP address, User-Agent information, and timestamp.
* **Click Statistics:** Tracks total visits for each shortened URL.
* **Collision-Protected Key Generation:** Prevents duplicate short links through database-backed validation.
* **Relational Database Architecture:** Clean One-to-Many relationship between links and click events.
* **Alembic Migrations:** Structured database version control and schema evolution.
* **Comprehensive Test Suite:** Critical business logic covered with Pytest and FastAPI TestClient.
* **Docker Containerization:** Fully reproducible PostgreSQL environment through Docker Compose.


## Testing

The project includes automated tests covering:

* URL creation
* Redirect behavior
* Analytics logging
* Database interactions
* Statistics retrieval

Run tests with:

```bash
pytest
```

---

## Project Structure

```text
shorty/
├── backend/
│   ├── app/
│   │   ├── api/          # FastAPI routers (endpoints)
│   │   ├── core/         # Configuration & key generation
│   │   ├── crud/         # Database query operations
│   │   ├── db/           # Database connection & sessions
│   │   ├── models/       # SQLAlchemy models (Link, Click)
│   │   ├── schemas/      # Pydantic schemas
│   │   └── main.py
│   ├── migrations/       # Alembic migration history
│   └── tests/            # Automated tests
└── docker-compose.yml
```

---

## How to Run

### 1. Clone Repository

```bash
git clone https://github.com/Ophion666/Shorty-URL-shortener-.git
cd shorty/backend
```

### 2. Create Environment Variables

```ini
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/shorty_db
```

### 3. Start PostgreSQL

```bash
docker-compose up -d
```

### 4. Create Virtual Environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 5. Install Dependencies & Run Migrations

```bash
pip install -r requirements.txt
alembic upgrade head
```

### 6. Start API

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://localhost:8000
```

Swagger documentation:

```text
http://localhost:8000/docs
```

Run tests:

```bash
pytest
```
