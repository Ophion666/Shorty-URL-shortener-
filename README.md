#  Shorty - URL Shortener & Click Analytics API

##  Motivation
I built this project to deepen my understanding of HTTP request mechanics, REST API architecture, and database relationships. URL shorteners are a classic system design challenge, and I wanted to build a production-ready version from scratch that doesn't just minify links, but also provides built-in, real-time traffic analytics.

##  Tech Stack
- **Language:** Python 3.11+
- **Framework:** FastAPI
- **Database & ORM:** PostgreSQL, SQLAlchemy
- **Migrations:** Alembic
- **Testing:** Pytest, HTTPX
- **Infrastructure:** Docker, Docker Compose
##  Architectural Decisions
- **The 307 Redirect Strategy:** Standard `301 Moved Permanently` redirects are aggressively cached by browsers. If used, subsequent clicks by the same user wouldn't hit the backend, ruining the analytics. I explicitly implemented `HTTP 307 Temporary Redirect` to force the browser to ping the server on every transition, ensuring 100% accurate click tracking and IP logging.
- **Collision-Safe Key Generation:** Generating random 6-character strings (`a-z`, `A-Z`, `0-9`) always carries a statistical risk of collision. I implemented a loop-guarded algorithm during link creation that verifies key uniqueness against the PostgreSQL database before committing, completely eliminating `IntegrityError` crashes.

##  Key Features
- **Real-time Analytics:** Automatically logs the visitor's IP address, User-Agent (browser/device info), and exact UTC timestamp on every single redirect.
- **Data Integrity:** Strict One-to-Many relational database architecture (`Link` -> `Clicks`) managed via SQLAlchemy ORM.
- **Test-Driven Reliability:** The core redirection logic, analytics counters, and database interactions are thoroughly tested using `Pytest` and FastAPI's `TestClient`.
- **Alembic Migrations:** Robust database schema version control for safe and structured updates.
- **Docker Containerization:** The entire API and Database infrastructure is fully containerized using Docker and Docker Compose.

## Project Structure
```text
shorty/
├── backend/
│   ├── app/
│   │   ├── api/          # FastAPI routers (endpoints)
│   │   ├── core/         # Security configs & key generation logic
│   │   ├── crud/         # Database query operations
│   │   ├── db/           # Database connection & sessions
│   │   ├── models/       # SQLAlchemy tables (Link, Click)
│   │   └── schemas/      # Pydantic validation models
│   │   └── main.py   
│   ├── migrations/       # Alembic migration history
│   └── tests/           
└── docker-compose.yml
```
##  How to Run

### 1. Backend Setup (FastAPI + PostgreSQL)
You can run this project using either Docker (recommended) or a local Python virtual environment.

**Step 1: Clone the repository and set up environment variables**
```bash
git clone https://github.com/Ophion666/Shorty-URL-shortener-.git
cd shorty/backend
```
Create a .env file in the root of the backend directory:
```ini

# Database Configuration (Use 'localhost' if running API locally, or 'db' if fully Dockerized)
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/shorty_db
```
Run with Docker:

Make sure Docker is running on your machine, then start the PostgreSQL container:
```Bash

docker-compose up -d
```

Step 2: Set up the Python Virtual Environment

For Windows:
```Bash

python -m venv .venv
.venv\Scripts\activate
```
For macOS/Linux:
```Bash

python3 -m venv .venv
source .venv/bin/activate
```
Step 3: Install dependencies & Run migrations
```Bash

pip install -r requirements.txt
alembic upgrade head
```
Step 4: Start the backend server
``` Bash

uvicorn app.main:app --reload
```
The API is now running at http://localhost:8000.
You can interact with the endpoints and generate short URLs via the built-in Swagger documentation at http://localhost:8000/docs. To run the automated tests, simply execute pytest in your terminal.
