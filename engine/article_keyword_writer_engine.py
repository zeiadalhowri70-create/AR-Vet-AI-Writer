# -*- coding: utf-8 -*-
from providers.provider_manager import ProviderManager


class ArticleKeywordWriterEngine:
    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic):
        return {
            "section": "keywords",
            "content": self.provider.generate(
                f"استخرج الكلمات المفتاحية الخاصة بـ {topic}."
            ),
        }

    def info(self):
        return {
            "engine": "Article Keyword Writer Engine",
            "version": "2.0",
            "type": "AI Powered",
        }
