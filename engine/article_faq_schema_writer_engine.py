# -*- coding: utf-8 -*-
from providers.provider_manager import ProviderManager


class ArticleFAQSchemaWriterEngine:
    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic):
        return {
            "section": "faq_schema",
            "content": self.provider.generate(f"أنشئ FAQ Schema لمقال {topic}."),
        }

    def info(self):
        return {
            "engine": "Article FAQ Schema Writer Engine",
            "version": "2.0",
            "type": "AI Powered",
        }
