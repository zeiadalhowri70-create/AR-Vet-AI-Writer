# -*- coding:utf-8 -*-
from providers.provider_manager import ProviderManager


class ArticleRevisionWriterEngine:
    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic):
        return {
            "section": "revision",
            "content": self.provider.generate(f"راجع وعدّل مقال {topic}."),
        }

    def info(self):
        return {
            "engine": "Article Revision Writer Engine",
            "version": "2.0",
            "type": "AI Powered",
        }
