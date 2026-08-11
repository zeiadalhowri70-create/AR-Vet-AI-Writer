# -*- coding: utf-8 -*-

from providers.provider_manager import ProviderManager


class RecommendationWriterEngine:

    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic):
        return {
            "section": "recommendation",
            "content": self.provider.generate(f"اكتب توصيات بيطرية مهمة حول {topic}."),
        }

    def info(self):
        return {
            "engine": "Recommendation Writer Engine",
            "version": "2.0",
            "type": "AI Powered",
        }
