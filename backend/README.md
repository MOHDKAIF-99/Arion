# AI Companion Backend (FastAPI)

Backend for Cosmo (email drafts) and Eris (general assistant).

## Setup
1. python -m venv venv
2. venv\Scripts\activate
3. pip install -r requirements.txt
4. Copy .env.example to .env and fill in real keys
5. uvicorn main:app --reload
6. Open http://localhost:8000/docs