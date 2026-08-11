# -*- coding:utf-8 -*-
from providers.provider_manager import ProviderManager


class ArticleAdSenseWriterEngine:
    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic):
        return {
            "section": "adsense",
            "content": self.provider.generate(
                f"حسن مقال {topic} ليتوافق مع Google AdSense."
            ),
        }

    def info(self):
        return {
            "engine": "Article AdSense Writer Engine",
            "version": "2.0",
            "type": "AI Powered",
        }
