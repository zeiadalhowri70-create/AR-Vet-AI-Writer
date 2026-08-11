# -*- coding:utf-8 -*-
from providers.provider_manager import ProviderManager


class ArticleSummaryAIEngine:
    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic):
        return {
            "section": "summary_ai",
            "content": self.provider.generate(f"لخص مقال {topic} في فقرة احترافية."),
        }

    def info(self):
        return {
            "engine": "Article Summary AI Engine",
            "version": "2.0",
            "type": "AI Powered",
        }
