# -*- coding: utf-8 -*-
from providers.provider_manager import ProviderManager


class ArticleMobileWriterEngine:
    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic):
        return {
            "section": "mobile",
            "content": self.provider.generate(
                f"حسّن عرض مقال {topic} على الهواتف المحمولة."
            ),
        }

    def info(self):
        return {
            "engine": "Article Mobile Writer Engine",
            "version": "2.0",
            "type": "AI Powered",
        }
