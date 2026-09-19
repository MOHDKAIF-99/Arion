"""
routes/cosmo.py — Endpoints for Cosmo, the email automation companion.
"""

from fastapi import APIRouter
from pydantic import BaseModel

from services.llm_service import generate_email_draft
from services.gmail_service import create_gmail_draft

router = APIRouter()


class DraftRequest(BaseModel):
    command: str


class DraftResponse(BaseModel):
    success: bool
    message: str
    draft_link: str | None = None


@router.post("/draft", response_model=DraftResponse)
def create_draft(request: DraftRequest):
    try:
        email_content = generate_email_draft(request.command)

        draft_link = create_gmail_draft(
            subject=email_content["subject"],
            body=email_content["body"],
        )

        return DraftResponse(
            success=True,
            message=f"Draft ready: \"{email_content['subject']}\". Review it in Gmail before sending.",
            draft_link=draft_link,
        )

    except Exception as e:
        return DraftResponse(
            success=False,
            message=f"Couldn't create the draft: {str(e)}",
        )