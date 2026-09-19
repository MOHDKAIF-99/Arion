"""
routes/eris.py — Endpoints for Eris, the general-purpose assistant.
"""

from fastapi import APIRouter
from pydantic import BaseModel

from services.llm_service import generate_general_reply
from services.weather_service import get_weather
from services.calculator_service import calculate
from services.youtube_service import search_youtube

router = APIRouter()


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    reply: str


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    text = request.message.lower()

    if "weather" in text or "mausam" in text:
        city = extract_city(text) or "Kanpur"
        reply = get_weather(city)
        return ChatResponse(reply=reply)

    if any(op in text for op in ["+", "-", "*", "/", "calculate"]):
        reply = calculate(text)
        return ChatResponse(reply=reply)

    if "youtube" in text or "play video" in text or "watch" in text:
        query = text.replace("youtube", "").replace("play video", "").strip()
        reply = search_youtube(query)
        return ChatResponse(reply=reply)

    reply = generate_general_reply(request.message)
    return ChatResponse(reply=reply)


def extract_city(text: str) -> str | None:
    if " in " in text:
        return text.split(" in ")[-1].strip("? .")
    return None