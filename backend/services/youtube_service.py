"""
services/youtube_service.py — Searches YouTube via YouTube Data API v3.
"""

import os
import requests

API_KEY = os.getenv("YOUTUBE_API_KEY")
SEARCH_URL = "https://www.googleapis.com/youtube/v3/search"


def search_youtube(query: str) -> str:
    if not query:
        return "What would you like me to search for on YouTube?"

    try:
        response = requests.get(
            SEARCH_URL,
            params={
                "part": "snippet",
                "q": query,
                "type": "video",
                "maxResults": 1,
                "key": API_KEY,
            },
            timeout=5,
        )
        data = response.json()

        items = data.get("items", [])
        if not items:
            return f"Couldn't find any videos for '{query}'."

        video_id = items[0]["id"]["videoId"]
        title = items[0]["snippet"]["title"]
        link = f"https://www.youtube.com/watch?v={video_id}"

        return f"Here's a video for '{query}': {title} — {link}"

    except Exception as e:
        return f"YouTube search failed: {str(e)}"