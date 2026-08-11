# -*- coding: utf-8 -*-

from datetime import datetime


class ArticlePipelineStateEngine:
    """
    محرك تتبع حالة خط إنتاج المقال.
    """

    def __init__(self):
        self.state = {}

    def update(self, topic, stage):
        self.state[topic] = {
            "stage": stage,
            "updated_at": datetime.utcnow().isoformat() + "Z",
        }

    def get(self, topic):
        return self.state.get(topic)

    def info(self):
        return {
            "engine": "Article Pipeline State Engine",
            "version": "1.0",
            "status": "production",
            "tracked_articles": len(self.state),
        }
