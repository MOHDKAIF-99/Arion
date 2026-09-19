"""
main.py — Entry point for the AI Companion backend.

Run locally with:
    uvicorn main:app --reload

Interactive API docs will be available at:
    http://localhost:8000/docs
"""

from dotenv import load_dotenv
load_dotenv()  # Reads .env and loads GROQ_API_KEY etc. into the environment — must run before routes/services are imported

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import cosmo, eris

app = FastAPI(
    title="AI Companion Backend",
    description="Backend for Cosmo (email automation) and Eris (general assistant)",
    version="1.0.0",
)

# Allow the frontend (served from a different origin/port) to call this API.
# In production, replace "*" with your actual frontend URL for security.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount each companion's routes under its own prefix
app.include_router(cosmo.router, prefix="/api/cosmo", tags=["Cosmo"])
app.include_router(eris.router, prefix="/api/eris", tags=["Eris"])


@app.get("/api/health")
def health_check():
    """Simple endpoint to confirm the server is alive."""
    return {"status": "ok", "message": "AI Companion backend is running"}