# -*- coding:utf-8 -*-
from providers.provider_manager import ProviderManager


class ArticleImagePromptWriterEngine:
    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic):
        return {
            "section": "image_prompt",
            "content": self.provider.generate(
                f"أنشئ وصفاً احترافياً لصورة غلاف مقال {topic}."
            ),
        }

    def info(self):
        return {
            "engine": "Article Image Prompt Writer Engine",
            "version": "2.0",
            "type": "AI Powered",
        }
