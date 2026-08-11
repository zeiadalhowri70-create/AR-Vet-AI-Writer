# -*- coding:utf-8 -*-
from providers.provider_manager import ProviderManager


class ArticleSEOIntegrationWriterEngine:
    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic):
        return {
            "section": "seo_integration",
            "content": self.provider.generate(f"ادمج عناصر SEO داخل مقال {topic}."),
        }

    def info(self):
        return {
            "engine": "Article SEO Integration Writer Engine",
            "version": "2.0",
            "type": "AI Powered",
        }
