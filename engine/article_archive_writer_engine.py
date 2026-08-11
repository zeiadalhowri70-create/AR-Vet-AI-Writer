# -*- coding:utf-8 -*-
from providers.provider_manager import ProviderManager


class ArticleArchiveWriterEngine:
    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic):
        return {
            "section": "archive",
            "content": self.provider.generate(f"أنشئ بيانات أرشفة لمقال {topic}."),
        }

    def info(self):
        return {
            "engine": "Article Archive Writer Engine",
            "version": "2.0",
            "type": "AI Powered",
        }
