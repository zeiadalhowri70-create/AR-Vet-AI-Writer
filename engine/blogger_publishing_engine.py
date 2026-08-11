# -*- coding: utf-8 -*-

from datetime import datetime, timezone
from engine.blogger_api_client_engine import BloggerAPIClientEngine


class BloggerPublishingEngine:
    """
    Final Blogger Publishing Engine v2.0
    Production Blogger publishing layer.
    """

    VERSION = "2.0"

    def __init__(self):
        self.platform = "Blogger"
        self.api_client = BloggerAPIClientEngine()

    def prepare(self, article):

        title = article.get("title", "")
        html = article.get("html", "")

        draft_result = None

        if article.get("save_as_draft", True):
            draft_result = self.api_client.create_draft(article)

        return {
            "platform": self.platform,
            "api_draft": draft_result,
            "post": {"title": title, "content": html, "status": "draft"},
            "seo": {
                "canonical_url": article.get("canonical_url", ""),
                "labels": article.get("labels", ["طب بيطري", "أمراض الدواجن"]),
            },
            "metadata": {
                "prepared_at": datetime.now(timezone.utc).isoformat(),
                "ready_for_api": True,
            },
            "publishing": {"draft": bool(draft_result), "published": False, "api_ready": True},
        }

    def info(self):

        return {
            "engine": "Final Blogger Publishing Engine",
            "version": self.VERSION,
            "status": "production",
            "platform": self.platform,
            "api_ready": True,
        }
