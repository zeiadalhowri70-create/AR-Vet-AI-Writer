# -*- coding: utf-8 -*-

from providers.provider_manager import ProviderManager


class PrognosisWriterEngine:

    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic):
        prompt = f"اكتب التوقعات والنتائج المستقبلية لحالات {topic}."
        return {"section": "prognosis", "content": self.provider.generate(prompt)}

    def info(self):
        return {
            "engine": "Prognosis Writer Engine",
            "version": "2.0",
            "type": "AI Powered",
        }
