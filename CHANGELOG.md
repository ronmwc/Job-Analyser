<!-- Claude: read [current] block first, then only load files listed in ADDED sections -->

# Changelog

## [current]
STATUS: In progress
STEP: 3 — Database models and migrations
NEXT: Install PostgreSQL, create the database, define SQLAlchemy models

---

## [29-06-2026] Step 2 complete — Environment variables and config
ADDED:
- app/core/__init__.py — makes core/ a Python package
- app/core/config.py — reads .env and exposes settings as importable object
- .env — local settings file (not committed to Git)
- .env.example — safe template showing required environment variables
- requirements.txt — all project dependencies

VERIFIED:
- python3 -c "from app.core.config import settings; print(settings.app_name)"
- Output: Job Analyser

---

## [29-06-2026] Step 1 complete — Project folder structure and virtual environment
ADDED:
- app/__init__.py — makes app/ a Python package
- .venv/ — isolated Python environment for this project (not committed to Git)

VERIFIED:
- ls app/ shows __init__.py
- which python returns a path containing .venv
