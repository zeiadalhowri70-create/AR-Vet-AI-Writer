# -*- coding: utf-8 -*-
from providers.provider_manager import ProviderManager


class ArticleFeaturedImageWriterEngine:
    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic):
        return {
            "section": "featured_image",
            "content": self.provider.generate(
                f"أنشئ وصفاً لصورة الغلاف الخاصة بمقال {topic}."
            ),
        }

    def info(self):
        return {
            "engine": "Article Featured Image Writer Engine",
            "version": "2.0",
            "type": "AI Powered",
        }
