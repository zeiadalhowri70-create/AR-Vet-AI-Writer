# -*- coding: utf-8 -*-

from providers.provider_manager import ProviderManager


class LaboratoryWriterEngine:

    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic):
        return {
            "section": "laboratory",
            "content": self.provider.generate(
                f"اكتب الفحوصات المخبرية لتشخيص {topic}."
            ),
        }

    def info(self):
        return {
            "engine": "Laboratory Writer Engine",
            "version": "2.0",
            "type": "AI Powered",
        }
