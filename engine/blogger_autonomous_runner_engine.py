# -*- coding: utf-8 -*-

import uuid
from datetime import datetime, timezone

from engine.blogger_article_request_adapter import BloggerArticleRequestAdapter

from engine.blogger_topic_planner_engine import BloggerTopicPlannerEngine


class BloggerAutonomousRunnerEngine:

    VERSION = "1.0"

    def __init__(self):

        self.planner = BloggerTopicPlannerEngine()
        self.request_adapter = BloggerArticleRequestAdapter()

    def create_job(self, category="veterinary"):

        topic = self.planner.suggest(category)

        job_id = str(uuid.uuid4())

        return {
            "job_id": job_id,
            "topic": topic,
            "article_request": self.request_adapter.build(
                {"job_id": job_id, "topic": topic}
            ),
            "created_at": datetime.now(timezone.utc).isoformat(),
            "status": "READY",
            "engine": "Blogger Autonomous Runner Engine",
            "version": self.VERSION,
        }

    def info(self):

        return {
            "engine": "Blogger Autonomous Runner Engine",
            "version": self.VERSION,
            "status": "production",
        }
