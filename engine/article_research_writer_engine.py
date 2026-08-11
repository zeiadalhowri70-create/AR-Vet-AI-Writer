# -*- coding:utf-8 -*-
from providers.provider_manager import ProviderManager


class ArticleResearchWriterEngine:
    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic):
        return {
            "section": "research",
            "content": self.provider.generate(f"اكتب بحثاً علمياً عن {topic}."),
        }

    def info(self):
        return {
            "engine": "Article Research Writer Engine",
            "version": "2.0",
            "type": "AI Powered",
        }
