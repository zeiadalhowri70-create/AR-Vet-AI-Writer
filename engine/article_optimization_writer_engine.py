# -*- coding:utf-8 -*-
from providers.provider_manager import ProviderManager


class ArticleOptimizationWriterEngine:
    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic):
        return {
            "section": "optimization",
            "content": self.provider.generate(
                f"حسن المقال علمياً وتقنياً بعنوان {topic}."
            ),
        }

    def info(self):
        return {
            "engine": "Article Optimization Writer Engine",
            "version": "2.0",
            "type": "AI Powered",
        }
