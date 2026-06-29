<!-- Claude: read [current] block first, then only load files listed in ADDED sections -->

# Changelog

## [current]
STATUS: In progress
STAGE: 1 — Basic FastAPI app
NEXT: Write app/main.py, run FastAPI with uvicorn, verify /health endpoint responds

## Stage tracker
Stage 1  — Basic FastAPI app             — 🔄 In progress
Stage 2  — PostgreSQL + SQLAlchemy       — ⬜ Not started
Stage 3  — Skills dictionary             — ⬜ Not started
Stage 4  — MyCareersFuture fetcher       — ⬜ Not started
Stage 5  — Skill extraction processor    — ⬜ Not started
Stage 6  — Fetch endpoint                — ⬜ Not started
Stage 7  — Jobs and Skills endpoints     — ⬜ Not started
Stage 8  — Companies and Market          — ⬜ Not started
Stage 9  — Docker setup                  — ⬜ Not started
Stage 10 — Testing                       — ⬜ Not started
Stage 11 — Kubernetes                    — ⬜ Not started
Stage 12 — Portfolio polish              — ⬜ Not started

---

## [29-06-2026] Stage 1 in progress — Basic FastAPI app
ADDED:
- app/__init__.py — makes app/ a Python package
- app/core/__init__.py — makes core/ a Python package
- app/core/config.py — reads .env and exposes settings as importable object
- .env — local settings file (not committed to Git)
- .env.example — safe template showing required environment variables
- requirements.txt — all project dependencies
- .venv/ — isolated Python environment (not committed to Git)

VERIFIED:
- python3 -c "from app.core.config import settings; print(settings.app_name)"
- Output: Job Analyser

IN PROGRESS:
- app/main.py not yet written — FastAPI not yet running
