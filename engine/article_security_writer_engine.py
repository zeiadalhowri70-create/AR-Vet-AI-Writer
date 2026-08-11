# -*- coding:utf-8 -*-
from providers.provider_manager import ProviderManager


class ArticleSecurityWriterEngine:
    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic):
        return {
            "section": "security",
            "content": self.provider.generate(f"راجع الجوانب الأمنية لمقال {topic}."),
        }

    def info(self):
        return {
            "engine": "Article Security Writer Engine",
            "version": "2.0",
            "type": "AI Powered",
        }
