# -*- coding: utf-8 -*-

from providers.provider_manager import ProviderManager


class VaccineWriterEngine:

    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic):
        prompt = f"اكتب برنامج التحصين واللقاحات ضد {topic}."
        return {"section": "vaccine", "content": self.provider.generate(prompt)}

    def info(self):
        return {
            "engine": "Vaccine Writer Engine",
            "version": "2.0",
            "type": "AI Powered",
        }
