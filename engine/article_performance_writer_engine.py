# -*- coding:utf-8 -*-
from providers.provider_manager import ProviderManager


class ArticlePerformanceWriterEngine:
    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic):
        return {
            "section": "performance",
            "content": self.provider.generate(f"حسن أداء صفحة المقال {topic}."),
        }

    def info(self):
        return {
            "engine": "Article Performance Writer Engine",
            "version": "2.0",
            "type": "AI Powered",
        }
