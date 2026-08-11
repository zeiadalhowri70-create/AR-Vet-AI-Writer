# -*- coding: utf-8 -*-
from providers.provider_manager import ProviderManager


class TitleWriterEngine:
    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic):
        return {
            "section": "title",
            "content": self.provider.generate(
                f"اقترح أفضل عنوان SEO لمقال عن {topic}."
            ),
        }

    def info(self):
        return {"engine": "Title Writer Engine", "version": "2.0", "type": "AI Powered"}
