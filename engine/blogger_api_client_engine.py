# -*- coding: utf-8 -*-

from datetime import datetime, timezone
from pathlib import Path
import pickle

from googleapiclient.discovery import build
from google.auth.transport.requests import Request


class BloggerAPIClientEngine:
    """
    Blogger API Client Engine v2.0
    Real Google Blogger Draft Uploader
    """

    VERSION = "2.0"

    def __init__(self):
        self.platform = "Blogger API"
        self.blog_id = None
        self.service = None

        try:
            from config import BLOG_ID

            self.blog_id = BLOG_ID
        except Exception:
            self.blog_id = None

        self._load_service()

    def _load_service(self):
        token_file = Path("token.pickle")

        if not token_file.exists():
            return

        with open(token_file, "rb") as f:
            creds = pickle.load(f)

        if creds.expired and creds.refresh_token:
            creds.refresh(Request())

        self.service = build("blogger", "v3", credentials=creds)

    def create_draft(self, article):

        title = article.get("title", "")
        html = article.get("html", "")

        if self.service and self.blog_id:

            body = {"title": title, "content": html}

            result = (
                self.service.posts()
                .insert(blogId=self.blog_id, body=body, isDraft=True)
                .execute()
            )

            return {
                "platform": self.platform,
                "status": "draft",
                "published": False,
                "id": result.get("id"),
                "url": result.get("url"),
                "title": title,
                "content_length": len(html),
                "created_at": datetime.now(timezone.utc).isoformat(),
                "api_ready": True,
                "real_api": True,
            }

        return {
            "platform": self.platform,
            "status": "draft",
            "published": False,
            "title": title,
            "content_length": len(html),
            "created_at": datetime.now(timezone.utc).isoformat(),
            "api_ready": True,
            "real_api": False,
        }

    def info(self):
        return {
            "engine": "Blogger API Client Engine",
            "version": self.VERSION,
            "status": "production",
            "real_api": bool(self.service),
            "draft_only": True,
        }
