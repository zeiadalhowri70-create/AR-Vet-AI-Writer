# -*- coding:utf-8 -*-
from providers.provider_manager import ProviderManager


class ArticleFinalWriterEngine:
    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic):
        return {
            "section": "final_writer",
            "content": self.provider.generate(f"أنشئ النسخة النهائية من مقال {topic}."),
        }

    def info(self):
        return {
            "engine": "Article Final Writer Engine",
            "version": "2.0",
            "type": "AI Powered",
        }
