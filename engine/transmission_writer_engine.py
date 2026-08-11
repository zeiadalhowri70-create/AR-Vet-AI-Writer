# -*- coding: utf-8 -*-

from providers.provider_manager import ProviderManager


class TransmissionWriterEngine:

    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic):

        prompt = f"اكتب طرق انتقال وانتشار {topic}."

        return {"section": "transmission", "content": self.provider.generate(prompt)}

    def info(self):
        return {"engine": "Transmission Writer Engine", "version": "2.0"}
