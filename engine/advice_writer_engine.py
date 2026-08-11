# -*- coding: utf-8 -*-

from providers.provider_manager import ProviderManager


class AdviceWriterEngine:

    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic):
        return {
            "section": "advice",
            "content": self.provider.generate(
                f"اكتب نصائح الطبيب البيطري حول {topic}."
            ),
        }

    def info(self):
        return {
            "engine": "Advice Writer Engine",
            "version": "2.0",
            "type": "AI Powered",
        }
