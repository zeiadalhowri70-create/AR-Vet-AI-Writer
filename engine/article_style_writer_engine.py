# -*- coding:utf-8 -*-
from providers.provider_manager import ProviderManager


class ArticleStyleWriterEngine:
    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic):
        return {
            "section": "style",
            "content": self.provider.generate(f"حسن الأسلوب اللغوي لمقال {topic}."),
        }

    def info(self):
        return {
            "engine": "Article Style Writer Engine",
            "version": "2.0",
            "type": "AI Powered",
        }
