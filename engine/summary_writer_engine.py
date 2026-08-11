# -*- coding: utf-8 -*-
from providers.provider_manager import ProviderManager


class SummaryWriterEngine:
    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic):
        return {
            "section": "summary",
            "content": self.provider.generate(f"اكتب ملخصاً علمياً لمقال {topic}."),
        }

    def info(self):
        return {
            "engine": "Summary Writer Engine",
            "version": "2.0",
            "type": "AI Powered",
        }
