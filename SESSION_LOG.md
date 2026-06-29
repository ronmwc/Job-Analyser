# Session Log

<!-- Claude: append a new entry to the bottom of this file when user says "end session" -->

## Format to use for every entry:
## [DD-MM-YYYY] Session N — Short title
STAGE: Which stage we were on
COMPLETED:
- What was finished this session
IN PROGRESS:
- What was started but not finished (skip if nothing)
ERRORS ENCOUNTERED:
- Any errors hit and how they were resolved (skip if none)
NEXT SESSION STARTS AT:
- Exact next step, file, and what needs to be done
TIME SPENT: X hours

---

<!-- entries go below this line -->

## [29-06-2026] Session 2 — CLAUDE.md restructure and stage realignment
STAGE: Stage 1 — Basic FastAPI app
COMPLETED:
- User updated CLAUDE.md with new stage numbering and teaching rules
- CHANGELOG.md updated to match new stage structure and tracker format
- Registered ALL PUSH and CONFIRM DELETE command rules in memory
IN PROGRESS:
- Stage 1 partially done — folder structure and config complete, main.py not yet written
NEXT SESSION STARTS AT:
- Stage 1 — write app/main.py with FastAPI instance and GET /health endpoint
- Then run: uvicorn app.main:app --reload and verify /health responds

---

## [29-06-2026] Session 1 — Project setup and config
STAGE: Stage 2 — Environment variables and config
COMPLETED:
- Connected project to GitHub (git@github.com:ronmwc/Job-Analyser.git)
- Created CHANGELOG.md with [current] tracking format
- Created virtual environment (.venv)
- Created app/core/__init__.py and app/core/config.py
- Created .env and .env.example
- Created requirements.txt and installed all dependencies
- Verified config.py reads .env correctly
- Registered ALL PUSH command rules
NEXT SESSION STARTS AT:
- Stage 3 — Database models and migrations
- First step: install PostgreSQL on Mac, create the database
