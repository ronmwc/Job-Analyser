# Singapore Job Analyser

A backend API that fetches Singapore job listings on demand, stores them in PostgreSQL, extracts in-demand skills from job descriptions, and exposes job market insights through FastAPI REST endpoints.

This is a portfolio project built to practise backend engineering, database design, REST API development, Docker, and Kubernetes deployment.

---

## Project Overview

The Singapore Job Analyser helps obtain results such as:

* What are the most in-demand skills for software engineer roles in Singapore?
* Which skills appear most often in data engineer job listings?
* What companies are hiring for roles that require Python, SQL, Docker, or Kubernetes?
* What job titles appear most often in the stored job listings?

The system fetches job listings only when manually triggered through an API endpoint. It does not run automatic scheduled jobs.

---

## Tech Stack

* **Python
* **FastAPI** — REST API framework
* **PostgreSQL** — relational database
* **SQLAlchemy** — ORM for database interaction
* **Alembic** — database migrations
* **httpx** — async HTTP client for calling job APIs
* **Docker** — containerisation
* **Docker Compose** — local multi-container setup
* **Kubernetes** — later deployment practice
* **pytest** — testing
