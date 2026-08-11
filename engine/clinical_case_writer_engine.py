# -*- coding: utf-8 -*-

from providers.provider_manager import ProviderManager


class ClinicalCaseWriterEngine:

    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic):
        return {
            "section": "clinical_case",
            "content": self.provider.generate(f"اكتب حالة سريرية بيطرية عن {topic}."),
        }

    def info(self):
        return {
            "engine": "Clinical Case Writer Engine",
            "version": "2.0",
            "type": "AI Powered",
        }
