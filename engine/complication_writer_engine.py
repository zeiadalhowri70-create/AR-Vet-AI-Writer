# -*- coding: utf-8 -*-

from providers.provider_manager import ProviderManager


class ComplicationWriterEngine:

    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic):
        return {
            "section": "complication",
            "content": self.provider.generate(f"اكتب مضاعفات مرض {topic} في الدواجن."),
        }

    def info(self):
        return {
            "engine": "Complication Writer Engine",
            "version": "2.0",
            "type": "AI Powered",
        }
