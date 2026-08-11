# -*- coding: utf-8 -*-

from providers.provider_manager import ProviderManager


class FAQWriterEngine:

    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic):
        return {
            "section": "faq",
            "content": self.provider.generate(f"اكتب أسئلة وأجوبة شائعة عن {topic}."),
        }

    def info(self):
        return {"engine": "FAQ Writer Engine", "version": "2.0", "type": "AI Powered"}
