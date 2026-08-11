# -*- coding:utf-8 -*-
from providers.provider_manager import ProviderManager


class ArticleAnalyticsWriterEngine:
    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic):
        return {
            "section": "analytics",
            "content": self.provider.generate(f"أنشئ تقرير تحليلات لمقال {topic}."),
        }

    def info(self):
        return {
            "engine": "Article Analytics Writer Engine",
            "version": "2.0",
            "type": "AI Powered",
        }
