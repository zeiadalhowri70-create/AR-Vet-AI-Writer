# -*- coding:utf-8 -*-
from providers.provider_manager import ProviderManager


class ArticleVersionWriterEngine:
    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic):
        return {
            "section": "version",
            "content": self.provider.generate(f"أنشئ معلومات الإصدار لمقال {topic}."),
        }

    def info(self):
        return {
            "engine": "Article Version Writer Engine",
            "version": "2.0",
            "type": "AI Powered",
        }
