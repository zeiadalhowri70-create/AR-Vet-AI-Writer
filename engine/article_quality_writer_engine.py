# -*- coding:utf-8 -*-
from providers.provider_manager import ProviderManager


class ArticleQualityWriterEngine:
    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic):
        return {
            "section": "quality",
            "content": self.provider.generate(f"قيّم جودة مقال {topic}."),
        }

    def info(self):
        return {
            "engine": "Article Quality Writer Engine",
            "version": "2.0",
            "type": "AI Powered",
        }
