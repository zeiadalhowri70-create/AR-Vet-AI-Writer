# -*- coding: utf-8 -*-

import uuid

from engine.blogger_quality_gate_engine import BloggerQualityGateEngine

from engine.blogger_content_safety_engine import BloggerContentSafetyEngine


class BloggerProductionPipelineEngine:

    VERSION = "1.0"

    def __init__(self):

        self.quality = BloggerQualityGateEngine()

        self.safety = BloggerContentSafetyEngine()

    def process(self, article):

        quality = self.quality.check(article)

        safety = self.safety.check(article)

        return {
            "production_id": str(uuid.uuid4()),
            "article": article,
            "quality": quality,
            "safety": safety,
            "approved": quality["passed"] and safety["safe"],
            "engine": "Blogger Production Pipeline Engine",
            "version": self.VERSION,
        }

    def info(self):

        return {
            "engine": "Blogger Production Pipeline Engine",
            "version": self.VERSION,
            "status": "production",
        }
