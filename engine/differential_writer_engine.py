# -*- coding: utf-8 -*-

from providers.provider_manager import ProviderManager


class DifferentialWriterEngine:

    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic):
        return {
            "section": "differential",
            "content": self.provider.generate(f"اكتب التشخيص التفريقي لمرض {topic}."),
        }

    def info(self):
        return {
            "engine": "Differential Writer Engine",
            "version": "2.0",
            "type": "AI Powered",
        }
