# -*- coding: utf-8 -*-
from providers.provider_manager import ProviderManager


class ArticleBreadcrumbWriterEngine:
    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic):
        return {
            "section": "breadcrumb",
            "content": self.provider.generate(f"أنشئ Breadcrumb Schema لمقال {topic}."),
        }

    def info(self):
        return {
            "engine": "Article Breadcrumb Writer Engine",
            "version": "2.0",
            "type": "AI Powered",
        }
