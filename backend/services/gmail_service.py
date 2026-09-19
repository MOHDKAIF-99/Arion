"""
services/gmail_service.py — Gmail API integration for Cosmo.

PRIVACY RULE: only drafts.create is used, never send.
"""

import base64
from email.mime.text import MIMEText

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/gmail.compose"]


def _get_gmail_service(user_credentials: dict):
    creds = Credentials.from_authorized_user_info(user_credentials, SCOPES)
    return build("gmail", "v1", credentials=creds)


def create_gmail_draft(subject: str, body: str, to: str = "", user_credentials: dict = None) -> str:
    if user_credentials is None:
        raise ValueError("No user credentials provided — user must connect Gmail first")

    service = _get_gmail_service(user_credentials)

    message = MIMEText(body)
    message["to"] = to
    message["subject"] = subject
    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

    draft = service.users().drafts().create(
        userId="me",
        body={"message": {"raw": raw_message}},
    ).execute()

    draft_id = draft["id"]
    return f"https://mail.google.com/mail/u/0/#drafts?compose={draft_id}"