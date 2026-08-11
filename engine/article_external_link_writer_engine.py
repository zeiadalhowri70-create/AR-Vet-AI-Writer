# -*- coding: utf-8 -*-
from providers.provider_manager import ProviderManager


class ArticleExternalLinkWriterEngine:
    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic):
        return {
            "section": "external_links",
            "content": self.provider.generate(
                f"اقترح روابط خارجية موثوقة لمقال {topic}."
            ),
        }

    def info(self):
        return {
            "engine": "Article External Link Writer Engine",
            "version": "2.0",
            "type": "AI Powered",
        }
