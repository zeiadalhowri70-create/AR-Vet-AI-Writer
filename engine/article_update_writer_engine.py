# -*- coding:utf-8 -*-
from providers.provider_manager import ProviderManager


class ArticleUpdateWriterEngine:
    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic):
        return {
            "section": "update",
            "content": self.provider.generate(
                f"حدّث مقال {topic} بأحدث المعلومات العلمية."
            ),
        }

    def info(self):
        return {
            "engine": "Article Update Writer Engine",
            "version": "2.0",
            "type": "AI Powered",
        }
