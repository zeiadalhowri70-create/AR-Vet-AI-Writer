# -*- coding:utf-8 -*-
from providers.provider_manager import ProviderManager


class ArticleVideoPromptWriterEngine:
    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic):
        return {
            "section": "video_prompt",
            "content": self.provider.generate(
                f"أنشئ سيناريو فيديو قصير لمقال {topic}."
            ),
        }

    def info(self):
        return {
            "engine": "Article Video Prompt Writer Engine",
            "version": "2.0",
            "type": "AI Powered",
        }
