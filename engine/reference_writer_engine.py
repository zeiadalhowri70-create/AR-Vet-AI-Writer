# -*- coding: utf-8 -*-

from providers.provider_manager import ProviderManager


class ReferenceWriterEngine:

    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic, context=None):
        return {
            "section": "references",
            "content": self.provider.generate(f"اكتب مراجع علمية مناسبة عن {topic}."),
        }

    def info(self):
        return {
            "engine": "Reference Writer Engine",
            "version": "2.0",
            "type": "AI Powered",
        }
