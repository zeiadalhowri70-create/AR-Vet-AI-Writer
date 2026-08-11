# -*- coding:utf-8 -*-
from providers.provider_manager import ProviderManager


class ArticleReleaseWriterEngine:
    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic):
        return {
            "section": "release",
            "content": self.provider.generate(
                f"أنشئ بيانات نشر الإصدار النهائي لمقال {topic}."
            ),
        }

    def info(self):
        return {
            "engine": "Article Release Writer Engine",
            "version": "2.0",
            "type": "AI Powered",
        }
