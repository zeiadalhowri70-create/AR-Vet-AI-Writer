# -*- coding:utf-8 -*-
from providers.provider_manager import ProviderManager


class ArticleLanguageWriterEngine:
    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic):
        return {
            "section": "language",
            "content": self.provider.generate(f"دقق اللغة والأسلوب لمقال {topic}."),
        }

    def info(self):
        return {
            "engine": "Article Language Writer Engine",
            "version": "2.0",
            "type": "AI Powered",
        }
