# -*- coding: utf-8 -*-

from providers.provider_manager import ProviderManager


class EpidemiologyWriterEngine:

    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic):
        return {
            "section": "epidemiology",
            "content": self.provider.generate(f"اكتب الوبائيات وانتشار {topic}."),
        }

    def info(self):
        return {
            "engine": "Epidemiology Writer Engine",
            "version": "2.0",
            "type": "AI Powered",
        }
