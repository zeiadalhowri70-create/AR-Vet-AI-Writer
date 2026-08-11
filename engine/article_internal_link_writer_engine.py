# -*- coding: utf-8 -*-
from providers.provider_manager import ProviderManager


class ArticleInternalLinkWriterEngine:
    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic):
        return {
            "section": "internal_links",
            "content": self.provider.generate(
                f"اقترح روابط داخلية مناسبة لمقال {topic}."
            ),
        }

    def info(self):
        return {
            "engine": "Article Internal Link Writer Engine",
            "version": "2.0",
            "type": "AI Powered",
        }
