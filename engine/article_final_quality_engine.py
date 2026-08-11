# -*- coding:utf-8 -*-
from providers.provider_manager import ProviderManager


class ArticleFinalQualityEngine:
    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic):
        return {
            "section": "final_quality",
            "content": self.provider.generate(
                f"نفذ مراجعة الجودة النهائية لمقال {topic}."
            ),
        }

    def info(self):
        return {
            "engine": "Article Final Quality Engine",
            "version": "2.0",
            "type": "AI Powered",
        }
