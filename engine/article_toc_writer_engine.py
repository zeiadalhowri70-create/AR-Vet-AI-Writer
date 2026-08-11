# -*- coding: utf-8 -*-
from providers.provider_manager import ProviderManager


class ArticleTOCWriterEngine:
    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic):
        return {
            "section": "toc",
            "content": self.provider.generate(f"أنشئ جدول محتويات لمقال {topic}."),
        }

    def info(self):
        return {
            "engine": "Article TOC Writer Engine",
            "version": "2.0",
            "type": "AI Powered",
        }
