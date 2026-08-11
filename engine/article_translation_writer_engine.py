# -*- coding:utf-8 -*-
from providers.provider_manager import ProviderManager


class ArticleTranslationWriterEngine:
    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic):
        return {
            "section": "translation",
            "content": self.provider.generate(
                f"ترجم مقال {topic} إلى الإنجليزية العلمية."
            ),
        }

    def info(self):
        return {
            "engine": "Article Translation Writer Engine",
            "version": "2.0",
            "type": "AI Powered",
        }
