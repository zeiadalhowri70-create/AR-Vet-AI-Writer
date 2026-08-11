# -*- coding:utf-8 -*-
from providers.provider_manager import ProviderManager


class ArticleReadabilityWriterEngine:
    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic):
        return {
            "section": "readability",
            "content": self.provider.generate(f"حسن قابلية قراءة مقال {topic}."),
        }

    def info(self):
        return {
            "engine": "Article Readability Writer Engine",
            "version": "2.0",
            "type": "AI Powered",
        }
