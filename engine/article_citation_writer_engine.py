# -*- coding:utf-8 -*-
from providers.provider_manager import ProviderManager


class ArticleCitationWriterEngine:
    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic):
        return {
            "section": "citations",
            "content": self.provider.generate(
                f"أنشئ قائمة مراجع واستشهادات لمقال {topic}."
            ),
        }

    def info(self):
        return {
            "engine": "Article Citation Writer Engine",
            "version": "2.0",
            "type": "AI Powered",
        }
