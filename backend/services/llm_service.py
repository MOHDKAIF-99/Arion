"""
services/llm_service.py — Wraps calls to the LLM.

Uses Groq's free API — OpenAI-compatible, no credit card needed.
Sign up at https://console.groq.com
"""

import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

MODEL_NAME = "openai/gpt-oss-20b"


def generate_email_draft(command: str) -> dict:
    system_prompt = (
        "You are Cosmo, an email-writing assistant. Given a user's instruction, "
        "write a professional email. Respond ONLY in this exact format:\n"
        "SUBJECT: <subject line>\n"
        "BODY: <email body>"
    )

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": command},
        ],
        max_tokens=500,
    )

    text = response.choices[0].message.content

    subject = "New message"
    body = text
    if "SUBJECT:" in text and "BODY:" in text:
        subject = text.split("SUBJECT:")[1].split("BODY:")[0].strip()
        body = text.split("BODY:")[1].strip()

    return {"subject": subject, "body": body}


def generate_general_reply(message: str) -> str:
    system_prompt = (
        "You are Eris, a friendly and helpful general assistant. "
        "Give concise, useful answers and advice."
    )

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": message},
        ],
        max_tokens=300,
    )

    return response.choices[0].message.content